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
  // watch: {},
  // methods: {},
  created() {
    this.$state.createCourseVm = this
  },
  // mounted() {},
  beforeDestroy() {
    this.state.validations.forEach(item => {
      item.clear && item.clear()
    })
  },
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
