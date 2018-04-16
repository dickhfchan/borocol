<template lang="pug">
.Tabs(:class="'style-' + styleName")
  // Nav tabs
  .tabs-header(role='tablist')
    .tabs-header-item(
      v-for="(name, index) in names" :class="{active: activeIndex === index}"
    )
      a(href="javascript:void(0)", @click.prevent="$emit('input', name)") {{name}}
    .clearfix
  // Tab panels
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
@import "~assets/style/global.scss";
.Tabs{
  .tabs-header{
    border-bottom: 3px solid #ddd;
  }
  .tabs-header-item{
    position: relative;
    display: block;
    float: left;
    margin-bottom: -1px;
    > a{
      display: block;
      &:hover{
        text-decoration: none;
      }
    }
  }
  &.style-1{
    %aHover{
      background-color: transparent;
      border-color: transparent;
      color: #fff;
    }
    .tabs-header-item {
      background-color: #ccc;
      margin-right: 10px;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      &.active{
        background-color: $primaryColor;
        a, a:hover, a:focus, a:visited{
          @extend %aHover;
        }
      }
      a{
        font-size: 16px;
        color: rgb(255, 255, 255);
        text-transform: uppercase;
        font-weight: 500;
        padding: 12px 20px 6px 20px;
        background-color: transparent;
        &:hover, &:focus, &:visited{
          @extend %aHover;
        }
      }
    }
  }
  &.style-2{
    %aHover{
      border-color: transparent;
      color: $primaryColor;
    }
    .tabs-header-item {
      padding: 0;
      margin-right: 40px;
      border-bottom: 3px solid transparent;
      position: relative;
      bottom: -2px;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      &.active{
        border-color: $primaryColor;
        a, a:hover, a:focus, a:visited{
          @extend %aHover;
          color: $primaryColor;
        }
      }
      a{
        color: $primaryColor;
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
</style>
