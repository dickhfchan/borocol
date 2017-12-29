<template lang="pug">
.Home.container
  .content-card
    div
      router-link(:to="{name: 'createCourse'}") Create Course 
</template>

<script>
export default {
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
.Home{}
</style>
