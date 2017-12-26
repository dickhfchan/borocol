<template lang="pug">
.CreateCourse2.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .row
        .form-group.col-sm-3
          label *Group Size
          input.form-control.input-lg(type="number" placeholder='Fitness & Sports - Yoya')
        .form-group.col-sm-3
          label Gender
          select.form-control.input-lg()
            option Male
            option Female
        .form-group.age.col-sm-6
          label Age
          .help-block2 todo Slider
      .form-group._1.mtm
        .help-block2 Number of hours
        input.form-control.input-lg.mlm.hours(type="number")
        .flex-1
        .help-block2 *The course will be offered in
        input.form-control.input-lg.mlm.language(type='input', placeholder='English, French')
      .form-group._2.mtm
        label Host / Instructor(s) Info
        ._2-1
          .upload
            .icon.icon-plus
          textarea.form-control(rows='3' placeholder='Selena is a….')
      .form-group.mtm
        label *Will you issue Certificate to your guest?
        Checkbox.mls
        span.mls No
        Checkbox.mls
        span.mls Yes
        textarea.form-control.mts(rows='3' placeholder='With at least 70% attendance...')
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
@import "~@/assets/css/global.scss";
.CreateCourse2{
  ._1{
    display: flex;
    justify-content: space-between;
    .hours{
      width: 120px;
    }
    .language{
      width: 230px;
    }
  }
  ._2{

  }
  ._2-1{
    $h: 100px;
    height: $h;
    display: flex;
    justify-content: space-between;
    .upload{
      $side: $h;
      width: $side;
      height: $side;
      line-height: $side;
      display: inline-block;
      border: $bd1 dashed 2px;
      margin-right: 20px;
      flex-shrink: 0;
      text-align: center;
      .icon{
        font-size: 30px;
        color: $bd1;
      }
    }
    textarea{
      height: 100%;
    }
  }
}
</style>
