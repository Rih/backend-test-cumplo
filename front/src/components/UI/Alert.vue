<template>
  <div v-if="alert.isActive" class="alert__container">
    <div v-click-outside="hide" class="alert__box">
      <div>
        <div class="alert__title">
          {{ alert.title }}
        </div>
        {{ alert.msg }}
      </div>

      <div class="alert__footer">
        <MainBtn @click="hide" plain small> CANCELAR </MainBtn>

        <div class="alert__spacer"></div>

        <MainBtn @click="onSubmit" secondary small> ACEPTAR </MainBtn>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Dialog from '@/js/dialog'
import MainBtn from '@/components/UI/MainBtn.vue'

// @typescript-eslint/ban-ts-comment
import ClickOutside from 'vue-click-outside'

export default {
  props: {
    value: Object,
  },
  data: () => ({
    firstClick: true,
    preventClickOutside: false,
  }),
  methods: {
    onSubmit() {
      Dialog.close('setAlert', { ok: true })
    },
    hide() {
      if (this.firstClick) return (this.firstClick = false)
      if (this.preventClickOutside) return (this.preventClickOutside = false)
      Dialog.close('setAlert', { ok: false })
    },
    ...mapActions(['setAlert']),
  },
  watch: {
    isActive(val) {
      this.firstClick = val
    },
  },
  computed: {
    isActive() {
      return this.alert.isActive
    },
    ...mapState(['alert']),
  },
  mounted() {
    this.popupItem = this.$el
  },
  components: {
    MainBtn,
  },
  directives: {
    ClickOutside,
  },
}
</script>

<style lang="sass" scoped>
.alert__container
  z-index: 800
  position: fixed
  top: 0
  left: 0
  width: 100%
  height: 100%
  background: rgb(0, 0, 0, 0.4)
  display: flex
  align-items: center
  justify-content: center

.alert__box
  width: 400px
  background: white
  border-radius: 6px
  padding: 20px 30px
  box-shadow: 0 11px 10px -7px rgba(0,0,0,.2), 0 24px 38px 3px rgba(0,0,0,.14), 0 9px 46px 8px rgba(0,0,0,.12)

.alert__title
  color: rgb(26, 32, 44)
  font-weight: 600
  font-size: 22px
  margin-bottom: 10px

.alert__footer
  margin-top: 30px
  width: 100%
  display: flex
  justify-content: flex-end

.alert__spacer
  width: 20px
  height: 10px
</style>
