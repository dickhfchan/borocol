<template lang="pug">
button.UploadBtn
  span(v-if="uploading") Uploading {{files[0].progress.slice(0, -3)}}%
  span(v-else) Upload File
  VueUploadComponent.VueUploadComponent.man(
    :inputId="inputId"
    ref="upload"
    v-model="files"
    :accept="accept"
    :name="name"
    :post-action="$state.urls.serverBase + '/file'"
    :drop="true"
    @input-file="inputFile"
    @input-filter="inputFilter"
  )
</template>

<script>
import BaseUploader2 from './BaseUploader2'
import valueDetails from './valueDetails'
export default {
  mixins: [valueDetails],
  extends: BaseUploader2,
  // props: {},
  // components: {},
  // data() {
  //   return {
  //   }
  // },
  // computed: {},
  // watch: {},
  methods: {
    added(file) {
      this.startUploadFile(file)
    },
    succeeded(file) {
      this.$emit('input', file.response.data)
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.UploadBtn{
  @include btnColors(rgb(151, 151, 151), #fff);
  font-weight: bold;
  width: 200px;
  position: relative;
  .VueUploadComponent{
    @extend %mask;
  }
}
</style>
