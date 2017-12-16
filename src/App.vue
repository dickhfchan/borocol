<template lang="pug">
#app
</template>

<script>
// import TopNavbar from './components/TopNavbar.vue'
// import Sidebar from './components/Sidebar.vue'

export default {
  // components: { TopNavbar, Sidebar },
  data () {
    return {
    }
  },
  computed: {
    state() { return this.$store.state },
  },
  methods: {
    clickSidebarMenuItem(item) {
      if (item.routeName) {
        this.$router.push({name: item.routeName})
      }
    },
    getSidebarMenuItem(item) {
      if (item.routeName) {
        return this.$router.resolve({name: item.routeName}).href
      } else {
        return null
      }
    },
  },
  created() {
  },
}
</script>

<style lang="scss">
// <!-- libraries-->
// <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500" rel="stylesheet">
// <link href="https://file.myfontastic.com/DhuomFVWA52VBraDyGBsZ/icons.css" rel="stylesheet">
// <link href="assets/css/common.css" rel="stylesheet">
// <link href="assets/css/home.css" rel="stylesheet">
</style>
