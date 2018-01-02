<template lang="pug">
.CreateCourse4
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form
        .form-group
          label Itinerary / Typical Daily Schedule
          select.form-control(multiple="multiple", size="10")
            option Day 1
            option Day 2
            option Day 3
        .form-group
          label *Are meals included?
          CheckboxGroup(:multiple="false" v-model="formData.mealsIncluded")
            Checkbox.mls(:value="false")
            span.mls No
            Checkbox.mls(:value="true")
            span.mls Yes
        .form-group
          CheckboxGroup(v-model="formData.meals")
            Checkbox(value="breakfast")
            label.mls Breakfast
            Checkbox.mls(value="lunch")
            label.mls Lunch
            Checkbox.mls(value="bunch")
            label.mls Bunch
            Checkbox.mls(value="dinner")
            label.mls Dinner
        textarea.form-control(rows='5' placeholder='More Information')
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
.CreateCourse4{
}
</style>
