<template lang="pug">
.CreateCourse6.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group
        label Guest Requirement
        textarea.form-control(rows='3' placeholder='Selena is a….')
      .form-group
        label *Will you issue Certificate to your guest?
        Checkbox.mls
        span.mls No
        Checkbox.mls
        span.mls Yes
      ._1
        .form-group
          Checkbox
          span.mls Question 1 :
          textarea.form-control.mls(rows='3')
          .clearfix
        .form-group
          Checkbox
          span.mls Question 2 :
          textarea.form-control.mls(rows='3')
          .clearfix
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
.CreateCourse6{
  ._1{
    textarea{
      width: 80%;
      float: right;
      display: inline-block;
    }
  }
}
</style>
