<template lang="pug">
.CreateCourse3
  .content-card
    .content-card-header
      .step Step {{state.step}}
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', :style="{width: state.progressStr}") {{state.progressStr}}
    .content-card-body.has-tips
      form.row
        .form-group.col-sm-12
          label *Address
          input.form-control.input-lg(type='text', placeholder='')
        .form-group.col-sm-4
          label *City
          input.form-control.input-lg(type='text', placeholder='')
        .form-group.col-sm-4
          label *Country
          select.form-control.input-lg()
            option England
        .form-group.col-sm-4
          label
            span *API Key
            //- span.icon.icon-question-circle
          .api-input
            img(src="~@/assets/img/google-map.png")
            input.form-control.input-lg(type='text', placeholder='')
        .form-group.col-sm-12
          label Describe the location
          textarea.form-control(rows='3' placeholder='Please describe the location')
        .form-group.col-sm-6
          label How to get there?
          textarea.form-control(rows='3' placeholder='e.g. Please book your flight to arrive at JFK Airport, New York.')
        .form-group.col-sm-6
          label Where to meet up your guest?
          textarea.form-control(rows='3' placeholder='')
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
.CreateCourse3{
  .api-input{
    position: relative;
    img{
      position: absolute;
      top: 5px;
      left: 10px;
    }
    input{
      padding-left: 65px;
    }
  }
}
</style>
