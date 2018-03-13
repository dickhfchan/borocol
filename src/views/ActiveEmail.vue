<template lang="pug">
include ../common.pug
.ActiveEmail
  .container
    .content-card
      .text-center
        template(v-if="$state.user.email_confirmed")
          h1 Thank You
          ._1 You email({{$state.user.email}}) has been confirmed.
        template(v-else)
          h1 Confirm Your Email
          ._1
            p Prease check your inbox <i><b>{{$state.user.email}}</b></i> for a confirmation email. Clink the link in the email to confirm your email address.
            p If your email is not right, you can <a href="javascript:void(0)" @click.prevent="changeEmail">click here</a> to change it.
          GoogleRecaptcha(ref="recaptcha")
          el-button.send-btn.btn.btn-primary.btn-lg(@click="send" :loading="sending") Re-send confirmation email
</template>

<script>
import GoogleRecaptcha from '@/components/GoogleRecaptcha'

export default {
  components: {GoogleRecaptcha},
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
        await this.$apiPost(`/user/send-activation-email`, {email: this.$state.user.email, recaptcha})
        this.$notifySuccess(`Sent Successfully`)
      } catch (e) {
        throw e
      } finally {
        this.sending = false
      }
    },
    changeEmail() {
      this.$prompt('Please enter your email', {inputValue: this.$state.user.email}).then(async ({ value }) => {
        await this.$apiPost(`/user/update-email`, {email: value})
        this.$notifySuccess(`Your email has been changed successfully`)
        this.$state.user.email = value
      })
    },
  },
  async mounted() {
    const {token} = this.$route.query
    if (!this.$state.user.email_confirmed && token) {
      const loading = this.$loading({text: 'Confirming email'})
      try {
        await this.$apiPost(`/user/active-email`, {token})
        this.$notifySuccess(`Confirmed Successfully`)
        this.$state.user.email_confirmed = true
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
.ActiveEmail{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px;
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
