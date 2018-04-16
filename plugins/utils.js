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
  data = cloneObjAndCamelCaseKey(data)
  for (const key in fields) {
    const fld = fields[key]
    if (data[key] != null && !fld.hasOwnProperty('value')) {
      let val = data[key]
      if (hp.isNumber(data[key]) && data[key].toString().length === 10) {
        // timestamp
        // to millisecond
        val = val * 1000
      }
      Vue.set(fld, 'value', val)
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
};
