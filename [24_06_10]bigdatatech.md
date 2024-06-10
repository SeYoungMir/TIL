# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
3. 스크립트 수정 - 해설
- DEBUG 부분은 장고의 디버그 객체, True로 설정 시 개발 서버 화면을 출력할 때 오류가 있으면 오류의 원인을 출력해줌. 참고로 장고로 만든 웹 애플리케이션을 외부로 공개할 때는 이를 False로 해 두는 것이 좋음.(악의를 가진 제삼자가 오류를 통해 공격 수단을 찾을 수 있기 때문)
- ALLOWED_HOSTS에서는 장고 웹 애플리케이션을 호스트할 머신의 호스트 이름을 넣음. *을 지정하면 아무것이나 괜찮다는 의미
- ALLOWED_HOSTS 정의에 포함되지 않은 호스트 머신에서애플리케이션을 실행하면 Bad Request(400)이라는 오류 출력(위에서 DEBUG=False로 지정시만)
- INSTALLED_APPS 에서는 웹 애플리케이션에서 사용할 모듈을 지정. 기본값은 다음과 같음.
  - ```
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ```
- 웹 애플리케이션 아래에 python manage.py startapp book 명령어로 생성한 bokk 애플리케이션을 활성화.
- book.apps.BookConfig는 book_db/book/app.py의 BookConfig 클래스를 지정. 이 클래스는 python manage.py startapp book 명령어를 실행 시 book 디렉터리와 함께 자동으로 생성.
- DATABASEDS 에서는 웹 애플리케이션에서 사용할 데이터베이스와 접근 정보를 지정. 로컬의 MySQL 내부에 있는 book_db 데이터베이스를 지정함.
4. 기본 양식 출력
- 장고에는 기존 데이터베이스에서 데이터베이스 모델의 기본 양식을 출력하는 기능이 있음. 다음 명령어로 데이터베이스 모델의 기본 형태를 출력해서 book_db/book/models.py를 생성할 때 참고.
- ```cmd
  (venv_django)$ python manage.py inspectdb
  ```
- 위 명령어를 실행 시 book_db데이터베이스의 내용을 기반으로 장고 데이터베이스 모델의 기본 양식이 출력.