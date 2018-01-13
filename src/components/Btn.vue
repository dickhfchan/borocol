<template lang="pug">
button.Btn(:type="type" @click="!loading && $emit('click', $event)" :class="{loading: loading}")
  .loading(v-if="loading")
    .icon-wrapper
      span.icon.icon-arrows-ccw
  slot
  .loading-mask(v-if="loading")
</template>

<script>
export default {
  props: {
    type: {default: 'button'},
    loading: {},
  },
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Btn{
  position: relative;
  &.loading:focus{
    outline: none;
  }
  .loading {
    width: 1.5em;
    display: inline-block;
    .icon-wrapper{
      width: 1em;
      height: 1em;
      line-height: 1;
      display: inline-block;
      text-align: center;
      animation: rotation 2s infinite linear;
    }
    .icon {
      position: relative;
      top: -1px
    }
  }

  @keyframes rotation {
      from {
          transform: rotate(0deg);
      }
      to {
          transform: rotate(359deg);
      }
  }
  .loading-mask{
    @extend %mask;
    background: rgba(255, 255, 255, 0.35);
  }
}
</style>
