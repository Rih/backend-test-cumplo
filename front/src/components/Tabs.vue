<template>
  <div>
    <div class="tabs__header">
      <div
        v-for="(tab, i) in getTabs"
        :key="i"
        @click="onClick(tab.key)"
        class="tabs__header_item"
        :class="{ tabs__active: tab.isActive }"
        style="transition: border-bottom 0.2s ease"
      >{{ tab.name }}</div>
    </div>

    <div class="tabs__contents">
      <div :style="move" class="tabs__content">
        <div v-for="(tab, i) in getTabs" :key="i" class="tab_item">
          <slot v-if="tab.isActive" :name="`tab${i + 1}`"></slot>
        </div>
      </div>
    </div>
  </div>
</template>


<script lang="ts">
import Vue from 'vue'
import { mapState, mapActions, mapGetters } from 'vuex'

export default Vue.extend({
  props: {
    secondary: Boolean,
    outline: Boolean,
    small: Boolean,
  },
  data: () => ({}),
  methods: {
    onClick(k: string) {
      if(k == 'obs' && (!this.obs || !this.obs?.photos)) return
      this.changeTab(k)
      this.$emit('change', k)
    },
    ...mapActions(['changeTab']),
  },
  computed: {
    move() {
      const tabs: Array<any> = this.getTabs
      const i = tabs.findIndex((tab: any) => tab.isActive)
      return {
        transform: `translateX(-${i * 100}%)`,
      }
    },
    ...mapState(['tabs', 'obs']),
    ...mapGetters(['getTabs']),
  },
})
</script>

<style lang="sass" scoped>
.tabs__header
  margin-bottom: 30px
  display: flex

.tabs__header_item
  cursor: pointer
  font-size: 14px
  padding: 5px
  text-align: center
  width: 200px
  border-bottom: 3px solid #eee
  color: #777
  font-weight: 600px
  text-transform: uppercase
  font-family: 'Poppins', sans-serif

.tabs__contents
  width: 100%
  overflow: hidden

.tabs__content
  display: flex
  transition: transform .5s ease

.tabs__active
  color: #4299e1
  border-bottom: 3px solid #4299e1

.tab_item
  flex: 0 0 100%
</style>
