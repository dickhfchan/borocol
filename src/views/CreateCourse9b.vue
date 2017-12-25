<template lang="pug">
.CreateCourse9b.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body.row
      .form-group.col-sm-4
        Checkbox.top3
        select.top3.form-control.input-lg(placeholder='Shared Room')
          option asfasg
          option help-block
          option Why
      .form-group.col-sm-3
        span.top3 Quota
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.col-sm-4
        span.Price Price
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
        span.r USD
      .form-group.col-sm-4
        Checkbox.top3
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.col-sm-3
        span.top3 Quota
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.col-sm-4
        span.Price Price
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
        span.r USD
      .form-group.has-feedback.col-sm-6
        label *Registration Start Date
        input.form-control.input-lg(type='text')(placeholder='')
        span.i1.icon.icon-calendar.form-control-feedback
      .form-group.has-feedback.col-sm-6
        label *Registration End Date
        input.form-control.input-lg(type='text')(placeholder='')
        span.icon.icon-calendar.form-control-feedback
          //- todo
          //-   todo
          //-     todo
      .col-sm-4
        Checkbox
        span *Early Bird Discount copy
      .form-group.col-sm-4
        span Discount Rate
        select.form-control.input-lg(placeholder='10% off copy')
          option asfasg
          option help-block
          option Why
      .form-group.col-sm-4
        span  Quota copy
        select.form-control.input-lg(placeholder='')
          option asfasg
          option help-block
          option Why
      .col-sm-12
        Checkbox
        span Down Payment 25%  copy
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

}
</style>
