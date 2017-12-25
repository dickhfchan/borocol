<template lang="pug">
.CreateCourse2.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .form-group.inline.multiple
        label *Group Size
        input.form-control.input-lg(type="number" placeholder='Fitness & Sports - Yoya')
      .form-group.inline.rightside
        label Gender
        select.form-control.input-lg(placeholder='Beginner')
          option asfasg
          option help-block
          option Why
      span.age age age age age age
      span.hours Number of hours
      .form-group.inline.middle
        select.form-control.input-lg(placeholder='Fitness & Sports - Yoya',multiple="multiple", size="3")
          option asfasg
          option help-block
          option Why
      label.course *The course will be offered in
      input.form-control.input-lg.lang(type='input', placeholder='English, French')
      span.info Host / Instructor(s) Info
      textarea.form-control.Selena(rows='3' placeholder='Selena is a….')
      span.left_span *Will you issue Certificate to your guest?
      Checkbox
      span.left_span yes
      Checkbox
      span.left_span no
      textarea.form-control(rows='3' placeholder='With at least 70% attendance...')
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
  .inline{
  width: 15%;
  display: inline-block;
  }
  .multiple {
    /* height: 92px; */
    /* overflow: hidden; */
    float: left;
    margin-right: 40px;
  }

  .rightside {
    margin-right: 50px;
    margin-bottom: 35px;
    float: left;
   }
   span.age {
    margin-left: 7%;
    width: 40%;
    height: 115px;
    line-height: 115px;
    float: left;
    }
    span.hours {
        float: left;
        margin-right: 20px;
    }
    .lang {
    width: 25%;
    float: right;
    margin-bottom: 35px;
    }

    span.info {
        float: left;
    }

    .middle {
        margin-right: 15px;
        float: left;
    }

    label.course {
        /* line-height: 75px; */
        /* height: 75px; */
        margin-bottom: 60px;
        display: block;
        float: left;
    }

    .Selena {
        width: 74%;
        /* padding-top: 145px; */
    }
}
</style>
