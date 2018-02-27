<template lang="pug">
.GoogleRecaptcha.g-recaptcha(:data-sitekey="sitekey2", :data-callback='callbackName', data-size='invisible')
</template>

<script>
import $script from 'scriptjs'

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
          grecaptcha.reset()
        }
        grecaptcha.execute()
        this.grecaptchaExecuted = true
        return callbackProm
      })
    },
  },
  // created() {},
  mounted() {
    $script('https://www.google.com/recaptcha/api.js', () => {
      this.readyResolve()
    })
  },
}
</script>

<style lang="scss">
.GoogleRecaptcha{}
</style>
