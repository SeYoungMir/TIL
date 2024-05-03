# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 1. 장고를 사용해서 웹 AI 만들기
4. models.py의 내용 변경 - 해설
   - 각 애플리케이션 디렉터리의 models.py 파일에서는 장고에서 사용할 데이터베이스의 테이블 전용 데이터 모델을 정의
   - Class Language 부분은 sakila 데이터베이스의 language 테이블 전용 모델을 정의. 이어서 film 테이블 전용 모델인 Film의 language 필드 정의에 사용
   - models.Model을 상속한 데이터베이스 테이블 전용 모델 필드 정의에 대해서는 다음 문서를 참고
     - Model field reference|Django documentation|Django[[URL](https://docs.djangoproject.com/en/2.1/ref/models/fields/)]
   - 이후에 설명하는  pythonmanage.py runserver 명령어로 개발 서버를 실행하고 브라우저에서 http://127.0.01:8000/films를 열면 데이터 관리 페이지가 나옴. 여기에서 [Filters]버튼을 클릭해서 출력되는 [Language]드롭다운 리스트에는 모델이 가지고 있는 `__str__ ` 메서드의 결과가 문자열로 출력. 이 때 language 데이터베이스의 language_id와 name 필드를 쉽게 볼 수 있게 출력.
   - 이후 Language 클래스 밑의 Class Meta 에서는 Meta 클래스의 managed 필드에 False를 지정. models.py의 내용을 기반으로 데이터베이스 테이블을 생성/저장하는 명령어인 python manage.py migration을 실행하더라도 실제 데이터베이스에 테이블이 만들어지지 않게 함. (장고 관리 화면 기능 Django Admin을 만들 때에도 사용) 이는 데이터베이스를 중복으로 생성하지 않게 하기 위함 이는 하단의 코드에서도 동일.