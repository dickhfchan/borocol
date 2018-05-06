// both server and client
import Vue from 'vue'
import * as VueDataValidator from 'vue-data-validator'
import * as hp from 'helper-js'

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
  // custom rules
  Object.assign(Vue.validator.rules, {
    phone({value}) {
      const t = value.split(' ')
      return t.length === 2 && t[0].length > 1 && t[0][0] === '+' && hp.isNumeric(t[0].substr(1)) && t[1].length > 0 && hp.isNumeric(t[1])
    },
    price({value}) {
      if (!hp.isNumber(value)) {
        return false
      }
      const [a, b] = value.toString().split('.')
      return b == null || b.length <= 2
    },
  })
  Object.assign(Vue.validator.messages, {
    phone({value}) {
      if (!value.includes('+')) {
        return 'Area code is required'
      }
      const t = value.split(' ')
      if (t.length !== 2 || !t[1]) {
        return 'Phone number is required'
      }
      return 'Invalid phone number'
    },
    price: 'The :name field is invalid price.',
  })
}
