<template lang="pug">
.popover(@mouseenter="hovering=true" @mouseleave="hovering=false")
  slot
  .popover-popup(ref="tip" :style="style" v-dom-portal v-show="visible" :class="'popover-popup-' + realPosition")
    //- top and bottom arrow width 22 height 11
    .popover-arrow
    slot(name="inner")
      h3.popover-title(v-if="title") {{title}}
      .popover-content
        slot(name="content")
</template>

<script>
import * as hp from 'helper-js'
export default {
  props: {
    title: {},
    position: {default: 'bottom'},
    width: {},
  },
  // components: {},
  data() {
    return {
      hovering: false,
      visible: false,
      top: null,
      left: null,
      realPosition: null,
    }
  },
  computed: {
    style() {
      let r = {
        left: this.left + 'px',
        top: this.top + 'px',
      }
      if (this.width != null) {
        r.width = hp.isNumber(width) ? width + 'px' : width
      }
      return r
    },
  },
  // watch: {},
  methods: {
    resolveVisible() {
      this.visible = this.hovering
      if (this.visible && this._isMounted) {
        this.$nextTick(() => {
          this.$nextTick(() => {
            const tipW = this.$refs.tip.offsetWidth
            const el = this.$el
            const elOf = hp.getOffset(el)
            this.realPosition = this.position
            switch (this.realPosition) {
              case 'bottom':
                this.top = elOf.y + el.offsetHeight + 11
                this.left = elOf.x + (el.offsetWidth - tipW) / 2
                break
            }
          })
        })
      }
    },
  },
  // created() {},
  mounted() {
    this.$watch('title', this.resolveVisible)
    this.$watch('hovering', this.resolveVisible)
    this.resolveVisible()
  },
}
</script>

<style lang="scss">
.popover{
  display: inline-block;
}
.popover-block{
  display: block;
}
.popover-popup{
  position: absolute;
  background: #fff;
  min-width: 150px;
  border-radius: 4px;
  border: 1px solid #ebeef5;
  padding: 12px;
  z-index: 2000;
  color: #606266;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
}
.popover-arrow, .popover-arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
// top and bottom arrow width 22 height 11
.popover-arrow, .popover-arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover-arrow {
  border-width: 11px;
}
.popover-arrow:after {
  border-width: 10px;
  content: "";
}
.popover-popup-bottom > .popover-arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover-popup-bottom > .popover-arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #ffffff;
}
</style>
