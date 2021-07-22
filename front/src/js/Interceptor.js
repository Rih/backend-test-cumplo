import store from '@/store'
import { parseJwt } from '@/js/helpers'
import { APP_BASE_URL } from '@/js/constants'
import router from '@/router'
import axiosInstance from '@/js/AxiosWrapper.js'

const tokenURL = `${APP_BASE_URL}/api/token/`
const signupURL = `${APP_BASE_URL}/account/signup/`
const refreshURL = `${APP_BASE_URL}/api/token/refresh/`
const verifyURL = `${APP_BASE_URL}/api/token/verify/`

class Interceptor {
  constructor({ axios }) {
    this.isRefreshing = false
    this.isVerified = false
    this.failedQueue = []
    this._apiAxios = axios
    this.logged = false
  }

  start() {
    this._apiAxios.interceptors.response.use(
      (response) => this.responseHandler(response),
      (error) => this.errorHandler(error)
    )
  }

  responseHandler(response) {
    const { access, refresh, recaptcha } = response.data
    const { config } = response

    // User has signed in
    if (config.url === tokenURL || config.url === signupURL) {
      if (recaptcha.success) {
        this.setHeaders(access)
        const user = parseJwt(this.getAccessToken())
        this.logged = true
        store.dispatch('setAuthenticated', {
          access,
          refresh,
          user,
        })
      }
    }

    // Access-Token hasn't expired yet
    if (config.url === verifyURL) {
      if (
        window.location.pathname !== '/dashboard' &&
        window.location.pathname !== '/refresh' &&
        window.location.pathname !== '/redirect'
      ) router.push('/dashboard')
      this.setHeaders()
      const user = parseJwt(this.getAccessToken())
      store.dispatch('setAuthenticated', { user })
      this.logged = true
      this.isVerified = false
    }

    // Access-Token renew using Refresh-Token
    if (config.url === refreshURL) {
      this.setHeaders(access)
      const user = parseJwt(access)
      store.dispatch('setAuthenticated', { user })
      this.logged = true
    }

    return response
  }

  errorHandler(error) {
    let originalRequest = error.config
    if (!(error.response.status === 401 && originalRequest)) {
      return Promise.reject(error)
    }

    if (originalRequest.url === verifyURL && this.isVerified) {
      return Promise.reject(error)
    }

    if (originalRequest.url === verifyURL && !this.isVerified) {
      this.isVerified = true
    }

    // Refresh-Token has expired
    if (originalRequest.url === refreshURL) {
      store.dispatch('setUnauthenticated')
      if (this.logged) router.push('/')
      this.logged = false
      return Promise.reject(error)
    }

    if (this.isRefreshing) {
      return new Promise((resolve, reject) => {
        this.failedQueue.push({ resolve, reject })
      })
        .then((token) => {
          originalRequest = this.setHeaders(token, originalRequest)
          return this._apiAxios(originalRequest)
        })
        .catch((err) => {
          return Promise.reject(err)
        })
    }

    this.isRefreshing = true
    const refresh = this.getRefreshToken()

    // Getting a new Access-Token
    return new Promise((resolve, reject) => {
      this._apiAxios
        .post(refreshURL, { refresh })
        .then(({ data }) => {
          originalRequest = this.setHeaders(data.access, originalRequest)
          this.processQueue(null, data.access)
          resolve(this._apiAxios(originalRequest))
        })
        .catch((err) => {
          this.processQueue(err, null)
          reject(err)
        })
        .then(() => {
          this.isRefreshing = false
        })
    })
  }

  getRefreshToken() {
    let token = 'none'
    if (localStorage.getItem('ref')) token = localStorage.getItem('ref')
    return token
  }

  getAccessToken() {
    let token = 'none'
    if (localStorage.getItem('tkn')) token = localStorage.getItem('tkn')
    return token
  }

  verifyToken() {
    const token = this.getAccessToken()
    this._apiAxios.post(verifyURL, { token })
  }

  setHeaders(accessToken = null, request = null) {
    const token = accessToken ? accessToken : localStorage.getItem('tkn')
    const authStr = 'Bearer ' + token
    this._apiAxios.defaults.headers.common['Authorization'] = authStr

    if (accessToken) localStorage.setItem('tkn', accessToken)

    if (request) {
      request.headers['Authorization'] = authStr
      return request
    }
  }

  processQueue = (error, token = null) => {
    this.failedQueue.forEach((prom) => {
      if (error) {
        prom.reject(error)
      } else {
        prom.resolve(token)
      }
    })

    this.failedQueue = []
  }
}

export default new Interceptor({ axios: axiosInstance })
