<template>
  <div class="login__container">
    <div class="login__holder">
      <div class="login__title-box">
        <img src="@/assets/logo.png" style="width: 60px" />
        <div class="login__title">Cumplo</div>
      </div>

      <div v-if="login.alert && login.btn" class="login__alert-1">
        <div style="max-width: 250px">{{ login.msg }}</div>
        <MainBtn @click="backToLogin" small outline round>Iniciar sesión</MainBtn>
      </div>

      <div v-if="login.alert && !login.btn" class="login__alert-2">{{ login.msg }}</div>

      <div v-if="login.error" class="login__error">{{ login.msg }}</div>

      <SignIn />

    </div>
  </div>
</template>

<script>
import SignIn from '@/components/login/SignIn.vue'

import MainBtn from '@/components/UI/MainBtn.vue'

import { SIGN_IN, FORGOT, RECOVERY } from '@/js/constants'
import { mapState } from 'vuex'

export default {
  data: () => ({
    SIGN_IN,
    FORGOT,
    RECOVERY,
    type: SIGN_IN,
  }),
  methods: {
    backToLogin() {
      this.type = SIGN_IN
      this.$router.push('/')
    },
  },
  computed: {
    ...mapState(['login']),
  },
  components: {
    SignIn,
    MainBtn,
  },
}
</script>

<style lang="sass" scoped>
.login__container
  background: #eee
  height: 100%
  width: 100%
  display: flex
  align-items: center
  justify-content: center
  flex-wrap: wrap
  padding: 30px

.login__holder
  width: 380px

.login__title-box
  margin-bottom: 30px
  display: flex
  align-items: center
  justify-content: center

.login__title
  margin-left: 5px
  color: #444
  font-size: 20px
  font-weight: 500
  color: #555

.login__footer-a
  cursor: pointer
  margin-top: 30px
  font-size: 14px
  color: #777
  text-align: center

.login__footer-b
  cursor: pointer
  margin-top: 30px
  font-size: 14px
  color: #777
  text-align: center
  display: flex
  align-items: center
  justify-content: center

.login__alert-1
  padding: 10px
  background: white
  margin-bottom: 20px
  border-radius: 3px
  border-left: 4px solid #4299e1
  color: #555
  display: flex
  justify-content: space-between
  align-items: center
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.01), 0 2px 2px 0 rgba(0, 0, 0, 0.05), 0 1px 5px 0 rgba(0, 0, 0, 0.1)

.login__alert-2
  padding: 10px
  background: white
  margin-bottom: 20px
  border-radius: 3px
  border-left: 4px solid #4299e1
  color: #555
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.01), 0 2px 2px 0 rgba(0, 0, 0, 0.05), 0 1px 5px 0 rgba(0, 0, 0, 0.1)

.login__error
  padding: 10px
  background: #FFEBE8
  margin-bottom: 20px
  border-radius: 3px
  border: 1.5px solid #E89A92
  color: #555
  boxx-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.01), 0 2px 2px 0 rgba(0, 0, 0, 0.05), 0 1px 5px 0 rgba(0, 0, 0, 0.1)
</style>
