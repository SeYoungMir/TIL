# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 1. 자바스크립트로 렌더링 되는 페이지를 스크레이핑하기
### 2. 파이썬 가상 환경과 venv
1. 자바스크립트로 렌더링되는 페이지 스크레이핑 - 설명
- `<li>` 태그부분에서는 항목 영화 데이터 배열 items를 v-for디렉티브로 하나씩 변수 item에 넣어 반복
- `<span>`부분은 추출한 item 변수를 Vue.js 템플릿 구문을 사용해서 출력
- items 부분은 페이지에서 사용하는 변수 items를 정의
- 파이썬 3에서 표준으로 제공하는 http 모듈을 사용해서 간단하게 HTTP 서버를 실행할 수 있음. 새로운 터미널을 열고 venv를 활성화한 후에 다음 명령어로 HTTP 서버 실행
- ```cmd
  $ source venv_selenium/bin/activate
  (venv_selenium)$ python -m http.server &
  ```
- 터미널에 Serving HTTP ... 라는 문자가 출력되었다면 브라우저에서 http://0.0.0.0:8000/vue_sample.html에 접근.
- `<span>`부분 처럼 vue_sample.html은 문자열 내용을 Vue.js의 기능으로 렌더링하므로 단순하게 HTML 부분을 기반으로 `<span>` 태그 내부의 도서 제목을 스크레이핑 하면 {{item}}이라는 문자열이 추출. 만약 셀레니움을 사용하면 자바스크립트를 내부적으로 실행, `<span>`태그의 내용이 Vue.js로 렌더링되어 도서 이름이 들어있는 HTML 요소를 추출할 수 있음.