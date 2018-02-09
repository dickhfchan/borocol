import store from './index'
import {snakeCaseKeys} from '@/utils'

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
  register() {
    const vm = store.state.appVm
    if (this.submitting) {
      return
    }
    this.registrationValidation.check().then(data => {
      data = snakeCaseKeys(data)
      data.user_type = 'student'
      this.submitting = true
      return vm.$http.post(`${vm.$state.urls.api}/user/register`, data).then(({data}) => {
        vm.$alert(`Registered Successfully`)
      }, (e) => {
        console.log(e);
        vm.$alert(`Register Failed. ${e.response.data.message || ''}`)
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
