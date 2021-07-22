<template>
  <div>
    <Card>
      <div style="display: flex; align-items: center; flex-direction: column; padding: 10px">
        <Tips :tips="tips" :title="titleTip" />
        <div class="home__obs-container">
          <div class v-for="(photo, i) in obs.photos" :key="i" style="max-height: 300px">
            <img class="home__obs-img" :src="photo.medium_url" @click="onSelectedImage(photo)" />
          </div>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
import Card from '@/components/UI/Card.vue'
import Tips from '@/components/Tips.vue'
import { mapState } from 'vuex'
import dialog from '@/js/dialog'
import { mapActions } from 'vuex'

export default {
  data: () => ({
    titleTip: 'Metadatos',
  }),
  computed: {
    tips() {
      if (this.obs) {
        return [
          `Ubicación: (${this.obs.latitude}, ${this.obs.longitude})`,
          `Lugar aproximado: ${this.obs?.place_guess || 'No disponible'}`,
          `Descripción: ${this.obs?.description || 'No disponible'}`,
          `Ubicación: (${this.obs.latitude}, ${this.obs.longitude})`,
          `Nombre: ${this.obs.taxon.name}`,
          `Nombre Común: ${this.obs.taxon.common_name.name}`,
          `Especies: ${this.obs.species_guess}`,
          `author: ${this.obs.user.login}`,
          `Licencia de uso: ${this.obs.photos?.[0].license_name}`,
          `Creditos: ${this.obs.photos?.[0].attribution}`,
          ]
      }
      return []
    },
    imgDefault() {
      return require('@/assets/logo.png')
    },
    ...mapState(['tabs', 'obs']),
  },
  methods: {
    async onSelectedImage(photo) {
      console.log({ obs: this.obs })
      debugger //eslint-disable-line
      const { ok } = await dialog.open('setAlert', {
        msg: 'Desea agregar como avatar?',
        title: 'Agregar Avatar',
        isActive: true,
      })
      if (ok) {
        this.assignAvatar(photo)
      }
    },
    ...mapActions(['assignAvatar', 'setAlert']),
  },
  components: {
    Tips,
    Card,
  },
}
</script>


<style lang="sass" scoped>
.home__obs-container
  display: flex
  flex-direction: row
  align-items: flex-start
  justify-content: center
.home__obs-img
  padding: 10px 10px
  border-radius: 10px
  margin: 10px
  background: whitesmoke
  text-align: center
  font-size: 14px
  height: 300px
.home__obs-img:hover
  background: lightgray
  cursor: pointer
.home__download
  margin-top: 20px
  display: flex
  justify-content: flex-end
</style>
