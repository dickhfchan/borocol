<template lang="pug">
.CreateCourseTips.container
  .content-card
    .content-card-body
      .tips
        .tips-title
          span.icon.icon-idea
          | Tips
        .tips-text More information more chance to attract your student!
      br
      a.btn.btn-link.btn-lg.back-btn
        span.icon.icon-arrow-left.mrs
        | Back
      a.btn.btn-primary.btn-lg Next
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
.tips{
  border-width: 2px;
  border-color: $bd1;
  border-style: solid;
  border-radius: 3px;
  padding: 20px;
  width: 286px;
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
  &:hover{
    text-decoration: none;
  }
  .icon{
    position: relative;
    top: -3px;
  }
}
</style>
