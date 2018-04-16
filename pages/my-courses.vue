<template lang="pug">
CardContainer.my-courses
  .card-container-title My Courses
  .space
  .space
  el-tabs.style-1(v-model='activeTab', type='card')
    el-tab-pane(label="Enrolled" name="Enrolled")
      Row(v-if="activeTab==='Enrolled'" :gutter="16")
        Col(v-for="i in 10" :key="i" :width="240" same-width)
          .course-item
            .img-area
              AspectImage(:src="'https://picsum.photos/400/300?image=6'+i" :aspect="1.7")
              .mask
                .title General Purpose<br />Immersion Program
            .text-area
              div
                .address SAN DIEGO, USA
                .time Feb 20, 16 - Mar 30, 17
              el-dropdown(trigger="click" placement="bottom-start")
                Icon.action-btn(name="bars")
                el-dropdown-menu.action-dropdown-menu(slot='dropdown')
                  el-dropdown-item(
                    v-for="(item, i) in actionDropDownMenu"
                    :key="item.text" :divided="i>0"
                  )
                    a {{item.text}}
      el-pagination.pull-right(:total="50" :page-size="10")
      .clearfix
    el-tab-pane(label="Pending") Pending
    el-tab-pane(label="Expired") Expired
    el-tab-pane(label="Terminated") Terminated
</template>

<script>
import CardContainer from '@/components/CardContainer'

export default {
  components: {CardContainer},
  data() {
    return {
      activeTab: 'Enrolled',
      actionDropDownMenu: [
        {text: 'Student List'},
        {text: 'Attach Visa'},
        {text: 'View Visa'},
        {text: 'Message School'},
        {text: 'Request Refund'},
      ],
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
.my-courses{
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
