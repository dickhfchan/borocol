const routes = [
  { path: '/', name: 'home', component: resolve => require(['../views/Home.vue'], resolve), meta: {title: 'Borocol'}},
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
