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
            .users-list
              .user-item.pas(v-for="item in possibleUsers" :class="{active:user_id===item.id}" @click="user_id=item.id")
                img.avatar(:src="item.avatar || anonymousAvatar")
                .text-area
                  label {{item.name}}
                  label.mlm {{item.user_type}}
                  .datetime Registered at: {{datetime(item.created_at)}}
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
import {errorRequestMessage, ajaxDataFilter} from '@/utils'
import GoogleRecaptcha from '@/components/GoogleRecaptcha'
import anonymousAvatar from '@/assets/img/anonymous.jpg'
import * as df from 'date-functions'

export default {
  components: {GoogleRecaptcha},
  data() {
    return {
      anonymousAvatar,
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
      this.processing = true
      const recaptcha = await this.$refs.recaptcha.getToken()
      this.$http.post(`${this.$state.urls.api}/user/send-reset-password-email`, {email: this.email, recaptcha}).then(({data}) => {
        this.$notifySuccess(`Sent Successfully`)
        this.sentCount++
      }, (e) => {
        console.log(e);
        this.$alert(`Sent Failed. ${errorRequestMessage(e)}`)
      }).then(() => {
        this.processing = false
      })
    },
    resetPassword() {
      if (!this.user_id) {
        this.$alert('Please select your account')
        return
      }
      this.validation.check().then(async data => {
        this.processing = true
        data = ajaxDataFilter(data)
        const token = await this.$refs.recaptcha.getToken()
        data.recaptcha = token
        data.token = this.$route.query.token
        data.user_id = this.user_id
        this.$http.post(`${this.$state.urls.api}/user/reset-password`, data).then(({data}) => {
          this.$alert('Reset password successfully. Please login', {
            callback: () => {
              const user = this.possibleUsers.find(v => v.id === this.user_id)
              this.$state.auth.role = user.user_type
              this.$state.auth.visible = true
            }
          })
        }, (e) => {
          console.log(e);
          this.$alert(`Reset Failed. ${errorRequestMessage(e)}`)
        })
      }, e => {
        console.log(e);
        if (e.message === 'invalid') {
          this.$alert(this.validation.getFirstError().message)
        }
      }).then(() => {
        this.processing = false
      })
    },
    datetime(ts) {
      const t = df.format(new Date(ts * 1000))
      return t.substr(0, t.length - 3)
    },
  },
  async mounted() {
    const {token} = this.$route.query
    if (token) {
      this.$validate(this.validation, this.fields)
      const loading = this.$loading({
         lock: true,
         text: 'Checking',
         spinner: 'el-icon-loading',
         background: 'rgba(0, 0, 0, 0.7)'
      })
      const recaptcha = await this.$refs.recaptcha.getToken()
      this.$http.post(`${this.$state.urls.api}/user/check-reset-password-token`, {token, recaptcha}).then(({data}) => {
        this.possibleUsers = data.data
        if (this.possibleUsers.length === 1) {
          this.user_id = this.possibleUsers[0].id
        }
      }, (e) => {
        console.log(e);
        this.$alert(`Checking Failed. ${errorRequestMessage(e)}`)
      }).then(() => {
        loading.close()
      })
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
  .user-item{
    display: flex;
    align-items: center;
    border-bottom: 1px solid #ccc;
    cursor: pointer;
    .text-area{
      margin-left: 20px;
    }
    &:hover{
      background: #fbfbfb;
    }
    &.active{
      background: #2196F3;
      color: #fff;
    }
  }
  .avatar{
    $side: 60px;
    width: $side;
    height: $side;
    border-radius: 100%;
  }
}
</style>
