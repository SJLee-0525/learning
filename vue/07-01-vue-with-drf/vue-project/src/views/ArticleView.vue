<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">CREATE</RouterLink>
    <hr>
    <ArticleList/>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import ArticleList from '@/components/ArticleList.vue';

const store = useCounterStore()

onMounted(() => {
  // mount 되기 전에 store에 있는 전체 게시글 요청 함수를 호출 (화면에 그려지기 전에 미리)
  store.getArticles()
})
</script>

<style>

</style>
