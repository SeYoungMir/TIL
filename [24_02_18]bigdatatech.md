# 4. 스크레이핑 기본
## 4. 데이터를 데이터베이스에 저장, 분석
### 3. 데이터베이스와 사용자 생성
- 스크레이핑한 데이터를 저장하려면 데이터베이스에 접속할 때 사용할 사용자 필요
- 하단 명령어를 이용해 root 사용자로 MySQL 서버에 접속, u 옵션은 사용자 지정 옵션, p 옵션은 비밀번호 지정 옵션
- p 옵션 뒤에 비밀번호를 입력할 수도 있지만 명령어 입력 이력에 비밀번호 출력 시 비밀번호가 유출될 가능성 있으므로, 일반적으로 비밀번호 입력 하지 않고 [Enter]키 누른 후 Enter password: 라고 나오면 비밀번호 입력
- macOS에서 root 사용자의 비밀번호가 설정되어있지 않으면 따로 입력하지 않고 그냥 [Enter]키 입력
```python
$ mysql -u root -p
Enter password:
```
- 접속 완료 시 명령어 또는 SQL 구문을 입력할 수 있는 프롬프트 나옴. 데이터베이스 접속을 종료할 때는 exit 입력, [Enter]입력하거나 [Ctrl]+[D]키 입력

- CREATE DATABASE는 데이터베이스를 만들 때 사용하는 명령어
- CREATE DATABASE 뒤에 데이터베이스 이름을 지정, DEFAULT CHARACTER SET 뒤에 문자 코드 지정.
- 예시로 다음과 같은 데이터베이스 제작
  - 이름:scraping
  - 문자코드:utf8
  ```mysql
  mysql> CREATE DATABASE scrapingdata DEFAULT CHARACTER SET utf8;
  ```
- CREATE USER 명령어로 사용자 생성. CREATE USER 뒤에 사용자 이름 지정, 뒤에 IDENTIFIED BY '<사용자 비밀번호>' 입력. 비밀번호는 하나 이상의 숫자 ,하나 이상의 알파벳, 하나 이상의 특수문자를 모두 포함해야함
  - 사용자 이름:scraping1
  - 비밀번호:pass1#
  ```mysql
  mysql> CREATE USER 'scraping1' IDENTIFIED BY 'pass1#';
  ```
- 생성한 사용자(scraping1)에 생성한 데이터베이스(scraping)을 읽고 쓸 수 있는 권한 부여. GRANT ALL ON <데이터베이스 이름>.* TO <사용자 이름> 으로 권한 부여
    ```mysql
    mysql> GRANT ALL ON scraping.* TO scraping1
    ```
- 이후 exit 명령어로 MySQL 서버에서 로그아웃