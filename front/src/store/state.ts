import { LOGIN, SIGNUP, DEFAULT_GPS, DEFAULT_ZOOM } from '@/store/init'

export default {
  auth: {
    logged: false,
    requesting: true,
  },
  center: {
    lat: DEFAULT_GPS[0],
    lng: DEFAULT_GPS[1],
  },
  zoom: DEFAULT_ZOOM,
  user: {
    nombre: '',
    id: 0,
    email: '',
    picture: '',
  },
  observations: [],
  obs: {},
  tabs: {
    map: {
      name: 'Mapa',
      isActive: true,
      key: 'map',
    },
    obs: {
      name: 'Observaciones',
      isActive: false,
      key: 'obs',
    },
  },
  loading: {
    isActive: false,
  },
  toast: {
    msg: '',
    type: 'success',
    isActive: false,
  },
  alert: {
    title: '',
    msg: '',
    isActive: false,
  },
  login: { ...LOGIN },
  signup: { ...SIGNUP },
  loadingElipse: {
    isActive: false,
  },
  statistics: {
    hasNext: false,
    hasPrev: false,
    total: 0,
    current: 1,
    totalCurrent: 0,
    data: []
  },
  globalUI: {
    tableWidth: 900,
    isSideMenuCollapsed: false,
  },
}
