<template lang="pug">
.CreateCourse1
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form.row
        .form-group.col-sm-12
          label *Title
          input.form-control.input-lg(type='text' placeholder="e.g. 5 Days Yoga Retreat in Bali")
        .form-group.col-sm-8
          label *Category
          select.form-control.input-lg()
            option Fitness & Sports - Yoya
        .form-group.col-sm-4
          label *Level
          select.form-control.input-lg()
            option Beginner
        .col-sm-4
          .form-group
            label *Start Date
            DatePicker(v-model="formData.startDate" :format="dateFormat")

        .col-sm-4
          .form-group
            label *End Date
            DatePicker(v-model="formData.endDate" :format="dateFormat")
        .col-sm-4.duration
          .form-group
            label &nbsp;
            //- .help-block2.duration 4 Days 3 Nights

        .form-group.col-sm-12
          label What Will We Do? (Description)
          textarea.form-control(rows='5' placeholder="e.g. We will go to Rain Forest to hunt….")
      Tips
</template>

<script>
import base from './base'
import DatePicker from '@/components/DatePicker';
export default {
  extends: base,
  components: {DatePicker},
  data() {
    return {
      dateFormat: 'MMM dd yyyy',
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCourse1{
  .duration{
    text-align: right;
  }
}
</style>
