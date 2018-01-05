<template lang="pug">
.Tips
  .tips
    .tips-title
      span.icon.icon-idea
      | Tips
    .tips-text More information more chance to attract your student!
  .tips
    .tips-title
      span.icon.icon-idea
      | Tips
    .tips-text More information more chance to attract your student!
  .flex-1
  .footer
    a.btn.btn-link.btn-lg.back-btn(@click="state.goPrevPage()")
      span.icon.icon-arrow-left.mrs
      | Back
    a.btn.btn-primary.btn-lg.pull-right(@click="state.checkAndGoNextPage()") Next
</template>

<script>
export default {
  components: {},
  data() {
    return {
      state: this.$state.createCourse,
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
.Tips{
  display: flex;
  flex-direction: column;
  .tips{
    border-width: 2px;
    border-color: $bd1;
    border-style: solid;
    border-radius: 3px;
    padding: 15px;
    width: 256px;
    margin-bottom: 30px;
  }
  .tips-title{
    font-size: $fs-title * 0.8;
    .icon{
      font-size: $fs-title * 1.2;
      margin-right: 15px;
    }
  }
  .tips-text{
    margin-top: 20px;
  }
  .back-btn{
    color: $color1;
    padding-left: 0;
    &:hover{
      text-decoration: none;
    }
    .icon{
      position: relative;
      top: -3px;
    }
  }
}
</style>
