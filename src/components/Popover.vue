<template lang="pug">
.Popover
  slot
  .popover.bottom(ref="tip" :style="style")
    .arrow
    h3.popover-title(v-if="title") {{title}}
    .popover-content
      slot(name="content")
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
.Popover{
  display: inline-block;
  position: relative;
  .popover{
    display: none;
    &.bottom{
      top: 100%;
    }
  }
  &:hover{
    .popover{
      display: block;
    }
  }
}
</style>
