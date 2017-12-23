<template lang="pug">
.Home.container
  .content-card
    div
      router-link(:to="{name: 'createCourse0'}") Create Course 0
    div
      router-link(:to="{name: 'createCourse1'}") Create Course 1
    div
      router-link(:to="{name: 'createCourse2'}") Create Course 2
    div
      router-link(:to="{name: 'createCourse3'}") Create Course 3
    div
      router-link(:to="{name: 'createCourse4'}") Create Course 4
    div
      router-link(:to="{name: 'createCourse5'}") Create Course 5
    div
      router-link(:to="{name: 'createCourse6'}") Create Course 6
    div
      router-link(:to="{name: 'createCourse7'}") Create Course 7
    div
      router-link(:to="{name: 'createCourse8'}") Create Course 8
    div
      router-link(:to="{name: 'createCourse9a'}") Create Course 9a
    div
      router-link(:to="{name: 'createCourse9b'}") Create Course 9b
    div
      router-link(:to="{name: 'createCourseTips'}") Create Course Tips
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
