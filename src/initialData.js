const initialData = process.env.NODE_ENV === 'production' ? window.initialData : {
  serverRoot: 'http://127.0.0.1/works/xiaochengxu-maker/public/apps/111111',
  clientBase: '/',
}
export default initialData
