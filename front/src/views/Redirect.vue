<template>
  <div style="padding: 50px">
    <div class="home__download">
      redirected..
      <router-link to="/dashboard">
        <MainBtn large style="height: 43px">Regresar</MainBtn>
      </router-link>
    </div>
  </div>
</template>
<script>
import API from '@/js/API'
import { SUCCESS, ERROR } from '@/js/constants'
import MainBtn from '@/components/UI/MainBtn.vue'
import { mapActions } from 'vuex'

export default {
  data: () => ({
  }),
  methods: {
    ...mapActions(['setToast']),
  },
  async mounted() {
    const code = this.$route.query.code
    const api = new API()
    api.createEntity({ name: 'inaturalist' })
    const response = await api.endpoints.inaturalist.get({
      pathParams: ['token'],
      queryParams: { code },
    })
    if (response?.result?.code === code && response?.result?.tkn?.length){
      this.$router.push('/dashboard')
      this.setToast({msg: 'Actualización exitosa', 'type': SUCCESS})
      return
    }
    this.setToast({msg: 'Error solicitando llaves', 'type': ERROR})

  },
  components: {
    MainBtn,
  },
}
</script>


<style lang="sass" scoped>
.home__download
  margin-top: 20px
  display: flex
  justify-content: flex-end
</style>
