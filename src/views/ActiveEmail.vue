<template lang="pug">
include ../common.pug
.ActiveEmail
  .container
    .content-card
      .text-center
        el-alert(title='Illegal request' type='error' show-icon) 
        h1 Confirm Your Email
        ._1 Prease check your inbox for a confirmation email. Clink the link in the email to confirm your email address.
        button.send-btn.btn.btn-primary.btn-lg Re-send confirmation email
</template>

<script>
export default {

}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.ActiveEmail{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px;
  }
  ._1{
    margin: 60px 0;
  }
  .send-btn{
    text-transform: none;
    white-space: pre-wrap;
  }
}
</style>
