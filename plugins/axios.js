import Vue from 'vue'
import axios from 'axios'
import * as hp from 'helper-js'

export default ({store, req}) => {
  let baseURL = ''
  if (req) {
    // baseURL is needed when in nuxt middle server
    // if the server is not behind proxy or no header x-forwarded-proto, it can't get proto, may cause error
    baseURL = req.headers['x-forwarded-proto'] + '://' + req.headers.host
  }
  const axiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 20000, // 20 seconds
    withCredentials: true,
  })
  if (req) {
    // for nuxt middle server
    if (req.headers.cookie) {
      // axiosInstance.defaults.headers['Cookie'] = req.headers.cookie // only cookie
      // all
      Object.assign(axiosInstance.defaults.headers, req.headers)
    }
  }
  Vue.Axios = axios
  Vue.http = Vue.prototype.$http = axiosInstance
  function apiHttp(method, url, requestData, requestCompeleted) {
    if (url.startsWith('/')) {
      url = url.substr(1)
    }
    url = store.state.api + '/' + url
    if (requestData) {
      requestData = resolveRequestData(requestData)
    }
    return Vue.http[method](url, requestData).then((resp) => {
      requestCompeleted && requestCompeleted()
      return Promise.resolve(resp.data, resp)
    }, e => {
      requestCompeleted && requestCompeleted()
      if (process.browser) {
        Vue.alert(`Failed. ${errorRequestMessage(e)}`)
      }
      throw e
    })
  }
  Vue.apiGet = Vue.prototype.$apiGet = (url, requestCompeleted) => apiHttp('get', url, undefined, requestCompeleted)
  Vue.apiPost = Vue.prototype.$apiPost = (...args) => apiHttp('post', ...args)
}

function errorRequestMessage(error, msg) {
  const data = hp.objectGet(error, 'response.data')
  if (data) {
    if (hp.isString(data)) {
      // ignore error page html content
      if (!data.startsWith('<!DOCTYPE')) {
        return data
      }
    } else if (data.message) {
      return data.message
    }
  }
  return  error.message || msg || ''
}

function resolveRequestData(requestData) {
  return hp.mapObjectTree(requestData, (value, key, parent) => {
    if (!parent) return
    if (value instanceof Date) {
      value = parseInt(value.getTime() / 1000)
    }
    if (hp.isString(key)) {
      key = hp.snakeCase(key)
    }
    return {key, value}
  })
}
