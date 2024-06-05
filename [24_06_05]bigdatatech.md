# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 2. peewee와 flask-admin 사용 
4. 스크립트 생성. - 이어서
   - def on_model_change 부분은 flask_admin_peewee.ModelView 메서드를 오버라이드 한 것. on_model_change 메서드는 데이터 편집 화면에서 데이터를 생성하거나 수정할 때 호출
   - peewee는 데이터를 생성할 때 id 필드에 자동 순번(AUTO_INCREMENT)이 할당되어 있지 않으면 peewee.Model.save를 실행해도 데이터베이스에 데이터가 저장되지 않음. 강제로 데이터를 데이터베이스에 저장하고 싶다면 peewee.Model.save 메서드의 매개 변수에 force_insert=True를 지정해야 함.
   - flask_admin 데이터 수정 화면에서는 데이터를 만들 때 내부적으로 peewee.Model.save를 호출, 기본값으로는 매개 변수에 아무것도 들어가지 않으므로 앞서 설명한 이유로 데이터가 저장되지 않음. 그래서 이 메서드를 오버라이드.
   - 매개변수 form에는 POST 데이터로 전달된 데이터 포함
   - 매개변수 model에는 해당 관리 화면과 연결된 모델의 객체가 포함
   - 매개변수 is_created에는 생성 화면일 때 True, 수정 화면일 때 False를 반환.
   - admin.add_view 부분에서는 book_db.Publisher 클래스의 객체를 생성, 관리 화면에 추가. 이 메서드와 관련된 자세한 내용은 다음 공식 문서 참고
     - flask_admin.model - flask-admin 1.5.0 documentation[[URL](http://flask-admin.readthedocs.io/en/latest/api/mod_model/#flask.ext.admin.model.BaseModelView.on_model_change)]
   - 추가로 peewee 데이터베이스의 모델 정의,id 필드와 관련된 자세한 내용은 다음 공식문서 참고.
     - Models and Fields -peewee 2.10.1 documentation[[URL](http://docs.peewee.-orm.com/en/latest/peewee/models.html#id3)]
   - @app.route 부분에서는 최상위 페이지 URL 경로(/)에 접근했을 때 실행할 하수를 정의. flask_admin 라이브러리를 사용 시 /admin/으로 접근했을 때 관리 화면 출력. 이 경로에 대한 링크만 출력하도록 함.
   - admin 부분은 flask_admin.Admin메서드를 사용, flask_admin 라이브러리를 사용한 관리 화면 구축 전용 객체 생성. 첫 번째 매개 변수에는 app= Flask(`__name__`)에서 만든 app을 지정. 키워드 매개 변수 name에는 관리 화면의 제목(`<title>`태그로 출력할 내용)을 지정. 데이터베이스 조작 전용 라이브러리인 peewee를 살펴보고 있으므로 Example:peewee라고 지정
 - admin.add_view 부분에서는 PublisherAdmin 부분에서 만든 관리 화면 정보를 구축하기 위한 클래스를 writterAdmin 메서드로 객체화. admin.add_view 메서드에 전달, publisher 테이블 전용 관리 화면을 @app.route 부분에서 만든 관리 화면 전용 객체로 등록. PublisherAdmin 메서드에는 관리 화면 조작 대상이 될 데이터베이스 테이블publisher의 데이터베이스 모델 정보를 가진 book_db.Publisher를 매개 변수로 전달.