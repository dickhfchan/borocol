<template lang="pug">
.Home.container
  .content-card
    ul
      li(v-for="item in routes")
        router-link(:to="item") {{item.meta && item.meta.title || item.path}}
</template>

<script>
import routes from '@/routes/index'

export default {
  components: {},
  data() {
    return {
      routes: routes,
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
.Home{}
</style>
