<template lang="pug">
.CreateCourse8.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group.top
        span.l Options
        Checkbox
        span.option Hotel
        Checkbox
        span.option Resort
        Checkbox
        span.option Dorm
        Checkbox
        span.option Others
        input.form-control.input-lg.lang(type='input', placeholder='')
      .form-group.middle
        span Describe the location
        textarea.form-control.txt(rows='3')(placeholder='ABC Resorts is located at Country side….')
      span Facilities
      .form-group
        Checkbox
        span.option WiFi
        Checkbox
        span.option Gym
        Checkbox
        span.option Air-conditionor
        Checkbox
        span.option Heater
        Checkbox
        span.option TV
        Checkbox
        span.option.r Balcony
        Checkbox
        span.option Washing machine
        Checkbox
        span.option Drying Machine
        Checkbox
        span.option Kitchen
        Checkbox
        span.option Swimming pool
        Checkbox
        span.option Free parking
        Checkbox
        span.option Wheel Chair Accessible
        Checkbox
        span.option Others:
        input.form-control.input-lg.lang(type='input', placeholder='e.g. Other facilities')
          //- todo
          //-   todo
          //-     todo
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
  .l {
    margin-right: 20px;
    float: left;
    margin-top: 20px;
  }

  .option {
    margin-right: 30px;
    float: left;
    margin-top: 20px;
  }

  .lang {
    width: 30%;
    position: relative;
    left: 70%;
    top: -30px;
  }
  .form-group.top {
    height: 35px;
    /* line-height: 70px; */
  }

  span.r {
    margin-right: 40px;
  }

  .Checkbox {
    float: left;
    margin-top: 20px;
  }
  .middle{
    margin-top: 25px;
  }
}
</style>
