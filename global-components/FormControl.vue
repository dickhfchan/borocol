<template lang="pug">
.form-control(:class="[field.getValidationClass && field.getValidationClass()]")
  slot
</template>

<script>
export default {
  props: {
    field: {},
  },
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.form-control{}
.is-error{
  .el-input__inner,
  .el-input__inner:focus,
  .el-textarea__inner,
  .el-textarea__inner:focus{
    border-color: $dangerColor;
  }
}
</style>
