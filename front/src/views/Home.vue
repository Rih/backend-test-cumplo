<template>
  <div style="padding: 50px">
    <Tabs v-model="tabs" v-on:change="onTabChange" style="margin-top: -50px">
      <div slot="tab1">
        <MapSearch />
      </div>
      <div slot="tab2" class="research__tab2">
        <Observations v-if="hasImages" />
      </div>
    </Tabs>
  </div>
</template>

<script>
import MapSearch from '@/components/MapSearch.vue'
import Observations from '@/components/Observations.vue'
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
    ...mapState(['tabs', 'obs']),
  },
  methods: {
    onTabChange(index) {
      console.log(index)
    },
    ...mapActions([]),
  },
  components: {
    MapSearch,
    Tabs,
    Observations,
  },
}
</script>


<style lang="sass" scoped>
.home__download
  margin-top: 20px
  display: flex
  justify-content: flex-end
</style>
