<template lang="pug">
#app.flex.flex-col(v-loading.fullscreen.lock="!state.initialized", element-loading-text="拼命加载中")
  router-view(v-if="$route.name === 'login'")
  template(v-else-if="state.initialized && state.authenticated && $route.name")
    TopNavbar
    .flex-1.flex
      Sidebar
      .page-content.flex-1
        router-view
</template>
<script>
import TopNavbar from './components/TopNavbar.vue'
import Sidebar from './components/Sidebar.vue'

export default {
  components: { TopNavbar, Sidebar },
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
// @import "../node_modules/font-awesome/css/font-awesome.css";
@import "./plugins/element/index.css";
@import "../node_modules/css-spacing-helper/css-spacing-helper.css";
@import "./assets/css/helper.scss";
@import "./assets/css/style.scss";
</style>
<!-- 注入font-awesome到element-ui -->

<style lang="less">
[class^="el-icon-fa"], [class*=" el-icon-fa"] {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome!important;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
};
@import url("../node_modules/font-awesome/less/font-awesome.less");
@fa-css-prefix: el-icon-fa;
</style>

<style lang="scss">
html{
  overflow-x: hidden;
}
body{
  margin: 0;
  font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}
html, body, #app{
  width: 100%;
  height: 100%;
}
</style>

<style lang="scss" scoped>
.page-content{
  overflow: auto;
}
</style>
