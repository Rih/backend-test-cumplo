import API from '@/js/API'
import { APP_BASE_URL } from '@/js/constants'

export default {
  startLoading: ({ commit }) => {
    commit('START_LOADING')
  },
  stopLoading: ({ commit }) => {
    commit('STOP_LOADING')
  },
  setAuthenticated: ({ commit }, payload) => {
    const { refresh, access } = payload
    if (refresh && access) {
      localStorage.setItem('tkn', payload.access)
      localStorage.setItem('ref', payload.refresh)
    }
    commit('SET_AUTHENTICATED', payload)
  },
  setRequesting: ({ commit }) => {
    commit('SET_REQUESTING')
  },
  setUnauthenticated: ({ commit }) => {
    localStorage.removeItem('tkn')
    localStorage.removeItem('ref')
    commit('SET_UNAUTHENTICATED')
  },
  setCenter: ({ commit }, payload) => {
    commit('SET_CENTER', payload)
  },
  setZoom: ({ commit }, payload) => {
    commit('SET_ZOOM', payload)
  },
  updateAuthCode: ({ commit }, payload) => {
    commit('UPDATE_AUTH_CODE', payload)
  },
  getLatestObservations: async ({ commit }, payload) => {
    const api = new API()
    api.createEntity({ name: 'observations' })
    const result = await api.endpoints.observations.post({ gps: payload })
    commit('GET_LATEST_OBSERVATIONS', result)
  },
  viewObservation: ({ commit }, payload) => {
    commit('VIEW_OBSERVATION', payload)
  },
  assignAvatar: async ({ commit }, payload) => {
    const api = new API()
    const avatar = payload.photos[0].thumb_url
    api.createEntity({ name: 'profile' })
    const response = await api.endpoints.profile.post({ obs: avatar })
    commit('SET_AVATAR', { success: response.status === 200, avatar })
  },
  changeTab: ({ commit }, tabKey) => {
    commit('CHANGE_TAB', tabKey)
  },
  setLogin: ({ commit }, payload) => {
    commit('SET_LOGIN', payload)
  },
  resetLogin: ({ commit }) => {
    commit('RESET_LOGIN')
  },
  setToast: ({ commit }, payload) => {
    commit('SET_TOAST', payload)
  },
  setAlert: ({ commit }, payload) => {
    commit('SET_ALERT', payload)
  },
  setLoadingElipse: ({ commit }, payload) => {
    commit('SET_LOADING_ELIPSE', payload)
  },
  setGlobalUI: ({ commit }, payload) => {
    commit('SET_GLOBAL_UI', payload)
  },
}
