<template>
  <div class="signin__container">
    <MainInput
      v-model="username"
      large
      label="Nombre de usuario o email"
      placeholder="ejemplo@gmail.com"
    />

    <MainInput
      v-model="password"
      large
      type="password"
      label="Contraseña"
      placeholder="*******"
    />

    <Recaptcha
      @captchaOk="onSubmit"
      :disable="!isValid"
      text="Iniciar sesión"
    />
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
    username: '',
    password: '',
  }),
  computed: {
    isValid() {
      return this.username.length > 3 && this.password.length > 7
    },
  },
  methods: {
    onSubmit(recaptchaToken) {
      this.setRequesting()
      const api = new API({ url: `${APP_BASE_URL}/api`, toast: false })
      api.createEntity({ name: 'token' })
      const payload = {
        username: this.username,
        password: this.password,
        recaptchaToken,
      }
      api.endpoints.token.create(payload).then(async ({ error, result }) => {
        if (!error) {
          this.$router.push('dashboard')
        }

        if (error) {
          this.setLogin({
            error: true,
            msg: 'Usuario o contraseña incorrecto',
          })
        }
      })
    },
    ...mapActions([
      'setRequesting',
      'setLogin',
      'resetLogin',
    ]),
  },
  mounted() {
    this.resetLogin()
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
