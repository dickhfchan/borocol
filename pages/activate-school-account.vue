<template lang="pug">
CardContainer.activate-school-account
  .page-title Activate Account
  .space
  .space
  form.mtm(@submit.prevent="submit")
    FormItem
      FormLabel School Email
      el-input(v-model="email" readonly)
    el-row.mtm(:gutter="16")
      el-col(:span="12")
        FormItem(:field="fields.password" type="password")
      el-col(:span="12")
        FormItem(:field="fields.passwordConfirmation" type="password")
    GoogleRecaptcha(ref="recaptcha")
    .mtm
    el-button.btn-block(size="large" type="primary" native-type="submit"
      :loading="loading"
    ) Confirm & Complete Profile »
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
      email: this.$route.query.email,
      token: this.$route.query.token,
      validation: {},
      fields: {
        password: {
          rules: 'required|lengthBetween:5,16',
          text: 'Create a Password',
          nameInMessage: 'password',
        },
        passwordConfirmation: {
          rules: 'required|same:password',
          text: 'Confirm Password',
        },
      },
    }
  },
  methods: {
    submit() {
      this.$checkValidation(this.validation).then(async requestData => {
        this.loading = true
        const token = await this.$refs.recaptcha.getToken()
        requestData.recaptcha = token
        requestData.email = this.email
        requestData.token = this.token
        await this.$apiPost(`/school/activate`, requestData)
        this.$alert('Activate school successfully. Please login', {
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
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.activate-school-account{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 30px 20px;
  }
  .page-title{
    text-align: center;
    font-size: 38px;
    font-weight: 300;
  }
  .form-label{
    font-size: 13px;
  }
  .el-button{
    text-transform: none;
    white-space: pre-wrap;
  }
}
</style>
