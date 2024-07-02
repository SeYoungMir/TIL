# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 1. 자바스크립트로 렌더링 되는 페이지를 스크레이핑하기
### 2. 파이썬 가상 환경과 venv
1. 자바스크립트로 렌더링되는 페이지 스크레이핑
   - 샘플로 자바스크립트를 사용해 렌더링되는 페이지를 Vue.js를 이용해 생성
   - Vue.js는 자바스크립트 프레임워크로, 동적 HTML을 조합하고 출력해주는 기능이 있음.
   - 여기서는 Vue.js코드에 관해서 정말 간단하게 설명, 관심 있다면 공식 사이트 참고
     - Vue.js [[URL](https://vuejs.org)]
   - 다음 코드를 작성, vue_sample.html이라는 이름으로 파일저장
   - ```html
     <meta charset="utf-8">
     <script src = "https://unpkg.com/vue"></script>

     <div id = "app">
        <h1>좋아하는 영화 랭킹 Top3</h1>
        <ol>
            <li v-foor="item in items">
                <span class = "cinema_title">{{item}}</span>
            </li>    
        </ol>
     </div>
     <script>
        new Vue({
            el:'#app',
            data: { 
                items: [
                    'AKIRA(감독: 오오토모 카츠히로)',
                    '2001: 스페이스 오디세이(감독: 스탠리 큐브릭)',
                    '아이언맨 (감독: 존 패브로)',
                ]
            }
        })
     </script>
     ```
   - vue_sample.html은 영화를 자바스크립트 객체로 정의하고 `<ol>`,`<li>`태그를 사용해 브라우저에 내용을 렌더링.