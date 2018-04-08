<template lang="pug">
.form-item(:class="[field.getValidationClass && field.getValidationClass()]")
  slot(:field="field")
    FormLabel(:field="field")
    slot(name="control" :field="field")
      el-select(v-if="type==='select'" v-model="field.value"
        :placeholder="placeholder" v-bind="controlAttrs"
      )
        el-option(
          v-for="item in options"
          :key="item.text"
          :label="item.text"
          :value="item.value"
        )
      el-input(v-else v-model="field.value" :type="type"
        :placeholder="placeholder" v-bind="controlAttrs"
      )
    FormError(:field="field")
</template>

<script>
export default {
  props: {
    field: {},
    type: {default: 'text'},
    placeholder: {},
    options: {}, // for select. [{text, value}, ...]
    controlAttrs: {},
  },
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~assets/style/global.scss";
.form-item{}
.is-error{
  .el-input__inner,
  .el-input__inner:focus,
  .el-textarea__inner,
  .el-textarea__inner:focus{
    border-color: $dangerColor;
  }
}
</style>
