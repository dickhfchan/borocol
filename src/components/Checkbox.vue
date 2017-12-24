<template lang="pug">
.Checkbox
  span.icon.icon-check
  input(type="checkbox" v-model="value2")
</template>

<script>
// todo
export default {
  props: {
    multiple: {default: true},
    value: {},
    values: {},
  },
  components: {},
  data() {
    return {}
  },
  computed: {
    value2: {
      get() {return this.value},
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Checkbox{
  position: relative;
  border: 1px solid $bd1;
  border-radius: 3px;
  display: inline-block;
  $side: $lh;
  width: $lh;
  height: $lh;
  .icon{
    font-size: 18px;
    position: relative;
    top: -2px;
  }
  input{
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    visibility: hidden;
  }
}
</style>
