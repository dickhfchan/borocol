import Vue from 'vue'
import axios from 'axios'
import * as hp from 'helper-js'
import * as ut from '@/plugins/utils'

export default ({store, req, env}) => {
  let baseURL = ''
  if (req) {
    // x-base-url is set in nginx config, pls check nginx-config-example.conf
    baseURL = req.headers['x-base-url']
    if (!baseURL) {
      throw new Error('header x-base-url is required')
    }
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
    const opt = {url, method, headers: {}}
    if (requestData) {
      requestData = resolveRequestData(requestData)
      if ('get,delete'.includes(method)) {
        opt.params = requestData
      } else {
        opt.data = requestData
      }
    }
    return Vue.http.request(opt).then((resp) => {
      requestCompeleted && requestCompeleted()
      return Promise.resolve(resolveResponseData(resp.data), resp)
    }, e => {
      if (env.devStatic) {
        return
      }
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
    } else if (Number.isInteger(value) && value.toString().length === 13) {
      value = value / 1000
    }
    if (hp.isString(key)) {
      key = hp.snakeCase(key)
    }
    return {key, value}
  })
}

function resolveResponseData(respData) {
  return hp.mapObjectTree(respData, (value, key, parent) => {
    if (!parent) return
    if (hp.isNumber(value) && value.toString().length === 10) {
      // timestamp
      // to millisecond
      value = value * 1000
    }
    if (hp.isString(key)) {
      key = hp.camelCase(key)
    }
    return {key, value}
  })
}
