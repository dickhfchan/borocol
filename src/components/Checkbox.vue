<template lang="pug">
.Checkbox
  span.icon.icon-check(v-if="value2")
  input(type="checkbox" v-model="value2")
</template>

<script>
import {arrayRemove} from 'helper-js'
export default {
  props: {
    value: {},
  },
  components: {},
  data() {
    return {}
  },
  computed: {
    value2: {
      get() {
        if (this.inGroup()) {
          const parent  = this.$parent
          if (parent.multiple) {
            return parent.value && parent.value.includes(this.value)
          } else {
            return parent.value === this.value
          }
        } else {
          return this.value
        }
      },
      set(value) {
        if (this.inGroup()) {
          const parent  = this.$parent
          if (parent.multiple) {
            const arr = (parent.value || []).slice(0)
            if (value) {
              if (!arr.includes(this.value)) {
                arr.push(this.value)
              }
            } else {
              arrayRemove(arr, this.value)
            }
            parent.$emit('input', arr)
          } else {
            parent.$emit('input', this.value)
          }
        } else {
          this.$emit('input', value)
        }
      },
    },
  },
  // watch: {},
  methods: {
    inGroup() {
      try {
        return this.$parent.$options.name === 'CheckboxGroup'
      } catch (e) {
        return false
      }
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Checkbox{
  position: relative;
  border: 1px solid $bd1;
  border-radius: 3px;
  display: inline-block;
  $side: $lh;
  width: $side;
  height: $side;
  vertical-align: middle;
  .icon{
    font-size: 1.3em;
    position: relative;
    top: -2px;
  }
  input{
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    opacity: 0;
  }
}
</style>
