<template lang="pug">
.SchoolMyCourseStudent
  .container
    .content-card
      .titlebar
        .title2 English Max Course
        .date.mll Apr 30,17 - Sep 30,17
      .toolbar.align-c.mtm
        span Ref Ezewoszorxousn
        .flex-1
        .review-visa.btn2
          span.icon.icon-review-visa
        .mls Review Visa
        .accomodation.btn2.mlm
          span.icon.icon-accommodation
        .mls Accomodation
        .insurance.btn2.mlm
          span.icon.icon-insurance
        .mls Insurance
        .down-payment.btn2.mlm
          span.icon.icon-downpayment
        .mls Down Payment
        .icon.icon-printer.mlm.print
      .title3.mtl Student List (24 / 30)
      el-row.list.mtl(:gutter="8")
        el-col.item(v-for="i in 100" :key="i" :span="3")
          img.student-avatar(src="https://picsum.photos/100/100?image=1")
          .new-mark NEW!
          .student-name Philadelphian typesetter
          .joined-date Joined on May 25, 17
          .actions.mts
            .review-visa.btn2
              span.icon.icon-review-visa
            .accomodation.btn2.mls
              span.icon.icon-accommodation
            .insurance.btn2.mls
              span.icon.icon-insurance
            .down-payment.btn2.mls
              span.icon.icon-downpayment
            .refund-requested Refund requested
        el-col(:span="24")
          .show-more Show More
           .caret
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
.SchoolMyCourseStudent{
  background-image: url(~@/assets/img/orders-bg.jpg);
  background-size: 100%;
  @media(max-width: 1920px) {
    background-size: 1920px;
  }
  .content-card{
    padding: 60px 40px;
  }
  .titlebar{
    display: flex;
    align-items: center;
  }
  .title2 {
    font-weight: bold;
    font-size: 28px;
  }
  .date {
    font-weight: 300;
    font-size: 18px;
  }
  .toolbar {
    font-size: 13px;
    padding: 10px 0;
    border-bottom: 1px solid #ccc;
    display: flex;
  }
  .print{
    font-size: 22px;
    cursor: pointer;
  }
  .title3 {
    text-align: center;
    font-size: 22px;
    font-weight: 300;
  }
  .list{
    .item{
      text-align: center;
      margin-bottom: 20px;
      position: relative;
    }
    .new-mark{
      position: absolute;
      left:10px;
      top: 10px;
      background: rgb(255, 132, 149);
      color: #fff;
      font-weight: 500;
      padding: 0px 5px;
      font-size: 10px;
    }
  }
  .student-avatar{
    $side: 70px;
    width: $side;
    height: $side;
    border-radius: 100%;
  }
  .student-name{
    font-size: 13px;
  }
  .joined-date{
    font-size: 12px;
    color: #666;
  }
  .refund-requested{
    font-size: 12px;
    background: #808080;
    border-radius: 16px;
    color: #fff;
    display: inline-block;
    padding: 0 10px;
    margin-top: .5em;
  }
  .show-more{
    font-size: 12px;
    cursor: pointer;
    text-align: center;
    .caret{
      display: inline-block;
      margin-left: 10px;
    }
  }
}
</style>
