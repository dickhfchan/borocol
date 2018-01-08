const initialData = window.initialData ||  {
  serverRoot: 'http://127.0.0.1:8081', // 'http://52.76.70.227',
  clientBase: '/',
}
// production env but no window.initialData; 生产版本但未注入初始数据, 适用于线上调试
// if (process.env.NODE_ENV === 'production' && !window.initialData) {
//   Object.assign(initialData, {
//     clientBase: '/',
//   })
// }
export default initialData
