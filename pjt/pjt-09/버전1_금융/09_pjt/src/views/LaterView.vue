<template>
    <div class="container">
        <div class="my-3">
            <RouterLink :to="{ name: 'home' }" class="text-decoration-none text-dark">◀ 뒤로 가기</RouterLink>
        </div>
        <h1 class="my-3">나중에 볼 동영상</h1>
        <div v-if="store.savedVideos.length > 0" class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
            <div v-for="saveVideo in store.savedVideos" :key="saveVideo.id" class="col">
            <div class='card h-100' @click="getVideoDetail(saveVideo.id)">
                <img :src="saveVideo.snippet.thumbnails.high.url" alt="#" class="card-img-top">
                <div class="card-body">
                <h5 class="card-title">{{ saveVideo.snippet.title }}</h5>
                <p class="card-text">{{ saveVideo.channelTitle }}</p>
                </div>
                <div class="card-footer">
                <small class="text-body-secondary">{{ saveVideo.snippet.publishedAt.slice(0, 10) }}</small>
                </div>
            </div>
            </div>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center">
            <img :src="oops" alt="">
            <h3 class="m-3 fw-bold">등록된 비디오 없음</h3>
        </div>
    </div>
  </template>
  
  <script setup>
  import { useVideoStore } from '@/stores/counter';
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import oops from "@/assets/oops.png"
  
  const store = useVideoStore()
  const router = useRouter()
  
  const getVideoDetail = function (videoId) {
    router.push({ name: 'detail', params: { videoId } });
  };


  </script>
  
  <style scoped>
  
  </style>