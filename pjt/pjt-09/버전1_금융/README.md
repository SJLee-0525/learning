## E: 생성형 AI 활용하기

#### 질문
방금과 같은 영상 검색 프로그램에서 최상단에는 App.vue를 그리고 그 안에는 채널 검색을 맡는 SearchView.vue를, 나중에 볼 영상을 맡는 LaterView.vue를, 메인 페이지를 맡는 HomeView.vue를, 비디오 상세 정보를 담는 VideoDetailView.vue를 넣고 App.vue의 상단과 하단에 하위 컴포넌트인 nav와 footer르 두었는데, 더 효율적인 컴포넌트 구조가 있을까?  

그리고 영상을 검색하면 뒤로 가더라도 유지되도록 counter.js에 저장을하는 식으로 했는데, 과연 이게 최선일지 알려줘

#### 답변
현재 구조는 기본적으로 잘 구성되어 있지만, 몇 가지 개선 사항을 제안할 수 있습니다:  

컴포넌트 구조 개선:  
App.vue를 레이아웃 컴포넌트로 사용하고, 그 안에 RouterView를 배치하는 것이 좋습니다.   
Nav와 Footer 컴포넌트를 별도의 layouts 폴더에 넣어 관리할 수 있습니다.  
재사용 가능한 UI 컴포넌트들(버튼, 입력 필드 등)을 components/base 폴더에 넣어 관리하는 것이 좋습니다.  

개선된 구조 예시:
```text
src/
|-- components/
|   |-- base/
|   |   |-- BaseButton.vue
|   |   |-- BaseInput.vue
|   |-- SearchBar.vue
|   |-- VideoList.vue
|   |-- VideoItem.vue
|-- layouts/
|   |-- DefaultLayout.vue
|   |-- Nav.vue
|   |-- Footer.vue
|-- views/
|   |-- HomeView.vue
|   |-- SearchView.vue
|   |-- LaterView.vue
|   |-- VideoDetailView.vue
|-- App.vue
|-- router/
|-- store/
```

상태 관리 개선:  

현재 counter.js에 검색 결과를 저장하는 방식은 작동하지만, 더 효율적인 방법이 있습니다:  
Vuex를 사용하여 검색 결과와 관련 상태를 관리하는 것이 좋습니다.  
검색 결과를 캐싱하고 필요할 때 재사용할 수 있도록 Vuex 스토어를 구성할 수 있습니다.   
vuex-persistedstate 플러그인을 사용하여 Vuex 상태를 로컬 스토리지에 저장하면, 페이지 새로고침 후에도 상태를 유지할 수 있습니다.

개선된 Vuex 스토어 구조 예시:
```javascript
import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
  state: {
    searchResults: [],
    recentSearches: [],
    savedVideos: []
  },
  mutations: {
    SET_SEARCH_RESULTS(state, results) {
      state.searchResults = results;
    },
    ADD_RECENT_SEARCH(state, search) {
      state.recentSearches.unshift(search);
      state.recentSearches = state.recentSearches.slice(0, 5); // 최근 5개만 유지
    },
    SAVE_VIDEO(state, video) {
      state.savedVideos.push(video);
    }
  },
  actions: {
    async searchVideos({ commit }, query) {
      // API 호출 로직
      const results = await api.searchVideos(query);
      commit('SET_SEARCH_RESULTS', results);
      commit('ADD_RECENT_SEARCH', query);
    }
  },
  plugins: [createPersistedState()]
});
```
이 구조를 사용하면 검색 결과, 최근 검색어, 저장된 비디오 등을 효율적으로 관리할 수 있으며, 페이지 새로고침 후에도 상태가 유지됩니다.   
이러한 개선사항들을 적용하면 컴포넌트 구조가 더 명확해지고, 상태 관리가 더 효율적으로 이루어질 수 있습니다.  
또한, 코드의 재사용성과 유지보수성이 향상될 것입니다.

## 학습한 내용
- 관통 프로젝트 돌입 전 VUE를 다시한 번 복습할 수 있었습니다.
- 기존 초창기 관통 프로젝트에서 진행했던 글꼴 적용 등도 실습해 보았습니다.
- 부트스트랩을 활용해 VUE 파일 내에서 꾸미는 연습 또한 진행헀습니다

## 어려웠던 부분
- 동영상과 채널이 저장되었는지를 확인하고, 그를 확인해 버튼의 표기를 바꾸는 것을 구현하는데에 어려움을 겪었고, 해결하는데 실패했습니다.
- 아직 computed 활용이 많이 미숙한 것 같아 연습하도록 하겠습니다.

## 새로 배운 부분
- css, 구글 폰트를 적용하기 위해서 어디에 스크립트를 입력해야하는지 알게 되었습니다.
- vue 내에서의 부트스트랩과 글꼴, 그리고 main.css 활용법에 대해서 알게 되었습니다. 
- assets 내의 정적 이미지 활용법을 연습할 수 있었습니다.

## 느낀 점
- 여전히 어려운 점이 많지만 진행하면서 재미도 많이 느낀 프로젝트였습니다.
- 조원과 함께해서 더 힘을 얻을 수 있었던 것 같습니다.