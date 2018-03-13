<template lang="pug">
include ../common.pug
.ResetPassword
  .container
    .content-card
      .text-center
        h1 Reset Password
        form._2.ptm(v-if="token")
          +formGroup('fields.password')
            +inputLg(type="password" v-model="fields.password.value")
          +formGroup('fields.passwordConfirmation')
            +inputLg(type="password" v-model="fields.passwordConfirmation.value")
          .form-group(v-if="possibleUsers && possibleUsers.length > 1")
            label * Select your account
            UserTable(:data="possibleUsers" v-model="user_id")
          GoogleRecaptcha(ref="recaptcha")
          el-button.btn.btn-primary.btn-lg.btn-block.mtm(@click="resetPassword" :loading="processing") Submit
          br
          a(href="javascript:void(0)" @click="token = null") Go send reset password email
        template(v-else)
          ._1
            p(v-if="sentCount") Prease check your inbox <i><b>{{email}}</b></i> for a reset password email. Clink the link in the email to reset your password.
            .form-group
              +inputLg(placeholder="Please enter your account email address" v-model="email")
          GoogleRecaptcha(ref="recaptcha")
          el-button.btn.btn-primary.btn-lg(@click="send" :loading="processing") Send reset password email
</template>

<script>
import {errorRequestMessage, checkValidation} from '@/utils'
import GoogleRecaptcha from '@/components/GoogleRecaptcha'
import UserTable from '@/components/UserTable'

export default {
  components: {GoogleRecaptcha, UserTable},
  data() {
    return {
      processing: false,
      email: null,
      sentCount: 0,
      token: this.$route.query.token,
      validation: {},
      fields: {
        password: {
          rules: 'required|lengthBetween:5,16',
          text: 'Password',
        },
        passwordConfirmation: {
          rules: 'required|same:password',
          text: 'Repeat password',
        },
      },
      user_id: null,
      possibleUsers: null,
    }
  },
  methods: {
    async send() {
      try {
        this.processing = true
        const recaptcha = await this.$refs.recaptcha.getToken()
        await this.$apiPost(`/user/send-reset-password-email`, {email: this.email, recaptcha})
        this.$notifySuccess(`Sent Successfully`)
        this.sentCount++
      } catch (e) {
        throw e
      } finally {
        this.processing = false
      }
    },
    resetPassword() {
      if (!this.user_id) {
        this.$alert('Please select your account')
        return
      }
      checkValidation(this.validation).then(async requestData => {
        this.processing = true
        const token = await this.$refs.recaptcha.getToken()
        requestData.recaptcha = token
        requestData.token = this.$route.query.token
        requestData.user_id = this.user_id
        await this.$apiPost(`/user/reset-password`, requestData)
        this.$alert('Reset password successfully. Please login', {
          callback: () => {
            const user = this.possibleUsers.find(v => v.id === this.user_id)
            this.$state.auth.role = user.user_type
            this.$state.auth.visible = true
          }
        })
        this.processing = false
      }).catch(e => {
        this.processing = false
        throw e
      })
    },
  },
  async mounted() {
    const {token} = this.$route.query
    if (token) {
      this.$validate(this.validation, this.fields)
      const loading = this.$loading({text: 'Checking'})
      const recaptcha = await this.$refs.recaptcha.getToken()
      try {
        const data = this.$apiPost(`/user/check-reset-password-token`, {token, recaptcha})
        this.possibleUsers = data.data
        if (this.possibleUsers.length === 1) {
          this.user_id = this.possibleUsers[0].id
        }
      } catch (e) {
        throw e
      } finally {
        loading.close()
      }
    }
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.ResetPassword{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px;
  }
  ._1{
    margin: 60px 0;
  }
  .btn{
    text-transform: none;
    white-space: pre-wrap;
  }
  ._2{
    text-align: left;
  }
}
</style>
