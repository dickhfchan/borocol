export default {
  data: function() {
    return {
      mounted: new Promise((resolve, reject) => {
        this.mountedResolve = resolve
      }),
    }
  },
  mounted() {
    this.mountedResolve()
  },
}
