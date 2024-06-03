# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 2. peewee와 flask-admin 사용 
4. 스크립트 생성. - 이어서
- flask_admin_server.py - 이어서
  - ```python
    @app.route('/')
    def index():
        return '<a href="/admin/">Click me to get to Admin!</a>'
    
    if __name__=='__main__':
        import logging
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)

        # 관리 화면 전용 객체 생성
        admin = flask_admin.Admin(app, name='Example: Peewee')

        # publisher 테이블 전용 관리 화면 추가
        admin.add_view(PublisherAdmin(book_db.Publisher))

        app.run(debug=True)
    ```
  - 플라스크와 flask-admin 라이브러리를 사용한 웹 애플리케이션 코드. 
  - import 부분에서 flask-admin 라이브러리 모듈을 읽어들이고, ORM 라이브러리 peewee를 지원하기 위한 모듈(flask_admin.contrib.peewee)도 flask_admin_peewee라는 이름으로 읽어 들임.
  - 데이터베이스 테이블 모델을 가진 book_db.py로 읽어들임.
  - app 부분에서는 Flask(__name__)메서드로 플라스크 애플리케이션 전용 객체(app)를 생성.
  - 플라스크 애플리케이션을 만들 때 정형적으로 사용하는 코드
  - app.config 부분에서 이전에 만든 세션 전용 시크릿 키를 app.config['SECRET_KEY']로 지정
  - def on_model_change 부분에서 peewee 데이터베이스관리 화면 정보를 구축하기 위한 클래스를 생성. flask_admin_peewee.ModelView를 상속받아 PublisherAdmin 생성.
  - column_display_pk = True로 지정, 데이터의 프라이머리 키 출력 False로 지정 시 프라이머리 키 출력하지 않음.
  - column_sortable_list로 데이터 모곡 화면에 출력할 필드 지정. 현재 예제에서는 출판사 ID, 출판사 이름, 출판사 데이터의 활성화 상태를 출력할 수 있게 ('id','name','is_active')를 지정.
  - column_filters에는 데이터 목록 화면에서 데이터를 필터링할 때 사용할 필드를 지정. column_sortable_list와 같은 필드를 지정하면 되므로 동일 리스트 지정.
  - column_editable_list에는 데이터 목록 화면에서 직접 편집할 수 있는 필드 지정, 출판사 이름,출판사 데이터의 활성화 상태를 수정할 수 있게 ('name','is_active')를 지정
  - form_columns에는 데이터 수정 화면에서 수정할 필드 지정. 모두 수정할 수 있게 하면 되므로 column_sortable_list를 지정.