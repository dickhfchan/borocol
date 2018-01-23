<template lang="pug">
.MyCourses
  .container
    .content-card
      h1.content-card-title My Courses
      .content-card-body
        Tabs(v-model="activeTab")
          Tab.mtl(name="Enrolled")
            .list
              .item(v-for="i in 10")
                .img-area
                  img(src="~$static/course-cover.jpg")
                  .mask
                    .title General Purpose<br />Immersion Program
                .text-area
                  .left
                    .address SAN DIEGO, USA
                    .time Feb 20, 16 - Mar 30, 17
                  .dropdown.left
                    .actions
                      span.icon.icon-bars
                    ul.dropdown-menu
                      li
                        a(href="javascript:void(0)") Student List
                      li.divider
                      li
                        a(href="javascript:void(0)") Attach Visa
                      li.divider
                      li
                        a(href="javascript:void(0)")
                         | View Visa
                         .pull-right.icon.icon-link
                      li.divider
                      li
                        a(href="javascript:void(0)") Message School
                      li.divider
                      li
                        a(href="javascript:void(0)") Request Refund
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
          Tab.mtl(name="Pending") Pending
          Tab.mtl(name="Expired") Expired
          Tab.mtl(name="Terminated") Terminated
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
.MyCourses{
  background-image: url(~@/assets/img/orders-bg.jpg);
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
      }
      .text-area{
        margin-top: .5em;
        display: flex;
        justify-content: space-between;
        align-items: center;
        .left{
          font-size: 13px;
        }
        .actions{
          cursor: pointer;
          font-size: 18px;
        }
      }
    }
  }
}
</style>
