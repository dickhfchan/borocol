<template lang="pug">
.CreateCourse1
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form.row
        .form-group.col-sm-12
          label *Title
          input.form-control.input-lg(type='email', placeholder='5 Days Yoga Retreat in Bali')


        .form-group.col-sm-8
          label *Category
          select.form-control.input-lg(placeholder='Fitness & Sports - Yoya')
            option asfasg
            option help-block
            option Why
        .form-group.col-sm-4
          label *Level
          select.form-control.input-lg(placeholder='Beginner')
            option asfasg
            option help-block
            option Why
        .col-sm-4
          .form-group.has-feedback
            label *Start Date
            input.form-control.input-lg(type='text' placeholder='Sep 1, 2017')
            span.icon.icon-calendar.form-control-feedback
        .col-sm-4
          .form-group.has-feedback
            label *End Date
            input.form-control.input-lg(type='text' placeholder='Sep 13 2017')
            span.icon.icon-calendar.form-control-feedback
        .col-sm-4.duration
          .form-group
            label &nbsp;
            .help-block2.duration 4 Days 3 Nights

        .form-group.col-sm-12
          label What Will We Do? (Description)
          textarea.form-control(rows='5' placeholder='We will go to Rain Forest to hunt….')
      Tips
</template>

<script>
import base from './base'
export default {
  extends: base,
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCourse1{
  .duration{
    text-align: right;
  }
}
</style>
