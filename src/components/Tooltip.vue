<template lang="pug">
.Tooltip
  slot
  .tooltip.bottom(role='tooltip')
    .tooltip-arrow
    .tooltip-inner {{title}}
</template>

<script>
export default {
  props: {
    title: {},
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
.Tooltip{
  display: inline-block;
  position: relative;
  .tooltip{
    opacity: 1;
    left: -50%;
    display: none;
  }
  &:hover{
    .tooltip{
      display: block;
    }
  }
}
</style>
