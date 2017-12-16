// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// packages
// import 'babel-polyfill'
import Vue from 'vue'
import Router from 'vue-router'
// import axios from 'axios'
// vue-data-validator
// import * as VueDataValidator from 'vue-data-validator'
// files
import App from './App'
import store from './store/index.js'
import routes from './routes/index.js'
import { initAxios, initVDV, initRouter, getCurrentUser, registerPreventURLChange } from '@/utils.js'
//
Vue.config.productionTip = store.state.isDevelopment
Vue.config.debug = store.state.isDevelopment
Vue.config.devtools = store.state.isDevelopment

// axios
// initAxios(axios, store, Vue)

// VDV
// initVDV(VueDataValidator, store, Vue)
// router
const router = initRouter(Router, Vue, store, routes, () => {
  // unauthorized
})

registerPreventURLChange(Vue, router)
Vue.prototype.$state = store.state

// start
/* eslint-disable no-new */
const start = async () => {
  store.state.initialized = true
  // await getCurrentUser(store, Vue)
  new Vue({
    el: '#app',
    store,
    router,
    template: '<App/>',
    components: { App }
  })
}
start()
