# 6. 스크레이핑 개발(응용)
## 1. XML로 변환
### 1. 데이터베이스를 만들고 테이블 등록
5. 도서를 저장할 테이블 만들기
   - 다음 코드는 도서를 저장할 테이블
   - 크롤러 프로그램이 네트워크의 데이터를 수집하면서 새로운 도리를 발견하면 레코드 추가할 것이라 가정
   - 출판사 테이블처럼 id 칼럼이 프라이머리 키이지만 이는 ISBN을 넣어 사용한다고 가정, AUTO_INCREMENT 지정하지 않음
   - 크롤러 프로그램이므로 도서 이름으로 검색하는 경우는 거의 없을것이라 판단, name 칼럼에 인덱스 생성 X
   - 도서의 수는 매우 많아질 가능성, 이후에 관리 화면으로 관리 가능. 인덱스는 그때 추가해도 됨
   ```sql
   mysql> CREATE TABLE `books` (
    >   `id` int(11) unsigned NOT NULL,
    >   `publisher_id` int(11) NOT, NULL,
    >   `title` varcher(255) NOT NULL DEFAULT '',
    >   `language_id` int(11) NOT NULL,
    >   `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    >   `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    >   PRIMARY KEY(`id`)
    > ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

    > INSERT INTO `books`(`id`,`title`,`publisher_id`,`language_id`)
    > VALUES
    >   (34973284, `HTML5 웹 프로그래밍 입문`, 2, 1),
    >   (57556147, `Hello Coding 파이썬`, 2, 1),
    ...(이하생략)
   ```
   - 추가했다면 MySQL 데이터베이스에서 로그아웃
   ```sql
   mysql> exit
   ```

### 2. XML 사용
- XML은 트리 구조로 되어 있으며  RSS, Atom 등의 피드로도 사용. 이전에 살펴봤던 데이터르 독자적인 XML 형식으로 작성한 샘플 코드를 살펴봄
```xml
<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <book id="34973284">
        <publisher id="2">한빛미디어</publisher>
        <title>HTML5 웹 프로그래밍 입문</title>
        <language id= "1">한국어</language>
    </book>
    <book id="57556147">
        <publisher id="2">한빛미디어</publisher>
        <title>Hello Coding 파이썬</title>
        <language id= "1">한국어</language>
    </book>
</catalog>
```
- 위 코드를 보면 테이블에 데이터가 어떻게 결합되었는지 파악 가능
- 위는 도서를 기반 XML 작성, 출판사를 기반으로 XML 작성 시 하단처럼 작성 가능
```xml
<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <publisher id= "1" name= "위키북스">
        <book id ="71051687">
            <title>파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발</title>
            <language id= "1">한국어</language>
        </book>
    </publisher>
    <publisher id="2" name= "한빛미디어">
        <book id="34973284">
            <title>HTML5 웹 프로그래밍 입문</title>
            <language id= "1">한국어</language>
        </book>
        <book id="57556147">
            <title>Hello Coding 파이썬</title>
            <language id= "1">한국어</language>
        </book>
    </publisher>
</catalog>
```
- 위 코드처럼 유연한 표현을 할 수 있는 XML도 프로그램에서 데이터로 사용할 때는 몇 가지 주의해야 할 사항 있음
- 하나의 XML 내부에 대량의 도서가 포함되어 있을 때, 트리의 모든 부분을 해석하기 전까지는 중간에 있는 도서 데이터를 꺼낼 수 없음.
- 따라서 대량의 데이터를 다룰 때에는 도서 목록을 적당한 크기로 나누는 게 좋음