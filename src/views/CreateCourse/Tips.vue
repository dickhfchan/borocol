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
  br
  a.btn.btn-link.btn-lg.back-btn(@click="back")
    span.icon.icon-arrow-left.mrs
    | Back
  a.btn.btn-primary.btn-lg.pull-right(@click="next") Next
</template>

<script>
import {createCourse} from '@/routes/index'

export default {
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  methods: {
    getRouteIndex() {
      for (let i = 0; i < createCourse.length; i++) {
        if (createCourse[i].name === this.$route.name) {
          return i
        }
      }
    },
    back() {
      this.$router.push(createCourse[this.getRouteIndex() - 1])
    },
    next() {
      this.$router.push(createCourse[this.getRouteIndex() + 1])
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Tips{
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
