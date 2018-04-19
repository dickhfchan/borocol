<template lang="pug">
.test-panel.pas(v-if="visible" :class="{mini:mini}")
  .test-panel-inner(v-if="!mini")
    button(v-for="item in btns" @click="item.action") {{item.text}}
  button(@click="mini=!mini") toogle
</template>

<script>
import * as hp from 'helper-js'
export default {
  components: {},
  data() {
    return {
      visible: process.env.testPanelEnabled,
      mini: false,
      btns: [],
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  created() {
    const Vue = this.$root.constructor
    Vue.testPanel = Vue.prototype.$testPanel = (obj) => {
      this.btns = Object.keys(obj).map(key => ({text: key, action: obj[key]}))
    }
    Vue.testFill = Vue.prototype.$testFill = (fields) => {
      if (!this.visible) {
        return
      }
      Object.values(fields).forEach(v => {
        if (v.value != null) {
          return
        }
        if (v.type === 'file') {
          v.value = 'https://picsum.photos/40/40?image=401'
        } else if (v.type === 'date') {
          v.value = new Date()
        } else if (v.rules) {
          if (v.rules.includes('email')) {
            v.value = `example@example.com`
          } else if (v.rules.includes('accepted')) {
            v.value = true
          }
        } else {
          v.value = hp.strRand(5)
        }
      })
    }
  },
  // mounted() {},
}
</script>

<style lang="scss">
.test-panel{
  position: fixed;
  background: #fff;
  border: 1px solid #ddd;
  width: 100%;
  right: 0;
  bottom: 0;
  z-index: 9999;
  display: flex;
  opacity: 0.6;
  &:hover{
    opacity: 0.9;
  }
  &.mini{
    width: auto;
  }
}
.test-panel-inner{
  flex-grow: 1;
}
</style>
