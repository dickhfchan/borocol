const routes = [
  { path: '/', redirect: {name: 'dashboard'}},
  // todo move to authRoutes
  { path: '/dashboard', name: 'dashboard', component: resolve => require(['../views/Dashboard.vue'], resolve), meta: {title: 'Dashboard'}},
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
  { path: '*', redirect: {name: 'dashboard'} },
]
