export const createCourse = [
  { path: '', name: 'createCourse', component: resolve => require(['../views/CreateCourse/index.vue'], resolve), meta: {title: 'Create Course'}},
  { path: '/CreateCourse/Step1', name: 'createCourseStep1', component: resolve => require(['../views/CreateCourse/Step1.vue'], resolve), meta: {title: 'Step 1 - Create Course'}},
  { path: '/CreateCourse/Step2', name: 'createCourseStep2', component: resolve => require(['../views/CreateCourse/Step2.vue'], resolve), meta: {title: 'Step 2 - Create Course'}},
  { path: '/CreateCourse/Step3', name: 'createCourseStep3', component: resolve => require(['../views/CreateCourse/Step3.vue'], resolve), meta: {title: 'Step 3 - Create Course'}},
  { path: '/CreateCourse/Step4', name: 'createCourseStep4', component: resolve => require(['../views/CreateCourse/Step4.vue'], resolve), meta: {title: 'Step 4 - Create Course'}},
  { path: '/CreateCourse/Step5', name: 'createCourseStep5', component: resolve => require(['../views/CreateCourse/Step5.vue'], resolve), meta: {title: 'Step 5 - Create Course'}},
  { path: '/CreateCourse/Step6', name: 'createCourseStep6', component: resolve => require(['../views/CreateCourse/Step6.vue'], resolve), meta: {title: 'Step 6 - Create Course'}},
  { path: '/CreateCourse/Step7', name: 'createCourseStep7', component: resolve => require(['../views/CreateCourse/Step7.vue'], resolve), meta: {title: 'Step 7 - Create Course'}},
  { path: '/CreateCourse/Step8', name: 'createCourseStep8', component: resolve => require(['../views/CreateCourse/Step8.vue'], resolve), meta: {title: 'Step 8 - Create Course'}},
  { path: '/CreateCourse/Step9', name: 'createCourseStep9', component: resolve => require(['../views/CreateCourse/Step9.vue'], resolve), meta: {title: 'Step 9 - Create Course'}},
]

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
