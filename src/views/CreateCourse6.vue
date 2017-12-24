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
        span.left_span Number of hours
        textarea.form-control(rows='3')(placeholder='Selena is a….')
      .form-group
        span.left_span *Will you issue Certificate to your guest?
        Checkbox
        span.left_span yes
        Checkbox
        span.left_span no
      .form-group
        Checkbox.l
        span.l Question 1 :
        textarea.form-control.txt(rows='3')(placeholder='Selena is a….')
      .form-group
        Checkbox.l
        span.l Question 2 :
        textarea.form-control.txt(rows='3')(placeholder='Selena is a….')
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
  .l {
    float: left;
    margin-top: 20px;
  }

  .txt {
      width: 80%;
      /* margin-left: 10%; */
      margin-left: 125px;
  }
}
</style>
