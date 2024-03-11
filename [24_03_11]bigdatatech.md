# 6. 스크레이핑 개발(응용)
## 1. XML로 변환
### 3. Orator 사용
- 도서를 첫 번째 계층으로 두는 형태로 데이터베이스의 내용을 XML로 벼환
- 데이터베이스 테이블과 프로젝트 내부의 객체(출판사, 도서 등)를 대응하게 만들어주는 ORM(Object-Relational Mapping) 라이브러리로 'Orator' 사용
  - Orator[(URL)](https://orator-orm.com/)
- 파이썬의 ORM으로는 '웹 애플리케이션 프레임워크 장고(Django)에 들어있는 장고 ORM'과 'SQLAlchemy'가 대표적
- 설정이 복잡하다는 단점
- Orator는 규칙에 따라 테이블 이름과 객체 이름만 붙여 두면 사용할 수 있으므로 연습으로 Orator 사용
  - 장고 ORM[(URL)](https://docs.djangoproject.com/en/2.1/topics/db/)
  - SQLAlchemy[(URL)](https://www.sqlalchemy.org/)
- Orator는 MySQL 데이터베이스 어댑터로 'PyMySQL'과 'mysqlclient'를 선택해서 사용 가능
- 예제에서는 mysqlclient를 사용
- mysqlclient는 Orator가 MySQL에 접근할 때 내부적으로 사용
1. Orator 설치
   - pip install 명령어 사용, Orator 설치
   `$ pip install mysqlclient orator`