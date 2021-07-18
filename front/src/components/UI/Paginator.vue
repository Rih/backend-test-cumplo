<template>
  <div class="paginator__container">
    <div class="paginator__left">
      Mostrando {{ start }} a {{ end }} de {{ total }} registros
    </div>

    <div class="paginator__pages">
      <div class="paginator__prev">Previo</div>
      <div
        v-for="(item, i) in model"
        :key="i"
        @click="select(i)"
        class="paginator__page"
        :class="{ paginator__page_active: item.isActive }"
      >
        {{ item.n }}
      </div>
      <div class="paginator__next">Siguiente</div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  props: {
    pages: Number,
    value: Number,
    total: Number,
    start: Number,
    end: Number
  },
  computed: {
    model() {
      const data = []

      for (let i = 0; i < this.pages; i++) {
        data.push({
          n: i + 1,
          isActive: false
        })
      }
      
      if (data.length === 0) return []
      data[this.value].isActive = true
      return data
    }
  },
  methods: {
    select(i) {
      this.model.forEach(el => {
        el.isActive = false
      })
      this.model[i].isActive = true
      this.$emit('input', i)
    }
  }
});
</script>

<style lang="sass" scoped>
.paginator__container
  margin-top: 10px
  display: flex
  justify-content: space-between
  align-items: center

.paginator__left
  color: #666
  font-size: 14.5px

.paginator__pages
  font-size: 14px

.paginator__prev
  display: inline-block
  color: rgb(114, 119, 122, 0.5)
  margin-right: 10px

.paginator__page_active
  background: #4299e1 !important
  color: white !important
  border-radius: 50%

.paginator__page
  user-select: none
  margin-right: 5px
  display: inline-block
  padding: 5px 15px
  border-radius: 3px
  background: #ffffff
  color: #777
  border: 1px solid #eee
  cursor: pointer
  border-radius: 50%
  height: 38px
  width: 38px

.paginator__next
  display: inline-block
  color: rgb(114, 119, 122)
  margin-left: 10px
</style>
