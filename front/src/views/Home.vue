<template>
  <div style="padding: 50px">
    <Tabs v-model="tabs" v-on:change="onTabChange" style="margin-top: -50px">
      <div slot="tab1">
        <MapSearch />
      </div>

      <div slot="tab2" class="research__tab2">
        <div v-for="(photo, i) in obs.photos" :key="i" style="height: 260px">
          <img class="home__obs-img" :src="photo.medium_url" style="height: 160px" />
          <enlargeable-image :src="photo.thumb_url" :src_large="photo.large_url">
            <span>Ver</span>
          </enlargeable-image>
        </div>
        <div style="text-align: right">
          <MainBtn @click="(e) => assignAvatar(obs)" secondary>Asignar como avatar</MainBtn>
        </div>
      </div>
    </Tabs>
  </div>
</template>

<script>
import MapSearch from '@/components/MapSearch.vue'
import Tabs from '@/components/Tabs.vue'
import { mapState } from 'vuex'
import MainBtn from '@/components/UI/MainBtn.vue'
import { mapActions } from 'vuex'

export default {
  data: () => ({}),
  computed: {
    imgDefault() {
      return require('@/assets/logo.png')
    },
    ...mapState(['tabs', 'obs']),
  },
  methods: {
    onTabChange(index) {
      console.log(index)
    },
    ...mapActions(['assignAvatar']),
  },
  components: {
    MapSearch,
    Tabs,
    MainBtn,
  },
}
</script>


<style lang="sass" scoped>
.home__obs-img
  display: block
  padding: 3px 10px
  border-radius: 5px
  background: whitesmoke
  display: inline-block
  text-align: center
  font-size: 14px
.home__download
  margin-top: 20px
  display: flex
  justify-content: flex-end
</style>
