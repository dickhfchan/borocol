<template lang="pug">
.card-container
  .container
    el-card.content-card
      slot
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
.card-container{
  background: url('~assets/img/school-bg.jpg');
  background-size: cover;
  background-attachment: fixed;
  padding: 50px 0 200px 0;
  // &.no-bg{
  //   background: none;
  // }
}
.card-container-title{
  font-size: 70px;
  font-weight: 300;
}
.content-card{
  min-height: 300px;
}
</style>
