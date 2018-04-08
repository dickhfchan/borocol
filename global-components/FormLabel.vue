<template lang="pug">
label.form-label
  span.required-asterisk(v-if="field.required") *
  span {{field.text}}
</template>

<script>
export default {
  props: {
    field: {},
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
@import "~assets/style/global.scss";
.form-label{
  font-weight: 400;
  margin-bottom: 5px;
  display: inline-block;
}
.required-asterisk{
  color: $dangerColor;
  margin-right: .2em;
}
</style>
