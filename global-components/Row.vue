<template lang="pug">
.layout-row
  .layout-row-inner(ref="inner")
    slot
    .clearfix
</template>

<script>
import * as hp from 'helper-js'
import * as ut from '@/plugins/utils'

export default {
  props: {
    gutter: {default: 16, type: [Number, Array]},
  },
  // components: {},
  data() {
    return {
      width: null,
      gutterX: null,
      gutterY: null,
      colsMapping: {},
    }
  },
  computed: {
    colStyle() {
      return {
        marginRight: this.gutterX + 'px',
        marginBottom: this.gutterY + 'px',
      }
    },
  },
  // watch: {},
  methods: {
    updateWidth() {
      this.width = this.$el.offsetWidth
    },
    updateGutter() {
      const {gutter} = this
      let t = hp.isArray(gutter) ? gutter : [gutter, gutter]
      this.gutterX = t[0]
      this.gutterY = t[1]
    },
    // get responsive width
    getColWidth(col) {
      const w = window.innerWidth
      const prioritized = (...arr) => {
        for (const item of arr) {
          if (item != null) {
            return item
          }
        }
        return hp.arrayLast(arr)
      }
      if (w < 768) {
        return prioritized(col.xs, col.width)
      } else if (w < 992) {
        return prioritized(col.sm, col.width)
      } else if (w < 1200) {
        return prioritized(col.md, col.sm, col.width)
      } else {
        return prioritized(col.lg, col.md, col.sm, col.width)
      }
    },
    // find last col, row
    // ut.debounce
    update: ut.debounce(function () {
      const rowWidth = this.width + this.gutterX
      if (!this.$refs.inner) {
        return
      }
      const els = this.$refs.inner.children
      const len = els.length
      const rows = []
      let row
      let raw // row accumulate width; row累加宽度
      const newRow = () => {
        row = []
        rows.push(row)
        raw = 0
      }
      // split to rows
      newRow()
      for (let i = 0; i < len; i++) {
        const el = els[i]
        if (hp.hasClass(el, 'row-break')) {
          newRow()
          continue
        }
        const id = el.getAttribute('data-vm-id')
        if (id == null) {
          continue
        }
        const col = this.colsMapping[id]
        col.isLastCol = false
        col.isLastRow = false
        let cw
        // _realWidth contains margin
        const cpw = this.getColWidth(col) // col prop width
        if (cpw < 1) {
          // proportion; 比例
          cw = rowWidth * cpw
          col.cssWidth = cw - this.gutterX
        } else {
          // px; 指定像素
          cw = cpw + this.gutterX
          col.cssWidth = cpw
        }
        col._realWidth = cw
        raw += cw
        if (raw > rowWidth) {
          newRow()
          raw = cw
        }
        row.push(col)
        col.isFirstCol = row.length === 1
      }
      // when screen narrower than first col, first row is empty
      if (rows[0].length === 0) {
        rows.shift()
      }
      // grow col
      const sameWidthStore = {}
      for (let i = 0; i < rows.length; i++) {
        const row = rows[i]
        hp.arrayLast(row).isLastCol = true
        // sort
        let restW = rowWidth // rest width; 递减后剩余宽度
        const sorted = []
        row.forEach((col, i) => {
          if (col.fixed) {
            //
          } else if (hasSameWidth(col) && sameWidthStore[col.sameWidth]) {
            const rspsCol = sameWidthStore[col.sameWidth] // representative col
            col.cssWidth = rspsCol.cssWidth
            col._realWidth = rspsCol._realWidth
          } else {
            sorted.push(col)
            col._colIndex = i
          }
          restW -= col._realWidth
        })
        if (restW <= 0) {
          continue
        }
        sorted.sort((a,b) => {
          if (a.grow != null && b.grow != null) {
            return a.grow - b.grow
          } else if (a.grow != null) {
            return 1
          } else if (b.grow != null) {
            return -1
          } else {
            return -a._colIndex - (-b._colIndex)
          }
        })
        sorted.reverse()
        const sortedLen = sorted.length
        for (let j = 0; j < sortedLen; j++) {
          const col = sorted[j]
          const swn = col.sameWidth // 'same width' name
          if (hasSameWidth(col)) {
            const sameCols = [col]
            for (let k = j+1; k < sortedLen; k++) {
              if (sorted[k].sameWidth === swn) {
                sameCols.push(sorted[k])
              }
            }
            const t = restW / sameCols.length
            for (const col2 of sameCols) {
              col2.cssWidth += t
              col2._realWidth += t
            }
            sameWidthStore[swn] = col
            break
          } else {
            col.cssWidth += restW
            col._realWidth += restW
            break
          }
        }
      }
      hp.arrayLast(rows).forEach(col => {
        col.isLastRow = true
      })
      function hasSameWidth(col) {
        return col.sameWidth || col.sameWidth === ''
      }
      function checkColWithSameWidth(col) {
        if (hasSameWidth(col)) {
          if (!sameWidthStore.hasOwnProperty(col.sameWidth)) {
            sameWidthStore[col.sameWidth] = col.cssWidth
          }
        }
      }
    }, 10),
    registerCol(colVm) {
      this.colsMapping[colVm._uid] = colVm
      this.update()
    },
    unregisterCol(colVm) {
      delete this.colsMapping[colVm._uid]
      this.update()
    },
  },
  // created() {},
  mounted() {
    this.updateWidth()
    hp.onDOM(window, 'resize', this.updateWidth)
    this.$watch('gutter', this.updateGutter, {deep: true, immediate: true})
    this.$watch('gutterX', this.update)
    this.$watch('gutterY', this.update)
    this.$watch('width', this.update)
  },
  beforeDestroy() {
    hp.offDOM(window, 'resize', this.updateWidth)
  },
}
</script>

<style lang="scss">
.layout-row{
}
</style>
