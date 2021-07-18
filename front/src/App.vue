<template>
  <div id="app" style="">
    <Toast />
    <Loader />
    <Alert />
    <router-view style="overflow-y: scroll; height: 100%; min-height: 100vh" />
  </div>
</template>

<script>
import Vue from 'vue'
import Loader from '@/components/UI/Loader.vue'
import Toast from '@/components/UI/Toast.vue'
import Alert from '@/components/UI/Alert.vue'
import { mapState, mapActions } from 'vuex'
import interceptor from '@/js/Interceptor.js'
import axiosInstance from '@/js/AxiosWrapper.js'

import axios from 'axios'

export default Vue.extend({
  name: 'App',

  data: () => ({}),
  methods: {
    ...mapActions([]),
  },
  computed: {
    ...mapState(['dialog']),
  },
  mounted() {
    interceptor.start()
    interceptor.verifyToken()
  },
  components: {
    Loader,
    Toast,
    Alert,
  },
})
</script>


