import BaseUploader from './BaseUploader.js'

export default {
  extends: BaseUploader,
  methods: {
    prevented() {
      this.$alert('Your choice is not allowed')
    },
    uploadFailed(newFile, oldFile) {
      const message = newFile.response.data && newFile.response.data.message || newFile.response.toString() || ''
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
