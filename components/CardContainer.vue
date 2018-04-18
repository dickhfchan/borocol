<template lang="pug">
.card-container
  .container
    slot(name="card")
      .el-card.content-card
        .el-card__body.relative
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
@import "~assets/style/global.scss";
.card-container{
  background: url('~assets/img/school-bg.jpg');
  background-size: cover;
  background-attachment: fixed;
  padding: 50px 0 200px 0;
}
.card-container-title{
  font-size: 70px;
  font-weight: 300;
  @media(max-width: $medium) {
    font-size: 30px;
  }
}
.content-card{
  min-height: 300px;
  > .el-card__body{
    padding: 3em;
    @media(max-width: $medium) and (min-width: $small) {
      padding: 2em;
    }
    @media(max-width: $small) {
      padding: 1em;
    }
  }
}
</style>
