<template lang="pug">
.multiple-image-uploader
  .arrow.left-arrow(:style="arrowStyle")
    Icon(name="angle-left" :class="{disabled: boxesInnerLeft >= 0 }" @click="showLeft")
  .boxes(ref="boxes" :style="boxesStyle")
    .boxes-inner(:style="boxesInnerStyle")
      VueUploadComponent.VueUploadComponent(
        :inputId="inputId"
        ref="upload"
        v-model="files"
        :accept="accept"
        :name="name"
        :post-action="action"
        :drop="true"
        @input-file="inputFile"
        @input-filter="inputFilter"
        :maximum="maximum"
        :thread="thread"
        :multiple="true"
      )
      .preview(v-for="(item, index) in files" :index="index"  :style="getBoxStyle()")
        img.preview-img(:src="item.url" :style="item.imgStyle" @load="imgLoaded(item, index)")
        .black-mask
          .edit(v-show="!item.active")
            Icon(name="search" title="Preview" @click="preview(item, index)")
            Icon.mls(name="trash" title="Remove" @click="remove(item, index)")
          span(v-if="!item.simulated" v-show="item.active") {{item.progress.replace(/\..+$/, '')}}%
      .box(v-for="i in uploadBoxCount" :style="getBoxStyle(i)")
        Icon(name="plus-thin")
  .arrow.right-arrow(:style="arrowStyle")
    Icon(name="angle-right" :class="{disabled: boxesInnerLeft <= minBoxesInnerLeft }"  @click="showRight")
</template>

<script>
import BaseUploader2 from './BaseUploader2'
import valueDetails from './valueDetails'

const ui = {
  props: {
    visibleBlockCount: {default: 3},
    boxWidth: {default: 100},
    boxHeight: {default: 100},
    boxSpace: {}, // if boxSpace != null, boxesWidth will be assigned by computed, else boxes' initial width
  },
  data() {
    return {
      boxesWidth: null,
      boxesInnerLeft: 0,
      boxesStyle: {width: null},
    }
  },
  computed: {
    uploadBoxCount() {
      const r =  this.visibleBlockCount - this.files.length
      if (r > 0) {
        return  r
      } else {
        return 1
      }
    },
    space() {
      if (this.boxSpace != null) {
        return this.boxSpace
      }
      const {boxesWidth, boxWidth, visibleBlockCount} = this
      return Math.floor((boxesWidth - boxWidth * visibleBlockCount) / (visibleBlockCount - 1))
    },
    arrowStyle() {
      return {
        height: this.boxHeight + 'px',
        lineHeight: this.boxHeight + 'px',
      }
    },
    boxesInnerWidth() {
      const n = (this.boxWidth + this.space) * (this.files.length + this.uploadBoxCount) - this.space
      return n < this.boxesWidth ? this.boxesWidth : n
    },
    boxesInnerStyle() {
      return {
        left: this.boxesInnerLeft + 'px'
      }
    },
    minBoxesInnerLeft() {
      return -(this.boxesInnerWidth - this.boxesWidth)
    },
  },
  // watch: {},
  methods: {
    getBoxStyle(index) {
      return {
        width: this.boxWidth + 'px',
        height: this.boxHeight + 'px',
        lineHeight: this.boxHeight + 'px',
        marginRight: index === this.uploadBoxCount ? 0 : (this.space + 'px')
      }
    },
    showLeft() {
      const n = this.boxesInnerLeft + this.boxesWidth + this.space
      this.boxesInnerLeft = n >= 0 ? 0 : n
    },
    showRight() {
      const n = this.boxesInnerLeft - (this.boxesWidth + this.space)
      this.boxesInnerLeft = n <= this.minBoxesInnerLeft ? this.minBoxesInnerLeft : n
    },
  },
  mounted() {
    // if boxSpace != null, boxesWidth will be assigned by computed, else boxes' initial width
    this.$watch('boxSpace', (value) => {
      if (value) {
        this.boxesWidth = (this.boxWidth + value) * this.visibleBlockCount - value
        this.boxesStyle = {
          width: this.boxesWidth + 'px',
        }
      } else {
        this.boxesStyle = {
          width: 'auto',
          flexGrow: '1',
        }
        this.$nextTick(() => {
          this.boxesWidth = this.$refs.boxes.offsetWidth
        })
      }
    }, {immediate: true})
  },
}

export default {
  mixins: [valueDetails, ui],
  extends: BaseUploader2,
  components: {},
  props: {
    name: {default: 'file'},
    value: {required: true, type: Array},
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
  },
  methods: {
    getValueDetails(value) {
      this.files = value.map(v => {
        return {
          simulated: true, // not a fiel instance of VueUploadComponent, just a simulation
          initialUrl: v,
          url: v,
        }
      })
    },
    // a file uploaded or deleted
    filesChanged() {
      const {files} = this
      const arr = files.filter(v => !v.active && v.success && v.progress == 100).map(v => v.response.data || v.initialUrl)
      this.setValue(arr)
      this.$nextTick(() => {
        if (this.boxesInnerLeft > this.minBoxesInnerLeft) {
          this.showRight()
        }
      })
      setTimeout(() => {
        console.log(this.value);
      }, 300);
    },
    added(newFile) {
      let URL = window.URL || window.webkitURL
      if (URL && URL.createObjectURL) {
        newFile.url = URL.createObjectURL(newFile.file)
      }
      this.startUploadFile(newFile)
    },
    failed(newFile) {
      this.remove(newFile)
    },
    success(newFile) {
      newFile.url = newFile.response.data
      this.filesChanged(newFile)
    },
    imgLoaded(item, index) {
      const img = this.$el.querySelector(`.preview[index='${index}'] .preview-img`)
      if (img) {
        this.$set(item, 'imgStyle', {
          [img.naturalWidth > img.naturalHeight ? 'height' : 'width']: '100%'
        })
      }
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
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.multiple-image-uploader{
  display: flex;
  .boxes{
    display: inline-block;
    vertical-align: top;
    white-space: nowrap;
    overflow: hidden;
    position: relative;
  }
  .boxes-inner{
    position: absolute;
    transition: left .5s;
  }
  .box{
    display: inline-block;
    border: #ddd dashed 2px;
    text-align: center;
    position: relative;
    pointer-events: none;
  }
  .icon-plus-thin{
    font-size: 30px;
    color: #ddd;
  }
  .VueUploadComponent{
    @include mask;
    opacity: 0;
    margin: 0;
    cursor: pointer;
  }
  //
  .preview{
    position: relative;
    display: inline-block;
    overflow: hidden;
    border: 1px solid #ddd;
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
    @include mask;
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
  .box, .preview{
    vertical-align: top;
  }
  .box.last{
    margin-right: 0;
  }
  .arrow{
    width: 30px;
    flex-shrink: 0;
    text-align: center;
    .icon{
      font-size: 30px;
      cursor: pointer;
      color: #aaa;
      &:hover{
        color: #000;
      }
      &.disabled{
        cursor: not-allowed;
      }
    }
  }
}
</style>
