<template lang="pug">
CardContainer.my-course-visa
  div
    .title Profile
    .content-card-body
      .left
        img.avatar(v-lazy="'https://picsum.photos/100/100?image=100'")
      .right
        .bar1
          .name Philadelphian typesetter
          .bar1-right
            .time Joined on May 25, 17
            Icon.mls(name="printer")
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
                el-input(:rows="5" type="textarea")
                el-button.save-btn(type="primary") Save
          .right2
            .line
              Icon.review-visa-icon(name="review-visa")
              .text Review Visa
            .line
              Icon.accomodation-icon(name="bed")
              .text Accomodation
            .line
              Icon.insurance-icon(name="insurance")
              .text Insurance
            .line
              Icon.downpayment-icon(name="downpayment")
              .text Down Payment
            .btns
              el-button.remove-student-btn.btn(type="button")
                Icon(name="trash")
                span.mls Remove Student
              br
              el-button.message-btn(type="primary" size="large")
                span.icon.icon-talk
                Icon(name="dialog")
                span.mls Message
  CloseBtn(type="2")
</template>

<script>
import CardContainer from '@/components/CardContainer'

export default {
  components: {CardContainer},
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
@import "~assets/style/global.scss";
.my-course-visa{
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
    font-weight: 500;
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
  .btns{
  }
  .remove-student-btn{
    margin-top: 1em;
    background: none;
    padding: 0;
    border: none;
    // &:hover{
    //   background: $bg1;
    // }
    .icon{
      position: relative;
      // top: -3px;
      display: inline;
    }
  }
  .message-btn{
    margin-top: 1em;
    padding: 16px 25px;
    .icon{
      position: relative;
      top: 1px;
    }
  }
}
</style>
