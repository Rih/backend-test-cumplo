<template>
  <div style="padding: 50px">
    <Tabs v-model="tabs" v-on:change="onTabChange" style="margin-top: -50px">
      <div slot="tab1">
        <DashboardMapSearch />
      </div>

      <div slot="tab2" class="research__tab2">
        <img :src="renderObservation" style="max-height: 500px" />
        <div style="text-align: right">
          <MainBtn @click="(e) => assignAvatar(obs)" secondary>Asignar avatar</MainBtn>
        </div>
      </div>
    </Tabs>
  </div>
</template>

<script>
import DashboardMapSearch from '@/components/DashboardMapSearch.vue'
import Tabs from '@/components/Tabs.vue'
import { mapState } from 'vuex'
import MainBtn from '@/components/UI/MainBtn.vue'
import { mapActions } from 'vuex'

export default {
  data: () => ({
    tabModel: {},
  }),
  computed: {
    imgDefault(){
      return require('@/assets/logo.png')
    },
    renderObservation(){
      if (this.obs && this.obs?.photos) 
        return this.obs.photos[0].large_url 
      return this.imgDefault
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
    DashboardMapSearch,
    Tabs,
    MainBtn,
  },
}
</script>


<style lang="sass" scoped>
.home__download
  margin-top: 20px
  display: flex
  justify-content: flex-end
</style>
