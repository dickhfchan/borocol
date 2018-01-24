<template lang="pug">
include ../common.pug
.RequestRefund
  .container
    .content-card.has-close
      .title Request Refund
      form.content-card-body
        .form-group
          label Please state your request reason:
          +textarea(rows="15")
          button.send-btn.btn.btn-primary.btn-lg.mtl.pull-right Send
          .clearfix
      span.icon.icon-close.close
</template>

<script>
import Popover from '@/components/Popover'
export default {
  components: {Popover},
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
.RequestRefund{
  background: $bg3;
  .title {
    font-size: 21px;
    color: rgb(51, 51, 51);
    text-align: center;
  }
  .content-card-body{
    margin-top: 50px;
  }
  .send-btn{
    padding: 15px;
    width: 150px;
  }
}
</style>
