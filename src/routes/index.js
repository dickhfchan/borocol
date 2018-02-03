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
  { path: '/liked-courses', name: 'likedCourses', component: resolve => require(['../views/LikedCourses.vue'], resolve), meta: {title: 'Liked Courses'}},
  { path: '/my-course-visa', name: 'myCourseVisa', component: resolve => require(['../views/MyCourseVisa.vue'], resolve), meta: {title: 'My Course Visa'}},
  { path: '/my-course-visa-step1-popup-visa', name: 'unnamed1', component: resolve => require(['../views/MyCourseVisaStep1PopupVisa.vue'], resolve), meta: {}},
  { path: '/my-course-classmate', name: 'unnamed2', component: resolve => require(['../views/MyCourseClassmate.vue'], resolve), meta: {}},
  { path: '/request-refund', name: 'unnamed3', component: resolve => require(['../views/RequestRefund.vue'], resolve), meta: {}},
  { path: '/orders', name: 'orders', component: resolve => require(['../views/Orders.vue'], resolve), meta: {title: 'Orders'}},
  { path: '/settings', name: 'settings', component: resolve => require(['../views/Settings.vue'], resolve), meta: {title: 'Settings'}},
  { path: '/message', name: 'message', component: resolve => require(['../views/Message.vue'], resolve), meta: {title: 'Message'}},
  { path: '/create-course', component: resolve => require(['../views/CreateCourse.vue'], resolve),
    children: createCourse,
  },
  { path: '/course', name: 'unnamed4', component: resolve => require(['../views/Course.vue'], resolve),},
  { path: '/course-filter', name: 'unnamed5', component: resolve => require(['../views/CourseFilter.vue'], resolve),},
  { path: '/school-profile', component: resolve => require(['../views/SchoolProfile.vue'], resolve),},
  { path: '/SchoolMyCourse', component: resolve => require(['../views/SchoolMyCourse.vue'], resolve),},
  { path: '/SchoolMyCourseStudent', component: resolve => require(['../views/SchoolMyCourseStudent.vue'], resolve),},
  { path: '/SchoolReviews', component: resolve => require(['../views/SchoolReviews.vue'], resolve),},
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
