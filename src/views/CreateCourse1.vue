<template lang="pug">
.CreateCourse1.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body.row
      //- .form-group.has-feedback
      //-   label *Title
      //-   input.form-control.input-lg(type='text')
      //-   span.icon.icon-calendar.form-control-feedback
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
          span Duration: 4 Days 3 Nights

      .form-group.col-sm-12
        label What Will We Do? (Description)
        textarea.form-control(rows='5' placeholder='We will go to Rain Forest to hunt….')
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
.CreateCourse1{
  .duration{
    text-align: right;
    span{
      padding: $formControlVerticalPadding-lg 0;
      line-height: 1em;
      display: block;
    }
  }
}
</style>
