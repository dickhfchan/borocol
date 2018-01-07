<template lang="pug">
.CreateCourse6
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form
        .form-group
          label Guest Requirement
          textarea.form-control(rows='3' placeholder="- Skill level\n- Occupations")
        .form-group
          label *Do you want to set up a Request Form?
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
.CreateCourse6{
  ._1{
    textarea{
      width: 75%;
      float: right;
      display: inline-block;
    }
  }
}
</style>
