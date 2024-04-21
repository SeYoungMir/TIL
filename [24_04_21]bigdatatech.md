# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 3. 데이터베이스 연결
2. 데이터베이스 조작 전용 파일 만들기 - 이어서
- db= PooledMySQLDatabase() 부분에서 sakila 데이터베이스에 접근하기 위한 정보를 db 객체로 생성
- class BaseModel에서 'db.py에 정의할 데이터베이스 테이블 모델'의 기반이 되는 부모 클래스를 생성
- class Language에서 languager 테이블 전용 모델 정의, 이후에 film 테이블 전용 모델의 language 필드 정의에 사용
- film 테이블 전용 모델 정의. film 테이블에 존재하는 language_id 필드는 language 테이블의 language_id를 참조. 따라서 peewee.ForeignKeyField 메서드르 사용, Language 클래스를 참조하도록 지정. 이때 필드 이름은 _id를 생략한 language로 지정
- peewee를 사용해서 데이터 베이스 테이블 전용 모델을 만들때의 필드 정의와 관련된 내용은 다음 사이트 참고
  - peewee Model and Field[[URL](http://docs.peewee-orm.com/en/latest/peewee/models.html)]
  - 현재 코드에는 Film 객체를 사용 형식으로 응답하는 메서드인 to_dict 메서드 직접 정의. 이후에 만드는 플라스크 웹 애플리케이션에서 JSON 응답을 쉽게하기 위해 미리 만들어 둔 것.