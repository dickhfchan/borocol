<template lang="pug">
.ImageUploader
  .box
    img.preview(v-if="src" :src="src")
    .icon.icon-plus(v-else)
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
  .edit(@click="remove" v-show="src && !modalVisible && !uploading") Remove
  .progress-mask(v-show="uploading")
    span {{progress}}%
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
    getValueDetails(value) {
      this.src = value ? `${this.$state.urls.serverBase}/file/${value}` : null
    },
    modalClose () {
      this.modalVisible = false
    },
    inputFile(newFile, oldFile, prevent) {
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
      if (this.uploading) {
        if (newFile.error) {
          this.uploading = false
          this.$alert(`Upload Failed. ${newFile.response.message}`)
          this.src = this.value // restore src
        } else {
          this.progress = Math.ceil(newFile.progress)
          if (this.progress === 100 && newFile.success) {
            this.$notification.success(`The file was uploaded successfully`)
            this.uploading = false
            this.$emit('input', newFile.response.data)
          }
        }
      }
    },
    modalOk () {
      const oldFile = this.files[0]
      const base64Str = this.cropper.getCroppedCanvas().toDataURL(oldFile.type).split(',')[1]
      this.src = `data:${oldFile.type};base64,${base64Str}`
      const binStr = Base64.decode(base64Str)
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
  .box{
    $side: 100px;
    width: $side;
    height: $side;
    line-height: $side;
    display: inline-block;
    border: $bd1 dashed 2px;
    text-align: center;
    .preview{
      @extend %mask;
      width: 100%;
      height: 100%;
    }
  }
  .edit{
    display: none;
    padding: .5em;
    text-align: center;
    background-color: rgba(0,0,0,0.5);
    color: #fff;
    font-weight: $fw-md;
    cursor: pointer;
    position: absolute;
    width: 100%;
    left: 0;
    bottom: 0;
  }
  &:hover{
    .edit{
      display: block;
    }
  }
  .progress-mask{
    @extend %mask;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .icon-plus{
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
