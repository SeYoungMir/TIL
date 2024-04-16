# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 1. 웹 API와 파이썬 웹 프레임워크
- 파이썬에는 웹 API를 만들기 위한 편리한 프레임워크 있음. 이를 활용해서 데이터베이스에 저장한 데이터에 대한 요청이 있을 때 JSON으로 응답하는 웹 API 생성.
- 파이썬 웹 프레임워크라고 하면 범용적인 웹 애플리케이션을 만들 때 필요한 기능을 대부분 갖춘 풀스택 프레임워크인 장고가 유명.
- 하지만 웹 프레임워크로 필요한 최소한의 기능만 갖춘 마이크로 웹 프레임워크도 있음. 대표적인 마이크로 프레임워크로는 파일 하나만으로 만들어진 보틀(Bottle), 파이썬으로 유명한 템플릿 엔진인 진자2(Jinja2)를 만든 개발자가 만든 플라스크(Flask)도 있음.
  - 보틀(Bottle)[[URL](http://bottlepy.org/docs/dev/index.html)]
  - 진자2(Jinja2)[[URL](http://jinja.pocoo.org)]
  - 플라스크(Flask)[[URL](http://flask.pocoo.org)]
### 2. 플라스크를 사용한 웹 API 만들기
- 플라스크를 사용한 웹 API 예를 살펴보기
- 연습용 데이터베이스로는 MySQL 개발 그룹이 제공하는 'sakila 데이터베이스' 사용.
- sakila 데이터베이스는 다음 사이트에서 다운 가능
  - MySQL Documentation:Other MySQL Documentation[[URL](https://dev.mysql.com/doc/index-other.html)]
- 위 페이지에는 이외에도 세계 각국의 통계 모델을 데이터베이스로 만든 'world database'등도 제공.
- 이를 살펴보면 대규모 데이터를크롤ㄹ링할 때 어떤 식으로 데이터베이스를 설계해야하는지 참고 가능.
  - 연습 전용 데이터베이스 sakila database의 데이터베이스 통계
    - id필드의 이름처럼 몇 가지 실무에서 거의 사용하지 않는 설계도 있음. 참고만 하고 100% 동일하게 구현하는 것은 아님
  - PostgreSQL의 샘플 데이터베이스
    - PostgreSQL 샘플 데이터베이스는 다음 사이트에서 확인
    - PostgreSQL 튜토리얼:Postgre Sample Database[[URL](http://www.postgresqltutorial.com/postgresql-sample-database)]
1. sakila 데이터베이스
   - sakila 데이터베이스는 온라인 DVD 상점의 데이터 표현 자세한 내용은 다음 사이트 참고
     - MySQL Documentation:Sakila Sample Database[[URL](https://dev.mysql.com/doc/sakila/en/)]