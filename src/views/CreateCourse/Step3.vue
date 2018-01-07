<template lang="pug">
include ../../common.pug
+createCourse(3)
  form.row
    +formGroup('fields.address').col-sm-12
      +inputLg(v-model="fields.address.value")
    +formGroup('fields.city').col-sm-4
      +inputLg(v-model="fields.city.value")
    +formGroup('fields.country').col-sm-4
      +selectLg(v-model="fields.country.value")
        option(value="England") England
    +formGroup('fields.apiKey').col-sm-4
      .api-input
        img(src="~@/assets/img/google-map.png")
        +inputLg(v-model="fields.apiKey.value")
    +formGroup('fields.locationDescription').col-sm-12
      +textarea(v-model="fields.locationDescription.value" rows='3' placeholder='Please describe the location')
    +formGroup('fields.howToGetThere').col-sm-6
      +textarea(v-model="fields.howToGetThere.value" rows='3' placeholder='e.g. Please book your flight to arrive at JFK Airport, New York.')
    +formGroup('fields.whereToMeet').col-sm-6
      +textarea(v-model="fields.whereToMeet.value" rows='3')
</template>

<script>
import base from './base'
export default {
  extends: base,
  // components: {},
  data() {
    const state = this.$state.createCourse;
    const {fields, validations} = state
    const name = state.pageOrder[state.getRouteIndex()]
    return {
      name,
      fields: fields[name],
      validation: validations[name],
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
.CreateCourse3{
  .api-input{
    position: relative;
    img{
      position: absolute;
      top: 5px;
      left: 10px;
    }
    input{
      padding-left: 65px;
    }
  }
}
</style>
