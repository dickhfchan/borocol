import initialData from '@/initialData'
import routes from '../routes/index'

const urls = {
  clientBase: initialData.clientBase,
  serverBase: `${initialData.serverRoot}/api/v1`,
  api: `${initialData.serverRoot}/api/v1`,
}
// ''.split(',').forEach(uri => {
//   urls[uri] = `${initialData.serverRoot}/${uri}`
// });

// [].forEach(uri0 => {
//   const [uri, paramstr] = uri0.split(':')
//   const params = paramstr ? paramstr.split(',') : []
//   if (!urls[uri]) {
//     urls[uri] = {}
//   }
//   for (const t of ['find', 'select', 'store', 'update', 'destroy', 'restore', ...params]) {
//     urls[uri][t] = `${urls.serverBase}/${uri}.${t}`
//   }
// })

routes.forEach(item => {
  if (item.name && item.name.includes('.')) {
    const [l1, l2] = item.name.split('.')
    if (urls[l1]) {
      urls[l1][l2] = item.path
    }
  }
})

export default urls
