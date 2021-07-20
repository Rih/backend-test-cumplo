<template>
  <div class="card__container">
    <slot />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  data: () => ({
    show: false,
    model: ''
  }),
});
</script>

<style lang="sass" scoped>
.card__container
  border-radius: 8px
  padding: 20px
  padding-bottom: 30px
  box-shadow: 0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)
  @media(max-width: 425px)
    width: 100%
    padding: 0
</style>
