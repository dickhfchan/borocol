import BaseUploader from './BaseUploader.js'
import * as ut from '@/plugins/utils'

export default {
  extends: BaseUploader,
  data() {
    return {
      action: this.$store.state.api + '/file/store',
    }
  },
  methods: {
    prevented() {
      this.$alert('Your choice is not allowed')
    },
    uploadFailed(newFile, oldFile) {
      const message = ut.errorRequestMessage({response: newFile.response})
      if (message) {
        this.$alert(`Upload Failed. ${message}`)
      }
      this.failed && this.failed(newFile, oldFile)
    },
    uploadSuccess(newFile, oldFile) {
      this.$notifySuccess(`The file was uploaded successfully`)
      this.success && this.success(newFile, oldFile)
    },
  },
}
