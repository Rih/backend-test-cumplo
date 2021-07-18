import { LOGIN } from '@/store/init'

export default {
  START_LOADING: (state) => {
    state.loading.isActive = true
  },
  STOP_LOADING: (state) => {
    state.loading.isActive = false
  },
  SET_AUTHENTICATED: (state, payload) => {
    state.auth.logged = true
    state.auth.requesting = false
    state.user = payload.user
  },
  SET_CENTER: (state, payload) => {
    state.center = [payload.latitude, payload.longitude]
  },
  SET_ZOOM: (state, payload) => {
    state.zoom = payload
  },
  UPDATE_AUTH_CODE: (state, payload) => {
    console.log(state, payload)
  },
  GET_LATEST_OBSERVATIONS: (state, payload) => {
    state.observations = [...state.observations, ...payload.result]
  },
  VIEW_OBSERVATION: (state, payload) => {
    state.obs = payload
  },
  SET_AVATAR: (state, payload) => {
    debugger //eslint-disable-line
    if (payload.success)
      state.user.picture = payload.avatar
    else
      console.log("show error")
  },
  CHANGE_TAB: (state, payload) => {
    for(const k of Object.keys(state.tabs))
      state.tabs[k].isActive = k == payload
  },
  SET_REQUESTING: (state) => {
    state.auth.requesting = true
  },
  SET_UNAUTHENTICATED: (state) => {
    state.auth.requesting = false
    state.auth.logged = false
    state.user = {}
  },

  SET_LOGIN: (state, payload) => {
    state.login = { ...LOGIN, ...payload }
  },
  RESET_LOGIN: (state) => {
    state.login = LOGIN
  },
  SET_TOAST: (state, { type, msg }) => {
    state.toast = { type, msg, isActive: true }
  },
  SET_ALERT: (state, payload) => {
    state.alert = { ...state.alert, ...payload }
  },
  SET_GLOBAL: (state, payload) => {
    state.global = { ...state.global, ...payload }
  },
  SET_PREVIEW_DATA: (state, payload) => {
    state.preview = payload
  },
  SET_LOADING_ELIPSE: (state, payload) => {
    state.loadingElipse = { ...state.loadingElipse, ...payload }
  },

  SET_GLOBAL_UI: (state, payload) => {
    state.globalUI = { ...state.globalUI, ...payload }
  },
}
