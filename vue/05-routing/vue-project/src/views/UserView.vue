<template>
  <div>
    <h1>UserView</h1>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
    <hr>

    <h2>{{ $route.params }}</h2>
    <h2>{{ userId }}번 User 페이지</h2>
    <button @click="goHomePush">홈으로(push)</button>
    <button @click="goHomeReplace">홈으로(replace)</button>
    <button @click="routeUpdate">100번 유저 페이지</button>
    <hr>

    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, RouterLink, RouterView, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHomePush = function () {
  router.push({ name: 'home' })
}
const goHomeReplace = function () {
  router.replace({ name: 'home' })
}

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const routeUpdate = function () {
  router.push({ name: 'user', params: { id: 100 } })
}
onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>

<style lang="scss" scoped>
</style>