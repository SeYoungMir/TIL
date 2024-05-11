# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 2. film 테이블에서 아이템 추출
2. views.py 변경 - 이어서
   - urls.py from rest_framework 부분에서는 장고 REST 프레임워크의 라이브러리인 rest_framework 에서 URL 라우팅 전용 모듈 routers를 임포트
   - from film 부분에서는 django_film_api/film/views.py 임포트
   - router 부분에서는 장고 REST 프레임워크의 URL 라우팅 정보를 생성, routes 모듈의 DefaultRouter 클래스를 인스턴스화, router 객체 생성
   - router.register 부분에서는 router.register 메서드로 'films라는 URL 경로'와 'views.FilmViewSet 클래스'를 연결한 다음 router객체에 등록
   - urlpatterns 부분에서 장고의 URL 라우팅 정보는 프로젝트 디렉터리(django_film_api) 바로 아래의 urls.py 파일에서 리스트 형식의 변수 urlpatterns로 정의.
   - urlpatterns 리스트에 포함된 요소는 url 함수를 사용, 'URL 경로를 나타내는 정규 표현식'과 'URL 경로와 연결된 클래스와 함수'를 지정하는 형태로 사용. 이러한 연결 정보를 'URL 패턴'이라고 부름
   - url 함수의 첫 번째 매개 변수에 지정한 r'^'은 URL 경로 /를 의미. r'문자열'은 raw 문자열이라는 의미.
     - 정규표현식과 raw 문자열
       - 정규 표현식에서 백슬래시는 이스케이프를 의미. 따라서 백 슬래시를 표현하려면 두번 연속해서 사용하는 `'\\'` 형태로 사용해야함.
       - 파이썬의 문자열도 백 슬래시를 이스케이프 문자로 취급하므로 `'\\'`라고 표현 식 백슬래시 하나, 따라서 백슬래시 두 개를 정규 표현식 내부에서 사용하려면`'\\\\'`이라고 적어야 함.
       - 문자열 앞에 r을 붙인 raw 문자열은 백슬래시를 이스케이프 문자로 다루지 않음.
       - 따라서 파이썬에서 정규 표현식을 만들 때는 일반적으로 raw 문자열 사용.