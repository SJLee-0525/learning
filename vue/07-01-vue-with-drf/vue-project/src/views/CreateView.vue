<template>
  <div>
    <h1>CREATE</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" id=title v-model.trim="title">
      </div>
      <div>
        <div>
          <label for="content">내용 : </label>
          <textarea id="content" v-model.trim="content"></textarea>
        </div>
        <input type="submit">
      </div>
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const store = useCounterStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

// DRF로 게시글 생성 요청을 보내는 함수
const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
  })
    .then((response) => {
      console.log(response.data)
      console.log('게시글 작성 성공')
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
  }
</script>

<style>

</style>
