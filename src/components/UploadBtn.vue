<template lang="pug">
Btn.UploadBtn
  template(v-if="upload")
    span(v-if="upload.uploading") Uploading {{upload.progress}}%
    span(v-else) Upload File
  BaseUploader(ref="upload" v-model="value2" @input="$emit('change', $event)" :extensions="extensions" :mimes="mimes" :filter="filter")
</template>

<script>
import BaseUploader from './BaseUploader'
export default {
  props: {
    value: {},
    extensions: {default: is => []},
    mimes: {},
    filter: {},
  },
  components: {BaseUploader},
  data() {
    return {
      upload: null,
    }
  },
  computed: {
    value2: {
      get() { return this.value },
      set(value) { this.$emit('input', value) },
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    this.upload = this.$refs.upload
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.UploadBtn{
  @include btnColors(rgb(151, 151, 151), #fff);
  font-weight: bold;
  width: 200px;
  position: relative;
}
</style>
