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
    state.checkIsValidTillIndex(state.getRouteIndex(to)).then(() => {
      next()
    }, e => {
      const invalidRoute = state.routes[e.index]
      if (invalidRoute.name === to.name) {
        next()
      } else {
        next(invalidRoute)
        const vm = store.state.appVm
        if (vm) {
          vm.$alert(state.validations[e.index].getFirstError().message)
        }
      }
    })
  },
  data() {
    const state = this.$state.createCourse
    const {formData} = state
    const {fields, validations} = state
    const index = state.getRouteIndex()
    return {
      state,
      formData,
      index,
      fields: fields[index],
      validation: validations[index],
    }
  },
  computed: {
    stepMeta() {
      const {index} = this
      return this.state.steps.find(v => v.pageRange[0] <= index && index <= v.pageRange[1])
    },
    step() {
      return this.stepMeta.index
    },
    progress() {
      const {step} = this
      const total = this.state.steps.length
      return step / total
    },
    progressStr() {
      const {progress} = this
      return Math.floor(progress * 100) + '%'
    },
    title() {
      return this.stepMeta.title
    },
  },
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>
