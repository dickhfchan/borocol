import {steps} from '@/initialData'
export const createCourse = [
  { path: '', name: 'createCourse', component: resolve => require(['../views/CreateCourse/index.vue'], resolve), meta: {title: 'Create Course'}},
  { path: '/create-course/page1', name: 'createCoursePage1', component: resolve => require(['../views/CreateCourse/Page1.vue'], resolve), meta: {}},
  { path: '/create-course/page2', name: 'createCoursePage2', component: resolve => require(['../views/CreateCourse/Page2.vue'], resolve), meta: {}},
  { path: '/create-course/page3', name: 'createCoursePage3', component: resolve => require(['../views/CreateCourse/Page3.vue'], resolve), meta: {}},
  { path: '/create-course/page4', name: 'createCoursePage4', component: resolve => require(['../views/CreateCourse/Page4.vue'], resolve), meta: {}},
  { path: '/create-course/page5', name: 'createCoursePage5', component: resolve => require(['../views/CreateCourse/Page5.vue'], resolve), meta: {}},
  { path: '/create-course/page6', name: 'createCoursePage6', component: resolve => require(['../views/CreateCourse/Page6.vue'], resolve), meta: {}},
  { path: '/create-course/page7', name: 'createCoursePage7', component: resolve => require(['../views/CreateCourse/Page7.vue'], resolve), meta: {}},
  { path: '/create-course/page8', name: 'createCoursePage8', component: resolve => require(['../views/CreateCourse/Page8.vue'], resolve), meta: {}},
  { path: '/create-course/page9', name: 'createCoursePage9', component: resolve => require(['../views/CreateCourse/Page9.vue'], resolve), meta: {}},
]
createCourse.forEach((item, index) => {
  if (index > 0) {
    const title = steps.find(v => v.pageRange[0] <= index && index <= v.pageRange[1]).title
    item.meta.title = `${title} - Create Course`
  }
})

const routes = [
  { path: '/', name: 'home', component: resolve => require(['../views/Home.vue'], resolve), meta: {title: 'Borocol'}},
  { path: '/profile', name: 'profile', component: resolve => require(['../views/StudentProfile.vue'], resolve), meta: {title: 'Profile'}},
  { path: '/my-courses', name: 'myCourses', component: resolve => require(['../views/MyCourses.vue'], resolve), meta: {title: 'My Courses'}},
  { path: '/orders', name: 'orders', component: resolve => require(['../views/Orders.vue'], resolve), meta: {title: 'Orders'}},
  { path: '/create-course', component: resolve => require(['../views/CreateCourse.vue'], resolve),
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
