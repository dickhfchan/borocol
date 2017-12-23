const routes = [
  { path: '/', name: 'home', component: resolve => require(['../views/Home.vue'], resolve), meta: {title: 'Borocol'}},
  { path: '/CreateCourse0', name: 'createCourse0', component: resolve => require(['../views/CreateCourse0.vue'], resolve), meta: {title: 'Create Course 0'}},
  { path: '/CreateCourse1', name: 'createCourse1', component: resolve => require(['../views/CreateCourse1.vue'], resolve), meta: {title: 'Create Course 1'}},
  { path: '/CreateCourse2', name: 'createCourse2', component: resolve => require(['../views/CreateCourse2.vue'], resolve), meta: {title: 'Create Course 2'}},
  { path: '/CreateCourse3', name: 'createCourse3', component: resolve => require(['../views/CreateCourse3.vue'], resolve), meta: {title: 'Create Course 3'}},
  { path: '/CreateCourse4', name: 'createCourse4', component: resolve => require(['../views/CreateCourse4.vue'], resolve), meta: {title: 'Create Course 4'}},
  { path: '/CreateCourse5', name: 'createCourse5', component: resolve => require(['../views/CreateCourse5.vue'], resolve), meta: {title: 'Create Course 5'}},
  { path: '/CreateCourse6', name: 'createCourse6', component: resolve => require(['../views/CreateCourse6.vue'], resolve), meta: {title: 'Create Course 6'}},
  { path: '/CreateCourse7', name: 'createCourse7', component: resolve => require(['../views/CreateCourse7.vue'], resolve), meta: {title: 'Create Course 7'}},
  { path: '/CreateCourse8', name: 'createCourse8', component: resolve => require(['../views/CreateCourse8.vue'], resolve), meta: {title: 'Create Course 8'}},
  { path: '/CreateCourse9a', name: 'createCourse9a', component: resolve => require(['../views/CreateCourse9a.vue'], resolve), meta: {title: 'Create Course 9a'}},
  { path: '/CreateCourse9b', name: 'createCourse9b', component: resolve => require(['../views/CreateCourse9b.vue'], resolve), meta: {title: 'Create Course 9b'}},
  { path: '/CreateCourseTips', name: 'createCourseTips', component: resolve => require(['../views/CreateCourseTips.vue'], resolve), meta: {title: 'Create Course Tips'}},
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
