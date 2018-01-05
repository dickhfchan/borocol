<template lang="pug">
.CreateCourseIndex
  .content-card
    form.content-card-body
      .title I want to create
      ._1
        .text-box A Program<br><b>"With"</b> Accomodation <span class="icon icon-question-circle"></span>
        .or OR
        .text-box A Program<br><b>"With"</b> Accomodation <span class="icon icon-question-circle"></span>
      ._2
        .item
          Radio(v-model="fields.declared.value")
          span.mls I hereby declare than all information porvide above is true and accurate.
        .item
          Radio(v-model="fields.agreed.value")
          span.mls I agree to <a href="#">Borocol’s Terms of Service</a> and undestating <a href="#">the purpose of collecting personal data</a>.
      a.btn.btn-primary.btn-lg.confirm-btn(@click="confirm") Confirm
</template>

<script>
import base from './base'
export default {
  extends: base,
  // components: {},
  data() {
    const state = this.$state.createCourse
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
  methods: {
    confirm() {
      this.state.checkAndGoNextPage().catch(e => {
        this.$alert('Please check the terms')
      })
    },
  },
  created() {
    this.$validate(this.validation, this.fields)
  },
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.CreateCourseIndex{
  .content-card-body {
    text-align: center;
    width: 60%;
    padding: 120px 0;
    margin: 0 auto;
    .title{
      font-size: 35px;
      font-weight: $fw-light;
      margin-bottom: 80px;
    }
  }
  ._1 {
    display: flex;
    align-items: center;
  }
  .text-box{
    flex-grow: 1;
    width: 300px;
    display: inline-block;
    border: 1px solid $bd1;
    border-radius: $bdr;
    padding: 20px;
    .icon{
      color: #ccc;
      font-size: 1.4em;
    }
  }
  .or{
    display: inline-block;
    height: 100%;
    line-height: 100%;
    vertical-align: middle;
    padding: 30px;
  }
  ._2{
    margin-top: 30px;
    text-align: left;
    a{
      font-weight: $fw-md;
    }
  }
  .confirm-btn{
    margin-top: 50px;
  }
}
</style>
