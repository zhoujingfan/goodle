import Vue from 'vue'
import Router from 'vue-router'

import NotFound from '@/components/404'
import Home from '@/components/Home'
import SearchResult from '@/components/SearchResult'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Home',
      redirect: {
        path: '/'
      }
    },
    {
      path: '/HomePage',
      redirect: {
        path: '/'
      }
    },
    {
      path: '/HomeLogo',
      redirect: {
        path: '/'
      }
    },
    {
      path: '/goodle',
      redirect: {
        path: '/'
      }
    },
    {
      path: '/searchResult',
      name: 'SearchResult',
      component: SearchResult
    },
    {
      path: '/helloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/404',
      name: 'NotFoundLink',
      component: NotFound
    },
    {
      path: '*',
      redirect: {
        path: '/404'
      }
    }
  ]
})
