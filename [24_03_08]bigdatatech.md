# 6. 스크레이핑 개발(응용)
## 1. XML로 변환
### 1. 데이터베이스를 만들고 테이블 등록
1. 데이터베이스 만들기.
  - 데이터베이스 이름은 'book_db'
  - MySQL 설치 전제로 실행
  ```
  $ mysql -u root -p
  mysql > CREATE DATABASE book_db DEFAULT CHARACTER SET utf8;
  mysql > use book_db
  ```
2. 데이터베이스에 테이블 등록
   - 로컬 MySQL 데이터베이스에서 실행
   ```sql
   mysql> CREATE TABLE `languages` (
    > `id int(11) unsigned NOT NULL AUTO_INCREMENT,
    > `name` varchar(8) NOT NULL DEFAULT '',
    > `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    > `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    > PRIMARYKEY(`id`)
    > ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARTSET=utf8mb4;

    > INSERT INTO `languages`(`id`,`name`)
    > VALUES
    >   (1,'한국어'),
    >   (2,'영어');
   ```
3. 언어를 저장할 테이블 추가
   - 위의 코드는 문자의 종류를 저장하는 테이블 추가, 언어가 그렇게 많지 않아 따로 인덱스 추가하지 않음
4. 출판사를 저장할 테이블 추가
   - 다음 코드는 출판사를 저장할 테이블을 추가하는 코드
   - 크롤링 프로그램이 도서를 추가하는 과정에서 자신의 데이터베이스에서 출판사를 검사해보고, 없으면 테이블의 레코드로 추가한다고 가정
   - id 칼럼은 테이블 내부에서 유일한 레코드를 특정할 때 사용하는 PRIMARY KEY
   - 크롤러 프로그램이므로 출판사 이름으로 검색하는 경우는 거의 없을것이라 판단, name 칼럼에 인덱스를 만들지 않음.
   ```sql
   mysql > CREATE TABLE `publishers`(
    > `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    > `name` varchar(128) NOT NULL DEFAULT '',
    > `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    > `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    > PRIMARY KEY (`id`)
    > ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

    > INSERT INTO `publishers` (`id`,`name`)
    > VALUES
    >   (1,'위키북스'),
    >   (2,'한빛미디어'),
    >   (3,'Addision-Wesley')
    ```
    