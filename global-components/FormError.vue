<template lang="pug">
.form-error
  .form-error-items(v-if="visible")
    .form-error-item(v-for="item in errors") {{item.message}}
</template>

<script>
export default {
  props: {
    field: {},
    fields: {},
  },
  // components: {},
  // data() {
  //   return {}
  // },
  computed: {
    visible() {
      const fields = this.field ? [this.field] : this.fields
      if (fields && fields[0] && fields[0].isValidationErrorsVisible) {
        return fields[0].isValidationErrorsVisible(fields)
      }
      return false
    },
    errors() {
      const fields = this.fields || [this.field]
      if (!fields[0].isValidationErrorsVisible) {
        // not inited
        return []
      }
      const errors = []
      fields.forEach(fld => {
        if (fld.dirty && !fld.valid) {
          for (const ruleName in fld.errors) {
            errors.push({
              fieldName: fld.name,
              ruleName,
              message: fld.errors[ruleName].message,
            })
          }
        }
      })
      return errors
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.form-error{}
.form-error-items{
  .form-error-item:first-child{
    margin-top: 5px;
  }
}
.form-error-item{
  color: $dangerColor;
  font-size: 13px;
  line-height: 16px;
}
</style>
