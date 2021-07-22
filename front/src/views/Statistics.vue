<template>
  <div class="stepper__container">
    <div class="stepper__header">
      <div class="stepper__box-a">
        <div class="stepper__bubble_text stepper__bubble_text_active">Estadistica de uso</div>
      </div>

      <div class="stepper__header-line"></div>
      <div class="stepper__header-right"></div>
    </div>

    <div class="stepper__box-b">
      <DataTable :data="statistics.data" v-model="model" />

      <div class="stepper__footer">
        <Paginator
          :pages="pages"
          :value="statistics.current"
          @input="onPaginate"
          :start="start"
          :end="end"
          :hasPrev="statistics.hasPrev"
          :hasNext="statistics.hasNext"
          :total="statistics.total"
        />
      </div>
    </div>
  </div>
</template>

<script>
import DataTable from '@/components/DataTable.vue'
import Paginator from '@/components/UI/Paginator.vue'
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      model: {},
      perPage: 10,
    }
  },
  methods: {
    isInt(n) {
      const x = parseFloat(n)
      return isNaN(n) ? !1 : (0 | x) === x
    },
    onPaginate(page) {
      this.getStatistics(page)
    },
    ...mapActions(['getStatistics']),
  },
  created() {
    this.getStatistics(1)
  },
  computed: {
    start() {
      return (this.statistics.current - 1) * this.statistics.perPage + 1 || 0
    },
    end() {
      return this.statistics.current * this.statistics.perPage || 0
    },
    pages() {
      let pages = this.statistics.total / this.statistics.perPage
      if (pages < 1) pages = 1
      return Math.ceil(pages)
    },
    ...mapState(['checkedTables', 'statistics']),
  },
  components: {
    DataTable,
    Paginator,
  },
}
</script>

<style lang="sass" scoped>
.stepper__container
  backgroundd: #F4F5F7
  border-radius: 5px
  padding: 20px
  border: 1px solid #eee
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)

.stepper__header
  padding: 20px 0
  border-bottom: 1px solid #eee
  display: flex
  align-items: center

.stepper__line
  width: 200px
  height: 1px
  border-top: 1px solid #ccc

.stepper__box-b
  padding-left: 50px
  padding-right: 50px

.stepper__title
  margin-top: 20px
  font-size: 18px

.stepper__bold
  color: rgb(26, 32, 44)
  font-weight: 600

.stepper__footer
  margin-top: 0px
  width: 100%
  display: flex
  justify-content: center

.stepper__box-a
  display: flex
  align-items: center
  margin-right: 10px
  margin-left: 10px

.stepper__bubble_num
  font-weight: 600
  width: 45px
  height: 45px
  border-radius: 50%
  background: #fff
  border: 1px solid #ccc
  color: #555
  display: flex
  align-items: center
  justify-content: center

.stepper__bubble_text
  font-size: 20px
  margin-left: 10px
  font-weight: 400
  color: #444

.stepper__bubble_num_active
  background: #4299e1
  color: white
  border: 0

.stepper__bubble_text_active
  font-weight: 600

.stepper__header-right
  margin-left: 50px
  color: #555
  width: 200px
  text-align: center

.stepper__header-line
  border-left: 1.5px solid #eee
  height: 50px
  width: 2px
  margin-left: 100px
</style>
