### DB연결 Data 처리 패턴
1. 라이브러리 가져오기
   - python 각 DB 연결 라이브러리
     - pip install pymysql
     - import pymysql
2. 접속하기(DB)
   - .connect
     - userid, pw, db,IP(host)
3. 커서 가져오기(객체)
   - .cursor()
     - fetchall()/fetchone() 
       - 서버로부터 데이터가져오기
4. SQL 구문 만들기(CRUD SQL 구문등)
   - sql = 'select * from ~ '
   - select
   - update,delete,insert
5. SQL 구문 실험하기
   - execute()
6. DB에 complete하기
   - commit()
7. DB 연결 닫기
   -  close()

## pymysql 모듈 이해
- pymysql 라이브러리 소개 및 설치
  - mysql을 python에서 사용할 수 있는 라이브러리
  - ( pymysql 라이브러리 이외에도 MySQLdb(Mysql-pytion), MySQL connector 등 다양한 라이브러리 존재)
  - 이 중에서 설치가 가장 쉬운 라이브러리
  - !pip install pymysql
- 일반적인 mysql 핸들링 코드 작성 순서
  - PyMySql 모듈 import
  - pymysql.connect() 메소드를 사용하여 MySQL에 연결
  - 호스트명, 포트, 로그인, 암호, 접속할 DB 등을 파라미터로 지정
    - ex) localhost:3306:root:pwd:DBname:charset = 'UTF-8'
      - 데이터베이스종류마다 포트가 다름
  - MySQL 접속이 성공하면 Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져옴
  - Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 전송
  - SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 서버로부터 가져온 데이터를 코드에서 활용
  - 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이터를 확정
  - Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫음