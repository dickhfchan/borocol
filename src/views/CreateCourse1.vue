<template lang="pug">
.CreateCourse1.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group.has-feedback
        label Input with success
        input.form-control.input-lg(type='text')
        span.icon.icon-calendar.form-control-feedback

      .form-group
        label *Email address
        input.form-control.input-lg(type='email', placeholder='Email')
      .form-group
        label Password
        select.form-control.input-lg(placeholder='Password')
          option asfasg
          option help-block
          option Why
        span Duration: 4 Days 3 Nights
        textarea.form-control(rows='3')
        Checkbox
        span Option one is this and that—be sure to include why it's great
      .form-group
        label(for='exampleInputFile') File input
        input#exampleInputFile(type='file')
        p.help-block Example block-level help text here.
      .checkbox
        label
          input(type='checkbox')
          |  Check me out
      button.btn.btn-primary.btn-lg(type='submit') Submit
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
.CreateCourse1{}
</style>
