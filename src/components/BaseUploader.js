/*
example
VueUploadComponent.VueUploadComponent(
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
*/

import VueUploadComponent from 'vue-upload-component'
import {isFalseAndDefined} from '@/utils'
import valueDetails from './valueDetails'
import {arrayLast} from 'helper-js'

export default {
  components: {VueUploadComponent},
  props: {
    name: {default: 'file'},
    extensions: {default: is => []}, // only for image
    mimes: {},
    filter: {},
    debug: {default: true},
  },
  data() {
    return {
      inputId: `VueUploadComponent_${this._uid}`,
      files: [],
      upload: null,
      uploadingIds: {},
    }
  },
  computed: {
    accept() {
      return (this.mimes || (this.extensions && this.extensions.map(v => `image/${v}`)) || []).join(',')
    },
    uploading() {
      return this.upload && this.upload.uploading
    },
  },
  // watch: {},
  methods: {
    log(...args) {
      if (this.debug && window.uploadDebug !== false) {
        console.log(...args);
      }
    },
    inputFile(newFile, oldFile) {
      const {log, uploadingIds} = this
      if (newFile && !oldFile) {
        // Add file
        this.added && this.added(newFile)
      }
      else if (newFile && oldFile) {
        // Update file
        // Start upload
        if (newFile.active) {
          if (!uploadingIds[newFile.id]) {
            uploadingIds[newFile.id] = true
            log('Start upload', newFile.active, newFile)
            this.uploadStarted && this.uploadStarted(newFile, oldFile)
          }
          // Upload progress
          else if (newFile.progress !== oldFile.progress) {
            log('progress', newFile.progress, newFile)
            this.uploadProcessing && this.uploadProcessing(newFile, oldFile)
          }
        } else {
          // Upload error
          if (newFile.error) {
            log('error', newFile.error, newFile)
            this.uploadFailed && this.uploadFailed(newFile, oldFile)
            delete uploadingIds[newFile.id]
          }
          // Uploaded successfully
          else if (newFile.success && newFile.success !== oldFile.success) {
            log('success', newFile.success, newFile)
            this.uploadSucceeded && this.uploadSucceeded(newFile, oldFile)
            delete uploadingIds[newFile.id]
          }
        }
        this.updated && this.updated(newFile, oldFile)
      }
      else if (!newFile && oldFile) {
        // Remove file
        this.removed && this.removed(oldFile)
      }
    },
    inputFilter(newFile, oldFile, prevent) {
      // add
      if (newFile && !oldFile) {
        if (this.filter) {
          if (isFalseAndDefined(this.filter(newFile, oldFile))) {
            return prevent()
          }
        } else {
          if (this.mimes) {
            if (!this.mimes.includes(newFile.type)) {
              this.prevented && this.prevented()
              return prevent()
            }
          } else if (this.extensions && this.extensions.length > 0) {
            const ext = (arrayLast(newFile.name.split('.')) + '').toLowerCase()
            if (!this.extensions.includes(ext)) {
              this.prevented && this.prevented()
              return prevent()
            }
          }
        }
        if (this.beforeAdd && isFalseAndDefined(this.beforeAdd(newFile))) {
          return prevent()
        }
      }
      else if (!newFile && oldFile) {
        // remove
        if (this.beforeRemove && isFalseAndDefined(this.beforeRemove(oldFile))) {
          return prevent()
        }
      }
      else if (newFile && oldFile) {
        // Update file
        if (this.beforeUpdate && isFalseAndDefined(this.beforeUpdate(newFile, oldFile))) {
          return prevent()
        }
      }
    },
    startUploadFile(file) {
      file.active = true
    },
  },
  // created() {},
  mounted() {
    this.log(`assign window.uploadDebug with false can stop debug`);
    this.upload = this.$refs.upload
  },
}
