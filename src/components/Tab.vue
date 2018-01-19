<template lang="pug">
.Tab.tab-pane.active(role='tabpanel' v-if="$parent.value===name")
  slot
</template>

<script>
export default {
  // components: {},
  props: {
    name: {},
  },
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    this.$parent.names.push(this.name)
  },
}
</script>

<style lang="scss">
.Tab{}
</style>
