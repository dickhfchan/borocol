import {onDOM, offDOM, windowLoaded} from 'helper-js'
const vms = []
windowLoaded().then(() => {
  onDOM(window, 'resize', () => {
    const data = {
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      outerWidth: window.outerWidth,
      outerHeight: window.outerHeight,
    }
    vms.forEach(vm => {
      Object.assign(vm.window, data)
    })
  })
})

export default {
  data() {
    return {
      window: {
        innerWidth: window.innerWidth,
        innerHeight: window.innerHeight,
        outerWidth: window.outerWidth,
        outerHeight: window.outerHeight,
      }
    }
  },
  created() {
    vms.push(this)
  },
}
