import { titleCase, snakeCase, windowLoaded, unset, isArray, isObject, isString } from 'helper-js'
import Vue from 'vue'

export const loaded = windowLoaded()
export const dateTimeFields = ['start_time', 'end_time', 'time', 'start_date', 'end_date', 'date',
  'create_ts', 'update_ts', 'last_loc_update_ts', 'apps_ts', 'last_access_ts',
  'active_end_date', 'active_start_date', 'last_access_ts', 'last_loc_update_ts', 'last_login_ts']

export function initAxios(axios, store, Vue) {
  const axiosInstance = axios.create({
    // baseURL: store.state.urls.serverBase,
    timeout: 20000, // 20 seconds
    withCredentials: store.state.isCROS
  })
  Vue.Axios = axios
  Vue.http = Vue.prototype.$http = axiosInstance
}

export function initVDV(VueDataValidator, store, Vue) {
  Vue.use(VueDataValidator.validator)
  Object.assign(Vue.validator.rules, VueDataValidator.rules)
  Object.assign(Vue.validator.messages, store.state.lang === 'en' ? VueDataValidator.enMessages : VueDataValidator.zhCNMessages)
  // Vue.validator.validClass = 'has-success'
  // Vue.validator.invalidClass = 'has-error'
}

export function initRouter(Router, Vue, store, routes, authFailed) {
  Vue.use(Router)
  const router = new Router({
    mode: 'history',
    base: store.state.urls.clientBase,
    routes
  })
  router.beforeEach((to, from, next) => {
    const {auth, title} = to.meta
    if (auth && !store.state.authenticated) {
      authFailed && authFailed(to, from, next)
      store.state.intended = Object.assign({}, to)
      next({name: 'login'})
      return
    }
    if (title) {
      loaded.then(() => {
        document.title = title
      })
    }
    next()
  })
  return router
}

export function initBootstrapNotify(Vue) {
  Vue.notify = Vue.prototype.$notify = (msg, type = 'info', opt = {}) => {
    $.notify({
    	// title: '',
    	message: msg,
    },{
    	type: type,
      allow_dismiss: true,
      mouse_over: 'pause',
      offset: {
        x: 20,
        y: 60,
      },
    })
  }
}

export function registerPreventURLChange(Vue, router) {
  // only when leave
  if (!router) {
    let preventRouter = false
    const msg0 = '修改尚未保存，确认离开吗？'
    let msg
    const beforeunload = (e) => {
      var confirmationMessage = msg || msg0
      e.returnValue = confirmationMessage;     // Gecko, Trident, Chrome 34+
      return confirmationMessage;              // Gecko, WebKit, Chrome <34
    }
    Vue.preventURLChange = Vue.prototype.$preventURLChange = (msg2) => {
      if (msg2 != null) {
        msg = msg2
      }
      if (!preventRouter) {
        preventRouter = true
        window.addEventListener("beforeunload", beforeunload)
      }
    }
    Vue.allowURLChange = Vue.prototype.$allowURLChange = () => {
      preventRouter = false
      window.removeEventListener("beforeunload", beforeunload)
    }
    return
  }
  let preventRouter = false
  const msg0 = '修改尚未保存，确认离开吗？'
  let msg
  router.beforeEach((to, from, next) => {
    if (preventRouter) {
      if (window.confirm(msg || msg0)) {
        Vue.allowURLChange()
        next()
      } else {
        next(false)
      }
    } else {
      next()
    }
  })
  const beforeunload = (e) => {
    var confirmationMessage = msg || msg0
    e.returnValue = confirmationMessage;     // Gecko, Trident, Chrome 34+
    return confirmationMessage;              // Gecko, WebKit, Chrome <34
  }
  Vue.preventURLChange = Vue.prototype.$preventURLChange = (msg2) => {
    if (msg2 != null) {
      msg = msg2
    }
    if (!preventRouter) {
      preventRouter = true
      window.addEventListener("beforeunload", beforeunload)
    }
  }
  Vue.allowURLChange = Vue.prototype.$allowURLChange = () => {
    preventRouter = false
    window.removeEventListener("beforeunload", beforeunload)
  }
}

export function registerAssign(Vue) {
  Vue.assign = Vue.prototype.$assign = (obj, obj2, ignoreExisted) => {
    const set = this && this.$set || Vue.set
    for (const key of Object.keys(obj2)) {
      if (!ignoreExisted || obj[key] === undefined) {
        set(obj, key, obj2[key])
      }
    }
  }
}

export function initVueMaterial(VueMaterial, Vue) {
  Vue.use(VueMaterial)
  Vue.material.registerTheme({
    default: {
      primary: {
        color: 'light-green',
        hue: 700
      },
      accent: 'red'
    },
    blue: {
      primary: 'blue',
      accent: 'pink'
    },
    orange: {
      primary: 'orange',
      accent: 'purple'
    },
    green: {
      primary: 'green',
      accent: 'white'
    }
  })
}

export function initI18n(VueI18n, messages, store, Vue) {
  // this is disabled, because it has bug in ie 11
  // reload when other page change lang
  // window.addEventListener('storage', (e) => {
  //   if (e.key === 'lang') {
  //     window.location.reload()
  //   }
  // })
  Vue.use(VueI18n)
  return new VueI18n({
    locale: store.state.lang, // set locale
    messages, // set locale messages
  })
}

export function axiosNamedPost(name, url, query) {
  if (!this._axiosNamedPostStore) {
    this._axiosNamedPostStore = {}
  }
  // cancel prev request
  if (this._axiosNamedPostStore[name]) {
    this._axiosNamedPostStore[name]()
    delete this._axiosNamedPostStore[name]
  }
  // CancelToken
  const Axios = this.$root.constructor.Axios
  const CancelToken = Axios.CancelToken
  return this.$http.post(url, query, {
    cancelToken: new CancelToken((c) => {
      this._axiosNamedPostStore[name] = c
    })
  })
}

// use proxy in developing
export function axiosAutoProxy(http, url, method, data) {
  if (method === 'delete') {
    data = { data: data }
  }
  return http[method](url, data)
  // if (store.state.isDevelopment) {
  //   return http.post('http://' + window.location.host + '/proxy', {
  //     url,
  //     method,
  //     data
  //   })
  // } else {
  //   return http[method](url, data)
  // }
}
export function initColumns(vm, columns) {
  // auto generate column display name
  for (const col of columns) {
    if (!col.text) {
      vm.$set(col, 'text', titleCase(col.name))
    }
    if (col.visible == null) {
      vm.$set(col, 'visible', true)
    }
    if (col.sortAble == null) {
      vm.$set(col, 'sortAble', true)
    }
    if (col.type == null) {
      vm.$set(col, 'type', 'default')
    }
    // if (!col.width) {
    //   const len = col.text.length
    //   vm.$set(col, 'width', `${len > 3 ? (100 + (len - 6) * 5) : '60'}px`)
    // }
  }
}

export function initRows(vm, rows, columns, table) {
  if (table) {
    if (table.sortBy) {
      sortRows({name: table.sortBy, type: table.sortType}, rows, columns)
    }
  }
  for (const row of rows) {
    if (row.visible == null) {
      vm.$set(row, 'visible', true)
    }
    if (row.checked == null) {
      vm.$set(row, 'checked', false)
    }
    for (const col of columns) {
      if (col.valueProcessor) {
        row[col.name] = col.valueProcessor({value: row[col.name], column: col, row, rows})
      }
    }
  }
}

export function getRowData(row, cols) {
  const item = {}
  cols.forEach(col => {
    item[col.name] = row[col.name]
  })
  return item
}
export function beforeSave(row, cols) {
  dateTimeFields.forEach(fld => {
    if (row.hasOwnProperty(fld)) {
      try {
        row[fld] = Math.round(newDate(row[fld]).getTime() / 1000)
      } catch (e) {
        if (e.message === 'unexpected param format') {
          const col = cols.find(col => col.name === fld)
          throw Error(`Unexpected format of ${col.text}. The format should be yyyy-MM-dd HH:mm:ss`)
        }
      }
    }
  })
  cols.forEach(col => {
    if (col.notInDatabase) {
      delete row[col.name]
    } else if (row.hasOwnProperty(col.name) && !col.primaryKey && row[col.name] == null) {
      row[col.name] = ''
    }
  })
  return row
}

export function sortRows(event, rows, columns) {
  const col = columns.find(col => col.name === event.name)
  const sortBy = col.sortBy || event.name
  if (col.locale) {
    rows.sort((a, b) => (a[sortBy] || '').substr(1).localeCompare((b[sortBy] || '').substr(1)))
  } else {
    rows.sort((a, b) => {
      const aa = a[sortBy]
      const bb = b[sortBy]
      if (aa < bb) {
        return -1
      } else if (aa === bb) {
        return 0
      } else {
        return 1
      }
    })
  }
  if (event.type === 'desc') {
    rows.reverse()
  }
}

export function generateExcel(JSONData, FileName, ShowLabel) {
    // 先转化json
  var arrData = typeof JSONData !== 'object' ? JSON.parse(JSONData) : JSONData
  var excel = '<table>'
    // 生成表头
  var row = '<tr>'
  for (let i = 0; i < ShowLabel.length; i++) {
    row += '<td>' + ShowLabel[i] + '</td>'
  }
  excel += row + '</tr>'
    // 循环生成表身
  for (let i = 0; i < arrData.length; i++) {
    row = '<tr>'
    for (var j in arrData[i]) {
//                    var name = arrData[i][index].name === "." ? "" : arrData[i][index].name;
      var td = arrData[i][j]
      row += '<td>' + td + '</td>'
    }
    excel += row + '</tr>'
  }
  excel += '</table>'
  var excelFile = "<html xmlns:o='urn:schemas-microsoft-com:office:office' " +
        "xmlns:x='urn:schemas-microsoft-com:office:excel' xmlns='http://www.w3.org/TR/REC-html40'>"
  excelFile += '<meta http-equiv="content-type" content="application/vnd.ms-excel; charset=UTF-8">'
  excelFile += '<meta http-equiv="content-type" content="application/vnd.ms-excel'
  excelFile += '; charset=UTF-8">'
  excelFile += '<head>'
  excelFile += '<!--[if gte mso 9]>'
  excelFile += '<xml>'
  excelFile += '<x:ExcelWorkbook>'
  excelFile += '<x:ExcelWorksheets>'
  excelFile += '<x:ExcelWorksheet>'
  excelFile += '<x:Name>'
  excelFile += 'sheet'
  excelFile += '</x:Name>'
  excelFile += '<x:WorksheetOptions>'
  excelFile += '<x:DisplayGridlines/>'
  excelFile += '</x:WorksheetOptions>'
  excelFile += '</x:ExcelWorksheet>'
  excelFile += '</x:ExcelWorksheets>'
  excelFile += '</x:ExcelWorkbook>'
  excelFile += '</xml>'
  excelFile += '<![endif]-->'
  excelFile += '</head>'
  excelFile += '<body>'
  excelFile += excel
  excelFile += '</body>'
  excelFile += '</html>'
  var uri = 'data:application/vnd.ms-excel;charset=utf-8,' + encodeURIComponent(excelFile)
  var link = document.createElement('a')
  link.href = uri
  link.style = 'visibility:hidden'
  link.download = FileName + '.xls'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

// about map

export function loadGoogleMap(ak) {
  if (window.google && window.google.maps) {
    return Promise.resolve(window.google)
  }
  const fun = loadGoogleMap
  return windowLoaded().then(() => {
    if (fun.loaded) {
      return window.google
    } else {
      if (!fun.requested) {
        fun.requested = true
        window._GoogleMapLoadedCallback = () => { fun.loaded = true; unset(window, '_GoogleMapLoadedCallback') }
        const script = document.createElement('script')
        script.src = `https://maps.googleapis.com/maps/api/js?key=${ak}&callback=_GoogleMapLoadedCallback`
        document.body.appendChild(script)
      }
      return new Promise(function(resolve, reject) {
        const requestInterval = window.setInterval(function () {
          if (fun.loaded) {
            window.clearInterval(requestInterval)
            resolve(window.google)
          }
        }, 10)
      })
    }
  })
}
/**
 * [newDate description]
 * @param  {[type]} str [format: yyyy-MM-dd HH:mm:ss]
 * @return [type]       [description]
 */
export function newDate(str) {
  if (!str) {
    return new Date()
  }
  const m = (str || '').match(/^(\d{4}-\d{1,2}-\d{1,2})( \d{1,2}:\d{1,2}:\d{1,2})?$/)
  if (!m) {
    throw Error('unexpected param format')
  }
  const args = m[1].split('-').map(v => parseInt(v))
  args[1]-- // convert month to 0 -11
  // HH:mm:ss
  if (m[2]) {
    m[2].substr(1).split(':').forEach(v => { args.push(parseInt(v)) })
  } else {
    args.push(0)
    args.push(0)
    args.push(0)
  }
  return new Date(...args)
}

export function getRankColor(rank, max, order = 'asc') {
  const blue = 30
  const min = 1
  if (max === min) {
    return order === 'asc' ? `rgb(0, 255, ${blue})` : `rgb(255, 0, ${blue})`
  }
  const halfL = Math.floor((max - min + 1) / 2)
  const halfR = max - min + 1 - halfL
  const unitL = 255 / halfL
  const unitR = 255 / halfR
  const center = halfL + min - 1
  let red, green
  if (rank <= center) {
    red = Math.round((rank - min) * unitL)
    green = 255
  } else {
    red = 255
    green = Math.round(255 - (rank - center) * unitR)
  }
  if (order === 'desc') {
    const t = red
    red = green
    green = t
  }
  return `rgb(${red}, ${green}, 30)`
}

export function getRanks(arr0, order = 'asc') {
  const arr = arr0.slice(0)
  arr.sort((a, b) => a - b)
  if (order === 'desc') {
    arr.reverse()
  }
  return arr0.map(item => arr.indexOf(item) + 1)
}

export function sortRowsByProp(rows, prop) {
  rows.sort((a, b) => {
    const aProp = a[prop]
    const bProp = b[prop]
    if (aProp < bProp) {
      return -1
    }
    if (aProp > bProp) {
      return 1
    }
    // equal
    return 0
  })
}

export function exportExcel(rows, columns, title) {
  const cols = columns.filter(col => col.exportAble !== false && col.visible !== false)
  const data = rows.map(row => {
    const r = []
    cols.forEach(col => {
      const val = row[col.name]
      r.push(col.formatter ? col.formatter(val) : val)
    })
    return r
  })
  const titleLabels = cols.map(col => col.text)
  generateExcel(data, title, titleLabels)
}

export function loadBaiduMap(ak) {
  if (window.BMap) {
    return Promise.resolve(window.BMap)
  }
  const fun = loadBaiduMap
  return windowLoaded().then(() => {
    if (fun.loaded) {
      return Promise.resolve(window.BMap)
    } else {
      if (!fun.requested) {
        fun.requested = true
        window._BaiduMapLoadedCallback = () => { fun.loaded = true; unset(window, '_BaiduMapLoadedCallback') }
        const script = document.createElement('script')
        script.src = `http://api.map.baidu.com/api?v=2.0&ak=${ak}&callback=_BaiduMapLoadedCallback`
        document.body.appendChild(script)
      }
      return new Promise(function(resolve, reject) {
        const requestInterval = window.setInterval(function () {
          if (fun.loaded) {
            window.clearInterval(requestInterval)
            resolve(window.BMap)
          }
        }, 10)
      })
    }
  })
}

/**
 * [baiduMapReady must be under vm]
 * @return [type] [description]
 */
export function baiduMapReady() {
  return loadBaiduMap(this.ak).then(BMap => {
    this.BMap = BMap
    if (!this.map) {
      this.map = new BMap.Map(this.id)
      this.map.enableScrollWheelZoom()
    }
    this.map.addControl(new BMap.NavigationControl({anchor: window.BMAP_ANCHOR_BOTTOM_RIGHT, type: window.BMAP_NAVIGATION_CONTROL_ZOOM}))
    return Promise.resolve({BMap, map: this.map})
  })
}

/**
 * [googleMapReady must be under vm]
 * @return [type] [description]
 */
export function googleMapReady() {
  return loadGoogleMap(this.ak).then(google => {
    if (!this.map) {
      this.map = new google.maps.Map(document.getElementById(this.id), {
        zoom: 15,
        mapTypeId: 'roadmap',
        mapTypeControl: true,
        mapTypeControlOptions: {
          mapTypeIds: [
            google.maps.MapTypeId.ROADMAP,
            google.maps.MapTypeId.SATELLITE
          ]
        }
      })
    }
    return Promise.resolve({google, map: this.map})
  })
}

// http
const storeOfCancelOldRequest = {}
export function cancelOldRequest(name) {
  const cancel = storeOfCancelOldRequest[name]
  if (cancel) {
    cancel()
    delete storeOfCancelOldRequest[name]
  }
}
export function namedHttpGet(name, url, options0) {
  cancelOldRequest(name)
  const CancelToken = Vue.Axios.CancelToken
  const http = Vue.http
  const options = Object.assign({}, options0 || {})
  options.cancelToken = new CancelToken((c) => { storeOfCancelOldRequest[name] = c })
  return http.get(url, options)
}

export function getCSRFToken(store, Vue) {
  const {http} = Vue
  const {urls} = store.state
  // get CSRFToken if necessary
  if (store.state.isCROS && store.state.CROS.CSRFTokenRequired) {
    const updateCSRFToken = () => {
      return new Promise(function(resolve, reject) {
        http.get(urls.CSRFToken).then(({data}) => {
          http.defaults.headers.common['X-CSRF-TOKEN'] = data
          resolve(data)
        })
        .catch((error) => { throw error })
      })
    }
    window.setInterval(updateCSRFToken, store.state.CROS.updateCSRFTokenIn)
    return updateCSRFToken()
  } else {
    return Promise.resolve()
  }
}

export function getRoutes() {
  const store = this.$store
  const http = this.$http
  const {urls} = store.state
  return http.get(urls.routes).then(({data}) => {
    for (const key of Object.keys(data)) {
      if (urls[key] && isObject(urls[key])) {
        Object.assign(urls[key], data[key])
      } else {
        urls[key] = data[key]
      }
    }
  })
}

export function getCurrentUser(store, Vue) {
  const {http} = Vue
  const {urls} = store.state
  return Vue.http.get(urls.currentUser).then(({data}) => {
    if (data) {
      store.state.user = data
      store.state.authenticated = true
    }
  })
}

export function selectAll(vm, name) {
  return vm.$http.post(vm.$store.state.urls[name].select, {perPage: 'all'})
}

export function cloneObj(obj, exclude) {
  const type = typeof(obj)
  switch (type) {
    case 'undefined':
    case 'boolean':
    case 'nuber':
    case 'string':
    case 'function':
        return obj
      break;
    case 'object':
        if (obj === null) {
          // null is object
          return obj
        }
        let r
        if (isArray(obj)) {
          r = []
          for (const item of obj) {
            r.push(cloneObj(item, exclude))
          }
        } else {
          r = {}
          for (const key of Object.keys(obj)) {
            if (!exclude || !exclude.includes(key)) {
              r[key] = cloneObj(obj[key], exclude)
            }
          }
        }
        return r
      break;
    default:
        return obj
      break;
  }
}

export function setTimeoutInterval(timeout, interval, func, immediate = true) {
  if (immediate) {
    func()
  }
  const i = setInterval(func, interval);
  const t = setTimeout(() => {
    clearInterval(i)
  }, timeout)
  // cancel
  return () => {
    clearInterval(i)
    clearTimeout(t)
  }
}

export function doOnce(fun) {
  fun()
  return fun
}

export function timeoutPromise(ms) {
  return new Promise(function(resolve, reject) {
    setTimeout(function () {
      resolve()
    }, ms);
  });
}

export function isFalseAndDefined(v) {
  return v !== undefined && !v
}

export function ajaxDataFilter(obj) {
  const obj2 = {}
  Object.keys(obj).forEach(key => {
    const v = obj[key]
    obj2[snakeCase(key)] = isString(v) ? v.trim() : v
  })
  return obj2
}
