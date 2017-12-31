<script>
import Tips from './Tips.vue'
export default {
  components: {Tips},
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
