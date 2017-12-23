<template lang="pug">
#app
  MainHeader
  MainMenu
  MainContent
  MainFooter
</template>

<script>
import MainHeader from './components/MainHeader.vue'
import MainMenu from './components/MainMenu.vue'
import MainContent from './components/MainContent.vue'
import MainFooter from './components/MainFooter.vue'

export default {
  components: { MainHeader, MainMenu, MainContent, MainFooter },
  data () {
    return {
    }
  },
  computed: {
  },
  methods: {
  },
  created() {
  },
}
</script>

<style lang="scss">
</style>
