<template lang="pug">
.CreateCourse5.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      span.left_span What You’ll Provide?
      textarea.form-control(rows='3')(placeholder='- Equipment - Airport Pickup - Towels ')
      span.left_span What Your Guest Needs to Bring?
      textarea.form-control(rows='3')(placeholder='- Goggle - Swimsuits ')
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
