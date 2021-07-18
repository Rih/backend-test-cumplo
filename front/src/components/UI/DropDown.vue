<template>
  <div v-click-outside="hide" class="dropdown__container">
    <div v-if="label" class="dropdown__label">
      {{ label }}
    </div>
    <MainBtn
      @click="open"
      v-model="model"
      slot="button"
      light
      float
      :large="large"
      :small="small"
      :width="width"
      :round="round"
    >
      <div :style="{ color: model.length > 0 ? '#333' : '#888' }">
        {{
          model.length > 0 ? model : placeholder ? placeholder : 'Seleccionar'
        }}
      </div>
      <Icon>sm-drop</Icon>
    </MainBtn>

    <div
      v-if="show"
      class="dropdown__holder"
      :class="{ dropdown__holder_small: small }"
    >
      <button
        v-for="(item, i) in items"
        :key="i"
        @click="select(item)"
        class="dropdown__item"
        :class="{ dropdown__item_small: small }"
      >
        {{ item.text }}
      </button>
      <slot name="option"></slot>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
// @typescript-eslint/ban-ts-comment
import ClickOutside from 'vue-click-outside'
import MainBtn from '@/components/UI/MainBtn.vue'
import Icon from '@/components/UI/Icon.vue'

export default Vue.extend({
  props: {
    label: String,
    placeholder: String,
    items: Array,
    width: Number,
    large: Boolean,
    small: Boolean,
    round: Boolean,
    value: String,
  },
  data: () => ({
    show: false,
    model: '',
  }),
  mounted() {
    this.model = this.value
  },
  watch: {
    value(val) {
      this.model = val
    },
  },
  methods: {
    open() {
      this.$emit('click', event)
      this.show = true
    },
    select(item) {
      this.show = false
      this.model = item.text
      this.$emit('input', item.text)
      this.$emit('change', item.value)
    },
    hide() {
      this.show = false
    },
  },
  directives: {
    ClickOutside,
  },
  components: {
    MainBtn,
    Icon,
  },
})
</script>

<style lang="sass" scoped>
.dropdown__container
  position: relative

.dropdown__holder
  position: absolute
  top: 10px
  left: -10px
  border-radius: 5px
  padding: 10px 0
  background: white
  box-shadow: 0 5px 5px -5px #333
  border: 1px solid #eee
  width: 300px
  z-index: 900

.dropdown__holder_small
  width: 100%
  left: -5px

.dropdown__item
  all: unset
  cursor: pointer
  padding: 10px 15px !important
  width: 268px

.dropdown__item_small
  all: unset
  cursor: pointer
  padding: 5px 0 !important
  width: 100%
  text-align: center

.dropdown__item:hover
  background: #eee !important

.dropdown__label
  margin-bottom: 1px
  color: #555
</style>
