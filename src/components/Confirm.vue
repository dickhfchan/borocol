<template lang="pug">
Modal.conform.confirm-layer(
  v-if="visible",
  :options="modalOptions",
  @close="close", @ok="ok"
)
  div(slot="body") {{text}}
</template>

<script >
import Modal from './Modal.vue'
const Confirm = {
  install (Vue, vm) {
    Vue.confirm = Vue.prototype.$confirm = function (text = 'Are you sure?') {
      vm.text = text
      vm.visible = true
      return new Promise(function (resolve, reject) {
        vm.resolve = resolve
        vm.reject = reject
      })
    }
  }
}

export default {
  components: {
    Modal
  },
  data () {
    return {
      modalOptions: {
        size: 'sm',
        closeWhenClickBack: false,
        title: 'Confirm'
      },
      visible: false,
      text: null,
      resolve: null,
      reject: null
    }
  },
  methods: {
    ok () {
      this.resolve()
      this.visible = false
    },
    close () {
      this.reject()
      this.visible = false
    }
  },
  created () {
    this.$root.constructor.use(Confirm, this)
  }
}

</script>

<style>
.conform.modal{
  padding-top: 200px;
}
</style>
