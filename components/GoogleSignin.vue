<template lang="pug">
.GoogleSignin
  slot
</template>

<script>
let apiLoaded
export default {
  props: {
    clientId: {},
  },
  components: {},
  data() {
    return {}
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  mounted() {
    const $script = require('scriptjs')
    const onload = window._googleSigninJsInit = () => {
      apiLoaded = true
      const {gapi} = window
      gapi.load('auth2', () => {
       // Retrieve the singleton for the GoogleAuth library and set up the client.
       const auth2 = gapi.auth2.init({
         client_id: this.clientId || this.$store.state.googleSignin.clientId,
         cookiepolicy: 'single_host_origin',
         // Request scopes in addition to 'profile' and 'email'
         //scope: 'additional_scope'
       });
       auth2.attachClickHandler(this.$el, {}, (googleUser) => {
         this.$emit('success', googleUser)
       }, (error) => {
         console.warn(error);
       });
     });
    }
    $script(`https://apis.google.com/js/platform.js?onload=_googleSigninJsInit`)
    if (apiLoaded) {
      // after first time
      onload()
    }
  },
}
</script>

<style lang="scss">
.GoogleSignin{}
</style>
