<template lang="pug">
.auth(v-if="state.visible")
  el-dialog(:visible.sync='state.visible', width="430px" custom-class="auth-dialog")
    template(slot='title')
      .title {{state.mode === 'login' ? 'Log in' : 'Sign Up'}}
      .roles(v-if="state.mode === 'login'")
        .role(
          v-for="item in roles" :class="{active: state.role === item}"
          @click="state.role=item"
        ) {{studlyCase(item)}}
      .divider(v-else)
    form(v-if="state.mode==='login'" v-loading="loading" @submit.prevent="login")
      .mbs(v-if="state.role==='student'")
        .openid.openid-facebook
          .icon-wrapper
            Icon(name="facebook")
          | Log in with Facebook
        GoogleSignin.openid.openid-google.mtm(@success="googleSignin")
          .icon-wrapper
            img(src="~assets/img/google-icon-colorful.png")
          | Log in with Google
        .dividing-line-title.mtm
          .line
          small.mhm or
          .line
      FormItem(:field="loginFields.email")
        el-input(slot="control" v-model="loginFields.email.value" name="email")
      FormItem.mtm(:field="loginFields.password")
        el-input(slot="control" v-model="loginFields.password.value" type="password" name="password")
      el-row.mtm(type="flex" align="middle" justify="space-between")
        el-checkbox(v-model="loginFields.remember.value") Remember Me
        a(@click="goResetPassword"): b Forgot Password?
      GoogleRecaptcha(ref="recaptcha")
      .mtm
      el-button.btn-block(size="large" native-type="submit" type="primary") Log in
      el-row.mtm(type="flex" align="middle" justify="space-between")
        b Without an Account?
        el-button.go-register-btn.btn-primary-outline(size="large" @click="goRegister")
         | {{state.role==='student' ? 'Sign up as studnet' : 'Partner with Us'}}
    form(v-else v-loading="loading" @submit.prevent="register")
      template(v-if="registerStep===1")
        .mbm
          .openid.openid-facebook
            .icon-wrapper
              Icon(name="facebook")
            | Sign up with Facebook
          GoogleSignin.openid.openid-google.mtm(@success="googleSignUp")
            .icon-wrapper
              img(src="~assets/img/google-icon-colorful.png")
            | Sign up with Google
          .dividing-line-title.mtm
            .line
            small.mhm or
            .line
          .mtm
          el-button.btn-block.text-transform-n(size="large" type="primary" @click="registerStep=2") Sign Up with Email
      template(v-else)
        .text-center Sign up with <a @click="registerStep=1"><b>Facebook or Google</b></a>
        .mtl
        FormItem(:field="regFields.email")
        .mtm
          .form-label
            span.required-asterisk *
            span Name on Passport
          el-row(:gutter="16")
            el-col(:span="12")
              FormItem(:field="regFields.firstName")
                el-input(v-model="regFields.firstName.value" placeholder="First Name")
            el-col(:span="12")
              FormItem(:field="regFields.lastName")
                el-input(v-model="regFields.lastName.value" placeholder="Last Name")
          FormError(:fields="[regFields.firstName, regFields.lastName]")
        el-row.mtm(:gutter="16")
            el-col(:span="12")
              FormItem(:field="regFields.password" type="password")
            el-col(:span="12")
              FormItem(:field="regFields.passwordConfirmation" type="password")
        el-row.mtm(type="flex")
          el-checkbox(v-model="regFields.agreed.value")
          small.mlm By signing up, I agree to Brocol Terms of Service, No Discrimination Policy, Payments Terms of Service, Privacy Policy, Refund Policy, and Host Guarantee Terms.
        FormError(:field="regFields.agreed")
        GoogleRecaptcha(ref="recaptcha")
        .mtm
        el-button.btn-block(size="large" native-type="submit" type="primary") Sign Up

      el-row.mtl(type="flex" justify="space-between" align="middle")
        b Already Have an Borocol Account?
        el-button.go-login-btn.btn-primary-outline(size="large" @click="state.mode='login'") Log in
    span(slot='footer')
</template>

<script>
import {studlyCase, sessionStorage2} from 'helper-js'
import GoogleRecaptcha from '@/components/GoogleRecaptcha'
import GoogleSignin from '@/components/GoogleSignin'

export default {
  components: {GoogleRecaptcha, GoogleSignin},
  data() {
    return {
      state: this.$store.state.auth,
      roles: ['student', 'school'],
      registerStep: 1,
      loading: false,
      //
      loginFields: {
        email: {
          text: 'Email',
          rules: 'required|email',
        },
        password: {
          text: 'Password',
          rules: 'required',
        },
        remember: {
          value: false,
        },
      },
      loginValidation: {},
      regFields: {
        email: {
          text: 'Email',
          rules: 'required|email',
        },
        firstName: {
          text: 'first name',
          rules: 'required',
        },
        lastName: {
          text: 'last name',
          rules: 'required',
        },
        password: {
          text: 'Create a Password',
          rules: 'required|lengthBetween:5,16',
          nameInMessage: 'password',
        },
        passwordConfirmation: {
          text: 'Confirm Password',
          rules: 'required|same:password',
        },
        agreed: {
          nameInMessage: 'service and policy',
          rules: 'required|accepted',
          value: false,
        },
      },
      regValidation: {},
    }
  },
  // computed: {},
  // watch: {},
  methods: {
    studlyCase,
    login() {
      if (this.loading) {
        return
      }
      const {recaptcha} = this.$refs
      this.$checkValidation(this.loginValidation).then(async requestData => {
        this.loading = true
        const token = await recaptcha.getToken()
        requestData.recaptcha = token
        requestData.userType = this.state.role
        await this.$apiPost(`/user/login`, requestData)
        await this.$store.dispatch('auth/fetchUser')
        this.$notifySuccess(`Logined Successfully`)
        this.state.visible = false
        this.afterLogin()
        this.loading = false
      }).catch(e => {
        this.loading = false
        return Promise.reject(e)
      })
    },
    afterLogin() {
      const {intended} = this.$route.query
      if (intended) {
        if (this.$route.name === 'unauthenticated') {
          this.$router.push(intended)
        }
      }
      this.checkThirdAccount()
    },
    register() {
      if (this.loading) {
        return
      }
      const {recaptcha} = this.$refs
      this.$checkValidation(this.regValidation).then(async requestData => {
        this.loading = true
        const token = await recaptcha.getToken()
        requestData.recaptcha = token
        requestData.user_type = 'student'
        await this.$apiPost('/user/register', requestData)
        await this.$store.dispatch('auth/fetchUser')
        this.$notifySuccess(`Registered Successfully`)
        this.$router.push({name: 'confirm-email'})
        this.state.visible = false
        this.afterLogin()
        this.loading = false
      }).catch(e => {
        this.loading = false
        return Promise.reject(e)
      })
    },
    goResetPassword() {
      this.state.visible = false
      this.$router.push({name: 'reset-password'})
    },
    goRegister() {
      if (this.state.role === 'school') {
        this.goPartnerWithUs()
      } else {
        this.registerStep = 1
        this.state.mode = 'register'
      }
    },
    goPartnerWithUs() {
      this.state.visible = false
      this.$router.push({name: 'partner'})
    },
    async googleSignin(googleUser) {
      try {
        this.loading = true
        const token = googleUser.getAuthResponse().id_token
        const data = await this.$apiPost(`/google/login`, {token})
        if (data.linked) {
          await this.$store.dispatch('auth/fetchUser')
          this.$notifySuccess(`Logined Successfully`)
          this.state.visible = false
          this.afterLogin()
        } else {
          this.$alert('No linked account found, please login or sign up')
          const profile = googleUser.getBasicProfile()
          sessionStorage2.set('google_profile', {
            name: profile.getName(),
            avatar: profile.getImageUrl(),
            email: profile.getEmail(),
          })
        }
      } catch (e) {
        throw e
      } finally {
        this.loading = false
      }
    },
    async linkGoogleAccount(user_id) {
      await this.$apiPost('/google/link', {user_id})
      // after linked, user email_confirmed may be changed, so fetch user again
      await this.$store.dispatch('auth/fetchUser')
    },
    async linkFacebookAccount(user_id) {
      await this.$apiPost('/facebook/link', {user_id})
      // after linked, user email_confirmed may be changed, so fetch user again
      await this.$store.dispatch('auth/fetchUser')
    },
    checkThirdAccount() {
      let profile = sessionStorage2.get('google_profile')
      let loading
      if (profile) {
        this.$confirm(`Do you want link your Google account(name: ${profile.name}, email: ${profile.email})?`).then(async () => {
          try {
            loading = this.$loading()
            await this.linkGoogleAccount(this.$store.state.user.id)
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
          this.$confirm(`Do you want link your Facebook account(name: ${profile.name}, email: ${profile.email})?`).then(async () => {
            try {
              loading = this.$loading()
              await this.linkFacebookAccount(this.$store.state.user.id)
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
      try {
        this.loading = true
        const token = googleUser.getAuthResponse().id_token
        const data = await this.$apiPost(`/google/register`, {token})
        await this.$store.dispatch('auth/fetchUser')
        this.$notifySuccess(`Registered Successfully`)
        sessionStorage2.set('google_profile', null)
        sessionStorage2.set('facebook_profile', null)
        this.state.visible = false
        this.afterLogin()
      } catch (e) {
        throw e
      } finally {
        this.loading = false
      }
    },
  },
  // created() {},
  mounted() {
    this.$validate(this.loginValidation, this.loginFields)
    this.$validate(this.regValidation, this.regFields)
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.auth{}
.auth-dialog{
  max-width: 98%;
  .el-dialog__header{
    padding: 0;
  }
  .title{
    text-align: center;
    padding: 15px 0;
    font-size: 40px;
    font-weight: 300;
  }
  .role{
    width: 50%;
    display: inline-block;
    padding: 16px 0;
    text-align: center;
    font-weight: 500;
    background: #dddddd;
    cursor: pointer;
    &.active{
      background: $primaryColor;
      color: #fff;
    }
  }
  .divider{
    height: 15px;
    background: $primaryColor;
  }
  .btn-primary-outline{
    font-size: 12px;
    font-weight: bold;
    background: transparent;
    border: 2px solid $primaryColor;
    color: $primaryColor;
  }
  .el-form--label-top .el-form-item__label{
    padding: 0;
  }
  .el-input__inner{
    height: 46px;
    line-height: 46px;
  }
  //
  .openid{
    padding: 10px 0;
    text-align: center;
    font-weight: 500;
    border: 1px solid #ccc;
    position: relative;
    cursor: pointer;
    .icon-wrapper{
      position: absolute;
      left: 20px;
    }
    .icon{
      font-size: 18px;
    }
    img{
      width: 18px;
    }
  }
  .openid-facebook{
    background: rgb(58, 88, 158);
    border-color: rgb(58, 88, 158);
    color: #fff;
  }
  .openid-google{
    border-color: #ccc;
  }
  .go-register-btn, .go-login-btn{
    font-size: 15px;
    text-transform: none;
    padding: 12px 20px;
  }
}
</style>
