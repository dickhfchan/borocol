<script>
import vueSlider from 'vue-slider-component';
export default {
  extends: vueSlider,
  // components: {},
  // data() {
  //   return {}
  // },
  // computed: {},
  // watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
@import "~@/assets/css/global.scss";
.vue-slider-component{
  .vue-slider-tooltip{
    border-color: $bg2;
    background: $bg2;
  }
  .vue-slider-process{
    background: $bg2;
  }
}
</style>
