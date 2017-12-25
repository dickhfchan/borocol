<template lang="pug">
.CreateCourse5.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      span.left_span Number of hours
      textarea.form-control(rows='3' placeholder='Selena is a….')
      span.left_span Number of hours
      textarea.form-control(rows='3' placeholder='Selena is a….')
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
.CreateCourse5{}
</style>
