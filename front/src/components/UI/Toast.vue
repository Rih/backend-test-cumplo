<template>
  <div v-if="toast.isActive" class="toast__container">
    <div
      :class="{
        toastui__box_success: toast.type === SUCCESS,
        toastui__box_error: toast.type === ERROR,
      }"
    >
      <div class="toast__text_box">
        <i v-if="toast.type === SUCCESS" class="fas fa-check toast__icon"></i>
        <i v-if="toast.type === ERROR" class="fas fa-exclamation-circle toast__icon"></i>
        <div>{{ toast.msg }}</div>
      </div>
      <MainBtn v-if="toast.type === SUCCESS" @click="closeToast" plain dark
        >CERRAR</MainBtn
      >
    </div>
  </div>
</template>

<script>
// Vue
import MainBtn from '@/components/UI/MainBtn.vue'
import { SUCCESS, ERROR } from '@/js/constants'
import { mapState, mapActions } from 'vuex'

export default {
  data: () => ({
    SUCCESS,
    ERROR,
    timer: null,
  }),
  watch: {
    toast(data) {
      if (data.isActive) {
        clearTimeout(this.timer)
        this.timer = setTimeout(() => {
          this.toast.isActive = false
        }, 4000)
      }
    },
  },
  computed: {
    ...mapState(['toast']),
  },
  methods: {
    closeToast() {
      this.toast.isActive = false
    },
    ...mapActions(['setToast']),
  },
  components: {
    MainBtn,
  },
}
</script>
<style lang="sass" scoped>
.toast__container
  z-index: 999
  position: fixed
  bottom: 20px
  left: 0px
  width: 100%
  display: flex
  justify-content: center

.toastui__box_success
  background: #333
  color: #eee
  width: 95%
  max-width: 370px
  padding: 12px 15px
  border-radius: 4px
  display: flex
  align-items: center
  justify-content: space-between
  box-shadow: 0 -2px 5px -2px rgba(115,115,115,0.75), 0 2px 5px -5px rgba(115,115,115,0.75), 2px 0 5px -2px rgba(115,115,115,0.75)

.toastui__box_error
  background: #FF5353
  color: whitesmoke
  width: 95%
  max-width: 370px
  padding: 12px 15px
  border-radius: 4px
  display: flex
  align-items: center
  justify-content: space-between
  box-shadow: 0 -2px 5px -2px rgba(115,115,115,0.75), 0 2px 5px -5px rgba(115,115,115,0.75), 2px 0 5px -2px rgba(115,115,115,0.75)

.toast__text_box
  display: flex
  align-items: center

.toast__icon
  margin-right: 10px
  font-size: 20px
</style>