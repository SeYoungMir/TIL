# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
-  장고는 장고 어드민(Django Admin)이라고 불리는 관리 화면 기능을 기본으로 제공
1. 가상 환경을 만들고 장고 설치
   - venv 명령어로 가상 환경을 만들고 pip install 명령어로 장고를 설치
   - ```cmd
     $ python -m venv venv_django
     $ source venv_django/bin/activate
     (venv_django)$ pip install django mysqlclient ipython
     ```
2. 장고 프로젝트와 애플리케이션 생성
   - 가상 환경에 장고 설치했다면 다음 명령어를 실행해서 장고 프로젝트와 애플리케이션 생성
   - ```cmd
     (venv_django)$ django_admin startproject book_db
     (venv_django)$ cd book_db
     (venv_django)$ python manage.py startapp book
     ```
   - 위 명령어 실행 시 여러 파일들이 자동으로 생성.
3. 스크립트 수정.
   - 이어서 자동으로 생성된 파일 중에서 book_db/book_db/settings.py를 수정해서 장고의 기본적인 설정 수정. 다음 부분을 변경. 7장의 장고 웹 API를 참고, 설정과 관련된 자세한 내용 확인.