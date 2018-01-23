\<template lang="pug">
.LikedCourses
  .container
    .content-card
      h1.content-card-title Liked Courses
      .content-card-body
        .list
          .item(v-for="i in 10")
            .img-area
              img(src="~$static/course-cover.jpg")
              .mask
                .title General Purpose<br />Immersion Program
                span.close2.icon.icon-cancel
            .text-area
              .left
                .address SAN DIEGO, USA
                .time Feb 20, 16 - Mar 30, 17
          .clearfix
        ul.pagination.b.pull-right
          li.disabled
            a(href='#', aria-label='Previous')
              span(aria-hidden='true') «
          li.active
            a(href='#')
              | 1
              span.sr-only (current)
          li
            a(href='#') 2
          li
            a(href='#') 3
          li
            a(href='#') 4
          li
            a(href='#') 5
          li
            a(href='#', aria-label='Next')
              span(aria-hidden='true') »
        .clearfix
</template>

<script>
import Tabs from '@/components/Tabs'
import Tab from '@/components/Tab'
export default {
  components: {Tabs, Tab},
  data() {
    return {
      activeTab: 'Enrolled',
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
@import "~@/assets/css/global.scss";
.LikedCourses{
  background-image: url(~@/assets/img/liked-courses-bg.jpg);
  background-size: 100%;
  @media(max-width: 1920px) {
    background-size: 1920px;
  }
  .container{
    width: 1400px;
    padding: 0;
  }
  $space: 20px;
  .list{
    margin-right: -$space;
    margin-bottom: -$space;
    .item{
      float: left;
      margin-right: $space;
      margin-bottom: $space;
      .img-area{
        position: relative;
        img{
          width: 240px;
          height: 140px;
          border-top-left-radius: 5px;
          border-top-right-radius: 5px;
        }
        .mask{
          @extend %mask;
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
        .close2{
          font-size: 20px;
          color: rgb(255, 255, 255);
          text-shadow: rgb(47, 47, 47) 0px 2px;
          position: absolute;
          right: .2em;
          top: .2em;
          cursor: pointer;
          &:hover{
            transform: scale(1.2);
          }
        }
      }
      .text-area{
        margin-top: .5em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        .left{
          font-size: 13px;
        }
      }
    }
  }
}
</style>
