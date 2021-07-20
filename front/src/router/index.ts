import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import Redirect from '../views/Redirect.vue'
import { guard } from '@/guards'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'login',
    component: Login,
    beforeEnter: (to, from, next) => guard(to, from, next),
  },
  {
    path: '/signup',
    name: 'signup',
    component: Register,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    //beforeEnter: (to, from, next) => guard(to, from, next)
  },
  {
    path: '/redirect',
    name: 'redirect',
    component: Redirect,
    //beforeEnter: (to, from, next) => guard(to, from, next)
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    // beforeEnter: (to, from, next) => guard(to, from, next)
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
