<template lang="pug">
InputTag.TagsInput(:tags="tags")
</template>

<script>
import InputTag from 'vue-input-tag'
export default {
  props: {
    value: {},
  },
  components: {InputTag},
  data() {
    return {}
  },
  computed: {
    tags: {
      get() { return this.value },
      set(value) { this.$emit('input', value) },
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.TagsInput{
  &.vue-input-tag-wrapper{
    border-color: $bd-fc;
    border-radius: $bdr;
    .input-tag {
        background-color: $bg2;
        border-color: $bg2;
        color: #ffffff;
        .remove {
          color: #ffffff;
        }
    }
  }
}
</style>
