<template lang="pug">
span.icon.iconfont(:class="'icon-'+name" @click="$emit('click', $event)")
</template>

<script>
export default {
  props: {
    name: {},
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
</style>
