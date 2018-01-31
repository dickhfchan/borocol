<template lang="pug">
.StarScore
  span.icon(v-for="i in 5" :class="'icon-star' + (i <= value ? '' : '-o')" @click="$emit('input', i)")
</template>

<script>
export default {
  props: {
    value: {},
  },
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
.StarScore{
  display: inline-block;
  .icon{
    cursor: pointer;
    color: $bg2;
    font-size: 18px;
  }
}
</style>
