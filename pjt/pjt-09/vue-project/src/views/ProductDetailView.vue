<template>
    <div>
        <h1>상세 페이지</h1>
        <div v-if="product">
            <div class="product-card">
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
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCartStore } from '@/stores/cart';
import { onMounted } from 'vue';

const route = useRoute()
const store = useCartStore()
const product = ref(null)

onMounted(() => {
    const productId = route.params.productId
    product.value = store.getProductDetail(productId)
    console.log(product)
})



</script>

<style scoped>

</style>