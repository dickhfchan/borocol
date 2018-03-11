<template lang="pug">
.GoogleSignin
  slot
</template>

<script>
import $script from 'scriptjs'
import {waitFor} from 'helper-js'

export default {
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    $script('https://apis.google.com/js/api:client.js', () => {
      waitFor(() => window.gapi).then(() => {
        const {gapi} = window
        gapi.load('auth2', () => {
         // Retrieve the singleton for the GoogleAuth library and set up the client.
         const auth2 = gapi.auth2.init({
           client_id: this.$state.google.signin.client_id,
           cookiepolicy: 'single_host_origin',
           // Request scopes in addition to 'profile' and 'email'
           //scope: 'additional_scope'
         });
         auth2.attachClickHandler(this.$el, {}, (googleUser) => {
           console.log(googleUser.getBasicProfile().getName());
           this.$emit('success', googleUser)
         }, (error) => {
           console.log(error);
         });
       });
      })
    })
  },
}
</script>

<style lang="scss">
.GoogleSignin{}
</style>
