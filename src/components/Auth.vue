<template lang="pug">
include ../common.pug
.Auth(v-if="state.visible")
  el-dialog(:visible.sync='state.visible', width="430px" custom-class="auth-dialog")
    form(v-if="state.mode==='login'")
      .mbm(v-if="state.role==='student'")
        .openid.openid-facebook
          .icon-wrapper
            span.icon.icon-facebook
          | Log in with Facebook
        .openid.openid-google.mtm
          .icon-wrapper
            img(src="~@/assets/img/google-icon-colorful.png")
          | Log in with Google
        .dividing-line-title.mtm
          .line
          small.mhm or
          .line
      .form-group
        label Email
        +inputLg(v-model="state.loginFields.email.value" name="email")
      .form-group
        label Password
        +inputLg(v-model="state.loginFields.password.value" type="password" name="password")
      .form-group
        Checkbox(v-model="state.loginFields.remember.value")
        label.mls Remember Me
        router-link.pull-right(:to="{name: 'resetPassword'}"): b Forget Password?
      button.login-btn.btn.btn-primary.btn-block.btn-lg Log in
      .flex.justify-sb.align-c.mtl
        b Without an Account?
        a(href="javascript:void(0)" @click="register").btn.btn-primary-outline {{state.role==='student' ? 'Sign up' : 'Partner with Us'}}
    form(v-else @submit.prevent="state.register")
      template(v-if="registerStep===1")
        .mbm
          .openid.openid-facebook
            .icon-wrapper
              span.icon.icon-facebook
            | Sign up with Facebook
          .openid.openid-google.mtm
            .icon-wrapper
              img(src="~@/assets/img/google-icon-colorful.png")
            | Sign up with Google
          .dividing-line-title.mtm
            .line
            small.mhm or
            .line
          a.btn.btn-primary.btn-block.btn-lg.text-transform-n.mtm(@click="registerStep=2") Sign Up with Email
      template(v-else)
        .text-center Sign up with <a><b>Facebook</b></a> or <a><b>Google</b></a>
        .form-group.mtl
          label Email
          +inputLg(v-model="state.registrationFields.email.value" name="email")
        .form-group
          label Name on Passport
          .flex
            +inputLg(v-model="state.registrationFields.firstName.value" name="firstName" placeholder="First Name")
            +inputLg.mlm(v-model="state.registrationFields.lastName.value" name="lastName" placeholder="Last Name")
        .flex
          .form-group
            label Create a Password
            +inputLg(v-model="state.registrationFields.password.value" name="password" type="password")
          .form-group.mlm
            label Confirm Password
            +inputLg(v-model="state.registrationFields.passwordConfirmation.value" name="passwordConfirmation" type="password")
        .form-group.flex
          Checkbox.flex-s0(v-model="state.registrationFields.agreed.value")
          small.mlm By signing up, I agree to Brocol Terms of Service, No Discrimination Policy, Payments Terms of Service, Privacy Policy, Refund Policy, and Host Guarantee Terms.
        button.btn.btn-primary.btn-block.btn-lg Sign Up

      .flex.justify-sb.align-c.mtl
        b Already Have an Borocol Account?
        a(href="javascript:void(0)" @click="state.mode='login'").btn.btn-primary-outline Log in
    template(slot='title')
      .title {{state.mode === 'login' ? 'Log in' : 'Sign Up'}}
      .roles(v-if="state.mode === 'login'")
        .role(v-for="item in roles" :class="{active: state.role === item}" @click="state.role=item") {{studlyCase(item)}}
      .divider(v-else)
    span(slot='footer')
</template>

<script>
import {studlyCase} from 'helper-js'

export default {
  components: {},
  data() {
    return {
      state: this.$state.auth,
      roles: ['student', 'school'],
      registerStep: 1,
    }
  },
  // computed: {},
  // watch: {},
  methods: {
    studlyCase,
    partnerWithUs() {
      this.state.visible = false
      this.$router.push({name: 'partnerWithUs'})
    },
    register() {
      if (this.state.role === 'school') {
        this.partnerWithUs()
      } else {
        this.registerStep = 1
        this.state.mode = 'register'
      }
    },
  },
  // created() {},
  mounted() {
    this.$validate(this.state.loginValidation, this.state.loginFields)
    this.$validate(this.state.registrationValidation, this.state.registrationFields)
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.Auth{}
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
      background: $bg2;
      color: #fff;
    }
  }
  .divider{
    height: 15px;
    background: $bg2;
  }
  .btn-primary-outline{
    font-size: 12px;
    font-weight: bold;
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
  label{
    font-size: 13px;
    color: initial;
  }
}
</style>
