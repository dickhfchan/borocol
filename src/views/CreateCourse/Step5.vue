<template lang="pug">
.CreateCourse5
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form
        .form-group
          label What You’ll Provide?
          textarea.form-control(rows='5' placeholder='- Equipment\n- Airport Pickup\n- Towels ')
        .form-group
          label.left_span What Your Guest Needs to Bring?
          textarea.form-control(rows='5' placeholder='- Goggle\n- Swimsuits ')
      Tips
</template>

<script>
import base from './base'
export default {
  extends: base,
  // components: {},
  // data() {
  //   return {}
  // },
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
