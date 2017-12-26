<template lang="pug">
.CreateCourse4.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group
        label Itinerary / Typical Daily Schedule
        select.form-control(multiple="multiple", size="10")
          option Day 1
          option Day 2
          option Day 3
      .form-group
        label Are meals included?
        Checkbox.mls
        label.mls No
        Checkbox.mls
        label.mls Yes
      .form-group
        Checkbox
        label.mls Breakfast
        Checkbox.mls
        label.mls Lunch
        Checkbox.mls
        label.mls Bunch
        Checkbox.mls
        label.mls Dinner
      textarea.form-control(rows='5' placeholder='More information')
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
.CreateCourse4{
}
</style>
