<template lang="pug">
div
  .page-header
    .container
      el-row.hidden-xs-only
        el-col(:span="6")
          router-link.brand(:to="{name: 'index'}")
            img(src="~assets/img/brand.png")
        el-col.top-menu(:span="18")
          //- unauthenticated
          template(v-if="!$store.state.authenticated")
            router-link(:to="{name: 'partner'}") Partner with us
            .divider |
            Icon(name="user")
            a.mls(@click="$store.dispatch('auth/show')") Login
          //- authenticated
          template(v-else)
            el-dropdown(trigger="click" placement="bottom-start")
              a.avatar-name
                img.avatar(v-lazy="$store.state.user.avatar || $store.state.anonymousAvatar")
                span.mlm {{$store.state.user.name}}
              el-dropdown-menu.user-dropdown-menu(slot='dropdown')
                el-dropdown-item(
                  v-for="(item, i) in userDropDownMenu"
                  :key="item.text" :divided="i>0"
                  v-if="!item.role || item.role === $store.state.user.userType"
                )
                  router-link(v-if="item.routeName" :to="{name: item.routeName}") {{item.text}}
                  a(v-else @click.prevent="item.action($store)") {{item.text}}
            .divider |
            el-badge.message(:value="1")
              Icon(name="dialog")
          //- authenticated end
          .divider |
          Icon(name="credit-card")
          a.mls USD
          .divider |
          span.locale
            Icon(name="locale")
            a.mls EN
          .divider |
          a(href='#') Q&a
          a.search-btn.mls()
            Icon(name="search")
      .page-header-inner--xs.hidden-sm-and-up
        a.menu-btn
          Icon(name="bars")
        router-link.brand(:to="{name: 'index'}")
          img(src="~assets/img/brand.png")
        span.locale
          Icon(name="locale")
          a.mls EN
    .mobile-menu
      //- todo
  slot
    nuxt
  .page-footer
    ._1
      .container.phn
        el-row(:gutter="16")
          el-col(:xs="11" :sm="6" :md="5" :lg="4")
            .title Borocol
            .links
              a.link(href="#") About Us
              a.link(href="#") Recruitment
              a.link(href="#") Media
              a.link(href="#") FAQs
              a.link(href="#") Contact Us
          el-col(:xs="11" :sm="6" :md="5" :lg="4")
            .title Contact Us
            .links
              a.link(href="#") Borocol
              a.link(href="#") 103 Arthur Road
              a.link(href="#") Windsor
              a.link(href="#") SL4 1 RU
              a.link(href="#") sales@borocol.com
              a.link(href="#") 01753 833442
          el-col(:xs="11" :sm="6" :md="5" :lg="4")
            .title Legal & Cookies
            .links
              a.link(href="#") Terms & Conditions
              a.link(href="#") Privacy Policy
              a.link(href="#") Cookie Policy
              a.link(href="#") Returns Policy
              a.link(href="#")
    ._2
      .container.phn
        span © 2017 All Rights Reserved Borocol - Privacy Policy - Terms and conditions
        .brands
          a(href="#")
            Icon(name="facebook")
          a(href="#")
            Icon(name="linkedin")
          a(href="#")
            Icon(name="twitter")
          a(href="#")
            Icon(name="vimeo")
          a(href="#")
            Icon(name="pinterest")
  Auth
  TestPanel
</template>

<script>
import Auth from '~/components/Auth.vue'
import TestPanel from '~/components/TestPanel.vue'
export default {
  components: {Auth, TestPanel},
  data() {
    return {
      userDropDownMenu: [
        {text: 'Profile', routeName: 'profile'},
        {text: 'School Reviews', routeName: 'school-reviews', role: 'school'},
        {text: 'Liked Courses', routeName: 'liked-courses', role: 'student'},
        {text: 'My Courses', routeName: 'my-courses'},
        {text: 'Create Course', routeName: 'create-course', role: 'school'},
        {text: 'Settings', routeName: 'settings'},
        {text: 'Logout', action: async () => {
          const loading = this.$loading()
          await this.$apiPost('/user/logout')
          await this.$store.dispatch('auth/fetchUser')
          loading.close()
          this.$router.push({name: 'index'})
        }},
      ],
    }
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
body {
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  color: rgb(51, 51, 51);
}

*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
}

a{
  color: $primaryColor;
  cursor: pointer;
  text-decoration: none;
  &:hover{
    text-decoration:underline;
  }
}
// helper

.bg-grey{
  background-color: #f3f2f0;
}
.w-100{
  width: 100%;
}
.text-transform-n{
  text-transform: none;
}
.text-center{
  text-align: center;
}
.pull-left{
  float: left;
}
.pull-right{
  float: right;
}
.clearfix{
  clear: both;
}
.space{
  // vertical
  height: 1em;
  @media(max-width: $medium) {
    height: .5em;
  }
}
.relative{
  position: relative;
}
// flex helper
.flex{
  display: flex;
}
.flex-0{
  flex-shrink: 0;
}
.flex-s0{
  flex-shrink: 0;
}
.flex-g1{
  flex-grow: 1;
}
.flex-1{
  flex: 1;
}

// common
.container{
  width: $large2 - 30px;
  margin: 0 auto;
  padding-left: 15px;
  padding-right: 15px;
  @media(max-width: $large2) and (min-width: $large) {
    width: $large - 30px;
  }
  @media(max-width: $large) and (min-width: $medium) {
    width: $medium - 30px;
  }
  @media(max-width: $medium) {
    width: 100%;
  }
}
.container-sm{
  @media(min-width: $large) {
    width: $large - 30px;
  }
}
.btn-block {
  display: block;
  width: 100%;
}
.avatar{
  $side: 45px;
  width: $side;
  height: $side;
  border-radius: 100%;
}
.dividing-line-title{
  font-size: 22px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .line{
    height: 1px;
    flex-grow: 1;
    background: #ddd;
  }
}

.review-visa-icon{
  background: #69a2dd;
}
.accomodation-icon {
  background: #968ecb;
}
.insurance-icon {
  background: #63cace;
}
.downpayment-icon {
  background: #a6c875;
}

//
$pageHeaderColor: #000;
.page-header{
  color: $pageHeaderColor;
  a{
    color: $pageHeaderColor;
  }
  .divider {
    display: inline-block;
    color: $pageHeaderColor;
    padding: 0 .8em;
  }
  .avatar-name{
    display: flex;
    align-items: center;
  }
  .message .el-badge__content{
    top: -2px;
    right: 8px;
  }
  .search-btn{
    $side: 38px;
    width: $side;
    height: $side;
    line-height: $side;
    background: #000;
    display: inline-block;
    color: #fff;
    text-align: center;
    &:hover{
      text-decoration: none;
    }
  }
  @media(min-width: $small) {
    padding: 40px 0 30px 0;
  }
}
.user-dropdown-menu{
}
.page-header-inner--xs{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 0;
  .icon{
    font-size: 22px;
    vertical-align: middle;
  }
}
.top-menu{
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  a {
    text-transform: uppercase;
  }
}
.page-footer{
  ._1{
    background-color: #5B5B5D;
    padding-top: 90px;
    padding-bottom: 140px;
    .title{
      color: #fff;
      font-size: 20px;
      font-weight: bold;
    }
    .links{
      margin-top: 10px;
      line-height: 30px;
      a{
        color: #bababa;
        display: block;
      }
    }
  }
  ._2{
    color: #fff;
    font-weight: 500;
    background: #262626;
    padding: 15px 0;
  }
  .brands{
    float: right;
    a{
      display: inline-block;
      color: #fff;
      text-decoration: none;
      margin-right: 10px;
    }
    @media(max-width: $medium) {
      float: none;
      margin-top: 16px;
    }
  }
}
</style>
