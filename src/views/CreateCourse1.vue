<template lang="pug">
.CreateCourse1.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group
        label(for='exampleInputEmail1') Email address
        input#exampleInputEmail1.form-control(type='email', placeholder='Email')
      .form-group
        label(for='exampleInputPassword1') Password
        input#exampleInputPassword1.form-control(type='password', placeholder='Password')
      .form-group
        label(for='exampleInputFile') File input
        input#exampleInputFile(type='file')
        p.help-block Example block-level help text here.
      .checkbox
        label
          input(type='checkbox')
          |  Check me out
      button.btn.btn-default(type='submit') Submit
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
