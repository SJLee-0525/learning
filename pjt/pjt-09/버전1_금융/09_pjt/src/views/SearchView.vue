<template>
  <div class="container">
    <div class="my-3">
            <RouterLink :to="{ name: 'home' }" class="text-decoration-none text-dark">◀ 뒤로 가기</RouterLink>
        </div>
    <h1 class="my-3">비디오 검색</h1>
    <div>
      <form @submit.prevent="getVideoData" class="input-group mb-3">
        <input type="text" v-model="searchKeyword" class="form-control" placeholder="검색어를 입력하세요">
        <input class="btn btn-primary" type="submit" id="button-addon2"></input>
      </form>
    </div>
    <div v-if="store.searchVideos" class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
      <div v-for="searchVideo in store.searchVideos" :key="searchVideo.id.videoId" class="col">
        <div class='card h-100' @click="getVideoDetail(searchVideo.id.videoId)">
          <img :src="searchVideo.snippet.thumbnails.high.url" alt="#" class="card-img-top">
          <div class="card-body">
            <h5 class="card-title">{{ searchVideo.snippet.title }}</h5>
            <p class="card-text">{{ searchVideo.snippet.channelTitle }}</p>
          </div>
          <div class="card-footer">
            <small class="text-body-secondary">{{ searchVideo.snippet.publishTime.slice(0, 10) }}</small>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useVideoStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useVideoStore()
const router = useRouter()

const searchKeyword = ref(null)

const getVideoData = function () {
  axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/search',
    params: {
      key: store.API_KEY,
      part: 'snippet',
      type: 'video',
      maxResults: 30,
      q: searchKeyword.value,
    }
  })
    .then((response) => {
      console.log(response.data)
      store.searchVideos = response.data.items
      console.log(store.searchVideos)
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const getVideoDetail = function (videoId) {
    router.push({ name: 'detail', params: { videoId } });
  };

</script>

<style scoped>

</style>