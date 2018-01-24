<template lang="pug">
include ../common.pug
.MyCourseClassmate
  .container
    .content-card.has-close
      .title List of Classmate
      .content-card-body
        .list.mtl
          .item(v-for="i in 50")
            Popover
              template(v-if="i === 25")
                img.avatar(src="~@/assets/img/anonymous.jpg")
                .info(slot="content") A Mysterious Person
              template(v-else)
                img.avatar(src="~$static/student-avatar2.jpg")
                .info(slot="content")
                  .line
                    span.icon.icon-user-o
                    span Philadelphian
                  .line
                    span.icon.icon-position
                    span Saint Vincent and the Grenadines
                  .line
                    span.icon.icon-heart
                    span Liked Courses
          .clearfix
      span.icon.icon-close.close
</template>

<script>
import Popover from '@/components/Popover'
export default {
  components: {Popover},
  data() {
    return {
      photos: [],
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
.MyCourseClassmate{
  background: $bg3;
  .title {
    font-size: 21px;
    color: rgb(51, 51, 51);
    text-align: center;
  }
  .list{
    $space: 13px;
    margin-right: -$space;
    margin-bottom: -$space;
    .item{
      float: left;
      margin-right: $space;
      margin-bottom: $space;
    }
  }
  .avatar{
    $side: 90px;
    width: $side;
    height: $side;
    border-radius: 200px;
  }
  .info{
    width: 300px;
    line-height: 25px;
    .icon{
      display: inline-block;
      width: 1.5em;
      color: #989898;
      font-size: 18px;
    }
  }
}
</style>
