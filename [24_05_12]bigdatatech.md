# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 2. film 테이블에서 아이템 추출
3. 정규 표현식과 raw 문자열
   - routers.url 속성에는 이전 코드에서 router.register 메서드로 만든 URL 패턴 저장.
   - url 함수의 두 번째 매개 변수에 include(router.urls)를 지정 시 첫 번째 매개 변수에 넣은 URL 경로 뒤에 router.urls의 URL 패턴을 붙여 사용.
   - 장고의 URL 라우팅 설정과 관련된 내용은 다음 공식 문서 참고
     - URL dispatcher|Django documentation|Django[[URL](https://docs.djangoproject.com/en/2.1/topics/http/urls)]
   - 추가로 장고 REST 프레임워크의 URL 라우팅과 관련된 내용은 다음 공식 문서 참고
     - Routers - 장고 REST 프레임워크 [[URL](http://www.django-rest-framework.org/api-quide/routers)]
4. 개발 전용 웹 서버 실행.
   - views.py와 urls.py를 변경했다면 장고에 내장된 개발 전용 웹 서버를 다음 명령어로 실행
   - ```cmd
     $ python manage.py runserver
     ```
   - 브라우저에서 http://127.0.0.1:8000/films/에 접근, 페이지네이션 등도 화면 위에서 확인 가능.서버를 종료할 때는 터미널에서 [ctrl]+[c]키 입력. 