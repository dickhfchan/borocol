import Vue from 'vue'
import anonymousAvatar from '~/assets/img/anonymous.jpg'
import * as ut from '@/plugins/utils'


export const strict = false
export const state = () => ({
  anonymousAvatar,
  authenticated: false,
  user: {},
  lang: 'en',
  api: `/api/v1`,
})

export const mutations = {
  authenticated (state, user) {
    state.user = user
    state.authenticated = user.is_authenticated
  }
}

export const actions = {
  nuxtServerInit ({ state }, { req }) {
    return Vue.apiGet('/initial-data').then(data => {
      Object.assign(state, ut.cloneObjAndCamelCaseKey(data.data))
    })
  }
}
