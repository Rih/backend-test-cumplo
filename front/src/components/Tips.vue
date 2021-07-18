<template>
  <div>
    <div v-if="!showTip" class="tips__tip">
      <div class="tips__tip_header">
        <div style="font-weight: 600">Tip #1</div>
        <MainBtn @click="showTip = true" small outline class="tips__tip_btn">Ver</MainBtn>
      </div>
    </div>
    <div v-if="showTip" class="tips__tip-active">
      <div class="tips__tip-active_header">
        <div style="font-weight: 600">Tip #1</div>
        <MainBtn @click="showTip = false" icon>
          <Icon>close</Icon>
        </MainBtn>
      </div>
      <div
        class="tips__tip-activer_text"
      >Para consultar nombres en mayúscula debes agregar comillas dobles</div>
      <div style="font-size: 14px">
        Ej: SELECT id,
        <span style="font-size: 20px">"</span>coor_GPS
        <span style="font-size: 20px">",</span>
        nombre FROM
        <span style="font-size: 20px">"</span>BOSQUES
        <span style="font-size: 20px">"</span>
      </div>
    </div>
  </div>
</template>

<script>
import MainBtn from '@/components/UI/MainBtn.vue'
import Icon from '@/components/UI/Icon.vue'
import Vue from 'vue'

export default Vue.extend({
  data: () => ({
    showTip: false,
  }),
  components: {
    MainBtn,
    Icon,
  },
})
</script>

<style lang="sass" scoped>
.tips__tip
  background: whitesmoke
  width: 470px
  color: #666
  border-radius: 5px
  padding: 15px
  margin: 10px 0

.tips__tip_header
  display: flex
  align-items: center
  justify-content: space-between

.tips__tip_btn
  padding-left: 12px !important
  color: #777
  border: 1px solid #bbb

.tips__tip-active
  background: #9ae142
  width: 450px
  color: #fff
  border-radius: 5px
  padding: 15px
  margin: 10px 0

.tips__tip-active_header
  display: flex
  align-items: center
  justify-content: space-between

.tips__tip-activer_text
  fon-size: 15px
  margin: 10px 0
  margin-bottom: 5px
</style>
