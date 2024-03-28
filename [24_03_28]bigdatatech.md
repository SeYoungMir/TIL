# 6. 스크레이핑 개발(응용)
## 7. 데이터베이스에 저장
### 1. 데이터베이스에 아이템 저장
1. MySQL에 신규 데이터베이스와 테이블 생성- 이어서
```sql
mysql> CREATE TABLE `tags`(
    > `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    > `name` varchar(255) NOT NULL DEFAULT ``,
    > `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    > `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    > PRIMARY KEY (`id`)
    > UNIQUE KEY `tag` (`name`)
    >) ENGINE = InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

mysql> CREATE TABLE `quotes_tag`(
    > `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    > `quote_id` int(11) NOT NULL,
    > `tag_id` int(11) NOT NULL,
    > `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    > `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    > PRIMARY KEY (`id`)
    > UNIQUE KEY `quote_tag` (`quote_id`,`tag_id`)
    >) ENGINE = InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
```
- text_hash 칼럼과 그 유니크 인덱스에 주목, 각각의 격언(quotes)의 동일성을 확인하기 위한 칼럼과 인덱스. 같은 격언이 두 번 이상 올라올 수도 있다는 것을 가정, '내용이 동일하면 같은 아이템으로 판단하고 저장하지 않는다'는 사양을 만들기 위해 유니크 인덱스 적용
- 각각의 격언은 여러 개의 태그를 가지며, 각각의 태그도 여러 개의 격언을 가질 수 있음. 이처럼 서로 서로 여러 개의 연결을 갖는 관계를 다 대 다(Many-to-Many)관계라고 부름. 이는 각각의 연결을 quotes_tags에 저장해서 구현

