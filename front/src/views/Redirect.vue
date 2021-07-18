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
import { mapState } from 'vuex'
import MainBtn from '@/components/UI/MainBtn.vue'
import { mapActions } from 'vuex'

export default {
  data: () => ({
    preview: {
      data: [],
      headers: [],
    },
  }),
  computed: {
    ...mapState([]),
  },
  methods: {
    ...mapActions(['updateAuthCode']),
  },
  mounted() {
    this.updateAuthCode(this.$route.query.code)
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
