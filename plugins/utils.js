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
    if (data.hasOwnProperty(key)) {
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
