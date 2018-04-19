<template lang="pug">
el-select.nation-select(v-model="value2" :placeholder="placeholder" filterable)
  el-option(v-for="item in countries" :key="item.code" :value="item.code" :label="item.name")
</template>

<script>
import countries from '@/plugins/countries.json'
export default {
  props: {
    value: {},
    placeholder: {},
  },
  // components: {},
  data() {
    return {
      countries,
    }
  },
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
