<template lang="pug">
.Tooltip
  slot
  .tooltip.bottom(role='tooltip' ref="tip" :style="style")
    .tooltip-arrow
    .tooltip-inner {{title}}
</template>

<script>
import mounted from './mounted'
export default {
  mixins: [mounted],
  props: {
    title: {},
  },
  // components: {},
  data() {
    return {
      style: {
        left: null,
        display: '',
      }
    }
  },
  // computed: {},
  watch: {
    title: {
      immediate: true,
      handler(value) {
        this.mounted.then(() => {
          this.style.display = 'block'
          this.$nextTick(() => {
            const tipWidth = this.$refs.tip.offsetWidth
            this.style.left = (this.$el.offsetWidth - tipWidth) / 2 + 'px'
            this.style.display = ''
          })
        })
      }
    }
  },
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
    display: none;
  }
  &:hover{
    .tooltip{
      display: block;
    }
  }
  .tooltip-inner{
    white-space: nowrap;
  }
}
</style>
