<template lang="pug">
.CreateCourse9a.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group.top3
        Checkbox.top3
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span
        span.top3 Others
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span
        span.top3 Others
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
        span Others
      .form-group.top3
        Checkbox.top3
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span
        span.top3 Others
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.top3.span
        span.top3 Others
        select.top3.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
        span Others
    
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
.CreateCourse9a{
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
    top: 33px;
  }
  .top3.span{
    margin-top: -20px;
  }
}
</style>
