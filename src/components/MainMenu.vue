<template lang="pug">
include ../common.pug

.MainMenu
  .container
    .menu
      template(v-for="(item, index) in children")
        a.item(:href="getHref(item)" @click.prevent="clickItem(item)" :class="{active: activeIndex===index}")
          span.icon.item-icon(:class="'icon-' + item.icon")
            .notification-count(v-if="item.notificationCount") {{item.notificationCount}}
          .text {{item.text}}
        .divider(v-if="index < children.length - 1")
</template>

<script>
export default {
  components: {},
  data() {
    return {
      children: [
        { icon: 'user-o', text: 'Profile', route: {name: 'profile'}},
        { icon: 'like', text: 'School Reviews', },
        { icon: 'house', text: 'My Courses', route: {name: 'myCourses'}},
        { icon: 'paper', text: 'Orders', notificationCount: 2, route: {name: 'orders'}},
        { icon: 'plus-thin', text: 'Create Course', route: {name: 'createCourse'}},
        { icon: 'talk', text: 'Message', },
        { icon: 'cog', text: 'Settings', },
        { icon: 'question-book', text: 'Inquiry', },
      ],
    }
  },
  computed: {
    activeIndex() {
      for (let i = 0; i < this.children.length; i++) {
        const item = this.children[i]
        if (item.route && this.$route.name && this.$route.name.startsWith(item.route.name)) {
          return i
        }
      }
    },
  },
  // watch: {},
  methods: {
    getHref(item) {
      if (item.route) {
        return this.$router.resolve(item.route).href
      } else {
        return ''
      }
    },
    clickItem(item) {
      if (item.route) {
        this.$router.push(item.route)
      }
    },
  },
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
    &:focus, &:visited, &:hover{
      text-decoration: none;
    }
    &:hover{
      background: #e4e4e4;
    }
    &.active{
      cursor: pointer;
      background: $bg2;
      .item-icon, .text{
        color: #fff;
      }
    }
  }
  .item-icon{
    font-size: 35px;
    color: #b9b9b9;
    position: relative;
  }
  .text{
    margin-top: 10px;
    font-size: 15px;
    color: lighten($color1, 15%);
  }
  .notification-count{
    border-radius: 50%;
    background-color: rgb(224, 79, 79);
    color: #fff;
    font-size: 10px;
    font-weight: bold;
    font-family: serif;
    $side: 17px;
    width: $side;
    height: $side;
    line-height: $side;
    position: absolute;
    right: -10px;
    top: 0px;
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
