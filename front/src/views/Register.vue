<template>
  <div class="signup__container">
    <div class="signup__holder">
      <div class="signup__title-box">
        <img src="@/assets/logo.png" style="width: 60px" />
        <div class="signup__title">INaturalist</div>
      </div>

      <div v-if="signup.alert && signup.btn" class="signup__alert-1">
        <div style="max-width: 250px">{{ signup.msg }}</div>
        <MainBtn @click="backTosignup" small outline round>Iniciar sesión</MainBtn>
      </div>

      <div v-if="signup.alert && !signup.btn" class="signup__alert-2">{{ signup.msg }}</div>

      <div v-if="signup.error" class="signup__error">{{ signup.msg }}</div>

      <SignUp />

    </div>
  </div>
</template>

<script>
import SignUp from '@/components/login/SignUp.vue'

import MainBtn from '@/components/UI/MainBtn.vue'

import { mapState } from 'vuex'

export default {
  data: () => ({
  }),
  methods: {
    backTosignup() {
      this.$router.push('/')
    },
  },
  computed: {
    ...mapState(['signup']),
  },
  components: {
    SignUp,
    MainBtn,
  },
}
</script>

<style lang="sass" scoped>
.signup__container
  background: #eee
  height: 100%
  width: 100%
  display: flex
  align-items: center
  justify-content: center
  flex-wrap: wrap
  padding: 30px

.signup__holder
  width: 380px

.signup__title-box
  margin-bottom: 30px
  display: flex
  align-items: center
  justify-content: center

.signup__title
  margin-left: 5px
  color: #444
  font-size: 20px
  font-weight: 500
  color: #555

.signup__footer-a
  cursor: pointer
  margin-top: 30px
  font-size: 14px
  color: #777
  text-align: center

.signup__footer-b
  cursor: pointer
  margin-top: 30px
  font-size: 14px
  color: #777
  text-align: center
  display: flex
  align-items: center
  justify-content: center

.signup__alert-1
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

.signup__alert-2
  padding: 10px
  background: white
  margin-bottom: 20px
  border-radius: 3px
  border-left: 4px solid #4299e1
  color: #555
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.01), 0 2px 2px 0 rgba(0, 0, 0, 0.05), 0 1px 5px 0 rgba(0, 0, 0, 0.1)

.signup__error
  padding: 10px
  background: #FFEBE8
  margin-bottom: 20px
  border-radius: 3px
  border: 1.5px solid #E89A92
  color: #555
  boxx-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.01), 0 2px 2px 0 rgba(0, 0, 0, 0.05), 0 1px 5px 0 rgba(0, 0, 0, 0.1)
</style>
