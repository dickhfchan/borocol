<template lang="pug">
Modal.AlertMessagebox(
  v-if="visible",
  :options="modalOptions",
  @close="close", @ok="ok"
)
  div(slot="body")
    button.close(@click="close") &times;
    .text {{text}}
    .btns
      button.btn.btn-primary.ok-btn(type="button" @click="ok"): b OKAY
</template>

<script >
import Modal from './Modal.vue'
const AlertMessagebox = {
  install (Vue, vm) {
    Vue.alert = Vue.prototype.$alert = function (text) {
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
        size: 'md',
        closeWhenClickBack: false,
        headerVisible: false,
        footerVisible: false,
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
    this.$root.constructor.use(AlertMessagebox, this)
  }
}

</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.AlertMessagebox.modal{
  padding-top: 300px;
  .modal-content {
    border-radius: $bdr;
  }
  .text{
    font-size: $fs-md;
    padding: 1em;
  }
  .btns{
    margin-top: 1em;
    text-align: center;
  }
  .ok-btn{
    padding-left: 2em;
    padding-right: 2em;
  }
}
</style>
