<template lang="pug">
.carousel3.carousel2
  ._1(@mouseenter="cr && cr.stopAutoPlay()" @mouseleave="cr && cr.startAutoPlay()")
    Carousel(ref="cr" :slidesToShow="slidesToShow" :slidesToScroll="slidesToShow")
      slot
  .dots.mtm
    .dot(v-for="i in dots" :class="{active: i===cr.page}" @click="cr.page=i")
</template>

<script>
import Carousel2 from '@/components/Carousel2'

export default {
  extends: Carousel2,
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
</style>
