<template lang="pug">
include ../../common.pug
+createCourse
  form
    +formGroup('fields.provide')
      +textarea(v-model="fields.provide.value" rows='5' placeholder='- Equipment\n- Airport Pickup\n- Towels ')
    +formGroup('fields.guestNeedsToBring')
      +textarea(v-model="fields.guestNeedsToBring.value" rows='5' placeholder='- Goggle\n- Swimsuits ')
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
.CreateCoursePage5{}
</style>
