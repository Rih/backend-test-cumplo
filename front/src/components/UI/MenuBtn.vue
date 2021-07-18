<template>
  <div
    @click="clicked"
    class="btnMenu__normal"
    :class="{
      btnMenu__active: active,
      btn__shrink: shrink,
    }"
  >
    <Icon :stroke="active ? 2 : 1" style="color: #6c7280">{{ icon }}</Icon>
    <span v-if="!shrink" class="btnMenu__text">{{ text }}</span>
  </div>
</template>

<script>
import Vue from 'vue'
import Icon from '@/components/UI/Icon.vue'

export default Vue.extend({
  props: {
    icon: String,
    text: String,
    active: Boolean,
    shrink: Boolean,
  },
  methods: {
    clicked(event) {
      this.$emit('click', event)
    },
  },
  components: {
    Icon,
  },
})
</script>

<style lang="sass" scoped>
.btnMenu__normal
  margin-top: 5px
  padding: 10px
  display: flex
  align-items: center
  color: #666
  cursor: pointer
  user-select: none

.btnMenu__normal:hover
  background: #e4e7eb6e

.btnMenu__text
  margin-left: 10px
  color: #333

.btnMenu__active
  padding: 10px
  border-radius: 3px
  background: #E4E7EB
  color: #242C3C
  font-weight: 600

.btnMenu__icon_active
  color: rgb(26, 32, 44)

.btnMenu__textt
  margin-left: 10px
</style>
