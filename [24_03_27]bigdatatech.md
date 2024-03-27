# 6. 스크레이핑 개발(응용)
## 6. 링크를 따라 돌며 크롤링
### 1. 링크를 따라 돌며 크롤링하려면
2. 로그 확인
   - 로그 확인 시 메인 페이지도 무사히 스크레이핑.
   - /login 페이지 링크는 DEBUG:Ignoring link(depth>1)라고 출력되어 있어 무시하고 넘어감
   - 이는 Settings.py의 DEPTH_LIMIT = 1에 지정한대로 추출한 링크 대상 콘텐츠 계층만 스크레이핑.
   - 마지막 부분의 통계정보는 다믕과 같음
   - `'downloader/request_count':57`
   - 모두 57번의 요청이 있었음
## 7. 데이터베이스에 저장
### 1. 데이터베이스에 아이템 저장
   - Scrapy는 데이터 저장에 Item Pipeline이라는 기능 사용.
1. MySQL에 신규 데이터베이스와 테이블 생성
   - 로컬 MySQL에 'quotes'라는 데이터베이스를 만들고 다음처럼 테이블 생성
```sql
$ mysql.server start
$ mysql -u root -p

mysql> CREATE DATABASE quotes DEFAULT CHARACTER SET utf8;

mysql> use quotes;
    >  CREATE TABLE `quotes` (
    > `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    > `author` varchar(255) DEFAULT NULL,
    > `text` text,
    > `text_hash` char(64) DEFAULT NULL, 
    > `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    > `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    > PRIMARY KEY (`id`),
    > UNIQUE KEY `text_hash` (`text_hash`)
    >) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4
```