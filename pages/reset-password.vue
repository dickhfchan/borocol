<template lang="pug">
CardContainer.reset-password.text-center
  h1 Reset Password
  form._2.mtm(v-if="token" @submit.prevent="resetPassword")
    FormItem(:field="fields.password" type="password")
    FormItem.mtm(:field="fields.passwordConfirmation" type="password")
    GoogleRecaptcha(ref="recaptcha")
    .mtm
    el-button.btn-block(size="large" type="primary" native-type="submit" :loading="loading") Submit
    br
    a(@click="token = null") Go send reset password email
  template(v-else)
    ._1
      p(v-if="sentCount") Prease check your inbox <i><b>{{email}}</b></i> for a reset password email. Click the link in the email to reset your password.
      label Please enter your account email address
      el-input.mts(placeholder="Email" v-model="email")
    GoogleRecaptcha(ref="recaptcha")
    el-button.btn-block(size="large" type="primary" @click="send" :loading="loading") Send reset password email
</template>

<script>
import CardContainer from '@/components/CardContainer'
import GoogleRecaptcha from '@/components/GoogleRecaptcha'

export default {
  layout: 'nomenu',
  components: {GoogleRecaptcha, CardContainer},
  data() {
    return {
      loading: false,
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
          text: 'Confirm Password',
        },
      },
    }
  },
  methods: {
    async send() {
      try {
        this.loading = true
        const recaptcha = await this.$refs.recaptcha.getToken()
        await this.$apiPost(`/user/send-reset-password-email`, {email: this.email, recaptcha})
        this.$notifySuccess(`Sent Successfully`)
        this.sentCount++
      } catch (e) {
        throw e
      } finally {
        this.loading = false
      }
    },
    resetPassword() {
      this.$checkValidation(this.validation).then(async requestData => {
        this.loading = true
        const token = await this.$refs.recaptcha.getToken()
        requestData.recaptcha = token
        requestData.token = this.$route.query.token
        requestData.userId = this.userId
        await this.$apiPost(`/user/reset-password`, requestData)
        this.$alert('Reset password successfully. Please login', {
          callback: () => {
            this.$store.dispatch('auth/show', 'login', this.user.user_type)
          }
        })
        this.loading = false
      }).catch(e => {
        this.loading = false
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
        const data = await this.$apiPost(`/user/check-reset-password-token`, {token, recaptcha})
        this.user = data.data
        this.userId = this.user.id
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
@import "~assets/style/global.scss";
.reset-password{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px;
  }
  ._1{
    margin: 30px 0;
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
