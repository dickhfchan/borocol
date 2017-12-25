<template lang="pug">
.CreateCourse9b.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group.top3.l
        Checkbox.top3
        select.top3.form-control.input-lg(placeholder='Shared Room')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span.m
        span.top3 Quota
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span.r
        span.Price Price
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
        span.r USD
      .form-group.top3.l
        Checkbox.top3
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span.m
        span.top3 Quota
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span.r
        span.Price Price
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
        span.r USD
      .form-group.has-feedback.left
        label *Registration Start Date
        input.form-control.input-lg(type='text')(placeholder='')
        span.i1.icon.icon-calendar.form-control-feedback
      .form-group.has-feedback.right
        label *Registration End Date
        input.form-control.input-lg(type='text')(placeholder='')
        span.icon.icon-calendar.form-control-feedback
          //- todo
          //-   todo
          //-     todo
      .form-group.block.Early
        Checkbox.l
        span.l *Early Bird Discount copy
      .form-group.block.middle1
        span.l Discount Rate
        select.form-control.input-lg.option(placeholder='10% off copy')
          option asfasg
          option help-block
          option Why
      .form-group.block.middle2
        span.l  Quota
        select.form-control.input-lg.option(placeholder='')
          option asfasg
          option help-block
          option Why
      .form-group.block.Down
        Checkbox.l
        span.l Down Payment 25%  copy
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
.CreateCourse9b{
  .option {
      width: 30%;
      float: left;
  }

  .block {
      width: 75%;
      height: 50px;
      /* line-height: 50px; */
  }

  .form-group.left {
      width: 49%;
      position: relative;
      left: 0;
      top: 0px;
  }

  .form-group.right {
      width: 47%;
      float: right;
      position: relative;
      left: -1%;
      top: -86px;
  }

  .l {
    float: left;
    margin-right: 15px;
  }

  span.l {
      line-height: 50px;
  }
  .form-group.middle1 {
    width: 40%;
    position: relative;
    top: -48px;
    left: 37%;
  }
  .form-group.middle2 {
    width: 40%;
    position: relative;
    top: -105px;
    left: 72%;
  }
  .Checkbox.l {
    margin-top: 15px;
  }
  .form-group.block.Down {
    /* position: initial; */
    /* left: 0px; */
    /* top: -50px; */
    float: left;
    margin-top: -130px;
  }

  .form-group.block.Early {
      /* margin-top: 4px; */
      padding-top: 25px;
  }
  .form-group.top3 {
    width: 25%;
    float: left;
    margin-right: 50px;
  }

  select.top3 {
      width: 70%;
      float: right;
  }

  .Checkbox.top3 {
      margin-top: 12px;
  }

  span.top3 {
    position: relative;
    left: -20px;
    top: 15px;
  }
  span.r{
    position: relative;
    left: 80%;
    top: -30px;
  }
  span.i1{
    top:147px;
  }
  span.Price {
    position: relative;
    top: -33px;
  }
  span.i1{
    top: 185px;
  }
}
</style>
