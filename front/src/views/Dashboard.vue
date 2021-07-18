<template>
  <div class="dashboard__container">
    <div
      class="dashboard__sidemenu"
      :class="{ dashboard__sidemenu_shrink: globalUI.isSideMenuCollapsed }"
    >
      <div v-if="!globalUI.isSideMenuCollapsed" class="dashboard__close-icon">
        <MainBtn @click="onCollapse(true)" icon>
          <Icon>close</Icon>
        </MainBtn>
      </div>
      <div v-show="globalUI.isSideMenuCollapsed" class="dashboard__menu-icon">
        <MainBtn @click="onCollapse(false)" icon>
          <Icon>menu</Icon>
        </MainBtn>
      </div>

      <div class="dashboard__logo-box">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/INaturalist_text_logo.svg/320px-INaturalist_text_logo.svg.png"
          style="width: 70%"
        />
      </div>

      <div class="dashboard__v-spacer-10"></div>

      <div class="dashboard__avatar">
        <img :src="url" class="dashboard__avatar_img" />
        <div v-if="!globalUI.isSideMenuCollapsed" class="dashboard__avatar_box">
          <div class="dashboard__avatar_wrap">
            <div class="dashboard__avatar_name">{{ user.first_name }}</div>
          </div>
          <div class="dashboard__avatar_username">{{ user.email }}</div>
        </div>
      </div>

      <div class="dashboard__v-spacer-30"></div>

      <div v-for="(item, i) in menu" :key="i">
        <MenuBtn
          v-if="item.show"
          @click="onMenu(i, item.type)"
          :text="item.title"
          :icon="item.icon"
          :active="item.isActive"
          :shrink="globalUI.isSideMenuCollapsed"
        />
      </div>
    </div>
    <div
      class="dashboard__content"
      :class="{ dashboard__content_shrink: globalUI.isSideMenuCollapsed }"
    >
      <div class="dashboard__content_title">
        <div>{{ type }}</div>
        <MainBtn @click="onLogout" small outline>
          <Icon style="margin-right: 5px">logout</Icon>Salir
        </MainBtn>
      </div>
      <Home v-if="menu[0].isActive" />
    </div>
  </div>
</template>

<script>
import Home from '@/views/Home.vue'
import MenuBtn from '@/components/UI/MenuBtn.vue'
import Icon from '@/components/UI/Icon.vue'
import MainBtn from '@/components/UI/MainBtn.vue'
import { DEFAULT_AVATAR } from '@/js/constants'
import { mapState, mapActions } from 'vuex'


export default {
  data() {
    return {
      isTag1Active: true,
      type: 'Inicio',
      menu: [
        {
          title: 'Inicio',
          type: 'Inicio',
          icon: 'home',
          isActive: true,
          show: true,
        },
        {
          title: 'Estadistica',
          type: 'Estadistica',
          icon: 'home',
          isActive: false,
          show: false,
        },
      ],
    }
  },
  methods: {
    onMenu(i, type) {
      this.menu.forEach((item) => (item.isActive = false))
      this.menu[i].isActive = true
      this.type = type
    },
    onCollapse(val) {
      this.setGlobalUI({
        isSideMenuCollapsed: val,
        tableWidth: window.screen.width - (val ? 200 : 400),
      })
    },
    onLogout() {
      this.setUnauthenticated()
      this.$router.push('/')
    },
    ...mapActions(['setUnauthenticated', 'setGlobalUI']),
  },
  watch: {
    
  },
  computed: {
    url(){
      if (!this.user.profile){
        return DEFAULT_AVATAR
      }
      return this.user.profile
    },
    ...mapState(['globalUI', 'user']),
  },
  mounted() {
    const collapsed = this.globalUI.isSideMenuCollapsed
    this.setGlobalUI({
      tableWidth: window.screen.width - (collapsed ? 200 : 400),
    })

    this.menu[0].show = true
  },
  components: {
    Home,
    MenuBtn,
    Icon,
    MainBtn,
  },
}
</script>

<style lang="sass" scoped>
.dashboard__container
  position: fixed
  top: 0
  left: 0
  width: 100%
  height: 100%

.dashboard__sidemenu
  position: fixed
  width: 270px
  height: 100%
  border-right: 1px solid #eee
  background: #F4F5F7
  padding: 0 20px

.dashboard__sidemenu_shrink
  width: 80px !important

.dashboard__close-icon
  position: absolute
  top: 10px
  right: 10px
  color: #666

.dashboard__logo-box
  display: flex
  align-items: center
  padding: 15px 0
  font-size: 20px
  font-weight: 600
  color: #374151

.dashboard__logo-box_title
  margin-left: 10px

.dashboard__avatar
  display: flex
  alin-items: center

.dashboard__avatar_img
  height: 40px
  width: 40px
  border-radius: 50%
  object-fit: cover

.dashboard__avatar_box
  margin-left: 10px

.dashboard__avatar_name
  font-weight: 600
  color: #192031

.dashboard__avatar_username
  color: #828894

.dashboard__content
  margin-left: 270px

.dashboard__content_shrink
  margin-left: 80px

.dashboard__content_title
  padding: 20px 20px
  border-bottom: 1px solid #eee
  margin-bottom: 20px
  font-size: 20px
  font-weight: 600
  color: #161D2E
  display: flex
  justify-content: space-between

.dashboard__logout
  position: absolute
  bottom: 10px
  left: 20px
  padding: 10px

.dashboard__menu-icon
  margin-top: 15px
  margin-bottom: -5px
  color: #666

.dashboard__v-spacer-30
  height: 30px
  width: 100%

.dashboard__v-spacer-10
  height: 30px
  width: 100%

.dashboard__avatar_wrap
  display: flex
  align-items: center
</style>
