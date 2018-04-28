<template lang="pug">
.partner
  .banner-bar
    .container.container-sm
      .banner-text-area
        .big-title Create a Listing for Free
        .medium-title Spend less money on marketing but actually making more.
        .small-title.mtl Let the world know your program in a cost-effective way.
        el-button.partner-btn(type="danger" @click="dialogVisible=true") Partner with Us
  .main
    .container.container-sm
      .paragraph-title How to become a Host?
      .paragraph1.mtl
        .paragraph1-left
          | We look for <b>English-Taught</b> Program for <b>“Grown-Ups”</b> provided by <b>Registered Company</b> or <b>Licensed Instructor</b>.
        el-button.paragraph1-btn.btn.btn-md Got a Question?
      .paragraph2
        .paragraph-title2 Program could be anything Adventurous and Fun!
        .paragraph2-text.mtl (Eg. 3-Days Diving Course in Okinawa, 5-Days Yoga Retreat in Bali, 2-weeks Language immersion, Group travel with singles, etc.)
      .part2
        .paragraph-title Why host on Borocol?
        el-row.mtl(:gutter="30")
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="locale")
            .part2-block-title.mtl Grow your business
            .part2-block-text.mtl Open business to the global market and take advantage of a new channel to increasvve reputation.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="increase")
            .part2-block-title.mtl Unlimited Listings
            .part2-block-text.mtl We support an unlimited number of listings to help your business grows.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="dialog")
            .part2-block-title.mtl Chat Box
            .part2-block-text.mtl Be able to connect users, answer any of their questions and trace records.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="bed")
            .part2-block-title.mtl Accommodation option
            .part2-block-text.mtl Host can offer resorts, dorm or other living options for users’ convenience.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="discount")
            .part2-block-title.mtl Manage Early Bird Discounts
            .part2-block-text.mtl Increase the chance of getting user registered at early stage. Host has full flexibility with quota and percentage of discount.
          el-col.part2-block(:span="8" :xs="12")
            .part2-block-icon
              Icon(name="file-text")
            .part2-block-title.mtl Transaction Record
            .part2-block-text.mtl To help host to leap track on the payment status of each application.
      .part3
        .part3-paragraph
          .part3-left
            b School’s Authority
          .part3-right We render host the power to “Accept/ Reject Booking” and offer “Partial Reimbursement” to user.
        .part3-paragraph
          .part3-left
            b Cancellation Policy
          .part3-right Host is required to follow our <b><a href="#">Cancellation Policy</a></b>. Read before you list a program.
        .part3-paragraph
          .part3-left
            b Service Charge (12%)
          .part3-right To maintain our platform and provide world-class customer service to both our host and user, Borocol takes <b>12%</b> service charge only when a transaction is successfully made.
        .part3-paragraph
          .part3-left
            b Payment Gateway
          .part3-right Stripe takes <b>2.9% + USD30¢</b> on per successful card charge.
            .mtl They support processing payments in <b>135+ currencies</b> (https://stripe.com/docs/currencies#charge-currencies) and allow you to accept variety of payment methods with one single API. (Visa, MasterCard, American Express, Alipay, Discover, Bitcoin, Wechat pay, JCB, 3DS, ACH Debits, etc.)
        .part3-paragraph
          .part3-left
            b Payment Arrangement
            br
            span (When do I receive payout?)
          .part3-right When a transaction is successfully made, the amount of your payouts will be calculated and send to your Stripe’s account within 24 hrs. Borocol don’t get in the middle.
        .part3-paragraph
          .part3-left
            b Customer Support
          .part3-right Our support team is always happy to assist both you and your customer in any cases.
  Dialog(title="Partner with Us" width="80%" v-model='dialogVisible')
    .space
    form(@submit.prevent="submit")
      el-row(:gutter="32")
        el-col(:sm="12")
          FormItem.mbm(:field="fields.name")
          FormItem.mbm(:field="fields.address")
          el-row(:gutter="16")
            el-col(:sm="12")
              FormItem.mbm(:field="fields.city")
            el-col(:sm="12")
              FormItem.mbm(:field="fields.country")
                NationSelect(slot="control" v-model="fields.country.value")
          FormItem.mbm(:field="fields.email")
          FormItem.mbm(:field="fields.introduction" type="textarea" :controlAttrs="{rows:3}")
          FormItem.mbm(:field="fields.website")
        el-col(:sm="12")
          el-row(:gutter="16")
            //- 1
            el-col(:span="24")
              .form-item
                .form-label
                  span.required-asterisk *
                  span Contact Person 1
            el-col(:sm="8").mbm
              el-input(v-model="cp[0].lastName" placeholder="Last Name")
            el-col(:sm="8").mbm
              el-input(v-model="cp[0].firstName" placeholder="First Name")
            el-col(:sm="8").mbm
              el-input(v-model="cp[0].title" placeholder="Title")
            el-col(:sm="16").mbm
              el-input(v-model="cp[0].email" placeholder="Email")
            el-col(:sm="8").mbm
              el-input(v-model="cp[0].tel" placeholder="Tel")
            //- 2
            el-col(:span="24")
              .form-item
                .form-label
                  span Contact Person 2
            el-col(:sm="8").mbm
              el-input(v-model="cp[1].lastName" placeholder="Last Name")
            el-col(:sm="8").mbm
              el-input(v-model="cp[1].firstName" placeholder="First Name")
            el-col(:sm="8").mbm
              el-input(v-model="cp[1].title" placeholder="Title")
            el-col(:sm="16").mbm
              el-input(v-model="cp[1].email" placeholder="Email")
            el-col(:sm="8").mbm
              el-input(v-model="cp[1].tel" placeholder="Tel")
          .space
          .space
          FormItem(:field="fields.registrationDocument")
            FileUploader(slot="control" v-model="fields.registrationDocument.value" :extensions="['pdf']")
          el-row.mtm(type="flex")
            el-checkbox(v-model="fields.agreed.value")
            small.mlm By signing up, I agree to Brocol Terms of Service, No Discrimination Policy, Payments Terms of Service, Privacy Policy, Refund Policy, and Host Guarantee Terms.
          .space
          .space
          GoogleRecaptcha(ref="recaptcha")
          el-button.btn-block(type="primary" size="large" :loading="loading" native-type="submit") SUBMIT
</template>

<script>
import Dialog from '@/components/Dialog'
import NationSelect from '@/components/NationSelect';
import FileUploader from '@/components/FileUploader';
import GoogleRecaptcha from '@/components/GoogleRecaptcha'

export default {
  layout: 'nomenu',
  components: {Dialog, NationSelect, FileUploader, GoogleRecaptcha},
  data() {
    return {
      dialogVisible: false,
      validation: {},
      fields: {
        name: {
          text: 'Name of School/ Insitution',
          rules: 'required',
          nameInMessage: 'name',
        },
        address: {
          text: 'Address',
          rules: 'required',
        },
        city: {
          text: 'City',
          rules: 'required',
        },
        country: {
          text: 'Country',
          rules: 'required',
        },
        email: {
          text: 'Email  (This will be used for receiving notifications)',
          rules: 'required|email',
          nameInMessage: 'email',
        },
        introduction: {
          text: 'Introduction (Such as course types)',
          rules: 'required',
          nameInMessage: 'introduction',
        },
        website: {
          text: 'Official Website',
          rules: 'required',
        },
        contactPersons: {
          type: 'json',
          rules: 'required|required2',
          value: [
            {
              lastName: null,
              firstName: null,
              title: null,
              email: null,
              tel: null,
            },
            {
              lastName: null,
              firstName: null,
              title: null,
              email: null,
              tel: null,
            },
          ],
          customRules: {
            required2({value}) {
              return Object.values(value[0]).every(v => v)
            },
          },
          messages: {
            required2({value}) {
              for (const key in value[0]) {
                if (!value[0][key]) {
                  return `The ${key} of contact person 1 is required`
                }
              }
            },
          },
        },
        registrationDocument: {
          text: 'Business Registration Document (BR)',
          nameInMessage: 'business registration document',
          rules: 'required',
          type: 'file',
        },
        agreed: {
          rules: 'required|accepted',
        },
      },
      loading: false,
    }
  },
  computed: {
    cp() {return this.fields.contactPersons.value},
  },
  // watch: {},
  methods: {
    submit() {
      if (this.loading) {
        return
      }
      const {recaptcha} = this.$refs
      this.$checkValidation(this.validation).then(async requestData => {
        this.loading = true
        const token = await recaptcha.getToken()
        requestData.recaptcha = token
        await this.$apiPost(`/school/register`, requestData)
        this.dialogVisible = false
        this.$alert('Please wait a few business days for the account to be reviewed.', '')
        this.loading = false
      }).catch(e => {
        this.loading = false
        return Promise.reject(e)
      })
    },
  },
  // created() {},
  mounted() {
    this.$validate(this.validation, this.fields)
    this.$testPanel({
      fill: () => {
        this.dialogVisible = true
        this.$testFill(this.fields)
        this.fields.country.value = 'US'
        this.cp[0].lastName = 'test'
        this.cp[0].firstName = 'test'
        this.cp[0].title= 'Admin'
        this.cp[0].email= 'example@example.com'
        this.cp[0].tel = '+1234125'
      },
    })
  },
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.partner{
  .banner-bar {
    background-image: url('~assets/img/partner-banner.jpg');
    background-size: cover;
    background-position: center;
    padding: 85px 0 85px 0;
  }
  .container {
  }
  .banner-text-area {
    width: 585px;
    color: rgb(255,255,255);
    text-align: right;
  }
  .big-title {
    font-weight: bold;
    font-size: 70px;
    text-shadow: 0px 3px 15.04px rgb(51, 51, 51);
  }
  .medium-title {
    margin: 50px 0 0 0;
    font-weight: bold;
    font-size: 27px;
    text-shadow: 0px 3px 15.04px rgb(51, 51, 51);
  }
  .small-title {
    font-size: 25px;
    font-weight: 500;
    text-shadow: 0px 3px 15.04px rgb(51, 51, 51);
  }
  .partner-btn {
    margin: 50px 0 0 0;
    font-weight: bold;
    font-size: 24px;
    $bg: rgb(255, 82, 103);
    background: $bg;
    &:hover{
      background: darken($bg, 5%);
    }
  }
  .main {
    padding: 95px 0 95px 0;
  }
  .paragraph-title {
    font-weight: 300;
    font-size: 38px;
  }
  $p1Color: rgb(1,105,109);
  .paragraph1 {
    color: $p1Color;
    font-size: 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    // xs extra small 特小屏幕 手机
    @media(max-width: $small) {
      font-size: 18px;
    }
  }
  .paragraph1-btn {
    margin: 0 0 0 15px;
    font-weight: 500;
    border: 2px solid $p1Color;
  }
  .paragraph2 {
    margin: 60px 0 0 0;
  }
  .paragraph-title2 {
    font-size: 21px;
  }
  .paragraph2-text {
    font-size: 16px;
  }
  .part2 {
    margin: 125px 0 0 0;
    text-align: center;
  }
  .part2-block {
    height: 250px;
  }
  .part2-block-icon {
    .icon{
      color: rgb(99,202,206);
      font-size: 54px;
    }
  }
  .part2-block-title {
    font-weight: bold;
    font-size: 24px;
  }
  .part2-block-text {
    font-size: 16px;
  }
  .part3 {
    margin: 135px 0 0 0;
  }
  .part3-paragraph {
    min-height: 120px;
    display: flex;
  }
  .part3-left {
    width: 400px;
    font-weight: bold;
    font-size: 24px;
    border-right: 1px solid #ccc;
    flex-shrink: 0;
  }
  .part3-right {
    padding: 0 50px;
    font-size: 16px;
    max-width: 600px;
    line-height: 25px;
    padding-bottom: 30px;
  }
  // xs extra small 特小屏幕 手机
  @media(max-width: $small) {
    .part3-paragraph {
      min-height: auto;
      display: block;
      margin-bottom: 20px;
    }
    .part3-left {
      width: auto;
      font-weight: bold;
      border-right: none;
    }
    .part3-right {
      padding: 0;
      max-width: auto;
      padding-bottom: 0;
    }
  }
}
</style>
