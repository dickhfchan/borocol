<template lang="pug">
.MainContent
  router-view
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
.MainContent{
  background-image: url(~@/assets/img/school-bg.jpg);
  background-size: 100%;
  @media(max-width: 1920px) {
    background-size: 1920px;
  }
}
</style>
