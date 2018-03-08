<template lang="pug">
.Unauthorized
  .container
    .content-card.text-center
      h1 Unauthorized
      a.btn.btn-primary.btn-md.mtl(@click="$state.auth.show('login')") Login
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
.Unauthorized{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px;
  }
}
</style>
