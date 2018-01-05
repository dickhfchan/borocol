<template lang="pug">
include ../../common.pug
+createCourse(2)
  form
    .row
      +formGroup('fields.groupSize').col-sm-3
        +inputLg(type="number" v-model="fields.groupSize.value")
      +formGroup('fields.gender').col-sm-3
        +selectLg(v-model="fields.gender.value")
          option(value="male") Male
          option(value="female") Female
      .form-group.age.col-sm-6
        label Age
        .slider-wrapper
          Slider(v-model="fields.ageRange.value" v-bind="sliderOptions")
    .form-group._1.mtm
      .help-block2 * Number of hours
      input.form-control.input-lg.mlm.hours(type="number" v-model="fields.hours.value")
      .flex-1
      .help-block2 * The course will be offered in
      input.form-control.input-lg.mlm.language(type='input', placeholder='Language' v-model="fields.language.value")
    .form-group._2.mtm
      label Host / Instructor(s) Info
      ._2-1
        .upload
          .icon.icon-plus
        textarea.form-control(rows='3' v-model="fields.instructorInfo.value")
    .form-group.mtm
      label *Will you issue Certificate to your guest?
      CheckboxGroup(:multiple="false" v-model="fields.issueCertificate.value")
        Checkbox.mls(:value="false")
        span.mls No
        Checkbox.mls(:value="true")
        span.mls Yes
      textarea.form-control.mts(rows='3' placeholder='e.g. With at least 70% attendance...' v-model="fields.certificate.value")
</template>

<script>
import base from './base'
import Slider from '@/components/Slider';

export default {
  extends: base,
  components: {Slider},
  data() {
    const state = this.$state.createCourse;
    const {fields, validations} = state
    const name = state.pageOrder[state.getRouteIndex()]
    return {
      name,
      fields: fields[name],
      validation: validations[name],
      sliderOptions: {
        min: 16,
        max: 100,
      },
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
.CreateCourse2{
  .slider-wrapper{
    position: relative;
    top: 2em;
  }
  ._1{
    display: flex;
    justify-content: space-between;
    .hours{
      width: 70px;
    }
    .language{
      width: 200px;
    }
  }
  ._2{

  }
  ._2-1{
    $h: 100px;
    height: $h;
    display: flex;
    justify-content: space-between;
    .upload{
      $side: $h;
      width: $side;
      height: $side;
      line-height: $side;
      display: inline-block;
      border: $bd1 dashed 2px;
      margin-right: 20px;
      flex-shrink: 0;
      text-align: center;
      .icon{
        font-size: 30px;
        color: $bd1;
      }
    }
    textarea{
      height: 100%;
    }
  }
}
</style>
