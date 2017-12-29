<template lang="pug">
.CreateCourse7.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group
        label Tags
        textarea.form-control(rows='3' placeholder='')
      .form-group
        label Upload Photos (Min. 3)
        p todo 
      .form-group
        label Notes
        textarea.form-control(rows='3' placeholder='')
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
.CreateCourse7{}
</style>
