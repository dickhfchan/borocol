<template lang="pug">
.course-card
  .course-card-title {{title}}
  a.img-area(:href="href")
    HasReadMore
      AspectImage(:src="img" :aspect="imgAspect")
      .mark(v-if="mark") {{mark}}
      .price(v-if="price")
        span {{price}}
        .original-price(v-if="originalPrice") {{originalPrice}}
      slot(name="img-area")
  slot
</template>

<script>
export default {
  props: {
    title: {},
    href: {},
    img: {},
    imgAspect: {default: 1.85},
    price: {},
    originalPrice: {},
    mark: {},
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
// 课程卡片
.course-card {
  border-radius: 5px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0 3px 20.37px 0.63px rgba(159, 159, 159, 0.31);

  .course-card-title {
    $height: 50px;
    height: $height;
    line-height: $height;
    font-size: 21px;
  }

  .mark {
    background-color: rgb(255, 178, 0);
    position: absolute;
    left: 0;
    top: 10%;
    color: #fff;
    font-weight: bold;
    padding: 5px 10px;
  }

  .img-area {
    display: block;
    text-decoration: none;
    position: relative;
    .price {
      background-color: rgb(112, 112, 112);
      position: absolute;
      top: 70%;
      right: 0;
      padding: 5px 10px;
      font-size: 16px;
      color: rgb(255, 255, 255);
      font-weight: bold;
    }

    .original-price {
      font-size: 13px;
      text-align: right;
      text-decoration: line-through;
    }
  }

  .text-area {
    padding: 15px;
    .info {
      display: flex;
      line-height: 25px;
    }

    .icon {
      display: inline-block;
      width: 28px;
      font-size: 18px;
      text-align: center;
    }

  }
}
</style>
