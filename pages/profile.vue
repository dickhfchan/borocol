<template lang="pug">
.profile-page
  component(:is="$store.state.user.userType==='student'?'StudentProfile':'SchoolProfile'" :data="data")
</template>

<script>
import StudentProfile from '@/components/StudentProfile'
import SchoolProfile from '@/components/SchoolProfile'
import Vue from 'vue'

export default {
  async asyncData ({ store, params }) {
    const data = (await Vue.apiPost('/user/profile')).data
    data.email = store.state.user.email
    return {
      data,
    }
  },
  middleware: 'auth',
  components: {StudentProfile, SchoolProfile},
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
.profile-page{}
</style>
