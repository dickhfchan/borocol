<template lang="pug">
VueUploadComponent.BaseUploader(
  :inputId="inputId"
  ref="upload"
  v-model="files"
  :accept="accept"
  :name="name"
  :post-action="$state.urls.serverBase + '/file'"
  :drop="true"
  @input-file="inputFile"
  @input-filter="inputFilter"
)
</template>

<script>
import VueUploadComponent from 'vue-upload-component'
import {isFalseAndDefined} from '@/utils'
import valueDetails from './valueDetails'
import {arrayLast} from 'helper-js'

export default {
  mixins: [valueDetails],
  components: {VueUploadComponent},
  props: {
    name: {default: 'file'},
    extensions: {default: is => []},
    mimes: {},
    filter: {},
  },
  data() {
    return {
      inputId: `VueUploadComponent_${this._uid}`,
      files: [],
      uploading: false,
      progress: 0,
    }
  },
  computed: {
    accept() {
      return (this.mimes || (this.extensions && this.extensions.map(v => `image/${v}`)) || []).join(',')
    },
  },
  watch: {
  },
  methods: {
    inputFile(newFile, oldFile) {
      // when add
      if (newFile && !oldFile) {
        this.$refs.upload.update(newFile.id, {
          active: true,
        })
        this.uploading = true
        this.progress = 0
      }
      // when remove, 删除时, 仅当选择新文件同时旧文件自动删除才触发此
      else if (!newFile && oldFile) {
      }
      // uploading
      else if (this.uploading) {
        if (newFile.active) {
          this.progress = Math.ceil(newFile.progress)
        } else {
          this.uploading = false
          console.log(newFile.success);
          if (newFile.success) {
            this.$notification.success(`The file was uploaded successfully`)
            this.$emit('input', newFile.response.data)
          } else {
            const message = newFile.response.data && newFile.response.data.message || newFile.response.toString() || ''
            this.$alert(`Upload Failed. ${message}`)
          }
        }
      }
    },
    inputFilter(newFile, oldFile, prevent) {
      if (newFile && !oldFile) {
        if (this.filter) {
          if (isFalseAndDefined(this.filter(newFile, oldFile))) {
            return prevent()
          }
        } else {
          const msg = `Your choice is not allowed`
          if (this.mimes) {
            if (!this.mimes.includes(newFile.type)) {
              this.$alert(msg)
              return prevent()
            }
          } else if (this.extensions && this.extensions.length > 0) {
            const ext = (arrayLast(newFile.name.split('.')) + '').toLowerCase()
            if (!this.extensions.includes(ext)) {
              this.$alert(msg)
              return prevent()
            }
          }
        }
      }
      if (newFile && (!oldFile || newFile.file !== oldFile.file)) {
        newFile.url = ''
        let URL = window.URL || window.webkitURL
        if (URL && URL.createObjectURL) {
          newFile.url = URL.createObjectURL(newFile.file)
        }
      }
    },
    getValueDetails(value) {
      this.files = !value ? [] : [{
        simulated: true, // not a fiel instance of VueUploadComponent, just a simulation
        initialUrl: value,
      }]
    },
  },
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.BaseUploader{
  @extend %mask;
  margin: 0;
}
</style>
