<template lang="pug">
.GoogleRecaptcha()
</template>

<script>
import $script from 'scriptjs'
import {waitFor} from 'helper-js'

export default {
  props: {
    sitekey: {},
  },
  // components: {},
  data() {
    return {
      ready: new Promise((resolve, reject) => {
        this.readyResolve = resolve
      }),
      callbackName: `GoogleRecaptchaCallback_${this._uid}`,
    }
  },
  computed: {
    sitekey2() {
      try {
        return this.sitekey || this.$store.state.recaptcha.sitekey
      } catch (e) {}
    },
  },
  // watch: {},
  methods: {
    getToken() {
      return this.ready.then(() => {
        const {grecaptcha} = window
        const callbackProm = new Promise((resolve, reject) => {
          window[this.callbackName] = resolve
        })
        if (this.grecaptchaExecuted) {
          grecaptcha.reset(this.grecaptchaId)
        }
        grecaptcha.execute(this.grecaptchaId)
        this.grecaptchaExecuted = true
        return callbackProm
      })
    },
  },
  // created() {},
  mounted() {
    $script('https://www.google.com/recaptcha/api.js', () => {
      waitFor(() => window.grecaptcha).then(() => {
        this.grecaptchaId = window.grecaptcha.render( this.$el, { sitekey : this.sitekey2, size: 'invisible', callback: this.callbackName });
        this.readyResolve()
      })
    })
  },
}
</script>

<style lang="scss">
.GoogleRecaptcha{}
</style>
