<template lang="pug">
.Radio
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
.Radio{
  position: relative;
  border: 1px solid $bd1;
  border-radius: 300px;
  display: inline-block;
  $side: 1em;
  width: $side;
  height: $side;
  vertical-align: middle;
  input{
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    visibility: hidden;
  }
  &.checked{
    background-color: $bg2;
  }
}
</style>
