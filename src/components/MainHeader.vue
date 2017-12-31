<template lang="pug">
include ../common.pug
.MainHeader
  .container
    .brand-bar
      .brand
        img(src="~@/../static/images/brand.png")
      .tool-bar.pull-right
        a(href="#")
          .avatar
            img(src="~@/../static/pictures/avatar.jpg")
          span.mlm My Course
        .divider |
        a(href="#")
          +icon('talk')
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
</template>

<script>

export default {
  components: {},
  data() {
    return {}
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

.MainHeader{

  .brand-bar {
    padding: 30px 0 30px;

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

    .avatar{
      @extend %border-default;
      $side: 45px;
      width: $side;
      height: $side;
      border-radius: $side;
      overflow: hidden;
      display: inline-block;
      vertical-align: middle;
      img{
        width: 100%;
      }
    }
    .name{
      vertical-align: middle;
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

}
</style>
