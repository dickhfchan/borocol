<template lang="pug">
el-dialog.custom-dialog.style-1(:width="width" :visible.sync="value1")
  .custom-dialog__title(v-if="title") {{title}}
  slot
</template>

<script>

export default {
  props: {
    width: {},
    value: {},
    title: {},
  },
  components: {},
  data() {
    return {}
  },
  computed: {
    value1: {
      get() { return this.value },
      set(value) { this.$emit('input', value) },
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.custom-dialog{
  .el-dialog__header{
    padding: 0;
  }
  .el-dialog__body{
    padding: 90px 70px;
    @media(max-width: $medium) {
      padding: 20px;
    }
  }
}

.custom-dialog__title{
  font-size: 60px;
  font-weight: 300;
  color: #000;
  line-height: 1;
  @media(max-width: $medium) {
    font-size: 30px;
  }
}
</style>
