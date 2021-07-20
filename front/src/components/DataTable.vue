<template>
  <section>
    <div style="height: 20px; width: 20px"></div>
    <b-table
      ref="table"
      class="has-background-color-dark"
      :busy.sync="isBusy"
      :data="data"
      :striped="false"
      :current-page.sync="data.currentPage"
      :pagination-simple="isPaginationSimple"
      :pagination-position="paginationPosition"
      :pagination-rounded="isPaginationRounded"
      :loading="isLoading"
    >
      <template v-for="(column, columnIdx) in columns">
        <b-table-column :key="column.id" v-bind="column" style="border: 0">
          <template
            v-if="column.searchable && !column.numeric"
            slot="searchable"
            slot-scope="props"
          >
            <template v-if="columnIdx == 0">{{ catchFilterRef(props.filters) }}</template>
            <b-input
              v-model="props.filters[props.column.field]"
              placeholder="Buscar..."
              icon="magnify"
            />
          </template>
          <template v-slot="props">
            <div v-if="props.colindex == 0" class="datatable__datatype-holder">
              <div class="datatable__datatype">{{ props.row.uri }}</div>
            </div>
            <div v-if="props.colindex == 1" class="datatable__datatype-holder">
              <div class="datatable__datatype">NE: {{ formatGeoPosition(props.row.bbox.ne) }}</div>
              <div class="datatable__datatype">SW: {{ formatGeoPosition(props.row.bbox.sw) }}</div>
            </div>

            <div v-if="props.colindex == 2" class="datatable__datatype-holder">
              <div v-for="(photo, i) in props.row.results[0].photos" :key="i" class="datatable__datatype"> 
                <img :src="photo.thumb_url" style="height: 60px" />
                <enlargeable-image :src="photo.thumb_url" :src_large="photo.large_url">
                  <span>Ver</span>
                </enlargeable-image>
              </div>
            </div>
          </template>
        </b-table-column>
      </template>
      
    </b-table>
  </section>
</template>

<script>
import API from '@/js/API'
import { ADMIN_TABLES, PER_PAGE } from '@/js/constants'
import { mapActions } from 'vuex'

export default {
  props: {
    alias: Boolean,
    data: Array,
    value: Object,
  },
  data() {
    return {
      items: [],
      totalItems: 0,
      isBusy: false,
      isEmpty: false,
      isLoading: false,
      isPaginated: true,
      isPaginationSimple: false,
      isPaginationRounded: true,
      paginationPosition: 'bottom',
      currentPage: 1,
      perPage: PER_PAGE,
      columns: ADMIN_TABLES,
      filters: { uri: '', bbox: '' },
    }
  },
  methods: {
    formatGeoPosition({lat, lng}){
      return `(${lat.toFixed(4)}, ${lng.toFixed(4)})`;
    },
    onPrev() {
      this.$emit('clickedPrev', this.currentPage - 1)
    },
    onNext() {
      this.$emit('clickedNext', this.currentPage + 1)
    },
    catchFilterRef(filters) {
      this.filters = filters
    },
    ...mapActions(['getStatistics']),
  },
  watch: {},
}
</script>


<style lang="sass" scoped>
.datatable__datatype
  display: block
  padding: 3px 10px
  border-radius: 5px
  background: whitesmoke
  display: inline-block
  text-align: center
  font-size: 14px

.datatable__datatype_color
  display: block
  padding: 3px 10px
  border-radius: 5px
  background: #8CD163
  display: inline-block
  text-align: center
  font-size: 14px
  color: white

.datatable__datatype-holder
  text-transform: capitalize
</style>