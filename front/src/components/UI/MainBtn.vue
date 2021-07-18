<template>
  <button
    @click="clicked"
    class="btn__hover"
    :class="{
      btn__fav: fav,
      btn__fill: !secondary && !fav,
      btn__secondary: secondary,
      btn__outline: outline,
      btn__small: small,
      btn__large: large,
      btn__plain: plain,
      btn__light: light,
      btn__float: float,
      btn__icon: icon,
      btn__round: round,
      btn__dark: dark,
      btn_disabled: btnDisabled
    }"
    :disabled="btnDisabled"
    :style="{ width: width ? width + 'px' : 'none' }"
  >
    <slot></slot>
  </button>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  props: {
    fav: Boolean,
    secondary: Boolean,
    btnDisabled: Boolean,
    outline: Boolean,
    small: Boolean,
    large: Boolean,
    light: Boolean,
    float: Boolean,
    width: Number,
    icon: Boolean,
    round: Boolean,
    dark: Boolean,
    plain: Boolean,
  },
  methods: {
    clicked(event: any) {
      this.$emit('click', event);
    }
  }
});
</script>

<style lang="sass" scoped>
.btn__hover:hover
  opacity: 0.9

.btn__fav
  unset: all !important
  background: whitesmoke
  color: #666
  width: 45px
  height: 45px
  border-radius: 50%
  display: flex
  align-items: center
  justify-content: center
  outline: none !important
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)

.btn__fav:active
  background: #ccc

.btn__fill
  unset: all
  background: #4299e1
  color: white
  font-weight: 600
  border-radius: 5px
  padding: 5px 10px
  display: flex
  align-items: center

.btn__outline
  unset: all
  font-size: 16px
  border: 1px solid #777
  color: rgb(45, 55, 72)
  font-weight: 600
  border-radius: 5px
  padding: 5px 10px
  display: flex
  align-items: center
  background: none

.btn__small
  font-size: 14px
  padding: 5px 8px !important
  min-width: 50px
  text-align: center !important

.btn__round
  border-radius: 10px !important
  outline: none !important

.btn__large
  font-size: 16px
  padding: 7px 15px

.btn__secondary
  unset: all
  background: rgb(226, 232, 240)
  color: rgb(45, 55, 72)
  font-weight: 600
  border-radius: 5px
  padding: 5px 10px

.btn__plain
  background: none
  border: 0 !important
  color: rgb(45, 55, 72)
  font-weight: 600

.btn__dark
  background: none
  border: 1px solid #eee
  color: #4299e1
  font-weight: 400

.btn__light
  color: #222
  background: none
  border: 0
  font-weight: 400
  border: 1px solid #e2e2e2
  border-radius: 5px

.btn__light:hover
  opacity: 0.8 !important

.btn_disabled:hover
  cursor: not-allowed!important

.btn__float
  display: flex
  justify-content: space-between

.btn__icon
  all: unset
  cursor: pointer
  padding: 0 !important
  margin: 0 !important
  width: 35px
  height: 35px
  background: none !important
  border-radius: 50% !important
  display: flex
  justify-content: center
  align-items: center

.btn__icon:hover
  background: #eee !important
</style>
