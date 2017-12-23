<template lang="pug">
include ../common.pug

.MainMenu
  .container
    .menu
      template(v-for="(item, index) in children")
        a.item
          span.icon(:class="'icon-' + item.icon")
          .text {{item.text}}
        .divider(v-if="index < children.length - 1")
</template>

<script>
export default {
  components: {},
  data() {
    return {
      children: [
        { icon: 'user-o', text: 'Profile', },
        { icon: 'like', text: 'School Reviews', },
        { icon: 'house', text: 'My Courses', },
        { icon: 'paper', text: 'Orders', },
        { icon: 'plus', text: 'Create Course', },
        { icon: 'talk', text: 'Message', },
        { icon: 'cog', text: 'Settings', },
        { icon: 'question-book', text: 'Inquiry', },
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
@import "~@/assets/css/global.scss";
.MainMenu{
  background: $bg1;
  .menu{
    display: flex;
    align-items: center;
  }
  .item{
    display: inline-block;
    text-align: center;
    padding: 20px 0;
    width: 150px;
    &:hover{
      background: #e4e4e4;
      text-decoration: none;
    }
    &.active{
      cursor: pointer;
      background: $bg2;
      .icon{
        color: #fff;
      }
    }
  }
  .icon{
    font-size: 30px;
    color: #b9b9b9;
  }
  .text{
    margin-top: 10px;
    font-size: 15px;
    font-weight: 300;
    color: lighten($color1, 15%);
  }
  .divider{
    display: inline-block;
    width: 1px;
    height: 90px;
    background-color: #fff;
    flex-shrink: 0;
  }
}
</style>
