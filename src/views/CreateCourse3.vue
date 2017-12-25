<template lang="pug">
.CreateCourse3.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group
        label *Address
        input.form-control.input-lg(type='imput', placeholder='')
      .form-group.City
        label *City
        input.form-control.input-lg(type='imput', placeholder='')
      .form-group.Country
        label *Country
        select.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.API
        label *API Key
        input.form-control.input-lg(type='imput', placeholder='')
      span.left_span Describe the location
      textarea.form-control(rows='3' placeholder='Please describe the location')
      .form-group.how
        span.left_span How to get there?
        textarea.form-control(rows='3' placeholder='Please book your flight to arrive at JFK Airport, New York.')
      .form-group.guest
        span.left_span Where to meet up your guest?
        textarea.form-control(rows='3' placeholder='')
      //-   Checkbox
      //-   span Option one is this and that—be sure to include why it's great
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
  .City {
    width: 25%;
    float: left;
  }

  .Country {
      width: 25%;
      float: left;
      margin-left: 5%;
  }

  .API {
      width: 40%;
      margin-left: 5%;
      float: left;
  }
  .how,.guest{
    width: 49%;
    float: left;
    margin-top: 15px;
  }

  .guest {
      margin-left: 2%;
  }
}
</style>
