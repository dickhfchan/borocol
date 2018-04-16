import Vue from 'vue'

export default ({store}) => {
  Vue.mixin({
    beforeDestroy() {
      this.$emit('beforeDestroy')
    }
  })
  Vue.nextTickOnce = Vue.prototype.$nextTickOnce = function (name, func) {
    const vm = this || Vue
    const mark = `_nextTickOnce_${vm._uid}_${name}`
    if (!vm.hasOwnProperty(mark)) {
      vm[mark] = true
      Vue.nextTick((...args) => {
        func(...args)
        delete vm[mark]
      })
    }
  }
}
