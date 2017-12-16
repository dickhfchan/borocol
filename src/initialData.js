const initialData = process.env.NODE_ENV === 'production' ? window.initialData : {
  serverRoot: '',
  clientBase: '/',
}
export default initialData
