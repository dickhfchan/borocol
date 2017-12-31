<template lang="pug">
.CheckboxGroup
  slot
</template>

<script>
export default {
  props: {
    multiple: {default: true},
    value: {},
  },
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
.CheckboxGroup{
  display: inline-block;
}
</style>
