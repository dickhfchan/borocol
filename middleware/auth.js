export default function ({ store, route, redirect }) {
  if (!store.state.authenticated) {
    return redirect({name: 'unauthorized'}, {intended: route.fullPath})
  }
}
