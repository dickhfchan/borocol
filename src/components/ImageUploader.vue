<template lang="pug">
.ImageUploader
  .box
    .icon.icon-plus-thin
  VueUploadComponent.VueUploadComponent(
    ref="upload"
    v-model="files"
    :accept="accept"
    :name="name"
    :post-action="$state.urls.serverBase + '/file'"
    :drop="true"
    @input-file="inputFile"
    @input-filter="inputFilter"
  )
  .preview(v-if="src" @mouseenter="hovering=true" @mouseleave="hovering=false")
    img.preview-img(:src="src")
    .black-mask(v-show="hovering || uploading")
      .edit(v-show="!uploading")
        span.icon.icon-search(title="Preview" @click="preview")
        span.icon.icon-trash-o.mls(title="Remove" @click="remove")
      span(v-show="uploading") {{progress}}%
  Modal(
    v-if="modalVisible",
    :options="modalOptions",
    @close="modalClose", @ok="modalOk"
  )
    h4.modal-title(slot="title") {{title}}
    div
      img.editing-img(ref="editingImage" :src="files[0].url")
</template>

<script>
import VueUploadComponent from 'vue-upload-component'
import Modal from './Modal.vue'
import Cropper from 'cropperjs'
import 'cropperjs/dist/cropper.css'
import valueDetails from './valueDetails'
import { Base64 } from 'js-base64'

export default {
  mixins: [valueDetails],
  components: {VueUploadComponent, Modal},
  props: {
    name: {default: 'file'},
    extensions: {default: is => ["gif", "jpg", "jpeg", "png", "webp"]},
    aspectRatio: {},
  },
  data() {
    return {
      // preview
      hovering: false,
      editVisible: false,
      src: null,
      files: [],
      uploading: false,
      progress: 0,
      // modal
      modalVisible: false,
      title: '',
      modalOptions: {
        size: 'lg',
        closeWhenClickBack: false,
        okText: "Save",
        closeText: "Cancel",
      },
    }
  },
  computed: {
    accept() {
      return this.extensions.map(v => `image/${v}`).join(',')
    },
  },
  watch: {
    modalVisible: {
      immediate: true,
      handler(value) {
        if (value) {
          this.$nextTick(() => {
            if (!this.$refs.editingImage) {
              return
            }
            const cropper = new Cropper(this.$refs.editingImage, {
              aspectRatio: this.aspectRatio,
              viewMode: 1,
              crop: (e) => {
                const {width, height} = e.detail
                this.title = `Crop ${Math.ceil(width)}x${Math.ceil(height)}`
              }
            })
            this.cropper = cropper
          })
        } else {
          if (this.cropper) {
            this.cropper.destroy()
            this.cropper = null
          }
        }
      }
    },
  },
  methods: {
    getAbsUrl(value) {
      return value ? value.replace('~', `${this.$state.urls.serverBase}/file`) : null
    },
    getValueDetails(value) {
      this.src = this.getAbsUrl(value)
    },
    modalClose () {
      this.modalVisible = false
    },
    inputFile(newFile, oldFile) {
      // when add
      if (newFile && !oldFile) {
        this.$nextTick(function () {
          this.modalVisible = true
        })
      }
      // when remove, 删除时, 仅当选择新文件同时旧文件自动删除才触发此
      if (!newFile && oldFile) {
        this.modalVisible = false
      }
      // uploading
      if (this.uploading) {
        if (newFile.active) {
          this.progress = Math.ceil(newFile.progress)
        } else {
          this.uploading = false
          if (newFile.success) {
            this.$notification.success(`The file was uploaded successfully`)
            this.$emit('input', newFile.response.data)
          } else {
            this.$alert(`Upload Failed. ${newFile.response.data.message || ''}`)
            this.src = this.getAbsUrl(this.value) // restore src
          }
        }
      }
    },
    inputFilter(newFile, oldFile, prevent) {
      if (newFile && !oldFile) {
        const reg = RegExp(`\.(${this.extensions.join('|')})$`, 'i')
        if (!reg.test(newFile.name)) {
          this.$alert('Your choice is not a picture')
          return prevent()
        }
      }
      if (newFile && (!oldFile || newFile.file !== oldFile.file)) {
        newFile.url = ''
        let URL = window.URL || window.webkitURL
        if (URL && URL.createObjectURL) {
          newFile.url = URL.createObjectURL(newFile.file)
        }
      }
    },
    modalOk () {
      const oldFile = this.files[0]
      const base64Str = this.cropper.getCroppedCanvas().toDataURL(oldFile.type).split(',')[1]
      this.src = `data:${oldFile.type};base64,${base64Str}`
      const binStr = Base64.atob(base64Str)
      const arr = new Uint8Array(binStr.length)
      for (let i = 0; i < binStr.length; i++) {
        arr[i] = binStr.charCodeAt(i)
      }
      const file = new File([arr], oldFile.name, { type: oldFile.type })
      this.$refs.upload.update(oldFile.id, {
        file,
        type: file.type,
        size: file.size,
        active: true,
      })
      this.modalVisible = false
      this.uploading = true
      this.progress = 0
    },
    preview() {
      window.open(this.src)
    },
    remove() {
      this.$emit('input', null)
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.ImageUploader{
  display: inline-block;
  position: relative;
  flex-shrink: 0;
  $side: 100px;
  .box{
    width: $side;
    height: $side;
    line-height: $side;
    display: inline-block;
    border: $bd1 dashed 2px;
    text-align: center;
  }
  .preview{
    @extend %mask;
  }
  .preview-img{
    width: $side;
    height: $side;
  }
  .black-mask{
    @extend %mask;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    .edit{
      display: none;
      font-size: 1.7em;
      .icon{
        cursor: pointer;
      }
    }
    &:hover{
      .edit{
        display: block;
      }
    }
  }
  .icon-plus-thin{
    font-size: 30px;
    color: $bd1;
  }
  .VueUploadComponent{
    @extend %mask;
    opacity: 0;
    margin: 0;
    cursor: pointer;
  }
  .editing-img{
    max-width: 100%;
  }
}
</style>
