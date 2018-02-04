<template lang="pug">
#app
  MainHeader
  MainMenu(v-if="hasMenu")
  MainContent
  MainFooter
  Alert
  Confirm
  Notification
</template>

<script>
import MainHeader from './components/MainHeader.vue'
import MainMenu from './components/MainMenu.vue'
import MainContent from './components/MainContent.vue'
import MainFooter from './components/MainFooter.vue'
import Alert from './components/Alert.vue'
import Confirm from './components/Confirm.vue'
import Notification from './components/Notification.vue'

export default {
  components: { MainHeader, MainMenu, MainContent, MainFooter, Alert, Confirm, Notification },
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
  created() {
    this.$state.appVm = this
  },
}
</script>

<style lang="scss">
</style>
