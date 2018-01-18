<template lang="pug">
.Orders.container
  .content-card
    h1.content-card-title Orders
    //- form.content-card-body
    //-   .title I want to create
    //-   ._1
    //-     .text-box A Program<br><b>"With"</b> Accomodation <span class="icon icon-question-circle"></span>
    //-     .or OR
    //-     .text-box A Program<br><b>"Without"</b> Accomodation <span class="icon icon-question-circle"></span>
    //-   ._2
    //-     .item
    //-       Radio(v-model="fields.declared.value")
    //-       span.mls I hereby declare than all information porvide above is true and accurate.
    //-     .item
    //-       Radio(v-model="fields.agreed.value")
    //-       span.mls I agree to <a href="#">Borocol’s Terms of Service</a> and undestating <a href="#">the purpose of collecting personal data</a>.
    //-   a.btn.btn-primary.btn-lg.confirm-btn(@click="confirm") Confirm
</template>

<script>
export default {
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.Orders{}
</style>
