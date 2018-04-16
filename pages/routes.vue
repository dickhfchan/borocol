<template lang="pug">
CardContainer.pal.routes-page
  ul
   li: router-link(:to="{name: 'index'}") index
   li: router-link(:to="{name: 'profile'}") profile
   li: router-link(:to="{name: 'reset-password'}") reset-password
   li: router-link(:to="{name: 'unauthenticated'}") unauthenticated
   li: router-link(:to="{name: 'create-program'}") create-program
   li: router-link(:to="{name: 'school-reviews'}") school-reviews
   li: router-link(:to="{name: 'my-courses'}") my-courses
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
