<template lang="pug">
include ../common.pug
.ConfirmEmail
  .container
    .content-card
      .text-center
        h1 Confirm Your Email
        ._1 Prease check your inbox for a confirmation email. Clink the link in the email to confirm your email address.
        button.send-btn.btn.btn-primary.btn-lg Re-send confirmation email
</template>

<script>
import Slider from '@/components/Slider';
import DatePicker from '@/components/DatePicker';
export default {
  components: {Slider, DatePicker},
  data() {
    return {
      priceRange: [0, 50000],
    }
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
.ConfirmEmail{
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
