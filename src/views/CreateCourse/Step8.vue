<template lang="pug">
.CreateCourse8.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group
        label.mrl Options
        Checkbox.mls
        label.mls Hotel
        Checkbox.mls
        label.mls Resort
        Checkbox.mls
        label.mls Dorm
        Checkbox.mls
        label.mls Others
        input.form-control.input-lg.mll._1(type='text', placeholder='')
      .form-group
        label Describe the location
        textarea.form-control(rows='3' placeholder='ABC Resorts is located at Country side….')
      .form-group.facilities
        label Facilities
        br
        Checkbox
        label.mls WiFi
        Checkbox.mll
        label.mls Gym
        Checkbox.mll
        label.mls Air-conditionor
        Checkbox.mll
        label.mls Heater
        Checkbox.mll
        label.mls TV
        Checkbox.mll
        label.mls Balcony
        br
        Checkbox
        label.mls Washing machine
        Checkbox.mll
        label.mls Drying Machine
        Checkbox.mll
        label.mls Kitchen
        Checkbox.mll
        label.mls Swimming pool
        br
        Checkbox
        label.mls Free parking
        Checkbox.mll
        label.mls Wheel Chair Accessible
        Checkbox.mll
        label.mls Others:
        input.form-control.mll.other-facilities(type='text', placeholder='e.g. Other facilities')
      .form-group
        label Upload Photos (If Any)
        p todo
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
.CreateCourse8{
  ._1{
    display: inline-block;
    width: 300px;
  }
  .facilities{
    line-height: 30px;
  }
  .other-facilities{
    display: inline-block;
    width: 200px;
  }
}
</style>
