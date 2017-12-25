<template lang="pug">
.CreateCourse4.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      label Number of hours
      .form-group.inline.more
        select.form-control.input-lg(placeholder='Fitness & Sports - Yoya',multiple="multiple", size="3")
          option asfasg
          option help-block
          option Why
      .form-group.option
        label *Are meals included?
        Checkbox
        label yes
        Checkbox
        label no
      .form-group.option
        Checkbox.l
        label Breakfast
        Checkbox
        label Lunch
        Checkbox
        label Bunch
        Checkbox
        label Dinner
      textarea.form-control(rows='3' placeholder='More information')
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
  .Checkbox{
    margin-left: 20px;
  }
  .Checkbox.l{
  margin-left: 0px;
  }
  .option{
    margin-top: 20px;
  }
}
</style>
