<template lang="pug">
include ../../common.pug
+createCourse(1)
  form.row
    +formGroup('fields.name').col-sm-12
      +inputLg(placeholder="e.g. 5 Days Yoga Retreat in Bali" v-model="fields.name.value")
    +formGroup('fields.category_id').col-sm-8
      +selectLg(v-model="fields.category_id.value")
        option Fitness &amp; Sports - Yoya
    +formGroup('fields.level').col-sm-4
      +selectLg(v-model="fields.level.value")
        option Beginner
    .clearfix
    .col-sm-4
      +formGroup('fields.startDate')
        DatePicker(v-model="fields.startDate.value" :format="dateFormat")
    .col-sm-4
      +formGroup('fields.endDate')
        DatePicker(v-model="fields.endDate.value" :format="dateFormat")
    .col-sm-4.duration
      .form-group
        label &nbsp;
        //- .help-block2.duration 4 Days 3 Nights

    +formGroup('fields.description').col-sm-12
      +textarea(rows='5' placeholder="e.g. We will go to Rain Forest to hunt…." v-model="fields.description.value")
</template>

<script>
import base from './base'
import DatePicker from '@/components/DatePicker';
import {setTimeoutInterval} from '@/utils'
export default {
  extends: base,
  components: {DatePicker},
  data() {
    const state = this.$state.createCourse
    const {fields, validations} = state
    return {
      fields: fields.step1,
      validation: validations.step1,
      dateFormat: 'MMM dd yyyy',
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  created() {
    this.$validate(this.validation, this.fields)
  },
  mounted() {
    setTimeoutInterval(1000, 16, () => {
      this.validation.setDirty(false)
    })
  },
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCourse1{
  .duration{
    text-align: right;
  }
}
</style>
