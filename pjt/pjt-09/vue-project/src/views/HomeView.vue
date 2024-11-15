<template>
    <div>
        <h1>상품 목록 리스트</h1>
        <div v-if="store.products" class="product-list">
            <div v-for="product in store.products" :key="product.id" class="product-card">
                <img :src="product.image" alt="" class="product-image">
                <div class="product-detail">
                    <h3>{{ product.title }}</h3>
                    <p>가격: ${{ product.price }}</p>
                    <button @click="goDetail(product.id)">상세 페이지로 이동</button>
                    <button @click="store.addToCart(product)">장바구니로 이동</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useCartStore } from '@/stores/cart';
import { onMounted } from 'vue';

const store = useCartStore()
const router = useRouter()

onMounted(() => {
    store.getProducts()
})

const goDetail = function (productId) {
    router.push({ name: 'detail', params: { productId: productId } })
}
</script>

<style scoped>

</style>