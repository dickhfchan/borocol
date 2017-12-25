<template lang="pug">
.CreateCourse2.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body.row
      .form-group.col-sm-3
        label *Group Size
        input.form-control.input-lg(type="number" placeholder='Fitness & Sports - Yoya')
      .form-group.col-sm-3
        label Gender
        select.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      .form-group.age.col-sm-6
        span.age age age age age age
      .form-group.col-sm-3
        span.hours Number of hours
      .form-group.col-sm-2.right
        input.form-control.input-lg(type="number" placeholder='Fitness & Sports - Yoya')
      .form-group.col-sm-4.txt
        label.course *The course will be offered in
      .form-group.col-sm-3.end
        input.form-control.input-lg.end(type='input', placeholder='English, French')
      label.info.col-sm-12 Host / Instructor(s) Info
      .box.col-sm-12
        .tu.col-sm-2
          i.jia
        textarea.form-control.col-sm-10.text(rows='3' placeholder='Selena is a….')
      label.col-sm-8 *Will you issue Certificate to your guest?
      .form-group.col-sm-4
        Checkbox
        span.left_span yes
        Checkbox
        span.left_span no
      textarea.form-control.col-sm-4(rows='3' placeholder='With at least 70% attendance...')
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
.CreateCourse2{
  .age{
    height: 75px;
    line-height: 90px;
  }
  .right{
    padding-left: 0px;
  }
  .txt{
    padding: 0px;
  }
  .end{
    padding-right: 0px;
  }
  .tu{
    width: 20%;
    background: red;
    height: 100px;
    border: #c2b5b5 dashed 2px;
    margin-left: 15px;
    float: left;
  }
  .text{
    width: 75%;
    float: right;
    height: 100px;
  }
}
</style>
