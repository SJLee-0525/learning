<template>
    <nav>
        <RouterLink :to="{ name: 'home' }">HOME</RouterLink> | 
        <RouterLink :to="{ name: 'cart' }">CART</RouterLink>
    </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router';

</script>
