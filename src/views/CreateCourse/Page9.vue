<template lang="pug">
include ../../common.pug
+createCourse
  form.row
    ._1.col-sm-12
      +formGroup('fields.seats')
        span.question-circle.icon.icon-question-circle.mlm
        +input.mlm(v-model="fields.seats.value" type='number')
      +formGroup('fields.price')
        span.question-circle.icon.icon-question-circle.mlm
        +input.mlm(v-model="fields.price.value" type='number')
        span.help-block2.mlm.grey USD
    .mtm &nbsp;
    .col-sm-6
      +formGroup('fields.registrationStartDate')
        DatePicker(v-model="fields.registrationStartDate.value")
    .col-sm-6
      +formGroup('fields.registrationEndDate')
        DatePicker(v-model="fields.registrationEndDate.value")
    .form-group.col-sm-12.additional
      .dividing-line-title.mtl
        .line
        .mhm Additional
        .line
      .line1.mtm
        Checkbox(v-model="fields.earlyBirdDiscount.value")
        label.mls Early Bird Discount
        span.question-circle.icon.icon-question-circle.mlm
        label.mll Discount Rate
        +select.mls(v-model="fields.discountRate.value")
          option 10% off copy
          option 20% off copy
        label.mll Quota
        +select.mls(v-model="fields.quota.value")
          option 10% off copy
          option 20% off copy
      .line2
        Checkbox(v-model="fields.downPayment.value")
        label.mls Down Payment 25%
        span.question-circle.icon.icon-question-circle.mlm
</template>

<script>
import base from './base'
import DatePicker from '@/components/DatePicker';
export default {
  extends: base,
  components: {DatePicker},
  data() {
    return {
    }
  },

  // computed: {},
  // watch: {},
  // methods: {},
  created() {
    this.$validate(this.validation, this.fields)
  },
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCoursePage9{
  ._1{
    input{
      display: inline-block;
      width: 120px;
    }
  }
  .additional{
    input, select{
      display: inline-block;
      width: auto;
    }
    .line1{
      select{
        width: 95px;
      }
    }
  }
}
</style>
