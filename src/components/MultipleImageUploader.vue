<template lang="pug">
.MultipleImageUploader
  .preview(v-for="(item, index) in files" :index="index")
    img.preview-img(:src="item.url" :style="item.imgStyle" @load="imgLoaded(item, index)")
    .black-mask
      .edit(v-show="!item.active")
        span.icon.icon-search(title="Preview" @click="preview(item, index)")
        span.icon.icon-trash-o.mls(title="Remove" @click="remove(item, index)")
      span(v-if="!item.simulated" v-show="item.active") {{item.progress.replace(/\..+$/, '')}}%
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
      :maximum="maximum"
      :thread="thread"
      :multiple="true"
    )
  .clearfix
</template>

<script>
import VueUploadComponent from 'vue-upload-component'
import valueDetails from './valueDetails'
export default {
  extends: valueDetails,
  components: {VueUploadComponent},
  props: {
    name: {default: 'file'},
    value: {},
    extensions: {default: is => ["gif", "jpg", "jpeg", "png", "webp"]},
    maximum: {default: 20},
    thread: {default: 3},
  },
  data() {
    return {
      files: [],
    }
  },
  computed: {
    accept() {
      return this.extensions.map(v => `image/${v}`).join(',')
    },
    boxCount() {
      const r =  4 - this.files.length
      if (r > 0) {
        return  r
      } else {
        return 1
      }
    },
  },
  methods: {
    getAbsUrl(value) {
      return value ? value.replace('~', `${this.$state.urls.serverBase}/file`) : null
    },
    getValueDetails(value) {
      this.files = value.map(v => {
        return {
          simulated: true, // not a fiel instance of VueUploadComponent, just a simulation
          initialUrl: v,
          url: this.getAbsUrl(v),
        }
      })
    },
    // a file uploaded or deleted
    filesChanged() {
      const {files} = this
      const arr = files.filter(v => !v.active && v.success && v.progress == 100).map(v => v.response.data || v.initialUrl)
      this.setValue(arr)
      setTimeout(() => {
        console.log(this.value);
      }, 300);
    },
    inputFile(newFile, oldFile) {
      // when add
      if (newFile && !oldFile) {
        newFile.active = true
        console.log('upload start')
      }
      // when remove, 删除时, 仅当选择新文件同时旧文件自动删除才触发此
      if (!newFile && oldFile) {
      }
      if (newFile) {
        // uploading
        if (newFile.active) {
        } else {
          if (newFile.error) {
            console.log('upload failed');
            this.remove(newFile)
            this.$alert(`Upload Failed. ${newFile.response.data.message || ''}`)
          } else if (newFile.success && newFile.progress == 100) {
            console.log('upload succeeded')
            this.$notification.success(`The file was uploaded successfully`)
            newFile.url = this.getAbsUrl(newFile.response.data)
            this.filesChanged(newFile)
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
    imgLoaded(item, index) {
      const img = this.$el.querySelector(`.preview[index='${index}'] .preview-img`)
      this.$set(item, 'imgStyle', {
        [img.naturalWidth > img.naturalHeight ? 'height' : 'width']: '100%'
      })
    },
    preview(item, index) {
      window.open(item.url)
    },
    remove(item, index) {
      if (item.simulated) {
        this.files.splice(index, 1)
      } else {
        this.$refs.upload.remove(item)
      }
      this.filesChanged(item)
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.MultipleImageUploader{
  $side: 100px;
  .box{
    width: $side;
    height: $side;
    line-height: $side;
    display: inline-block;
    border: $bd1 dashed 2px;
    text-align: center;
    position: relative;
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
  //
  .preview{
    position: relative;
    width: $side;
    height: $side;
    display: inline-block;
    overflow: hidden;
    &:hover{
      .black-mask{
        display: flex;
      }
    }
  }
  .preview-img{
    position: absolute;
  }
  .black-mask{
    @extend %mask;
    display: none;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    font-weight: bold;
    justify-content: center;
    align-items: center;
    .edit{
      font-size: 1.7em;
      .icon{
        cursor: pointer;
      }
    }
  }
  //
  $space: .5em;
  .box, .preview{
    vertical-align: top;
    margin-right: $space;
    margin-bottom: $space;
  }
  margin-right: $space;
  margin-bottom: -$space;
  .box.last{
    margin-right: 0;
  }
}
</style>
