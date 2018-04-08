// both server and client
import Vue from 'vue'
import * as VueDataValidator from 'vue-data-validator'

export default ({store}) => {
  Vue.use(VueDataValidator.validator)
  Object.assign(Vue.validator.rules, VueDataValidator.rules)
  Object.assign(Vue.validator.messages, store.state.lang === 'en' ? VueDataValidator.enMessages : VueDataValidator.zhCNMessages)
  Object.assign(Vue.validator, {
    validClass: '',
    invalidClass: 'is-error',
  })
  Vue.checkValidation = Vue.prototype.$checkValidation = (validation) => {
    return validation.check().then(data => data, e => {
      if (e.message === 'invalid') {
        Vue.alert(validation.getFirstError().message)
      }
      return Promise.reject(e)
    })
  }
}
