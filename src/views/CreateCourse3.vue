<template lang="pug">
.CreateCourse3.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body.row
      .form-group.col-sm-12
        label *Address
        input.form-control.input-lg(type='imput', placeholder='')
      .form-group.col-sm-4
        label *City
        input.form-control.input-lg(type='imput', placeholder='')
      .form-group.col-sm-4
        label *Country
        select.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.col-sm-4
        label *API Key
        input.form-control.input-lg(type='imput', placeholder='')
      .form-group.col-sm-12
        label Describe the location
        textarea.form-control(rows='3' placeholder='Please describe the location')
      .form-group.col-sm-6
        label How to get there?
        textarea.form-control(rows='3' placeholder='Please book your flight to arrive at JFK Airport, New York.')
      .form-group.col-sm-6
        label Where to meet up your guest?
        textarea.form-control(rows='3' placeholder='')
      //-   Checkbox
      //-   label Option one is this and that—be sure to include why it's great
      //- .form-group
      //-   label(for='exampleInputFile') File input
      //-   input#exampleInputFile(type='file')
      //-   p.help-block Example block-level help text here.
      //- .checkbox
      //-   label
      //-     input(type='checkbox')
      //-     |  Check me out
      //- button.btn.btn-primary.btn-lg(type='submit') Submit
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
.CreateCourse3{

}
</style>
