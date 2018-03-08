import {steps} from '@/initialData'

export const createCourse = [
  { path: '', name: 'createCourse', component: resolve => require(['../views/CreateCourse/index.vue'], resolve), meta: {}},
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

const routes = [
  { path: '/', name: 'home', component: resolve => require(['../views/Home.vue'], resolve), meta: {hasMenu: false}},
  { path: '/partner-with-us', name: 'partnerWithUs', component: resolve => require(['../views/PartnerWithUs.vue'], resolve), meta: {hasMenu: false}},
  { path: '/active-email', name: 'activeEmail', component: resolve => require(['../views/ActiveEmail.vue'], resolve), meta: {hasMenu: false, auth: true}},
  { path: '/SchoolReviews', component: resolve => require(['../views/SchoolReviews.vue'], resolve),},
  { path: '/profile', name: 'profile', component: resolve => require(['../views/StudentProfile.vue'], resolve), meta: {}},
  { path: '/my-courses', name: 'myCourses', component: resolve => require(['../views/MyCourses.vue'], resolve), meta: {}},
  { path: '/liked-courses', name: 'likedCourses', component: resolve => require(['../views/LikedCourses.vue'], resolve), meta: {}},
  { path: '/my-course-visa', name: 'myCourseVisa', component: resolve => require(['../views/MyCourseVisa.vue'], resolve), meta: {}},
  { path: '/my-course-visa-step1-popup-visa', name: 'unnamed1', component: resolve => require(['../views/MyCourseVisaStep1PopupVisa.vue'], resolve), meta: {}},
  { path: '/my-course-classmate', name: 'unnamed2', component: resolve => require(['../views/MyCourseClassmate.vue'], resolve), meta: {}},
  { path: '/request-refund', name: 'unnamed3', component: resolve => require(['../views/RequestRefund.vue'], resolve), meta: {}},
  { path: '/orders', name: 'orders', component: resolve => require(['../views/Orders.vue'], resolve), meta: {}},
  { path: '/settings', name: 'settings', component: resolve => require(['../views/Settings.vue'], resolve), meta: {}},
  { path: '/message', name: 'message', component: resolve => require(['../views/Message.vue'], resolve), meta: {}},
  { path: '/create-course', component: resolve => require(['../views/CreateCourse.vue'], resolve),
    children: createCourse,
  },
  { path: '/course', name: 'unnamed4', component: resolve => require(['../views/Course.vue'], resolve),},
  { path: '/course-filter', name: 'unnamed5', component: resolve => require(['../views/CourseFilter.vue'], resolve),},
  { path: '/school-profile', component: resolve => require(['../views/SchoolProfile.vue'], resolve),},
  { path: '/SchoolMyCourse', component: resolve => require(['../views/SchoolMyCourse.vue'], resolve),},
  { path: '/SchoolMyCourseStudent', component: resolve => require(['../views/SchoolMyCourseStudent.vue'], resolve),},
  { path: '/SchoolReviews', component: resolve => require(['../views/SchoolReviews.vue'], resolve),},
  // special
  { path: '/unauthorized', name: 'unauthorized', component: resolve => require(['../views/Unauthorized.vue'], resolve), meta: {hasMenu: false}},
  { path: '/routes', component: resolve => require(['../views/Routes.vue'], resolve)}, // for dev
  { path: '/index', redirect: {name: 'home'} }, // for prerender
  { path: '*', redirect: {name: 'home'} },
  //
]

export default routes
