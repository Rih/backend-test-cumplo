import API from '@/js/API'

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
      localStorage.setItem('tkn', access)
      localStorage.setItem('ref', refresh)
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
  getLatestObservations: async ({ commit }, { ne, sw }) => {
    const api = new API()
    api.createEntity({ name: 'observations' })
    const result = await api.endpoints.observations.get({
      queryParams: {
        nelat: ne.lat,
        nelng: ne.lng,
        swlat: sw.lat,
        swlng: sw.lng,
      },
    })
    commit('GET_LATEST_OBSERVATIONS', result)
  },
  viewObservation: ({ commit }, payload) => {
    commit('VIEW_OBSERVATION', payload)
  },
  assignAvatar: async ({ commit }, payload) => {
    const api = new API()
    const avatar = payload.thumb_url
    api.createEntity({ name: 'profile' })
    const response = await api.endpoints.profile.post({ obs: avatar })
    commit('SET_AVATAR', { success: response.status === 200, avatar })
  },
  changeTab: ({ commit }, tabKey) => {
    commit('CHANGE_TAB', tabKey)
  },
  getStatistics: async ({ commit }, payload) => {
    const api = new API()
    api.createEntity({ name: 'audit' })
    const response = await api.endpoints.audit.get({
      queryParams: { page: payload },
    })
    commit('GET_STATISTICS', response)
  },
  setLogin: ({ commit }, payload) => {
    commit('SET_LOGIN', payload)
  },
  setSignup: ({ commit }, payload) => {
    commit('SET_SIGN_UP', payload)
  },
  resetLogin: ({ commit }) => {
    commit('RESET_LOGIN')
  },
  resetSignup: ({ commit }) => {
    commit('RESET_SIGNUP')
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
