<template lang="pug">
include ../common.pug
.MyCourseVisaStep1PopupVisa
  .container
    .content-card.has-close
      .title Upload Files
      .content-card-body
        MultipleImageUploader.mtl.w-100(v-model="photos" :visibleBlockCount="4" :boxWidth="220" :boxHeight="310")
        .text-center
          button.submit-btn.btn.btn-primary.btn-lg Submit
      span.icon.icon-close.close
</template>

<script>
import MultipleImageUploader from '@/components/MultipleImageUploader';
export default {
  components: {MultipleImageUploader},
  data() {
    return {
      photos: [],
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.MyCourseVisaStep1PopupVisa{
  background: $bg3;
  .submit-btn{
    width: 420px;
    margin-top: 100px;
  }
  .title {
    font-size: 21px;
    color: rgb(51, 51, 51);
    text-align: center;
  }
}
</style>
