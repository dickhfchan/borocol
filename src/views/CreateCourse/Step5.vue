<template lang="pug">
include ../../common.pug
+createCourse(5)
  form
    +formGroup('fields.provide')
      +textarea(v-model="fields.provide.value" rows='5' placeholder='e.g.\n- Equipment\n- Airport Pickup\n- Towels ')
    +formGroup('fields.guestNeedsToBring')
      +textarea(v-model="fields.guestNeedsToBring.value" rows='5' placeholder='e.g.\n- Goggle\n- Swimsuits ')
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
.CreateCourse5{}
</style>
