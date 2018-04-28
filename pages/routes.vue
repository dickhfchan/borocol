<template lang="pug">
CardContainer.pal.routes-page
  ul
   li: router-link(:to="{name: 'index'}") index
   li: router-link(:to="{name: 'partner'}") partner
   li: router-link(:to="{name: 'profile'}") profile
   li: router-link(:to="{name: 'reset-password'}") reset-password
   li: router-link(:to="{name: 'unauthenticated'}") unauthenticated
   li: router-link(:to="{name: 'create-program'}") create-program
   li: router-link(:to="{name: 'school-reviews'}") school-reviews
   li: router-link(:to="{name: 'my-courses'}") my-courses
   li: router-link(:to="{name: 'liked-courses'}") liked-courses
   li: router-link(:to="{name: 'my-course-visa'}") my-course-visa
   li: router-link(:to="{name: 'my-course-classmate'}") my-course-classmate
   li: router-link(:to="{name: 'transaction'}") transaction
   li: router-link(:to="{name: 'message'}") message
   li: router-link(:to="{name: 'course'}") course
   li: router-link(:to="{name: 'course-filter'}") course-filter
   li: router-link(:to="{name: 'about'}") about
   li: router-link(:to="{name: 'press'}") press
   li: router-link(:to="{name: 'career'}") career
</template>

<script>
import CardContainer from '@/components/CardContainer'
export default {
  layout: 'nomenu',
  components: {CardContainer},
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
@import "~assets/style/global.scss";
</style>
