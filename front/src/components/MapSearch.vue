<template>
  <div>
    <Card>
      <div style="display: flex; align-items: center; flex-direction: column; padding: 10px">
        <Tips />
        <MainBtn @click="onSearchObservations" large style="height: 43px">
          BUSCA TU AVATAR
          <Icon v-if="false">close</Icon>
        </MainBtn>
      </div>
      <div style="display: flex; align-items: center; align-content: center">
        <div id="map" style="width: 100%">
          <l-map
            ref="myMap"
            :zoom.sync="zoom"
            :center.sync="center"
            :options="{zoomControl: false}"
          >
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <l-marker ref="markerYou" :lat-lng="center">
              <l-popup :content="'Estas aqui'">
                <slot id="default"></slot>
              </l-popup>
            </l-marker>
            <div v-if="observations.length">
              <l-marker
                @click="(e) => setObservation(obs)"
                v-for="(obs, i) in observations"
                :lat-lng="{lat: obs.latitude, lng: obs.longitude}"
                :key="i"
              ></l-marker>
            </div>
          </l-map>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
import Card from '@/components/UI/Card.vue'
import Tips from '@/components/Tips.vue'
import MainBtn from '@/components/UI/MainBtn.vue'
import Icon from '@/components/UI/Icon.vue'
import { mapActions, mapState } from 'vuex'

export default {
  // props: {
  //   value: Object,
  // },
  data: () => ({
    img:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Sydney_Opera_House_-_Dec_2008.jpg/1024px-Sydney_Opera_House_-_Dec_2008.jpg',
  }),
  methods: {
    async checkPermission() {
      const result = await navigator.permissions.query({ name: 'geolocation' })

      if (result.state === 'prompt')
        setTimeout(() => console.log('prompting...'), 150)

      if (result.state === 'granted')
        navigator.geolocation.getCurrentPosition(this.positionGranted)
    },
    requestPermission() {
      navigator.geolocation.getCurrentPosition(
        this.positionGranted,
        this.positionDenied
      )
    },
    positionGranted(position) {
      this.setCenter({
        lat: position.coords.latitude.toFixed(7),
        lng: position.coords.longitude.toFixed(7),
      })
    },
    onSearchObservations() {
      console.log('fetch api')
      const result = this.$refs.myMap.mapObject.getBounds()
      this.getLatestObservations({
        ne: result._northEast,
        sw: result._southWest,
      })
    },
    setObservation(obs) {
      this.viewObservation(obs)
      this.changeTab('obs')
    },
    ...mapActions([
      'setCenter',
      'getLatestObservations',
      'viewObservation',
      'changeTab',
    ]),
  },
  mounted() {
    this.checkPermission()
    this.$nextTick(() => {
      //console.log(this.$refs.myMap.mapObject)
    })
  },
  computed: {
    zoom: {
      get() {
        return this.$store.state.zoom
      },
      set(value) {
        this.$store.dispatch('setZoom', value)
      },
    },
    center: {
      get() {
        return this.$store.state.center
      },
      set(value) {
        this.$store.dispatch('setCenter', value)
      },
    },
    ...mapState(['observations']),
  },
  components: {
    Card,
    MainBtn,
    Icon,
    Tips,
  },
}
</script>

<style lang="sass" scoped>
  #map
    width: 500px
    height: 500px
    @media(min-width: 425px)
      width: 90%
</style>
