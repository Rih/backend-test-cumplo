import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import { LMap, LTileLayer, LMarker, LPopup, LImageOverlay, LIcon } from 'vue2-leaflet'
import 'leaflet/dist/leaflet.css'
import { Icon } from 'leaflet'
delete Icon.Default.prototype._getIconUrl
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
})

Vue.use(Buefy)
Vue.config.productionTip = false

Vue.component('l-map', LMap)
Vue.component('l-tile-layer', LTileLayer)
Vue.component('l-marker', LMarker)
Vue.component('l-popup', LPopup)
Vue.component('l-icon', LIcon)
Vue.component('l-image-overlay', LImageOverlay)

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
