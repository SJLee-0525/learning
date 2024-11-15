import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LaterView from '@/views/LaterView.vue'
import SearchView from '@/views/SearchView.vue'
import VideoDetailView from '@/views/VideoDetailView.vue'
import ChannelView from '@/views/ChannelView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView,
    },
    {
      path: '/later',
      name: 'later',
      component: LaterView,
    },
    {
      path: '/detail/:videoId',
      name: 'detail',
      component: VideoDetailView,
    },
    {
      path: '/channel',
      name: 'channel',
      component: ChannelView,
    },
  ],
})

export default router
