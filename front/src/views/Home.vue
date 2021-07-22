<template>
  <div style="padding: 50px">
    <Tabs v-model="tabs" v-on:change="onTabChange" style="margin-top: -50px">
      <div slot="tab1">
        <MapSearch />
      </div>

      <div slot="tab2" class="research__tab2">
        <div class="home__obs-container" v-if="hasImages">
          <div
            class
            v-for="(photo, i) in obs.photos"
            :key="i"
            style="max-height: 300px"
          >
            <img class="home__obs-img" :src="photo.medium_url" @click="onSelectedImage(photo)" />
          </div>
        </div>
      </div>
    </Tabs>
  </div>
</template>

<script>
import MapSearch from '@/components/MapSearch.vue'
import Tabs from '@/components/Tabs.vue'
import { mapState } from 'vuex'
import dialog from '@/js/dialog'
import { mapActions } from 'vuex'

export default {
  data: () => ({}),
  computed: {
    hasImages() {
      return this.obs?.photos?.length > 0
    },
    imgDefault() {
      return require('@/assets/logo.png')
    },
    ...mapState(['tabs', 'obs']),
  },
  methods: {
    async onSelectedImage(photo) {
      const { ok } = await dialog.open('setAlert', {
        msg: 'Desea agregar como avatar?',
        title: 'Agregar Avatar',
        isActive: true,
      })
      if (ok) {
        this.assignAvatar(photo)
      }
    },
    onTabChange(index) {
      console.log(index)
    },
    ...mapActions(['assignAvatar', 'setAlert']),
  },
  components: {
    MapSearch,
    Tabs,
  },
}
</script>


<style lang="sass" scoped>
.home__obs-container
  display: flex
  flex-direction: row
  align-items: flex-start
  justify-content: center
.home__obs-img
  padding: 10px 10px
  border-radius: 10px
  margin: 10px
  background: whitesmoke
  text-align: center
  font-size: 14px
  height: 300px
.home__obs-img:hover
  background: lightgray
.home__download
  margin-top: 20px
  display: flex
  justify-content: flex-end
</style>
