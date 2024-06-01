# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 2. peewee와 flask-admin 사용
- 플라스크 관리 화면 라이브러리인 flask-admin은 여러 가지 ORM 라이브러리를 지원함. 이전에 살펴보았던 peewee도 지원하므로 이를 사용하도록 함.
1. 가상 환경 만들고 설치
   - venv를 사용해서 가상 환경을 만들고, 다음 사이트를 참고해서 pip install 명령어로 flask-admin과 peewee를 설치
     - flask-admon/examples/peewee [[URL](https://github.com/flask-admin/flask-admin/tree/master/examples/peewee)]
   - ```cmd
     $ python -m venv venv_flask_admin
     $ source venv_flask_admin/bin/activate
     (venv_flask_admin)$ pip install Flask Flask-Admin mysqlclient peewee wtf-peewee ipython
     ```
2. 데이터베이스 조작 전용 스크립트
   - 플라스크 자체는 데이터베이스 조작과 관련된 기능이 없음. 따라서 데이터베이스 조작과 테이블 정의를 별도의 스크립트에 작성해두고 이를 활용. 다음과 같이 코드를 입력, book_db.py라는 이름으로 저장.