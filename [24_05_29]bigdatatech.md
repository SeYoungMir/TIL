# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 1. 크롤링 대상을 데이터베이스로 관리.
- 크롤러를 운용하다 보면 처음에 크롤링 대상으로 삼던 사이트와 인덱스 페이지를 일시적으로 또는 영구적으로중지하고 싶은 경우가 생길 수 있음. 크롤링 대상을 데이터베이스로 관리하는 경우 브라우저에서 열람하고 조작할 수 있는 관리 화면을 개방해 둔다면 이를 굉장히 편리하게 할 수 있음.
- 데이터베이스를 기반으로 관리 화면을 개발하는 방법 살펴보기
1. 데이터베이스 생성.
   - MySQL 서버를 실행하고 로그인
   - ```cmd
     $ mysql.server start
     $ mysql -u root -p
     ```
   - 6장과 같은 이름의 데이터베이스를 생성할 것이므로 기존의 데이터베이스 제거.
   - ```sql
     mysql > DROP DATABASE book_db;
     ```
   - 같은 이름으로 새로 데이터베이스 생성.
   - ```sql
     mysql > CREATE DATABAE book_db DEFAULT CHARACTER SET utf8;
     ```
    - 해당 데이터베이스로 이동
    - ```sql
      mysql > use book_db
      ```
    - 'book_db'로 변경했다면 다음 코드 이용,테이블 생성.
    - ```sql
      CREATE TABLE `publisher`(
        `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
        `is_active` tinyint(1) NOT NULL DEFAULT '1',
        `name varchar(128)` NOT NULL DEFAULT '' ,
        `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)   
      ) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;

      INSERT INTO `publisher`(`is_active`,`name`)
      VALUES (1,'위키북스'),(2,'한빛미디어');
      ```