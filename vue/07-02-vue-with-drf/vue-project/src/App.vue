<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> | 
      <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> | 
      <RouterLink :to="{ name: 'LogInView' }">Login</RouterLink> | 
      <a @click.prevent="logOut">Logout</a>
    </nav>
  </header>
  <div>
    <h3 v-if="store.isLogin">안녕하세요 {{ store.loginusername }}님!</h3>
    <h3 v-else>로그아웃 됨</h3>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

const logOut = function () {
  store.logOut()
}
</script>

<style scoped>
</style>
