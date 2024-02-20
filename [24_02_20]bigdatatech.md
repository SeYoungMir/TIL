# 4. 스크레이핑 기본
## 4. 데이터를 데이터베이스에 저장, 분석
### 4. 파이썬에서 MySQL에 접속하기
6. 테이블 확인
   - 데이터베이스에 books라는 테이블 생성
   - 실제로 생성되었는지 확인
   - 터미널에서 MySQL 서버에 접속, 데이터베이스 내부의 테이블 출력
    ```python
    $ mysql -u root -p
    Enter password : <비밀번호 입력>

    mysql> SHOW TABLES FROM scraping;
    mysql> SHOW COLUMNS FROM books FROM scraping
    ```
7. 테이블에 레코드 추가
   - 테이블이 만들어졌는지 확인했다면 테이블에 레코드 추가
   - exit 명령어로 MySQL 서버에서 로그아웃
   - 레코드를 추가할 수 있게 파이썬에서 데이터베이스에 접속
   - 레코드 추가시에는 Cursor 클래스의 execute 메서드 사용
   - Cursor 클래스의 execute 메서드는 두 번째 매개변수 지정 가능
   - execute 메서드 사용, INSERT 구문 실행.
   - 첫 번째 매개 변수에는 SQL 구문, 두 번째 매개 변수에는 파라미터 지정
    ```python
    $ python
    >>> import MySQLdb
    >>> connection = MySQLdb.connect(
        user = "scraping1",
        passwd = "pass1#",
        host = "localhost",
        db = "scraping",
        charset = "utf8")
    >>> type(connection)
    >>> cursor = connection.cursor()
    >>> type(cursor)
    >>> cursor.execute("INSERT INTO books VALUES(%s,%s)",("책 제목","링크"))
    >>> connection.commit()
    ```
8. 테이블 변화 확인
   - 테이블 내부의 레코드 확인
    ```mysql
    mysql -u root -p
    Enter password : <비밀번호 입력>

    mysql> use scraping
    mysql> select * from books;
    ```
    - 만든 connection은 close 메서드 호출해서 접속을 제거해야함

