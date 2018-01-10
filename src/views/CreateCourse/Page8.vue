<template lang="pug">
include ../../common.pug
+createCourse
  form
    .form-group
      label Options
      CheckboxGroup.mll(v-model="fields.options.value")
        Checkbox.mls(value="hotel")
        label.mls Hotel
        Checkbox.mls(value="resort")
        label.mls Resort
        Checkbox.mls(value="dorm")
        label.mls Dorm
        Checkbox.mls(value="others")
        label.mls Others
      +input.mll._1(v-model="fields.otherOptions.value")
    +formGroup('fields.locationDescription')
      +textarea(v-model="fields.locationDescription.value" rows='3' placeholder='e.g. ABC Resorts is located at Country side….')
    +formGroup('fields.facilities').facilities
      br
      CheckboxGroup(v-model="fields.facilities.value")
        Checkbox(value="wifi")
        label.mls WiFi
        Checkbox.mll(value="gym")
        label.mls Gym
        Checkbox.mll(value="air-conditionor")
        label.mls Air-conditionor
        Checkbox.mll(value="heater")
        label.mls Heater
        Checkbox.mll(value="tv")
        label.mls TV
        Checkbox.mll(value="balcony")
        label.mls Balcony
        br
        Checkbox(value="washing machine")
        label.mls Washing Machine
        Checkbox.mll(value="drying machine")
        label.mls Drying Machine
        Checkbox.mll(value="kitchen")
        label.mls Kitchen
        Checkbox.mll(value="swimming pool")
        label.mls Swimming pool
        br
        Checkbox(value="free parking")
        label.mls Free parking
        Checkbox.mll(value="wheel chair accessible")
        label.mls Wheel Chair Accessible
        Checkbox.mll(value="others")
        label.mls Others:
        +input.mll.other-facilities(v-model="fields.otherFacilities.value" placeholder='e.g. Other facilities')
    +formGroup('fields.photos')
      MultipleImageUploader(v-model="fields.photos.value")
    ._2.mtl
      .dividing-line-title
        .title
          .line
          span Room
          .line
      .form-group
        Checkbox(v-model="fields.room1Enabled.value")
        +select.mlm(v-model="fields.room1Type.value")
          option(value="shared") Shared Room
          option(value="standard") Standard Room
        label.mll Quota
        +input.quota-input.mls(v-model="fields.room1Quota.value" type="number")
        label.mll Price
        +input.price-input.mls(v-model="fields.room1Price.value" type="number")
        span.help-block2.mlm.grey USD
      .form-group
        Checkbox(v-model="fields.room2Enabled.value")
        +select.mlm(v-model="fields.room2Type.value")
          option(value="shared") Shared Room
          option(value="standard") Standard Room
        label.mll Quota
        +input.quota-input.mls(v-model="fields.room2Quota.value" type="number")
        label.mll Price
        +input.price-input.mls(v-model="fields.room2Price.value" type="number")
        span.help-block2.mlm.grey USD
</template>

<script>
import base from './base'
import MultipleImageUploader from '@/components/MultipleImageUploader';
export default {
  extends: base,
  components: {MultipleImageUploader},
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
.CreateCoursePage8{
  ._1{
    display: inline-block;
    width: 200px;
  }
  .facilities{
    line-height: 30px;
  }
  .other-facilities{
    display: inline-block;
    width: 150px;
  }
  ._2{
    select{
      display: inline-block;
      width: 150px;
    }
    .quota-input{
      display: inline-block;
      width: 80px;
    }
    .price-input{
      display: inline-block;
      width: 120px;
    }
    // input, select{
    //   display: inline-block;
    // }
    // select{
    //   width: auto;
    // }
    .icon{
      color: #ccc;
      font-size: 1.4em;
    }
  }
}
</style>
