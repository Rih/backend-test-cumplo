<template>
  <div @click="onClick" :style="{ width: width ? width + 'px' : '100%' }">
    <div
      class="mainInput__label"
      :class="{
        mainInput__label_large: large,
        mainInput__label_outline: outline,
      }"
    >{{ label }}</div>
    <div
      class="mainInput__filled"
      :class="{
        mainInput__outline: outline,
        mainInput__large: large,
      }"
    >
      <input
        v-model="text"
        :placeholder="placeholder"
        :type="mutatedType"
        class="mainInput__input_filled"
        :class="{
          mainInput__input_outline: outline,
          mainInput__input_large: large,
        }"
      />

      <MainBtn v-if="showEye" icon @click="toggleType(mutatedType)">
        <Icon v-if="type === 'password'" style="color: #999">eye</Icon>
        <Icon v-if="type === 'text'" style="color: #999">eye-off</Icon>
      </MainBtn>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Icon from '@/components/UI/Icon.vue'
import MainBtn from '@/components/UI/MainBtn.vue'

export default Vue.extend({
  props: {
    placeholder: String,
    label: String,
    value: String,
    outline: Boolean,
    width: Number,
    large: Boolean,
    type: String,
  },
  data: () => ({
    text: '',
    mutatedType: 'text',
    showEye: false,
  }),
  methods: {
    toggleType(type) {
      if (type === 'text') return (this.mutatedType = 'password')
      this.mutatedType = 'text'
    },
    onClick(event: any) {
      this.$emit('click', event)
    },
  },
  mounted() {
    this.text = this.value
    this.showEye = this.type === 'password'
    if (this.type)
        this.mutatedType = this.type
  },
  watch: {
    value(val) {
      this.text = val
    },
    text(val) {
      this.$emit('input', val)
    },
  },
  components: {
    Icon,
    MainBtn,
  },
})
</script>

<style lang="sass" scoped>
.mainInput__input_filled
  all: unset !important
  width: 100% !important
  border: 0
  height: 25px
  color: #444 !important
  background: #eee !important

.mainInput__input_outline
  background: white !important

.mainInput__input_large
  height: 30px

.mainInput__filled
  background: #eee
  padding: 7px 10px
  margin-bottom: 10px
  border-radius: 3px
  display: flex
  justify-content: space-between
  align-items: center

.mainInput__outline
  background: white !important
  border: 1px solid rgb(206, 212, 218)
  border-radius: 5px

.mainInput__large
  padding: 12px 20px

.mainInput__label
  margin-bottom: 1px
  color: #555

.mainInput__label_outline
  color: #666

.mainInput__label_large
  margin-bottom: 5px

::placeholder
  color: #777
  opacity: 1

:-ms-input-placeholder
  color: #777

::-ms-input-placeholder
  color: #777
</style>
