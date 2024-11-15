<template>
  <NavBar />
  <RouterView />
  <Foot />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '@/components/Common/NavBar.vue';
import Foot from '@/components/Common/Footer.vue';

</script>

<style scoped>

</style>
