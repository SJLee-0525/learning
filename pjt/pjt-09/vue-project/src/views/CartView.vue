<template>
    <div>
        <h1>장바구니</h1>
        <div v-if="store.carts" class="product-list">
            <div v-for="cart in store.carts" :key="cart.id" class="product-card">
                <img :src="cart.image" alt="" class="product-image">
                <div class="product-detail">
                    <h3>{{ cart.title }}</h3>
                    <p>가격: ${{ cart.price }}</p>
                    <button @click="goDetail(cart.id)">상세 페이지로 이동</button>
                    <button @click="store.addToCart(cart)">장바구니에서 제거</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useCartStore } from '@/stores/cart';

const store = useCartStore()

</script>

<style scoped>

</style>