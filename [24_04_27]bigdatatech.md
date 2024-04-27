# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 4. 플라스크 플러그인:Flask-RESTful 사용
3. 웹 서버를 실행하고 응답 확인
   - 다음과 같이 웹 애플리케이션 실행
   - ```cmd
     $ python flask_film_api.py
     ```
   - 브라우저를 사용, http://127.0.0.1:5000/film/10에 접근,film 테이블에서 film_id가 10인 데이터 추출
   - 이어서 http://127.0.0.1:5000/films?page=2에 접근 시 데이터 5개 확인 가능
   - page 매개 변수를 변경하면 film 테이블에서 추출되는 범위도 변경, 응답되는 데이터가 바뀜
   - 현재 데이터에서는 film_id가 6~10까지 모두 5개 있고, URL 매개 변수를 ?page=2로 지정했으므로 처음 페이지의 5개를 건너뛴 것.

## 3. 장고(Django)로 웹 API 생성.
### 1. 장고를 사용해서 웹 AI 만들기
- 파이썬의 풀스택 웹 프레임워크인 장고를 이용해 장고 RESTful 웹 API를 만들어봄
1. 장고와 장고 REST 프레임워크 설치
   - 장고 REST 프레임워크[[URL](http://www.django-rest-framework.org)]
   - pip install 명령어로 장고와 장고 REST 프레임워크, 그리고 관련 라이브러리 설치
   - ```cmd
     $ pip install django djangorestframework django-filter djangorestframework-filters
     ```
2. 장고 프로젝트 생성
   - 설치 완료 시 장고 프로젝트 생성(장고에서 프로젝트란 특정 목적을 위한 프로그램 파일과 설정 파일의 집합을 나타냄) 다음 명령어 입력
   - ```cmd
    $ django-admin startproject django-film_api
    $ cd django_film_api
    $ python manage.py startapp film
     ```
   - 디렉터리 생성 완료