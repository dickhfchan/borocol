// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// packages
// import 'babel-polyfill'
import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'
// vue-data-validator
import * as VueDataValidator from 'vue-data-validator'
// other dependences
import Meta from 'vue-meta'
import VueLazyload from 'vue-lazyload'
// element-ui
import { Row, Col, Button, Alert, MessageBox, Notification, Dialog, Loading, Table, TableColumn, } from 'element-ui'
import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'
// files
import App from './App'
import store from './store/index.js'
import routes from './routes/index.js'
import { initAxios, initVDV, initRouter, getCurrentUser, registerPreventURLChange, errorRequestMessage, ajaxDataFilter } from '@/utils.js'
// components
import Btn from '@/components/Btn'
import Checkbox from '@/components/Checkbox'
import CheckboxGroup from '@/components/CheckboxGroup'
import Radio from '@/components/Radio'
// style
import '../node_modules/css-spacing/css/css-spacing.min.css'
import './assets/css/bootstrap.scss'
import '@/assets/css/helper.scss'
import '@/assets/css/common.scss'

//
Vue.config.productionTip = store.state.isDevelopment
Vue.config.debug = store.state.isDevelopment
Vue.config.devtools = store.state.isDevelopment

// axios
initAxios(axios, store, Vue)
function apiHttp(method, url, requestData, requestCompeleted) {
  if (url.startsWith('/')) {
    url = url.substr(1)
  }
  url = store.state.urls.api + '/' + url
  if (requestData) {
    requestData = ajaxDataFilter(requestData)
  }
  return Vue.http[method](url, requestData).then((resp) => {
    requestCompeleted && requestCompeleted()
    return Promise.resolve(resp.data, resp)
  }, e => {
    requestCompeleted && requestCompeleted()
    Vue.alert(`Failed. ${errorRequestMessage(e)}`)
    window.xx = e
    throw e
  })
}
Vue.apiGet = Vue.prototype.$apiGet = (url, requestCompeleted) => apiHttp('get', url, undefined, requestCompeleted)
Vue.apiPost = Vue.prototype.$apiPost = (...args) => apiHttp('post', ...args)

// VDV
initVDV(VueDataValidator, store, Vue)

// other dependences
Vue.use(Meta)
Vue.use(VueLazyload)

// element-ui
locale.use(lang)
Vue.use(Row)
Vue.use(Col)
Vue.use(Button)
Vue.use(Alert)
Vue.use(Dialog)
Vue.prototype.$msgbox = MessageBox
Vue.alert = Vue.prototype.$alert = (msg, title = 'Oops!') => MessageBox.alert(msg, title)
Vue.confirm = Vue.prototype.$confirm = MessageBox.confirm
Vue.prompt = Vue.prototype.$prompt = MessageBox.prompt
Vue.notify = Vue.prototype.$notify = Notification
Vue.prototype.$notifySuccess = (message, title = 'Successful') => Notification.success({title, message})
Vue.prototype.$notifyInfo = (message, title = 'Info') => Notification.info({title, message})
Vue.prototype.$notifyWarn = (message, title = 'Warning') => Notification.warning({title, message})
Vue.prototype.$notifyError = (message, title = 'Failed') => Notification.error({title, message})
Vue.prototype.$loading = Loading.service;
Vue.use(Loading.directive)
Vue.use(Table)
Vue.use(TableColumn)

// router
const router = initRouter(Router, Vue, store, routes, (to, from, next) => {
  // unauthorized
  store.state.intended = to
  next({name: 'unauthorized'})
})

registerPreventURLChange(Vue, router)
Vue.prototype.$state = store.state

// global components
Vue.component('Btn', Btn)
Vue.component('Checkbox', Checkbox)
Vue.component('CheckboxGroup', CheckboxGroup)
Vue.component('Radio', Radio)

// start
/* eslint-disable no-new */
const start = async () => {
  store.state.initialized = true
  // getCurrentUser by ajax when developing and not PhantomJS(prerender)
  if (store.state.isDevelopment && !/PhantomJS/.test(window.navigator.userAgent)) {
    await getCurrentUser()
  }
  new Vue({
    el: '#app',
    store,
    router,
    template: '<App/>',
    components: { App }
  })
}
start()
