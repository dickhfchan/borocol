<template lang="pug">
CardContainer.my-course-classmate
  div
    .title List of Classmate
    .space
    .space
    .space
    div
      Row(:gutter="16")
        Col(v-for="i in 50" :key="i" :width="90" same-width)
          Popover.popover-block.classmate-item
            template(v-if="i === 25")
              AspectImage.classmate-avatar(:src="anonymous" :aspect="1")
              .classmate-item-info(slot="content") A Mysterious Person
            template(v-else)
              AspectImage.classmate-avatar(:src="'https://picsum.photos/100/100?image=1'+i" :aspect="1")
              .classmate-item-info(slot="content")
                .line
                  Icon(name="user-o")
                  span Philadelphian
                .line
                  Icon(name="position")
                  span Saint Vincent and the Grenadines
                .line
                  Icon(name="heart")
                  span Liked Courses
  CloseBtn(type="2")
</template>

<script>
import CardContainer from '@/components/CardContainer'
import Popover from '@/components/Popover'
import anonymous from '@/assets/img/anonymous.jpg'
export default {
  components: {CardContainer, Popover},
  data() {
    return {
      anonymous,
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
.my-course-classmate{
  .title {
    font-size: 21px;
    color: rgb(51, 51, 51);
    text-align: center;
  }
  .classmate-avatar{
    // $side: 90px;
    // width: $side;
    // height: $side;
    border-radius: 100%;
  }
  .classmate-item{
  }
}
.classmate-item-info{
  line-height: 25px;
  .icon{
    display: inline-block;
    width: 1.5em;
    color: #888;
    font-size: 18px;
  }
}
</style>
