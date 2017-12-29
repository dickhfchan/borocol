<template lang="pug">
.CreateCourse.container
  router-view
</template>

<script>
export default {
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  watch: {
    // update progressStr
    '$route': {
      immediate: true,
      handler(value) {
        const num = this.$route.name.match(/\d+/)
        if (num) {
          this.$state.createCourse.progressStr = Math.floor(num / this.$state.createCourse.stepCount * 100) + '%'
        }
      }
    }
  },
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCourse{
  .content-card-body.has-tips{
    display: flex;
    // justify-content: space-between;
    .Tips{
      margin-left: 50px;
      flex-shrink: 0;
    }
  }
}
</style>
