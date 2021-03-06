import * as hp from 'helper-js'
import Vue from 'vue'

export function cloneObjAndCamelCaseKey(obj) {
  return hp.mapObjectTree(obj, (value, key, parent) => {
    if (!parent) return
    if (hp.isString(key)) {
      return {key: hp.camelCase(key), value}
    }
  })
}

export function setDataToFields(data, fields) {
  for (const key in fields) {
    const fld = fields[key]
    if (data[key] != null) {
      Vue.set(fld, 'value', data[key])
    }
  }
}

// source: https://gist.github.com/maxwihlborg/1911a28f988444db3ddc
export function debounce(fn, wait = 100) {
	let timeout;
	return function() {
		const ctx = this, args = arguments;
		clearTimeout(timeout);
		timeout = setTimeout(function() {
		    fn.apply(ctx, args);
		}, wait);
	};
}

export function errorRequestMessage(error, msg) {
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
  return  error.response && error.response.message || error.message || msg || ''
}

// 9-digit to 10-digit, Sat Mar 03 1973 17:46:40 GMT+0800 (CST) to Sun Nov 21 2286 01:46:39 GMT+0800 (CST)
export function isSecond(n) {
  if (Number.isInteger(n)) {
    const len = n.toString().length
    if (len === 9 || len === 10) {
      return true
    }
  }
  return false
}
// 12-digit to 13-digit
export function isMillisecond(n) {
  if (Number.isInteger(n)) {
    const len = n.toString().length
    if (len === 12 || len === 13) {
      return true
    }
  }
  return false
}
