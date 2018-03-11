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
import {errorRequestMessage} from '@/utils'
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
      this.$http.post(`${this.$state.urls.api}/user/send-activation-email`, {email: this.$state.user.email, recaptcha}).then(({data}) => {
        this.$notifySuccess(`Sent Successfully`)
      }, (e) => {
        console.log(e);
        this.$alert(`Sent Failed. ${errorRequestMessage(e)}`)
      }).then(() => {
        this.sending = false
      })
    },
    changeEmail() {
      this.$prompt('Please enter your email', {inputValue: this.$state.user.email}).then(({ value }) => {
        this.$http.post(`${this.$state.urls.api}/user/update-email`, {email: value}).then(({data}) => {
          this.$notifySuccess(`Your email has been changed successfully`)
          this.$state.user.email = value
        }, (e) => {
          console.log(e);
          this.$alert(`Failed. ${errorRequestMessage(e)}`)
        })
      })
    },
  },
  mounted() {
    const {token} = this.$route.query
    if (!this.$state.user.email_confirmed && token) {
      const loading = this.$loading({
         lock: true,
         text: 'Confirming email',
         spinner: 'el-icon-loading',
         background: 'rgba(0, 0, 0, 0.7)'
      })
      this.$http.post(`${this.$state.urls.api}/user/active-email`, {token}).then(({data}) => {
        this.$notifySuccess(`Confirmed Successfully`)
        this.$state.user.email_confirmed = true
      }, (e) => {
        console.log(e);
        this.$alert(`Confirm Failed. ${errorRequestMessage(e)}`)
      }).then(() => {
        loading.close()
      })
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
