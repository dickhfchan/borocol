<template lang="pug">
include ../../common.pug
+createCourse(6)
  form
    +formGroup('fields.guestRequirement')
      +textarea(v-model="fields.guestRequirement.value" rows='3' placeholder="- Skill level\n- Occupations")
    +formGroup('fields.requestFormExisted')
      CheckboxGroup(:multiple="false" v-model="fields.requestFormExisted.value")
        Checkbox.mls(:value="false")
        span.mls No
        Checkbox.mls(:value="true")
        span.mls Yes
    ._1
      .form-group(v-for="(item, i) in fields.requestForm.value")
        Checkbox(v-model="item.enabled")
        span.mls Question {{i + 1}} :
        +textarea.mls(v-model="item.value" rows='3')
        .clearfix
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
.CreateCourse6{
  ._1{
    textarea{
      width: 75%;
      float: right;
      display: inline-block;
    }
  }
}
</style>
