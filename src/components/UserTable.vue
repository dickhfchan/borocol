<template lang="pug">
el-table.UserTable.w-100(v-if="data" :data='data' highlight-current-row='' @current-change="$emit('input', $event.id)")
  el-table-column(label='Avatar')
    template(slot-scope="scope")
      img.avatar(:src="scope.row.avatar || $state.imgAnonymous")
  el-table-column(property='name', label='Name' width="150")
  el-table-column(property='user_type', label='Type')
  el-table-column(label='Registered at' width="150")
    template(slot-scope="scope") {{$state.dtFormat(scope.row.created_at)}}
</template>

<script>

export default {
  // components: {},
  props: {
    value: null,
    data: null,
  },
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.UserTable{}
</style>
