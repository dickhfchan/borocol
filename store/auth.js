import Vue from 'vue'
import * as ut from '@/plugins/utils'

export const state = () => ({
  visible: false,
  mode: 'login',
  role: 'student',
  intended: null,
})

export const mutations = {
}
export const actions = {
  show({state}, mode, role) {
    if (mode) {
      state.mode = mode
    }
    if (role) {
      state.role = role
    }
    state.visible = true
  },
  fetchUser({rootState}) {
    return Vue.apiPost('/user/current-user').then(data => {
      const user = ut.cloneObjAndCamelCaseKey(data.data)
      rootState.user = user
      rootState.authenticated = user.isAuthenticated
      return rootState.user
    })
  },
}
