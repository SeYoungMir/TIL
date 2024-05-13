# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 3. JSON으로 결과 확인
- HTTP로 만들어진 GUI 화면에 JSON 결과가 출력되는 것을 볼 수 있지만, 외부 프로그램에서 요청하면 HTML이 아니라 JSON으로 결과를 얻을 수 있음.
1. httpie 설치
   - 파이썬으로 만들어진 HTTP 요청 유틸리티인 'httpie'를 사용, 개발 전용 서버를 실행한 상태로 다른 터미널 실행. 이어서 pip install 명령어로 httpie 설치
   - ```cmd
     $ pip install httpie
     ```
2. 요청하기
   - 요청은 다음과 같이 http 명령어로 함
   - ```cmd
     $ http 'http://localhost:8000/films/?page=2'
     ```
3. 출력 결과 확인.
   - httpie를 사용하면 
   - JSON이 깨끗하게 출력.
   - 장고 REST 프레임워크를 사용하면 굉장히 간단하게 RESTful 웹 API를 만들 수 있음. 내부에서 사용하기 위한 API를 간단하게 만들 수 있음.
   - 장고 문섣는 다음 URL에서 참고.
     - 장고 문서|Django documentation | Django[[URL](https:/docs.djangoproject.com/2.1/)]