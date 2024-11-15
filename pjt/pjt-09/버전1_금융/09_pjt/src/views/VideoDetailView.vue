<template>
    <div class="container">
        <div class="my-3">
            <RouterLink :to="{ name: 'search' }" class="text-decoration-none text-dark">◀ 뒤로 가기</RouterLink>
        </div>
        <div v-if="videoDetail">
            <h1 class="my-3">{{ videoDetail.snippet.title }}</h1>
            <p>업로드 날짜: {{ videoDetail.snippet.publishedAt.slice(0, 10) }}</p>
            <iframe
            :src="`https://www.youtube.com/embed/${videoId}`"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            width="100%"
            height="400"
            ></iframe>
            <p>{{ videoDetail.snippet.description }}</p>
            <!-- <p>Channel: {{ videoDetail.snippet.channelTitle }}</p> -->
            <div class="d-grid d-md-block gap-2"> 
                <p>{{ isSavedVideo }}</p>
                <button @click.prevent="store.saveVideo(videoDetail)" class="btn btn-primary m-1" type="button">
                    SAVE VIDEO
                    <!-- {{ isSavedVideo ? 'DELETE VIDEO' : 'SAVE VIDEO' }} -->
                </button>
                <button @click="store.saveChannel(videoDetail.snippet.channelTitle)" class="btn btn-success m-1" type="button">SAVE CHANNEL</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useVideoStore } from '@/stores/counter';
import { onMounted, ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const store = useVideoStore()
const route = useRoute();

const videoId = route.params.videoId;
const videoDetail = ref(null);

const isSavedVideo = ref(null)
const isAddedChannel = ref(null)

onMounted(() => {
axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/videos',
    params: {
    key: store.API_KEY,
    part: 'snippet',
    id: videoId,
    }
})
    .then((response) => {
    videoDetail.value = response.data.items[0]
    console.log(videoDetail)
    isSavedVideo.value = computed(() => {
        const index = store.savedVideos.findIndex((element) => element.id === videoId)
        if (index === -1) {
            return false
        } else {
            return true
        }
    })
    })
    .catch((error) => {
    console.log(error);
    })
});



</script>
  