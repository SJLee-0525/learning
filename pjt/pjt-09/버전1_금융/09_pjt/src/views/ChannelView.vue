<template>
    <div class="container">
        <div class="my-3">
            <RouterLink :to="{ name: 'home' }" class="text-decoration-none text-dark">◀ 뒤로 가기</RouterLink>
        </div>
        <h1 class="my-3">저장한 채널</h1>
        <div v-if="store.savedChannels.length > 0">
            <ul class="list-group list-group-flush" v-for="savedChannel in store.savedChannels" :key="savedChannel">
                <div>
                    <li class="list-group-item my-1">{{ savedChannel }}</li>
                </div>
            </ul>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center">
            <img :src="oops" alt="">
            <h3 class="m-3 fw-bold">등록된 채널 없음</h3>
        </div>
    </div>
  </template>
  
  <script setup>
  import { useVideoStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router';
  import oops from "@/assets/oops.png"
  
  const store = useVideoStore()

  </script>
  
  <style scoped>
  
  </style>