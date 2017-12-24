<template lang="pug">
.CreateCourse1.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      //- .form-group.has-feedback
      //-   label *Title
      //-   input.form-control.input-lg(type='text')
      //-   span.icon.icon-calendar.form-control-feedback
      .form-group
        label *Title
        input.form-control.input-lg(type='email', placeholder='5 Days Yoga Retreat in Bali')


      .form-group.inline
        label *Category
        select.form-control.input-lg(placeholder='Fitness & Sports - Yoya')
          option asfasg
          option help-block
          option Why
      .form-group.inline.rightside
        label *Level
        select.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.has-feedback.left
        label *Start Date
        input.form-control.input-lg(type='text')(placeholder='Sep 1, 2017')
        span.icon.icon-calendar.form-control-feedback
      .form-group.has-feedback.right
        label *End Date
        input.form-control.input-lg(type='text')(placeholder='Sep 13 2017')
        span.icon.icon-calendar.form-control-feedback
      span.middle Duration: 4 Days 3 Nights

      span.left_span What Will We Do? (Description)
      textarea.form-control(rows='3')(placeholder='We will go to Rain Forest to hunt….')


      //- Checkbox
      //- span Option one is this and that—be sure to include why it's great
      //- .form-group
      //-   label(for='exampleInputFile') File input
      //-   input#exampleInputFile(type='file')
      //-   p.help-block Example block-level help text here.
      //- .checkbox
      //-   label
      //-     input(type='checkbox')
      //-     |  Check me out
      //- button.btn.btn-primary.btn-lg(type='submit') Submit
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
.CreateCourse1{
  .has-feedback{
  width: 32%;
  display: inline-block;
  margin-right: 15px;
   .right{
     flot:left;
   }
  }
  .left_span{
  flot:left;
  }
  .middle{
     width: 30%;
     display: inline-block;
     height: 90px;
     float: right;
     text-align: right;
     padding-top: 30px;
  }
  .inline{
  width: 65%;
  display: inline-block;
  }
  .rightside{
  width:33%;
  margin-left:2%;
  }

}
</style>
