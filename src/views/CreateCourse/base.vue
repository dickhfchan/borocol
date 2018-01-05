<script>
import Tips from './Tips.vue'
import store from '@/store'

export default {
  components: {Tips},
  beforeRouteEnter (to, from, next) {
    const state = store.state.createCourse
    if (store.state.isDevelopment && state.ignoreValidation) {
      next()
      return
    }
    const key = state.pageOrder[state.getRouteIndex(to) - 1]
    if (key) {
      state.checkIsValidTillKey(key).then(() => {
        next()
      }, e => {
        const invalidRoute = state.routes[e.index]
        next(invalidRoute)
      })
    } else {
      next()
    }
  },
  data() {
    const state = this.$state.createCourse
    const {formData} = state
    return {
      state,
      formData,
    }
  },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>
