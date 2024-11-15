<template>
  <AppNavBar />

  <RouterView></RouterView>
</template>

<script setup>
import { RouterView } from 'vue-router';
import AppNavBar from '@/components/Common/AppNavBar.vue';
</script>

<style scoped>
</style>
