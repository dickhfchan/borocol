<!-- default layout has menu -->
<template lang="pug">
nomenu
  .main-menu.hidden-xs-only
    .container
      .main-menu-inner
        template(v-for="(item, index) in mainMenu")
          router-link.menu-item(:to="item.route")
            //- span.icon.item-icon(:class="'icon-' + item.icon")
            //-   .notification-count(v-if="item.notificationCount") {{item.notificationCount}}
            el-badge.message(:value="item.notificationCount")
              Icon.menu-item-icon(:name="item.icon")
            .text {{item.text}}
          .divider(v-if="index < mainMenu.length - 1")
  nuxt
</template>

<script>
import nomenu from './nomenu.vue'
export default {
  components: {nomenu},
  data() {
    return {
      mainMenu: [
        { icon: 'user-o', text: 'Profile', route: {name: 'profile'}},
        { icon: 'heart-o', text: 'Reviews', route: {name: 'my-reviews'}, role: 'school'},
        { icon: 'house', text: 'My Program', route: {name: 'my-program'}},
        { icon: 'file-text', text: 'Orders', notificationCount: 2, route: {name: 'orders'}, role: 'school'},
        { icon: 'plus-thin', text: 'Create A Program', route: {name: 'create-a-program'}, role: 'school'},
        { icon: 'dialog', text: 'Chat Box', route: {name: 'chat-box'}},
        { icon: 'cog', text: 'Settings', route: {name: 'settings'}},
        { icon: 'inquiry', text: 'Inquiry', route: {name: 'inquiry'}},
      ],
    }
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.main-menu{
  background: #f3f2f0;
  .main-menu-inner{
    display: flex;
    align-items: center;
  }
  .menu-item{
    display: inline-block;
    text-align: center;
    padding: 25px 0;
    width: 150px;
    &:focus, &:visited, &:hover{
      text-decoration: none;
    }
    &:hover{
      background: #e4e4e4;
    }
    &.nuxt-link-exact-active{
      cursor: default;
      background: $primaryColor;
      .menu-item-icon, .text{
        color: #fff;
      }
    }
  }
  .menu-item-icon{
    font-size: 35px;
    color: #b9b9b9;
    position: relative;
  }
  .text{
    margin-top: 10px;
    font-size: 15px;
    color: #595959;
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
