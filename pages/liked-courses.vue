<template lang="pug">
CardContainer.liked-courses
  .card-container-title Liked Courses
  .space
  .space
  Row(:gutter="16")
    Col(v-for="i in 10" :key="i" :width="240" same-width)
      .course-item
        .img-area
          AspectImage(:src="'https://picsum.photos/400/300?image=6'+i" :aspect="1.7")
          .mask
            .title General Purpose<br />Immersion Program
            CloseBtn
        .text-area
          div
            .address SAN DIEGO, USA
            .time Feb 20, 16 - Mar 30, 17
  el-pagination.pull-right(:total="50" :page-size="10")
  .clearfix
</template>

<script>
import CardContainer from '@/components/CardContainer'

export default {
  components: {CardContainer},
  data() {
    return {
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.liked-courses{
  .course-item{
    .img-area{
      position: relative;
      .aspect-image{
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
      }
      .mask{
        @include mask;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .title{
        font-size: 16px;
        font-weight: bold;
        color: rgb(255, 255, 255);
        text-align: center;
        text-shadow: rgb(47, 47, 47) 0px 2px;
      }
    }
    .text-area{
      margin-top: .5em;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
    }
    .action-btn{
      cursor: pointer;
      font-size: 18px;
    }
  }
}
</style>
