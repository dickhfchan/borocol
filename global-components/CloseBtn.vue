<template lang="pug">
.close-btn(@click="$emit('click', $event)" :class="'type-'+type" :style="style")
  Icon.close-btn-icon(name="close-md")
</template>

<script>
import * as hp from 'helper-js'
export default {
  props: {
    type: {default: '1'},
    // margin: {default: 5},
  },
  // components: {},
  data() {
    return {
      margin: 5,
    }
  },
  computed: {
    style() {
      return {
        top: this.margin + 'px',
        right: this.margin + 'px',
      }
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    // 0.01666 is 5 / 300
    this.margin = hp.min(this.$el.offsetParent.offsetWidth * 0.01666, 5)
  },
}
</script>

<style lang="scss">
.close-btn{
  position: absolute;
  cursor: pointer;
}
.close-btn.type-1{
  $side: 20px;
  width: $side;
  height: $side;
  line-height: $side;
  text-align: center;
  border-radius: 100%;
  background-color: rgba(119, 119, 119, 0.3);
  color: rgb(255, 255, 255);
  &:hover{
    color: #eef;
    background-color: rgba(119, 119, 119, 0.9);
  }
  .close-btn-icon{
    font-size: 12px;
  }
}
.close-btn.type-2{
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  .close-btn-icon{
    font-size: 21px;
  }
  &:hover{
    opacity: 0.5;
  }
}
</style>
