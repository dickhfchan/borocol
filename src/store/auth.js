import store from './index'
import {ajaxDataFilter, errorRequestMessage} from '@/utils'

export default {
  visible: false,
  mode: 'login',
  role: 'student',
  loginFields: {
    email: {
      rules: 'required|email',
    },
    password: {
      rules: 'required',
    },
    remember: {
      value: false,
    },
  },
  loginValidation: {},
  registrationFields: {
    email: {
      rules: 'required|email',
    },
    firstName: {
      rules: 'required',
      nameInMessage: 'first name',
    },
    lastName: {
      rules: 'required',
      nameInMessage: 'last name',
    },
    password: {
      rules: 'required|lengthBetween:5,16',
    },
    passwordConfirmation: {
      rules: 'required|same:password',
      nameInMessage: 'password confirmation',
    },
    agreed: {
      rules: 'required|accepted',
    },
  },
  registrationValidation: {},
  submitting: false,
  show(mode, role) {
    if (mode) {
      this.mode = mode
    }
    if (role) {
      this.role = role
    }
    this.visible = true
  },
  login(recaptcha) {
    const vm = store.state.appVm
    if (this.submitting) {
      return
    }
    this.loginValidation.check().then(async data => {
      this.submitting = true
      data = ajaxDataFilter(data)
      const token = await recaptcha.getToken()
      data.recaptcha = token
      return vm.$http.post(`${vm.$state.urls.api}/user/login`, data).then(({data}) => {
        vm.$alert(`Logined Successfully`)
        vm.$state.authenticated = true
        vm.$state.user = data.data
      }, (e) => {
        console.log(e);
        vm.$alert(`Logined Failed. ${errorRequestMessage(e)}`)
      })
    }, e => {
      console.log(e);
      if (e.message === 'invalid') {
        vm.$alert(this.registrationValidation.getFirstError().message)
      }
    }).then(() => {
      this.submitting = false
    })
  },
  register(recaptcha) {
    const vm = store.state.appVm
    if (this.submitting) {
      return
    }
    this.registrationValidation.check().then(async data => {
      this.submitting = true
      data = ajaxDataFilter(data)
      const token = await recaptcha.getToken()
      data.recaptcha = token
      data.user_type = 'student'
      return vm.$http.post(`${vm.$state.urls.api}/user/register`, data).then(({data}) => {
        vm.$alert(`Registered Successfully`)
        vm.$router.push({name: 'activeEmail'})
      }, (e) => {
        console.log(e);
        vm.$alert(`Register Failed. ${errorRequestMessage(e)}`)
      })
    }, e => {
      console.log(e);
      if (e.message === 'invalid') {
        vm.$alert(this.registrationValidation.getFirstError().message)
      }
    }).then(() => {
      this.submitting = false
    })
  },
}
