<template lang="pug">
.carousel
  .carousel-items-wrapper(:style="wrapperStyle" ref="wrapper")
    .carousel-items(:style="itemsStyle" ref="items")
      slot
</template>

<script>
import * as hp from 'helper-js'
export default {
  props: {
    slidesToShow: {default: 3},
    slidesToScroll: {default: 3},
    gutter: {default: 16},
    autoplay: {default: true},
    duration: {default: 3000},
  },
  components: {},
  data() {
    return {
      page: 1,
      itemWidth: null,
      itemHeight: null,
      wrapperWidth: null,
      itemCount: null,
    }
  },
  computed: {
    // slides at left or visible
    leftAndVisibleCount() {
      return this.slidesToShow + (this.page - 1) * this.slidesToScroll
    },
    itemsStyle() {
      const left = this.wrapperWidth - this.getTotalWidth(this.itemWidth, this.leftAndVisibleCount)
      return {
        left: left + 'px',
      }
    },
    wrapperStyle() {
      return {
        height: this.itemHeight + 'px',
      }
    },
    pageCount() {
      let t = Math.ceil((this.itemCount - this.slidesToShow) / this.slidesToScroll)
      t = 1 + (t > 0 ? t : 0)
      return t == Infinity ? 0 : t
    },
  },
  // watch: {},
  methods: {
    updateSize() {
      const {gutter: g, slidesToShow: n} = this
      const w = this.wrapperWidth = this.$refs.wrapper.offsetWidth
      const itemW = this.itemWidth = this.getSingleWidth(w, n)
      const itemEls = [...this.$refs.items.children]
      this.itemCount = itemEls.length
      itemEls.forEach(el => {
        el.style.width = itemW + 'px'
        el.style.marginRight = g + 'px'
      })
      // must get height after set item with
      this.itemHeight = this.$refs.items.offsetHeight
    },
    getTotalWidth(singleW, n) {
      return singleW * n + this.gutter * (n - 1)
    },
    getSingleWidth(totalW, n) {
      return (totalW - this.gutter * (n - 1)) / n
    },
    moveLeft(move = 1) {
      this.page = hp.max(this.page + move, this.pageCount)
    },
    moveRight(move = 1) {
      this.page = hp.min(this.page - move, 1)
    },
    startAutoPlay() {
      if (this.autoplay) {
        this._autoPlayInterval = setInterval(() => {
          let t = this.page + 1
          if (t > this.pageCount) {
            t = 1
          }
          this.page = t
        }, this.duration)
      }
    },
    stopAutoPlay() {
      window.clearInterval(this._autoPlayInterval)
    },
  },
  // created() {},
  mounted() {
    this.updateSize()
    this.$watch('slidesToShow', this.updateSize)
    this.$watch('gutter', this.updateSize)
    this.startAutoPlay()
  },
}
</script>

<style lang="scss">
.carousel{
}
.carousel-items-wrapper{
  position: relative;
  overflow: hidden;
}
.carousel-items {
  position: absolute;
  white-space: nowrap;
  transition: left 1s;
  > *{
    display: inline-block;
  }
}
</style>
