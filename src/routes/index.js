import {steps} from '@/initialData'
export const createCourse = [
  { path: '', name: 'createCourse', component: resolve => require(['../views/CreateCourse/index.vue'], resolve), meta: {title: 'Create Course'}},
  { path: '/CreateCourse/Page1', name: 'createCoursePage1', component: resolve => require(['../views/CreateCourse/Page1.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page2', name: 'createCoursePage2', component: resolve => require(['../views/CreateCourse/Page2.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page3', name: 'createCoursePage3', component: resolve => require(['../views/CreateCourse/Page3.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page4', name: 'createCoursePage4', component: resolve => require(['../views/CreateCourse/Page4.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page5', name: 'createCoursePage5', component: resolve => require(['../views/CreateCourse/Page5.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page6', name: 'createCoursePage6', component: resolve => require(['../views/CreateCourse/Page6.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page7', name: 'createCoursePage7', component: resolve => require(['../views/CreateCourse/Page7.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page8', name: 'createCoursePage8', component: resolve => require(['../views/CreateCourse/Page8.vue'], resolve), meta: {}},
  { path: '/CreateCourse/Page9', name: 'createCoursePage9', component: resolve => require(['../views/CreateCourse/Page9.vue'], resolve), meta: {}},
]
createCourse.forEach((item, index) => {
  if (index > 0) {
    const title = steps.find(v => v.pageRange[0] <= index && index <= v.pageRange[1]).title
    item.meta.title = `${title} - Create Course`
  }
})

const routes = [
  { path: '/', name: 'home', component: resolve => require(['../views/Home.vue'], resolve), meta: {title: 'Borocol'}},
  // { path: '/CreateCourse9a', name: 'createCourse9a', component: resolve => require(['../views/CreateCourse9a.vue'], resolve), meta: {title: 'Create Course 9a'}},
  // { path: '/CreateCourse9b', name: 'createCourse9b', component: resolve => require(['../views/CreateCourse9b.vue'], resolve), meta: {title: 'Create Course 9b'}},
  { path: '/CreateCourse', component: resolve => require(['../views/CreateCourse.vue'], resolve),
    children: createCourse,
  },
  //
]

const authRoutes = [
]

for (const item of authRoutes) {
  if (!item.meta) {
    item.meta = {}
  }
  item.meta.auth = true
}

export default [
  ...routes,
  ...authRoutes,
  { path: '*', redirect: {name: 'home'} },
]
