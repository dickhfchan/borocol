<template lang="pug">
.marked-input
  input(ref="input" :disabled="maskCore===null || disabled" :value="value"
    @keydown="keyDown" @keypress="keyPress" @keyup="keyUp" @textInput="textInput"
    @mouseup="mouseUp" @focusout="focusOut" @cut="cut" @copy="copy" @paste="paste"
  )
</template>

<script>
export default {
  extends: process.browser ? require('vue-masked-input').default : null,
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
</style>
