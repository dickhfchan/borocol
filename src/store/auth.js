import Vue from 'vue'
import store from './index'
import {checkValidation, errorRequestMessage, getCurrentUser, sessionStorage2} from '@/utils'
import {objectGet} from 'helper-js'

const auth = {
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
    checkValidation(this.loginValidation).then(async requestData => {
      this.submitting = true
      const token = await recaptcha.getToken()
      requestData.recaptcha = token
      await vm.$apiPost(`/user/login`, requestData)
      await getCurrentUser()
      vm.$notifySuccess(`Logined Successfully`)
      this.visible = false
      this.afterLogin()
      this.submitting = false
      this.checkThirdAccount()
    }).catch(e => {
      this.submitting = false
      throw e
    })
  },
  afterLogin() {
    const vm = store.state.appVm
    if (vm.$state.intended) {
      const to = vm.$state.intended
      vm.$state.intended = null
      if (vm.$route.name === 'unauthorized') {
        vm.$router.push({path: to.fullPath})
      }
    }
  },
  register(recaptcha) {
    const vm = store.state.appVm
    if (this.submitting) {
      return
    }
    checkValidation(this.registrationValidation).then(async requestData => {
      this.submitting = true
      const token = await recaptcha.getToken()
      requestData.recaptcha = token
      requestData.user_type = 'student'
      await vm.$apiPost('/user/register', requestData)
      await getCurrentUser()
      vm.$notifySuccess(`Registered Successfully`)
      vm.$router.push({name: 'activeEmail'})
      this.visible = false
      this.checkThirdAccount()
    }).catch(e => {
      this.submitting = false
      throw e
    })
  },
  async logout() {
    const vm = store.state.appVm
    await vm.$apiPost('/user/logout')
    await getCurrentUser()
    if (objectGet(vm.$route, 'meta.auth')) {
      vm.$router.push({name: 'home'})
    }
  },
  //
  formLoading: false,
  possibleUsers: null,
  processingThird: null,
  async googleSignin(googleUser) {
    this.processingThird = 'google'
    const vm = store.state.appVm
    try {
      this.formLoading = true
      const token = googleUser.getAuthResponse().id_token
      const data = await vm.$apiPost(`/google/login`, {token})
      if (data.linked) {
        await getCurrentUser()
        vm.$notifySuccess(`Logined Successfully`)
        this.visible = false
        this.afterLogin()
      } else if (data.possible_users.length === 0) {
        vm.$alert('No linked account found, please sign up first')
        const profile = googleUser.getBasicProfile()
        sessionStorage2.set('google_profile', {
          name: profile.getName(),
          avatar: profile.getImageUrl(),
          email: profile.getEmail(),
        })
      } else {
        this.possibleUsers = data.possible_users
      }
    } catch (e) {
      throw e
    } finally {
      this.formLoading = false
    }
  },
  async linkGoogleAccount(user_id) {
    const vm = store.state.appVm
    await vm.$apiPost('/google/link', {user_id})
    await getCurrentUser()
  },
  async linkFacebookAccount(user_id) {
    const vm = store.state.appVm
    await vm.$apiPost('/facebook/link', {user_id})
    await getCurrentUser()
  },
  checkThirdAccount() {
    const vm = store.state.appVm
    let profile = sessionStorage2.get('google_profile')
    let loading
    if (profile) {
      vm.$confirm(`Do you want link your Google account(name: ${profile.name}, email: ${profile.email})?`).then(async () => {
        try {
          loading = vm.$loading()
          await this.linkGoogleAccount(vm.$state.user.id)
          sessionStorage2.set('google_profile', null)
        } catch (e) {
          throw e
        } finally {
          loading.close()
        }
      })
    } else {
      profile = sessionStorage2.get('facebook_profile')
      if (profile) {
        vm.$confirm(`Do you want link your Facebook account(name: ${profile.name}, email: ${profile.email})?`).then(async () => {
          try {
            loading = vm.$loading()
            await this.linkFacebookAccount(vm.$state.user.id)
            sessionStorage2.set('facebook_profile', null)
          } catch (e) {
            throw e
          } finally {
            loading.close()
          }
        })
      }
    }
  },
  async googleSignUp(googleUser) {
    const vm = store.state.appVm
    try {
      this.formLoading = true
      const token = googleUser.getAuthResponse().id_token
      const data = await vm.$apiPost(`/google/register`, {token})
      await getCurrentUser()
      vm.$notifySuccess(`Registered Successfully`)
    } catch (e) {
      throw e
    } finally {
      this.formLoading = false
    }
  },
}

export default auth
