<template lang="pug">
.CreateCourse9a.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body.row
      ._1.col-sm-12
        .form-group
          label *How many seats available on Borocol
          span.icon.icon-question-circle.mlm
          input.form-control.mlm(type='number' placeholder='')
        .form-group
          label *Price (13% service charge is included)
          span.icon.icon-question-circle.mlm
          input.form-control.mlm(type='number' placeholder='')
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
</template>

<script>
export default {
  components: {},
  data() {
    return {}
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
.CreateCourse9a{
  ._1{
    input{
      display: inline-block;
      width: 120px;
    }
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
