<template>
  <div class="signin__container">
    <MainInput v-model="firstname" large label="Nombre" placeholder="John" />
    <MainInput v-model="lastname" large label="Apellido" placeholder="Perez" />
    <MainInput
      v-model="username"
      large
      type="email"
      label="Nombre de Usuario (email)"
      placeholder="ejemplo@gmail.com"
    />

    <MainInput v-model="password" large type="password" label="Contraseña" placeholder="*******" />

    <Recaptcha @captchaOk="onSubmit" :disable="!isValid" text="Crear cuenta" />
    <div style="text-align: center; margin-top: 10px">
      <router-link to="/">Ya tengo una cuenta</router-link>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import { mapActions } from 'vuex'
import MainInput from '@/components/UI/MainInput.vue'
import Recaptcha from '@/components/Recaptcha.vue'
import API from '@/js/API.js'
import { APP_BASE_URL } from '@/js/constants'

export default Vue.extend({
  props: {
    value: String,
  },
  data: () => ({
    firstname: '',
    lastname: '',
    username: '',
    password: '',
  }),
  computed: {
    isValid() {
      return (
        this.firstname.length > 3 &&
        this.lastname.length > 3 &&
        this.username.length > 3 &&
        this.password.length > 7
      )
    },
  },
  methods: {
    onSubmit(recaptchaToken) {
      this.setRequesting()
      const api = new API({ url: `${APP_BASE_URL}/account`, toast: false })
      api.createEntity({ name: 'signup' })
      const payload = {
        firstname: this.firstname,
        lastname: this.lastname,
        username: this.username,
        password: this.password,
        recaptchaToken,
      }
      api.endpoints.signup.post(payload).then(async ({ error, result }) => {
        if (!error) {
          this.$router.push('dashboard')
        }
        if (error) {
          this.setSignup({
            error: true,
            msg: Object.values(error.response.data).join(';'),
          })
        }
      })
    },
    ...mapActions(['setRequesting', 'setSignup', 'resetSignup']),
  },
  mounted() {
    this.resetSignup()
  },
  components: {
    MainInput,
    Recaptcha,
  },
})
</script>

<style lang="sass" scoped>
.signin__container
  background: white
  padding: 35px 25px
  border-radius: 5px
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12)
</style>
