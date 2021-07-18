<template>
  <vue-recaptcha
    :sitekey="siteKey"
    ref="recaptcha"
    @verify="onCaptchaVerified"
    @expired="onCaptchaExpired"
    badge="inline"
    :loadRecaptchaScript="true"
    class="recaptcha__holder"
  >
    <button
      :class="{
        recaptcha__normal: !disable,
        recaptcha__disable: disable,
      }"
    >
      {{ text }}
    </button>
  </vue-recaptcha>
</template>
 
<script>
// Libs
import VueRecaptcha from 'vue-recaptcha'
import { RECAPTCHA_KEY } from '@/js/constants'
export default {
  props: ['text', 'disable'],
  data() {
    return {
      siteKey: RECAPTCHA_KEY,
    }
  },
  methods: {
    openPage(page) {
      this.setLoginUI({
        nav: page,
      })
    },
    onCaptchaVerified(recaptchaToken) {
      if (this.disable) return
      this.$refs.recaptcha.reset()
      this.$emit('captchaOk', recaptchaToken)
    },
    onCaptchaExpired: function () {
      if (this.disable) return
      this.$refs.recaptcha.reset()
    },
  },
  components: {
    VueRecaptcha,
  },
}
</script>

<style lang="sass" scoped>
.recaptcha__holder
  width: 100%
  overflow: hidden
  display: flex
  flex-wrap: wrap
  align-items: center
  justify-content: space-around
  margin-top: 20px

.recaptcha__normal
  text-transform: uppercase
  margin-top: 20px
  display: block
  background: #4299e1
  font-size: 14px
  color: white
  font-weight: 500
  cursor: pointer
  padding: 10px 20px
  text-align: center
  border-radius: 2px
  width: 100%

.recaptcha__disable
  text-transform: uppercase
  margin-top: 20px
  display: block
  background: #e2e2e2
  font-size: 14px
  color: #999
  font-weight: 500
  cursor: pointer
  padding: 10px 20px
  text-align: center
  border-radius: 2px
  width: 100%
</style>