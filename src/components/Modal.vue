<template lang="pug">
.Modal.modal.modal-layer(style="display:block;")
  .modal-backdrop.in(@click="backDropClick")
  .modal-dialog(:class="['modal-' + size]", :style="dialogStyle")
    .modal-content
      slot(name="content")
        .modal-header(v-if="headerVisible")
          slot(name="header")
            button.close(type='button', @click="$emit('close')")
              span(aria-hidden='true') &times;
              span.sr-only Close
            slot(name="title")
              h4.modal-title {{title}}
        .modal-body(v-if="bodyVisible")
          slot
            slot(name="body")
              p One fine body&mldr;
        .modal-footer(v-if="footerVisible")
          slot(name="footer")
            button.btn.btn-default(type='button', @click="$emit('close')") {{closeText}}
            button.btn.btn-primary(type='button', @click="$emit('ok')") {{okText}}
</template>
<script>
export default {
  props: {
    // options will assign to this once it changed. please check watch => options
    options: { default: is => Object() }
  },
  data() {
    return {
      closeWhenClickBack: true,
      // style
      size: 'md',
      width: null,
      marginTop: null,
      headerVisible: true,
      bodyVisible: true,
      footerVisible: true,
      // content
      title: null,
      closeText: 'Close',
      okText: 'OK'
    }
  },
  computed: {
    dialogStyle: function() {
      const r = {}
      if (this.width) r.width = this.width
      if (this.marginTop) r.marginTop = this.marginTop
      return r
    }
  },
  watch: {
    options: {
      immediate: true,
      handler(value) {
        Object.assign(this, value)
      }
    }
  },
  methods: {
    backDropClick: function() {
      if (this.closeWhenClickBack) {
        this.$emit('close')
      }
    }
  }
}

</script>
<style lang="scss">
.Modal{
  &.modal{
    position: fixed;
  }
  .modal-backdrop{
    z-index: 1000;
  }
  .modal-dialog{
    z-index: 1001;
  }
}
</style>
