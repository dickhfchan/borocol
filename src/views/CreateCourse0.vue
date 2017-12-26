<template lang="pug">
.CreateCourse0.container
  .content-card
    .content-card-header
      .step Step 1
      .title Start with the basic
    .content-card-progress-bar.progress
      .progress-bar.progress-bar-warning(role='progressbar', style='width: 12%') 12%
    form.content-card-body
      .title I want to create
      ._1
        .text-box A Program<br><b>"With"</b> Accomodation <span class="icon icon-question-circle"></span>
        .or OR
        .text-box A Program<br><b>"With"</b> Accomodation <span class="icon icon-question-circle"></span>
      ._2
        .item
          Radio
          span.mls I hereby declare than all information porvide above is true and accurate.
        .item
          Radio
          span.mls I agree to <a href="#">Borocol’s Terms of Service</a> and undestating <a href="#">the purpose of collecting personal data</a>.
      button.btn.btn-primary.btn-lg.confirm-btn Confirm
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
@import "~@/assets/css/global.scss";
.CreateCourse0{
  .content-card-body {
    text-align: center;
    width: 60%;
    padding-left: 0;
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
