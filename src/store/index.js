import Vue from 'vue'
import Vuex from 'vuex'
import initialData from '@/initialData'
// import {studlyCase} from 'helper-js'
import urls from './urls.js'
// import menu from './menu'
import createCourse from './createCourse'
// import noImg from '../assets/img/noThumb.jpg'
// import createLogger from '@/../node_modules/vuex/src/plugins/logger.js'

Vue.use(Vuex)

//
const state = {
  urls,
  // menu,
  createCourse,
  appVm: null,
  createCourseVm: null,
  //
  environment: process.env.NODE_ENV,
  isDevelopment: true,
  // isCROS: true,
  // // follow will be enabled when isCROS
  // CROS: {
  //   CSRFTokenRequired: true,
  //   updateCSRFTokenIn: 5 * 60 * 1000, // ms
  // },
  initialized: false,
  builtAt: window.builtAt,
  lang: 'en',
  authenticated: false,
  user: null,
  //
  //
  genderOptions: [
    {value: 'male', text: 'Male'},
    {value: 'female', text: 'Female'},
  ],
  style: {
    small: 768,
    medium: 992,
    large: 1200,
    superLarge: 1500,
  },
  //
  // noImg,
}
Object.assign(state, initialData)
//
const store = new Vuex.Store({
  state: state,
  mutations: {
    // initialized(state, val) { state.initialized = val },
  },
  actions: {
    // logout({state}, $router) {
    //   Vue.http.get(state.urls.logout).then(() => {
    //   }, () => {}).then(() => {
    //     state.authenticated = false
    //     state.user = null
    //     $router && $router.push({name: 'login'})
    //   })
    // },
  },
  // strict: store.state.isDevelopment
  // plugins: store.state.isDevelopment ? [createLogger()] : []
})

export default store
