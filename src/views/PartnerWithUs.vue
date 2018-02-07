<template lang="pug">
.PartnerWithUs
  .banner-bar
    .container.container-sm
      .banner-text-area
        .big-title Create a Listing for Free
        .medium-title Spend less money on marketing but actually making more.
        .small-title.mtl Let the world know your program in a cost-effective way.
        .partner-btn.btn.btn-danger.btn-lg Partner with Us
  .main
    .container.container-sm
      .paragraph-title How to become a Host?
      .paragraph1.flex.justify-sb.align-c.mtl
        .paragraph1-left
          | We look for <b>English-Taught</b> Program for <b>“Grown-Ups”</b> provided by <b>Registered Company</b> or <b>Licensed Instructor</b>.
        .paragraph1-btn.btn.btn-md Got a Question?
      .paragraph2
        .paragraph-title2 Program could be anything Adventurous and Fun!
        .paragraph2-text.mtl (Eg. 3-Days Diving Course in Okinawa, 5-Days Yoga Retreat in Bali, 2-weeks Language immersion, Group travel with singles, etc.)
      .part2
        .paragraph-title.text-center Why host on Borocol?
        el-row.mtl(:gutter="30")
          el-col.part2-block.text-center(:span="8")
            .part2-block-icon
              span.icon.icon-earth
            .part2-block-title.mtl Grow your business
            .part2-block-text.mtl Open business to the global market and take advantage of a new channel to increasvve reputation.
          el-col.part2-block.text-center(:span="8")
            .part2-block-icon
              span.icon.icon-increase
            .part2-block-title.mtl Unlimited Listings
            .part2-block-text.mtl We support an unlimited number of listings to help your business grows.
          el-col.part2-block.text-center(:span="8")
            .part2-block-icon
              span.icon.icon-talk
            .part2-block-title.mtl Chat Box
            .part2-block-text.mtl Be able to connect users, answer any of their questions and trace records.
        el-row.mtl(:gutter="30")
          el-col.part2-block.text-center(:span="8")
            .part2-block-icon
              span.icon.icon-accommodation
            .part2-block-title.mtl Accommodation option
            .part2-block-text.mtl Host can offer resorts, dorm or other living options for users’ convenience.
          el-col.part2-block.text-center(:span="8")
            .part2-block-icon
              span.icon.icon-discount
            .part2-block-title.mtl Manage Early Bird Discounts
            .part2-block-text.mtl Increase the chance of getting user registered at early stage. Host has full flexibility with quota and percentage of discount.
          el-col.part2-block.text-center(:span="8")
            .part2-block-icon
              span.icon.icon-file-text-o
            .part2-block-title.mtl Transaction Record
            .part2-block-text.mtl To help host to leap track on the payment status of each application.
      .part3
        .part3-paragraph.flex
          .part3-left
            b School’s Authority
          .part3-right We render host the power to “Accept/ Reject Booking” and offer “Partial Reimbursement” to user.
        .part3-paragraph.flex
          .part3-left
            b Cancellation Policy
          .part3-right Host is required to follow our <b><a href="#">Cancellation Policy</a></b>. Read before you list a program.
        .part3-paragraph.flex
          .part3-left
            b Service Charge (12%)
          .part3-right To maintain our platform and provide world-class customer service to both our host and user, Borocol takes <b>12%</b> service charge only when a transaction is successfully made.
        .part3-paragraph.flex
          .part3-left
            b Payment Gateway
          .part3-right Stripe takes <b>2.9% + USD30¢</b> on per successful card charge.
            .mtl They support processing payments in <b>135+ currencies</b> (https://stripe.com/docs/currencies#charge-currencies) and allow you to accept variety of payment methods with one single API. (Visa, MasterCard, American Express, Alipay, Discover, Bitcoin, Wechat pay, JCB, 3DS, ACH Debits, etc.)
        .part3-paragraph.flex
          .part3-left
            b Payment Arrangement
            br
            span (When do I receive payout?)
          .part3-right When a transaction is successfully made, the amount of your payouts will be calculated and send to your Stripe’s account within 24 hrs. Borocol don’t get in the middle.
        .part3-paragraph.flex
          .part3-left
            b Customer Support
          .part3-right Our support team is always happy to assist both you and your customer in any cases.
</template>

<script>
export default {
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.PartnerWithUs{
  .banner-bar {
    background-image: url('~@/assets/img/partner-banner.jpg');
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
  }
  .paragraph1-btn {
    margin: 0 0 0 125px;
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
  }
  .part2-block {

  }
  .part2-block-icon {
    color: rgb(99,202,206);
    font-size: 54px;
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
  .part3-paragraph {
    min-height: 120px;
  }
}
</style>
