# 4. 스크레이핑 기본
## 4. 데이터를 데이터베이스에 저장, 분석
### 4. 파이썬에서 MySQL에 접속하기
1. mysqlclient 설치
   - 파이썬으로 MySQL에 접속할 때 사용할 수 있는 라이브러리(드라이버)는 매우 많음.
   - 여기서는 mysqlclient 사용. mysqlclient는 파이썬 2.x에서 많이 사용된 MySQL-python 라이브러리를 포크한 것. 7장의 장고(Django)에도 포크되어있음.
   - pip install 명령어로 mysqlclient 설치
    ```python
    $ pip install mysqlclient
    ```
* 포크란 어떤 소스 코드를 기반으로 다른 소프트웨어를 만드는 것.
2. 데이터베이스에 접속해서 SQL 실행
   - mysqlclient를 설치했으므로 파이썬 사용, 데이터베이스에 접속
   - MySQLdb를 import하고 connect 함수의 매개 변수에 다음과 같은 것들을 지정해 호출하면 데이터베이스에 접속됨
     - 사용자 이름
     - 비밀번호
     - 호스트(localhost라면 생략 가능)
     - 데이터베이스 이름
     - 문자 코드(생략하면 디폴트 문자 코드 자동 지정)
     ```python
     >>> import MySQLdb
     >>> connection = MySQLdb.connect(
        user = "scraping1",
        passwd = "pass1#",
        host = "localhost",
        db = "scraping",
        charset = "utf8") 
     ```
3. connect 함수의 반환값 확인
   - connect 함수의 반환값은 Connection 클래스
    ```python
    >>> type(connection)
    ```
4. 커서 추출
   - Connection 클래스의 cursor 메서드 호출 시 커서 추출 가능
    ```python
    >>> cursor = connection.cursor()
    >>> type(cursor)
    ```
5. 테이블 생성
   - Cursor 클래스의 execute 메서드로 SQL 실행
   - 테이블 생성 예시
     - 도서 정보 저장 테이블, books 이름으로 테이블 생성
     - 칼럼으로 title과 url 지정, 두가지 모두 text 자료형
     - Connection 클래스의 commit 메서드를 호출해야 SQL 구문 실제로 실행
        ```python
        >>> cursor.execute("CREATE TABLE books (title text, url text)")
        >>> connection.commit()
        ```
