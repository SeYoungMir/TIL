# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
5. 스크립트 수정 - 해설
   - 예제에서는 이전 코드의 book_db/book/models.py에 정의할 데이터베이스 모델이 1개(class Publisher)밖에 없지만, 다른 모델을 추가하면 모든 모델의 created_at,updated_at 필드를 공통 정의하기 위한 부모 클래스가 만들어짐.
 - models.DateTimeField 메서드의 매개 변수 auto_now_add=True를 지정하면 모델 객체가 데이터베이스에 새로 추가될 때 생성 시각이 created_at 필드에 저장
 - models.DateTimeField 메서드의 매개 변수 auto_now=True를 지정하면 모델 객체가 벼경될 때, 변경 시각이 updated_at 필드에 저장.
 - models.Model을 상속한 데이터베이스 테이블의 전용 모델을 만들 때 필드를 정의하는 방법은 다음 문서 참고
   - Model field reference | Django documentation | Django[[URL](https://docs.djangoproject.com/en/2.1/ref/models/fields)]
   - 모델의 부모 클래스를 생성할 때는 Meta 클래스 내부에서 abstract =True를 지정해야 함.
   - Meta 클래스의 managed 필드에 False를 지정, 이는 models.py의 내용을 기반으로 데이터베이스 테이블을 생성하는 명령어인 python manage.py migration를 실행하더라도 실제 데이터베이스 테이블이 만들어지지 않게 하기 위함. 부모 클래스가 구체적인 데이터베이스 테이블과 연결되지 않게 하고 있음. 이러한 지정은 Publisher 모델에서도 동일.
   - class Publisher은 book_db 데이터베이스에서 출판사 데이터를 가진 publisher 테이블 전용 모델
   - is_active 필드는 출판사 데이터의 활성화 상태를 나타내는 필드. True 또는 False로 지정할 것이므로 models.BooleanField 메서드로 정의. 이 값은 데이터베이스에 저장될 때 각각 1과 0으로 변경되어 저장
   - python manage.py runserver 명령어로 개발 서버를 실행, 브라우저에서 http://127.0.0.1:8000/admin/book/publisher 로 접속하면 출판사의 데이터 목록 출력. 이때 목록에는 모델이 가진 `__str__` 메서드의 리턴값 출력. def `__str__` 부분에서는 이 때 id와 name 필드가 출력되게 정의.
   - db_table 부분은 이 모델을 데이터베이스의 publisher 테이블과 연결