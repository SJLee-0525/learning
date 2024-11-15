<template>
    <div class="nav_div sticky-top d-flex justify-content-start align-items-center w-100 p-3 gap-3">
        <h4 class="mx-2">MyTube</h4>
        <RouterLink :to="{ name: 'home' }" class="text-decoration-none">HOME</RouterLink>
        <RouterLink :to="{ name: 'search' }" class="text-decoration-none">SEARCH</RouterLink>
        <RouterLink :to="{ name: 'later' }" class="text-decoration-none">LATER</RouterLink>
        <RouterLink :to="{ name: 'channel' }" class="text-decoration-none">Channel</RouterLink>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>