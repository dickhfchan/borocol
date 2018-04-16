export default function ({ store, route, redirect, env }) {
  if (!store.state.authenticated) {
    if (env.devStatic) {
      return
    }
    return redirect({name: 'unauthenticated'}, {intended: route.fullPath})
  }
}
