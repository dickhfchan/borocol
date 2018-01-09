<template lang="pug">
include ../../common.pug
+createCourse
  form
    +formGroup('fields.schedule')
      +textarea(v-model="fields.schedule.value" rows="8" placeholder="e.g.\nDay 1\nDay 2\nDay 3")
    +formGroup('fields.mealsIncluded')
      CheckboxGroup(:multiple="false" v-model="fields.mealsIncluded.value")
        Checkbox.mls(:value="false")
        span.mls No
        Checkbox.mls(:value="true")
        span.mls Yes
    .form-group
      CheckboxGroup(v-model="fields.meals.value")
        Checkbox(value="breakfast")
        label.mls Breakfast
        Checkbox.mls(value="lunch")
        label.mls Lunch
        Checkbox.mls(value="bunch")
        label.mls Bunch
        Checkbox.mls(value="dinner")
        label.mls Dinner
    +textarea(v-model="fields.mealsInfo.value" rows='5' placeholder='More Information')
</template>

<script>
import base from './base'
export default {
  extends: base,
  // components: {},
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
.CreateCoursePage4{
}
</style>
