<template lang="pug">
.ImageUploader
  .icon.icon-plus
  VueUploadComponent.VueUploadComponent(
    v-model="files"
    extensions="gif,jpg,jpeg,png,webp"
    accept="image/png,image/gif,image/jpeg,image/webp"
    name="images"
    post-action="http://127.0.0.1:8081/api/v1/file"
  )
  Modal.Alert(
    v-if="modalVisible",
    :options="modalOptions",
    @close="modalClose", @ok="modalOk"
  )
</template>

<script>
import VueUploadComponent from 'vue-upload-component'
import Modal from './Modal.vue'

export default {
  components: {VueUploadComponent, Modal},
  data() {
    return {
      files: [],
      modalVisible: true,
      modalOptions: {
        size: 'lg',
        closeWhenClickBack: false,
        headerVisible: false,
        footerVisible: false,
      },
    }
  },
  // computed: {},
  // watch: {},
  methods: {
    modalOk () {
      this.modalVisible = false
    },
    modalClose () {
      this.modalVisible = false
    }
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.ImageUploader{
  $side: 100px;
  width: $side;
  height: $side;
  line-height: $side;
  display: inline-block;
  border: $bd1 dashed 2px;
  text-align: center;
  position: relative;
  flex-shrink: 0;
  .icon-plus{
    font-size: 30px;
    color: $bd1;
  }
  .VueUploadComponent{
    @extend %transparentMask;
    margin: 0;
  }
}
</style>
