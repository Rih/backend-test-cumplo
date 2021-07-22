<template>
  <div style="padding: 50px">
    <div class="home__download">
      redirected..
      <router-link to="/dashboard">
      <MainBtn large style="height: 43px">
            Regresar
        </MainBtn>
        </router-link>
    </div>
  </div>
</template>

<script>
import MainBtn from '@/components/UI/MainBtn.vue'
import API from '@/js/API'

export default {
  data: () => ({
  }),
  async mounted() {
    const api = new API()
    api.createEntity({ name: 'inaturalist' })
    const response = await api.endpoints.inaturalist.get({pathParams: ['request']})
    if (response?.status !== 200){
      this.$router.push('/')
      return
    }
    window.location.href = response.result.url
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
