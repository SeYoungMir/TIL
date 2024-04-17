# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 2. 플라스크를 사용한 웹 API 만들기
2. sakila 데이터베이스 임포트
   - https://dev.mysql.com/doc/index-other.html에서 sakila database라고 적혀 있는 줄의 zip 파일을 내려받고 압축 해제
   - 다음 명령어 사용, 압축 해제한 파일을 데이터베이스에 임포트
     - ```cmd
       $ cd sakila-db
       $ mysql -u root < sakila-schema.sql
       $ mysql -u root < sakila-data.sql
       ```
   - 위의 두 파일 이외에도 sakila.mwb라는 파일 존재. 이는 MySQL 개발 그룹이 제공하는 GUI 데이터베이스 관리 도구인 MySQL Workbench 전용 파일. MySQL Workbench로 열면 ER 다이어그램을 통한 데이터베이스의 구조 확인 가능
     - ER 다이어그램은  '실체 관계 다이어그램(Entity-relationship Diagram)'이라는 의미, 관계형 데이터베이스를 추상적으로 표현하는 방법 중 하나
   - MySQL Workbench[[URL](https://www.mysql.com/en/products/Workbench)]
 - sakila 데이터베이스의 구조는 다음 URL에서도 확인 가능
   - MySQL Documentation:Sakila Sample Database:Structure[[URL](https://dev.mysql.com/doc/sakila/en/sakila-structure.html)]
 - sakila 데이터베이스 내부에서 영화 제목 테이블을 나타내는 film 사용
3. 플라스크 설치
   - 플라스크 설치, pip install 명령어로 플라스크 설치 가능
   - ```cmd
     $ pip install Flask
     ```