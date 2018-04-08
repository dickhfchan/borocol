<template lang="pug">
CardContainer.confirm-email.text-center
  template(v-if="$store.state.user.email_confirmed")
    h1 Thank You
    ._1 You email({{$store.state.user.email}}) has been confirmed.
  template(v-else)
    h1 Confirm Your Email
    ._1
      p Prease check your inbox <i><b>{{$store.state.user.email}}</b></i> for a confirmation email. Click the link in the email to confirm your email address.
      p If your email is not right, you can <a @click="changeEmail">click here</a> to change it.
    GoogleRecaptcha(ref="recaptcha")
    el-button.send-btn(size="large" type="primary" @click="send" :loading="sending") Re-send confirmation email
</template>

<script>
import CardContainer from '@/components/CardContainer'
import GoogleRecaptcha from '@/components/GoogleRecaptcha'

export default {
  middleware: 'auth',
  components: {GoogleRecaptcha, CardContainer},
  data() {
    return {
      sending: false,
    }
  },
  methods: {
    async send() {
      this.sending = true
      const recaptcha = await this.$refs.recaptcha.getToken()
      try {
        await this.$apiPost(`/user/send-confirmation-email`, {email: this.$store.state.user.email, recaptcha})
        this.$notifySuccess(`Sent Successfully`)
      } catch (e) {
        throw e
      } finally {
        this.sending = false
      }
    },
    changeEmail() {
      this.$prompt('Please enter your email', {inputValue: this.$store.state.user.email}).then(async ({ value }) => {
        await this.$apiPost(`/user/update-email`, {email: value})
        this.$notifySuccess(`Your email has been changed successfully`)
        this.$store.state.user.email = value
      })
    },
  },
  async mounted() {
    const {token} = this.$route.query
    if (!this.$store.state.user.email_confirmed && token) {
      const loading = this.$loading({text: 'Confirming email'})
      try {
        await this.$apiPost(`/user/confirm-email`, {token})
        this.$notifySuccess(`Confirmed Successfully`)
        this.$store.state.user.emailConfirmed = true
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
.confirm-email{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px 0;
  }
  ._1{
    margin: 60px 0;
  }
  .send-btn{
    text-transform: none;
    white-space: pre-wrap;
  }
}
</style>
