import { LOGIN, DEFAULT_GPS, DEFAULT_ZOOM } from '@/store/init'

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
      name: 'Observación',
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
  loadingElipse: {
    isActive: false,
  },
  apiCalls: {
    data: [
      { data: [], headers: [] },
      { data: [], headers: [] },
      { data: [], headers: [] },
      { data: [], headers: [] },
      { data: [], headers: [] },
    ],
    headers: [],
  },
  globalUI: {
    tableWidth: 900,
    isSideMenuCollapsed: false,
  },
}
