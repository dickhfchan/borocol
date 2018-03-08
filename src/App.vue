<template lang="pug">
#app
  MainHeader
  MainMenu(v-if="hasMenu")
  MainContent
  MainFooter
  Auth
  //- Confirm
</template>

<script>
import MainHeader from './components/MainHeader.vue'
import MainMenu from './components/MainMenu.vue'
import MainContent from './components/MainContent.vue'
import MainFooter from './components/MainFooter.vue'
import Auth from './components/Auth.vue'

export default {
  components: { MainHeader, MainMenu, MainContent, MainFooter, Auth },
  data () {
    return {
    }
  },
  computed: {
    hasMenu() {
      if (this.$route.meta && this.$route.meta.hasMenu === false) {
        return false
      }
      return true
    },
  },
  methods: {
  },
  // created() {},
  mounted() {
    this.$state.appVm = this
  },
}
</script>

<style lang="scss">
</style>
