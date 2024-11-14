import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()

  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const token = ref(null)
  const loginusername = ref(null)

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // 회원가입 요청 액션
  const signUp = function (payload) {
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      }
    })
      .then((response) => {
        console.log(response)
        console.log('회원 가입 성공')
        const password = password1
        logIn({ username, password })
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  // 로그인 요청 액션
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      }
    })
      .then((response) => {
        console.log(response)
        console.log('로그인 성공')
        token.value = response.data.key
        loginusername.value = username
        router.push({ name: 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 로그아웃 요청 액션
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
      .then((response) => {
        console.log(response)
        token.value = null
        loginusername.value = null
        router.push({ name: 'LogInView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  return { articles, API_URL, token, isLogin, loginusername, getArticles, signUp, logIn, logOut }
}, { persist: true })
