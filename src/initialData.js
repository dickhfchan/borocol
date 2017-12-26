const initialData = window.initialData ||  {
  serverRoot: '',
  clientBase: '/',
}
if (process.env.NODE_ENV === 'production') {
  Object.assign(initialData, {
    clientBase: '/borocol/dist/',
  })
}
export default initialData
