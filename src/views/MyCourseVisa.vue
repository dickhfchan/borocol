<template lang="pug">
include ../common.pug
.MyCourseVisa
  .container
    .content-card.has-close
      .title Profile
      .content-card-body
        .left
          img.avatar(v-lazy="'https://picsum.photos/100/100?image=100'")
        .right
          .bar1
            .name Philadelphian typesetter
            .bar1-right
              .time Joined on May 25, 17
              .space
              span.icon.icon-printer
          .wrapper
            .left2
              div
                .line
                  .key Country of Residence:
                  .value New York, United States
                .line
                  .key Phone:
                  .value (852) 9000 0000 0000
                .line
                  .key Email:
                  .value example@gmail.com
                .line
                  .key Birthday:
                  .value Sep30, 1989
                .line
                  .key Gender:
                  .value Female
                .line
                  .key Nationality:
                  .value Chinese
                .line
                  .key Passport No.:
                  .value H201747119
                .line
                  .key Expiry Date:
                  .value May 30, 18
                .line
                  .key Isuued Country:
                  .value Hong Kong
                .line
                  .key Emergency Contact:
                  .value
                    span Dorothy, Mother, +852 9000 000
                    br
                    span Jon, Father, +852 9120 000
                form.form-group
                  label Status:
                  +textarea(rows="5")
                  button.save-btn.btn.btn-primary.btn-lg() Save
            .right2
              .line
                span.review-visa.icon.icon-review-visa
                .text Review Visa
              .line
                span.accomodation.icon.icon-accommodation
                .text Accomodation
              .line
                span.insurance.icon.icon-insurance
                .text Insurance
              .line
                span.downpayment.icon.icon-downpayment
                .text Down Payment
              .btns
                button.remove-student-btn.btn(type="button")
                  span.icon.icon-trash-o
                  span  Remove Student
                br
                button.message-btn.btn.btn-primary(type="button")
                  span.icon.icon-talk
                  span Message
      span.icon.icon-close.close
</template>

<script>
export default {
  components: {},
  data() {
    return {
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.MyCourseVisa{
  background: $bg3;
  // common
  .btn{
    padding: 10px 25px;
    text-transform: initial;
    .icon{
      font-size: 30px;
      width: 1.5em;
      display: inline-block;
      vertical-align: middle;
    }
  }
  .line{
    display: flex;
  }
  //
  .title {
    font-size: 21px;
    color: rgb(51, 51, 51);
    text-align: center;
  }
  .content-card-body{
    display: flex;
  }
  .left{
    width: 150px;
  }
  .right{
    flex-grow: 1;
  }
  .avatar{
    width: 130px;
    height: 130px;
    border-radius: 200px;
  }
  .bar1{
    display: flex;
    justify-content: space-between;
    align-items:flex-end;
    margin: 25px 0;
    padding-bottom: .5em;
    border-bottom: 2px solid #ccc;
  }
  .bar1-right{
    display: flex;
    justify-content: space-between;
    align-items:flex-end;
  }
  .name{
    font-size: 22px;
    font-weight: $fw-md;
  }
  .time{
    color: grey;
  }
  .icon-printer{
    cursor: pointer;
    font-size: 27px;
  }
  //
  .wrapper{
    display: flex;
    justify-content: space-between;
  }
  .left2{
    margin-right: 1em;
    flex-grow: 1;
    font-size: 16px;
    line-height: 30px;
  }
  .key{
    width: 200px;
    text-align: right;
    margin-right: 2em;
  }
  .save-btn{
    margin-top: 1em;
    float: right;
  }
  .right2{
    .line{
      align-items: center;
      margin-bottom: .5em;
      .icon{
        cursor: pointer;
        display: inline-block;
        width: 25px;
        height: 25px;
        line-height: 25px;
        text-align: center;
        font-size: 18px;
        color: #fff;
        border-radius: 3px;
        margin-right: .5em;
      }
    }
  }
  .review-visa{
    background: #69a2dd;
  }
  .accomodation {
    background: #968ecb;
  }
  .insurance {
    background: #63cace;
  }
  .downpayment {
    background: #a6c875;
  }
  .btns{
  }
  .remove-student-btn{
    margin-top: 1em;
    background: none;
    padding: 0;
    // &:hover{
    //   background: $bg1;
    // }
    .icon{
      position: relative;
      top: -3px;
      display: inline;
    }
  }
  .message-btn{
    margin-top: 1em;
    padding: 5px 25px;
  }
}
</style>
