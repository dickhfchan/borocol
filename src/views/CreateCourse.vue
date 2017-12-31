<template lang="pug">
.CreateCourse.container
  router-view
</template>

<script>
export default {
  // components: {},
  data() {
    return {
      state: this.$state.createCourse,
    }
  },
  // computed: {},
  watch: {
    // update step, progressStr
    '$route': {
      immediate: true,
      handler(value) {
        const num = this.$route.name.match(/\d+/)
        if (num) {
          const [step] = num
          Object.assign(this.state, {
            step,
            progressStr: Math.floor(step / this.state.stepCount * 100) + '%',
          })
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
    justify-content: space-between;
    > form{
      width: 100%;
    }
    .Tips{
      margin-left: 50px;
      flex-shrink: 0;
      margin-bottom: 15px;
    }
  }
}
</style>
