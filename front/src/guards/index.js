import store from '@/store'

const protectedRoutes = ['/dashboard']

let logged = false
let isLoggedSet = false
let resolveMe = 'none'

const platformReady = () => {
  return new Promise((resolve) => {
    resolveMe = resolve
  })
}

store.subscribe((mutation, state) => {
  logged = state.auth.logged
  const isRequesting = state.auth.isRequesting
  if (!isRequesting && !isLoggedSet) {
    if (resolveMe === 'none') return
    resolveMe()
    isLoggedSet = true
  }
})

export const guard = async (to, from, next) => {
  const route = protectedRoutes.find((route) => route === to.path)
  if (!route) return next()
  if (!isLoggedSet) await platformReady()
  if (route && logged) return next()
  next({ name: 'login' })
}
