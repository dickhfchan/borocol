<template lang="pug">
.aspect-image(:style="{'padding-bottom': 1 / aspect * 100 + '%'}" v-lazy:background-image="src")
</template>

<script>
export default {
  props: {
    src: {},
    aspect: {},
  },
  components: {},
  data() {
    return {
      style: {
        width: 'auto',
        width: 'auto',
      },
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.aspect-image{
  background-size: cover;
}
</style>
