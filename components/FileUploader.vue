<template lang="pug">
.file-uploader
  .file-uploader__upload-btn-wrapper
    el-button.file-uploader__upload-btn(:type="file ? 'primary' : 'info'") {{buttonText}} <i class="el-icon-upload el-icon--right"></i>
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
    )
    .progress(v-if="uploading")
      span {{progress}}%
  el-input.mls.file-uploader__file-name(v-if="file" :value="file.name")
</template>

<script>
import BaseUploader2 from './BaseUploader2'
import valueDetails from './valueDetails'

export default {
  mixins: [valueDetails],
  extends: BaseUploader2,
  components: {},
  props: {
    name: {default: 'file'},
    buttonText: {default: 'Select File'},
  },
  data() {
    return {
      files: [],
      progress: 0,
      url: null,
    }
  },
  computed: {
    file() {
      return this.files && this.files[0]
    },
  },
  watch: {
  },
  methods: {
    getValueDetails(value) {
      this.url = this.getAbsUrl(value)
    },
    added(newFile) {
      this.startUploadFile(newFile)
    },
    uploadProcessing(newFile) {
      this.progress = newFile.progress.slice(0, -3)
    },
    failed(newFile) {
      this.url = this.getAbsUrl(this.value) // restore url
    },
    success(newFile) {
      this.$emit('input', newFile.response.data)
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";

.file-uploader{
  display: flex;
  .VueUploadComponent{
    @include mask;
    opacity: 0;
    margin: 0;
    cursor: pointer;
  }
  .progress{
    @include mask;
    background: rgba(0, 0, 0, 0.3);
    color: #fff;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
.file-uploader__upload-btn-wrapper{
  position: relative;
}
</style>
