<template lang="pug">
.Tabs(:class="'style-' + styleName")
  // Nav tabs
  ul.nav.nav-tabs(role='tablist')
    li(
      role='presentation'
      v-for="(name, index) in names" :class="{active: activeIndex === index}"
    )
      a(href="javascript:void(0)", :aria-controls="name", role='tab' @click.prevent="$emit('input', name)") {{name}}
  // Tab panes
  .tab-content
    slot
    //- #home.tab-pane.active(role='tabpanel') ...
    //- #profile.tab-pane(role='tabpanel') ...
    //- #messages.tab-pane(role='tabpanel') ...
    //- #settings.tab-pane(role='tabpanel') ...
</template>

<script>
export default {
  props: {
    value: {},
    styleName: {default: '1'},
    lazy: {default: true},
  },
  components: {},
  data() {
    return {
      names: [],
    }
  },
  computed: {
    activeIndex() {
      return this.names.findIndex(v => v === this.value)
    },
  },
  watch: {
    activeIndex: {
      immediate: true,
      handler(index) {
        if (index === -1) {
          if (this.names.length > 0) {
            this.$emit('input', this.names[0])
          }
        }
      }
    }
  },
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Tabs{
  &.style-1{
    %aHover{
      background-color: transparent;
      border-color: transparent;
      color: #fff;
    }
    .nav-tabs{
      border-width: 3px;
      > li {
        background-color: #ccc;
        margin-right: 10px;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        &.active{
          background-color: $bg2;
          a, a:hover, a:focus, a:visited{
            @extend %aHover;
          }
        }
        a{
          font-size: 16px;
          color: rgb(255, 255, 255);
          text-transform: uppercase;
          font-weight: $fw-md;
          padding: 9px 20px 3px 20px;
          background-color: transparent;
          &:hover, &:focus, &:visited{
            @extend %aHover;
          }
        }
      }
    }
  }
  &.style-2{
    %aHover{
      border-color: transparent;
      color: $bg2;
    }
    .nav-tabs{
      border-width: 3px;
      > li {
        padding: 0;
        margin-right: 40px;
        border-bottom: 3px solid transparent;
        position: relative;
        bottom: -2px;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        &.active{
          border-color: $bg2;
          a, a:hover, a:focus, a:visited{
            @extend %aHover;
            color: $color1;
          }
        }
        a{
          color: $color1;
          text-transform: none;
          padding: 9px 0;
          background-color: transparent;
          &:hover, &:focus, &:visited{
            @extend %aHover;
          }
        }
      }
    }
  }
}
</style>
