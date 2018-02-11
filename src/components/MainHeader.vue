<template lang="pug">
include ../common.pug
.MainHeader
  .container.relative
    .brand-bar
      router-link.brand(:to="{name: 'home'}")
        img(v-lazy="brand")
      .tool-bar.pull-right
        template(v-if="$state.authenticated")
          a
            img.avatar(v-lazy="$state.user.avatar || anonymousAvatar")
          a(href="#")
            span.mlm {{$state.user.name}}
        template(v-else)
          a(href="/user-admin/create-course/") Partner with us
          .divider |
          +icon('user').moveup1
          a.mlm(@click="$state.auth.show('login')") Login
        .divider |
        +icon('credit-card')
        a.mlm(href="#") USD
        .divider |
        span.language
          +icon('language')
          a.mlm(href="#") EN
          +icon('caret-down').mls.hidden-md.hidden-lg
        .divider |
        a(href="#") Q&a
        button.mlm.no-bb.btn-black.search-btn(type="button")
          +icon('search')
        button.no-bb.btn-black.menu-btn.hidden-md.hidden-lg(type="button" @click="onclickMenuBtn")
          +icon('bars')
    .menu-card.bg1.pull-right.hidden-lg.hidden-md(ref="menuCard")
      .menu
        .menu-item
          a(href="#" @click="onclickMenuItem")
            span HKD
            +icon('caret-down')
          .sub-menu
            .menu-item
              a(href="#" @click="onclickMenuItem") HKD
            .menu-item
              a(href="#" @click="onclickMenuItem") HKD
            .menu-item
              a(href="#" @click="onclickMenuItem") HKD
        .menu-item
          a(href="#" @click="onclickMenuItem") Login
        .menu-item
          a(href="#" @click="onclickMenuItem") Join us
</template>

<script>
import brand from '@/assets/img/brand.png'
import anonymousAvatar from '@/assets/img/anonymous.jpg'

export default {
  components: {},
  data() {
    return {
      brand,
      anonymousAvatar,
    }
  },
  // computed: {},
  // watch: {},
  methods: {
    onclickMenuBtn() {
      const menuCard = $(this.$refs.menuCard)
      menuCard.toggleClass('active')
      if (menuCard.hasClass('active')) {
        menuCard.slideDown()
      } else {
        menuCard.slideUp()
      }
    },
    onclickMenuItem(e) {
      var el = e.target.tagName === 'A' ? $(e.target) : $(e.target).closest('a')
      if (el.next().is('.sub-menu')) {
        e.preventDefault()
        el.next().slideToggle()
      }
    },
  },
  // created() {},
  mounted() {
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";

.MainHeader{
  .brand-bar {
    padding: 60px 0 30px;

    .brand {
      display: inline-block;
    }
  }
  $toolBarHeight: 37.5px;

  .tool-bar {
    $height: $toolBarHeight;
    height: $height;
    line-height: $height;
    font-weight: 500;
    $color: #000;

    a {
      text-transform: uppercase;
      color: $color;
    }

    .divider {
      display: inline-block;
      color: $color;
      padding: 0 1em;
    }

    .btn-black {
      display: inline-block;
      width: $height;
      height: $height;
      line-height: $height;
      padding: 0;
      text-align: center;
      background-color: #000;
      color: #fff;

      .icon {
        font-size: 16px;
      }
      // flex
      flex-shrink: 0;
    }
    // flex
    display: flex;
    align-items: center;
  }
  .avatar{
    $side: 50px;
    width: $side;
    height: $side;
    border-radius: 100%;
  }

  .menu-card {
    display: none;
    position: absolute;
    top: 50px;
    right: 0;
    width: 300px;
    padding: 20px;
    font-weight: 500;
    font-size: 18px;
    text-transform: uppercase;
    z-index: 1;

    .menu-item {
      a {
        color: $color1;
        display: block;
        padding: 5px 10px;
        border-bottom: 3px solid #fff;
      }
    }

    .sub-menu {
      padding-left: 20px;
      display: none;
    }
  }
  // xs extra small and small
  @media(max-width: $medium) {
    .brand-bar {
      padding: 15px 0 15px 30px;
    }

    .tool-bar {
      > :not(.language):not(.btn-black) {
        display: none;
      }

      .search-btn {
        background: inherit;
        margin-left: 0;
        color: inherit;

        .icon {
          position: relative;
          top: -1px;
        }
      }

      .menu-btn {
        background: transparent;
        color: inherit;

        .icon {
          position: relative;
          top: -2px;
        }

        &.active {
          background: #000;
          color: #fff;
        }
      }
    }
  }
}
</style>
