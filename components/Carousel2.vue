<template lang="pug">
.carousel2
  ._1(@mouseenter="cr && cr.stopAutoPlay()" @mouseleave="cr && cr.startAutoPlay()")
    .carousel-btn.left-btn.mrm(v-if="!mini" @click="cr.moveRight()" :class="{disabled: cr && cr.page === 1}")
      Icon(name="angle-left")
    Carousel(ref="cr" :slidesToShow="slidesToShow" :slidesToScroll="slidesToShow")
      slot
    .carousel-btn.right-btn.mlm(v-if="!mini" @click="cr.moveLeft()" :class="{disabled: cr && cr.page === cr.pageCount}")
      Icon(name="angle-right")
  .dots.mtm(v-if="mini")
    .dot(v-for="i in dots" :class="{active: i===cr.page}" @click="cr.page=i")
</template>

<script>
import Carousel from '@/components/Carousel'
const mixins = []
if (process.browser) {
  mixins.push(require('@/components/windowSize').default)
}
export default {
  components: {Carousel},
  mixins,
  props: {
    responsive: {default: is => [1, 3, 4, 5]},
  },
  data() {
    return {
      slidesToShow: null,
      mini: null,
      cr: null,
    }
  },
  computed: {
    dots() {
      return this.cr && (new Array(this.cr.pageCount)).fill('').map((v, i) => i + 1)
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    this.cr = this.$refs.cr
    this.$watch('window.innerWidth', (w) => {
      this.mini = w < 768
      if (w < 768) {
        this.slidesToShow = this.responsive[0]
      } else if (w < 992) {
        this.slidesToShow = this.responsive[1]
      } else if (w < 1200) {
        this.slidesToShow = this.responsive[2]
      } else {
        this.slidesToShow = this.responsive[3]
      }
      this.cr.updateSize()
    }, {immediate: true})
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.carousel2{
  ._1{
    display: flex;
    align-items: center;
  }
  .carousel{
    flex-grow: 1;
  }
  .carousel-btn{
    .icon{
      font-size: 40px;
    }
    color: #7D7D7D;
    cursor: pointer;
    &.disabled{
      color: #d0d0d0;
      cursor: not-allowed;
    }
  }
  .dots{
    text-align: center;
  }
  .dot{
    display: inline-block;
    cursor: pointer;
    $side: 7px;
    width: $side;
    height: $side;
    border-radius: 100%;
    background-color: grey;
    margin: 0 3px;
    &.active{
      background: $primaryColor;
    }
  }
}
</style>
