import initialData from '@/initialData'
import routes from '../routes/index'

const urls = {
  clientBase: initialData.clientBase,
  serverBase: `${initialData.serverRoot}/admin-api`,
  ueditor: {
    dir: `${initialData.serverRoot}/vendor/ueditor`,
    api: `${initialData.serverRoot}/ueditor/server`,
  },
}
'CSRFToken,currentUser,captcha,login,register,logout,changeEmail,sendConfirmationEmail'.split(',').forEach(uri => {
  urls[uri] = `${initialData.serverRoot}/${uri}`
});

[
  'file:upload',
  'user:checkEmail',
  'post', 'postCategory:saveTree', 'page', 'pageCategory:saveTree', 'comment',
  'menu:allData,saveAll', 'friendLink:allData,saveAll', 'slider:allData,saveAll',
].forEach(uri0 => {
  const [uri, paramstr] = uri0.split(':')
  const params = paramstr ? paramstr.split(',') : []
  if (!urls[uri]) {
    urls[uri] = {}
  }
  for (const t of ['find', 'select', 'store', 'update', 'destroy', 'restore', ...params]) {
    urls[uri][t] = `${urls.serverBase}/${uri}.${t}`
  }
})

routes.forEach(item => {
  if (item.name && item.name.includes('.')) {
    const [l1, l2] = item.name.split('.')
    if (urls[l1]) {
      urls[l1][l2] = item.path
    }
  }
})

export default urls
