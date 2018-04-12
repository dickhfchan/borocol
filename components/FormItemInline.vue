<template lang="pug">
.form-item.form-item-inline(
  :class="[vldClass, {'fi-break-line': breakLine || breakLine===''}]"
)
  slot(:field="field")
    .fii-layout
      slot(name="label")
        FormLabel.fii-label(:field="field")
      .fii-control
        slot(name="control" :field="field")
          el-select(v-if="type==='select'" v-model="value"
            :placeholder="placeholder" v-bind="controlAttrs"
          )
            el-option(
              v-for="item in options"
              :key="item.text"
              :label="item.text"
              :value="item.value"
            )
          el-input(v-else v-model="value" :type="type"
            :placeholder="placeholder" v-bind="controlAttrs"
          )
    FormError(:field="field")
</template>

<script>
import FormItem from '@/global-components/FormItem'

export default {
  extends: FormItem,
  props: {
    breakLine: {}, // break-line in medium screen and down
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
.fii-layout{
  display: flex;
  align-items: center;
}
.fii-label{
  flex-shrink: 0;
}
.fii-control{
  flex-grow: 1;
  margin-left: 1em;
}
@media(max-width: $medium) {
  .fi-break-line{
    .fii-layout{
      display: block;
    }
    .fii-label{
      display: block;
    }
    .fii-control{
      margin-left: 0;
    }
  }
}
</style>
