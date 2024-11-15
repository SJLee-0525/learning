import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useVideoStore = defineStore('counter', () => {
  const API_KEY = 'AIzaSyCjgLJreYbE9m83Hu33fLPVVylCyVsDflw'

  const searchVideos = ref([])
  const savedVideos = ref([])
  const savedChannels = ref([])

  const saveVideo = function (videoDetail) {
    const index = savedVideos.value.findIndex((element) => element.id === videoDetail.id)
    if (index === -1) {
      alert('비디오를 저장합니다.')
      console.log(videoDetail)
      savedVideos.value.push(videoDetail)
    } else {
      alert('비디오를 제거합니다.')
      deleteVideo(videoDetail)
    }
  }

  const deleteVideo = function (videoDetail) {
    const index = savedVideos.value.findIndex((element) => element.id === videoDetail.id)
    if (index !== -1){
      savedVideos.value.splice(index, 1)
    }
  }

  const saveChannel = function (channelTitle) {
    const index = savedChannels.value.findIndex((element) => element === channelTitle)
    if (index === -1) {
      alert('채널을 저장합니다.')
      console.log(channelTitle)
      savedChannels.value.push(channelTitle)
    } else {
      alert('채널을 제거합니다.')
      deleteChannel(channelTitle)
    }
  }

  const deleteChannel = function (channelTitle) {
    const index = savedChannels.value.findIndex((element) => element === channelTitle)
    if (index !== -1){
      savedChannels.value.splice(index, 1)
    }
  }
  

  return { API_KEY, searchVideos, savedVideos, savedChannels, saveVideo, deleteVideo, saveChannel, deleteChannel }
}, { persist: true })
