# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 3. 데이터베이스 연결
- 플라스크에는 MySQL 데이터베이스에 연결할 수 있게 해 주는 기능이 없음. 데이터베이스를 다루려면 ORM 라이브러리가 필요. Peewee라는 ORM 라이브러리 사용
  - Peewee[[URL](https://github.com/coleifer/peewee)]
- ORM 라이브러리
  - 관계형 데이터베이스의 데이터를 객체 지향언어의 클래스와 같은 데이터로 맵핑하기 위한 라이브러리. ORM 라이브러리를 사용하면 SQL 구문을 사용하지 않아도 데이터베이스에서 데이터를 추출하거나 추가할 수 있음.
1. Peewee 설치
   - pip install 명령어를 사용해서 Peewee 설치
   - ```cmd
     $ pip install peewee
     ```
2. 데이터베이스 조작 전용 파일 만들기
   - 다음 사이트의 문서 참고, 데이터베이스 조작 전용 파일 만듦. 이후에는 이와 플라스크를 조합해서 데이터베이스에 접근하는 웹 애플리케이션 생성
   - Docs:Managing your Database[[URL](http://docs.peewee-orm.com/en/latest/peewee/database.html)]
   - 다음 명령어 실행 시 데이터베이스 조작 전용 파일의 기본 형태 확인 가능.
   - ```cmd
     $ python -m pwiz -e mysql -u root sakila
     ```
   - peewee는 데이터베이스의 내용을 기반으로 자동으로 데이터베이스 모델의 기본 형태를 출력해주는 기능 있음. 위 명령어로 터미널에 출력되는 기본 형태 참고
