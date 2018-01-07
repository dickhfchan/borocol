<template lang="pug">
.CreateCourse7
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form
        .form-group
          label Tags
          textarea.form-control(rows='3' placeholder='')
        .form-group
          label Upload Photos (Min. 3)
          p todo
        .form-group
          label Notes
          textarea.form-control(rows='3' placeholder='')
      Tips
</template>

<script>
import base from './base'
export default {
  extends: base,
  // components: {},
  data() {
    const state = this.$state.createCourse;
    const {fields, validations} = state
    const name = state.pageOrder[state.getRouteIndex()]
    return {
      name,
      fields: fields[name],
      validation: validations[name],
    }
  },

  // computed: {},
  // watch: {},
  // methods: {},
  created() {
    this.$validate(this.validation, this.fields)
  },
  // mounted() {},
}
</script>

<style lang="scss">
.CreateCourse7{}
</style>
