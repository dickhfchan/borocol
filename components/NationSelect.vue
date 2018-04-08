<template lang="pug">
el-select.nation-select(v-model="value2" :placeholder="placeholder")
  //- todo
  el-option(value="usa" label="USA")
  el-option(value="todo" label="todo")
</template>

<script>
export default {
  props: {
    value: {},
    placeholder: {},
  },
  // components: {},
  // data() {
  //   return {}
  // },
  computed: {
    value2: {
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
</style>
