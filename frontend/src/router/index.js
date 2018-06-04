import Vue from 'vue'
import Router from 'vue-router'
import InterfaceBoard from '../components/InterfaceBoard'
import Landing from '../Landing'
import Dashboard from '../components/Dashboard'
import Settings from '../components/Settings'
import Success from '../components/Success'

Vue.use(Router)

let id = localStorage.userId;

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Landing',
      component: Landing
    },
    {
      path: '/id:id',
      name: 'InterfaceBoard',
      component: InterfaceBoard,
      children: [
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: Dashboard
        },
        {
          path: 'settings',
          name: 'Settings',
          component: Settings
        }
      ]
    },
    {
      path: '/access_token=:token',
      name: 'VkAuth',
      component: Success
    }
  ]
})
