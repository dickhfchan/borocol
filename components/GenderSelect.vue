<template lang="pug">
el-select.gender-select(v-model="value2" :placeholder="placeholder" filterable)
  el-option(v-for="item in genders" :key="item.text" :value="item.value" :label="item.text")
</template>

<script>

export default {
  props: {
    value: {},
    placeholder: {},
  },
  // components: {},
  data() {
    return {
      genders: [
        {text: 'Male', value: 'male'},
        {text: 'Female', value: 'female'},
      ],
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
