const initialData = window.initialData ||  {
  serverRoot: '', // 'http://127.0.0.1:8081', // 'http://52.76.70.227',
  clientBase: '/',
}
// production env but no window.initialData; 生产版本但未注入初始数据, 适用于线上调试
// if (process.env.NODE_ENV === 'production' && !window.initialData) {
//   Object.assign(initialData, {
//     clientBase: '/',
//   })
// }
export default initialData

export const steps = [
  {index: 1, pageRange: [1,2], title: 'Start with the basic'},
  {index: 2, pageRange: [3, 3], title: 'Location'},
  {index: 3, pageRange: [4, 5], title: 'General Details'},
  {index: 4, pageRange: [6, 6], title: 'Request Form'},
  {index: 5, pageRange: [7, 7], title: 'Make your program looks more attractive'},
  {index: 6, pageRange: [8, 8], title: 'Accomodation'},
  {index: 7, pageRange: [9, 9], title: 'Pricing & Quota'},
]
