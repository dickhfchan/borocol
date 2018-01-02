<template lang="pug">
.CreateCourse9b.container
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips.row
      ._1.col-sm-12
        .form-group
          Checkbox
          select.form-control.mlm
            option Shared Room
          label.mll Quota
          input.form-control.quota-input.mls(type="number")
          label.mll Price
          input.form-control.price-input.mls(type="number")
          span.help-block2.mlm.grey USD
        .form-group
          Checkbox
          select.form-control.mlm
            option Standard Room
          label.mll Quota
          input.form-control.quota-input.mls(type="number")
          label.mll Price
          input.form-control.price-input.mls(type="number")
          span.help-block2.mlm.grey USD
      .mtm &nbsp;
      .col-sm-6
        .form-group.has-feedback
          label *Registration Start Date
          input.form-control.input-lg(type='text' placeholder='')
          span.icon.icon-calendar.form-control-feedback
      .col-sm-6
        .form-group.has-feedback
          label *Registration Start Date
          input.form-control.input-lg(type='text' placeholder='')
          span.icon.icon-calendar.form-control-feedback
      .form-group.col-sm-12.additional
        .title
          .line
          span Additional
          .line
        .line1
          Checkbox
          label.mls *Early Bird Discount copy
          span.icon.icon-question-circle.mlm
          label.mll Discount Rate
          select.form-control.mls(placeholder='')
            option 10% off copy
            option 20% off copy
          label.mll Quota
          select.form-control.mls(placeholder='')
            option 10% off copy
            option 20% off copy
        .line2
          Checkbox
          label.mls Down Payment 25%
          span.icon.icon-question-circle.mlm
      Tips
</template>

<script>
import Tips from './Tips.vue'
export default {
  components: {Tips},
  data() {
    return {
      state: this.$state.createCourse,
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
.CreateCourse9b{
  ._1{
    select{
      display: inline-block;
      width: 200px;
    }
    .quota-input{
      display: inline-block;
      width: 100px;
    }
    .price-input{
      display: inline-block;
      width: 150px;
    }
    // input, select{
    //   display: inline-block;
    // }
    // select{
    //   width: auto;
    // }
    .icon{
      color: #ccc;
      font-size: 1.4em;
    }
  }
  .additional{
    .title{
      font-size: $fs-title * 0.8;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 20px 0;
      .line{
        height: 1px;
        width: 35%;
        background: $bd1;
      }
    }
    input, select{
      display: inline-block;
      width: auto;
    }
    .line1{
      // display: flex;
      // justify-content: space-between;
      // align-items: center;
    }
    .icon{
      color: #ccc;
      font-size: 1.4em;
    }
  }
}
</style>
