import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCartStore = defineStore('counter', () => {
  let products = ref([])
  let carts = ref([])

  const getProducts = () => {
    axios({
      method: 'get',
      url: 'https://fakestoreapi.com/products',
    })
      .then((response) => {
        console.log(response)
        products.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const getProductDetail = function (productId) {
    const product = products.value.find((element) => {
      return element.id == productId
    })
    return product
  }


  const addToCart = function (product) {
    console.log('호출')
    const index = carts.value.findIndex((element) => element.id === product.id)
    if (index === -1) {
      alert('장바구니에 추가합니다.')
      carts.value.push(product)
    } else {
      alert('장바구니에서 제거합니다.')
      deleteToCart(product.id)
    }
  }
  
  const deleteToCart = function (productId) {
    const index = carts.value.findIndex((element) => element.id === productId)
    if (index !== -1) {
      carts.value.splice(index, 1)
    }
  }

  return { products, carts, getProducts, getProductDetail, addToCart, deleteToCart }
})
