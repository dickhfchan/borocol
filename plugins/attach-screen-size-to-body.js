import * as hp from 'helper-js'

export default () => {
  const sizes = [
    ['xs', 768],
    ['sm', 992],
    ['md', 1200],
    ['lg', 1920],
    ['xl', window.Infinity || 9999999999],
  ]
  let oldClass
  const fun = () => {
    const w = window.innerWidth
    let cur;
    for (const t of sizes) {
      const [name, width] = t
      if (w < width) {
        cur = name
        break
      }
    }
    if (oldClass) {
      hp.removeClass(document.body, oldClass)
    }
    hp.addClass(document.body, cur)
    oldClass = cur
  }
  hp.windowLoaded().then(() => {
    fun()
    hp.onDOM(window, 'resize', fun)
  })
}
