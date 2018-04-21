<template lang="pug">
.image-uploader
  .box
    Icon(name="plus-thin")
    span.title.mtm(v-if="title") {{title}}
  VueUploadComponent.VueUploadComponent(
    :inputId="inputId"
    ref="upload"
    v-model="files"
    :accept="accept"
    :name="name"
    :post-action="$store.state.api + '/file/store'"
    :drop="true"
    @input-file="inputFile"
    @input-filter="inputFilter"
  )
  .preview(v-if="src" @mouseenter="hovering=true" @mouseleave="hovering=false")
    img.preview-img(:src="src")
    .black-mask(v-show="hovering || uploading")
      .edit(v-show="!uploading")
        Icon(name="search" title="Preview" @click.native="preview")
        Icon.mls(name="trash" title="Remove" @click.native="remove")
      span(v-show="uploading") {{progress}}%
  el-dialog(
    :title="modalTitle"
    :visible.sync="modalVisible"
  )
    div
      img.editing-img(ref="editingImage" :src="files[0] && files[0].url")
    div(slot="footer")
      el-button(@click="modalClose" size="small") Cancel
      el-button.mlm(type="primary" @click="modalOk" size="small") Ok
</template>

<script>
import BaseUploader2 from './BaseUploader2'
import Cropper from 'cropperjs'
import 'cropperjs/dist/cropper.css'
import valueDetails from './valueDetails'
import { Base64 } from 'js-base64'

export default {
  mixins: [valueDetails],
  extends: BaseUploader2,
  components: {},
  props: {
    name: {default: 'file'},
    extensions: {default: is => ["gif", "jpg", "jpeg", "png", "webp"]},
    aspectRatio: {},
    title: {},
  },
  data() {
    return {
      inputId: `VueUploadComponent_${this._uid}`,
      // preview
      hovering: false,
      editVisible: false,
      src: null,
      files: [],
      progress: 0,
      // modal
      modalVisible: false,
      modalTitle: '',
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
                this.modalTitle = `Crop ${Math.ceil(width)}x${Math.ceil(height)}`
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
      this.src = this.getAbsUrl(value)
    },
    modalClose () {
      this.modalVisible = false
    },
    added(newFile) {
      let URL = window.URL || window.webkitURL
      if (URL && URL.createObjectURL) {
        newFile.url = URL.createObjectURL(newFile.file)
      }
      this.$nextTick(function () {
        this.modalVisible = true
      })
    },
    removed() {
      this.modalVisible = false
    },
    uploadProcessing(newFile) {
      this.progress = newFile.progress.slice(0, -3)
    },
    failed(newFile) {
      this.src = this.getAbsUrl(this.value) // restore src
    },
    success(newFile) {
      this.$emit('input', newFile.response.data)
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
      this.progress = 0
    },
    preview() {
      this.hovering = false
      window.open(this.src)
    },
    remove() {
      this.hovering = false
      this.$emit('input', null)
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
$border: #ddd;
.image-uploader{
  display: inline-block;
  position: relative;
  flex-shrink: 0;
  width: 100px;
  height: 100px;
  .box{
    width: 100%;
    height: 100%;
    display: inline-block;
    border: $border dashed 2px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    .title{
      color: #888888;
    }
  }
  .icon-plus-thin{
    font-size: 40px;
    color: $border;
  }
  .preview{
    @include mask;
    border: 1px solid $border;
  }
  .preview-img{
    width: 100%;
    height: 100%;
  }
  .black-mask{
    @include mask;
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
  .VueUploadComponent{
    @include mask;
    opacity: 0;
    margin: 0;
    cursor: pointer;
  }
  .editing-img{
    max-width: 100%;
  }
}
</style>
