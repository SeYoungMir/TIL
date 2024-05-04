# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 1. 장고를 사용해서 웹 AI 만들기
4. models.py의 내용 변경 - 해설 - 이어서
   - class meta의 하위 항목인 db_table 부분에서는 모델을 sakila 데이터베이스의 language 테이블과 연결
   - Class Film 부분은 sakila 데이터베이스에 있는 film 테이블의 모델 정의 film 테이블에 있는 language_id 필드는 language 테이블의 language_id를 참고한다는 의미, models.Foreign Key 메서드로 Language 클래스를 참조하게 지정. 이 때 필드 이름은 _id를 생략한 language로 붙임
   - 모델을 sakila 데이터베이스의 film 테이블과 연결
5. settings.py의 내용 변경
   - django_film_api/django_film_api/settings.py를 변경. 다음 내용처럼 내용 변경.