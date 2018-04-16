<template lang="pug">
CardContainer.unauthenticated.text-center
  h1 Unauthenticated
  .mtl
  el-button.login-btn(size="large" type="primary" @click="$store.dispatch('auth/show')") Login
</template>

<script>
import CardContainer from '@/components/CardContainer'
export default {
  layout: 'nomenu',
  components: {CardContainer},
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
.unauthenticated{
  .container{
    max-width: 500px;
  }
  .content-card{
    padding: 40px 0;
  }
  .login-btn{
    padding: 15px 60px;
  }
}
</style>
