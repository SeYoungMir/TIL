# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 2. peewee와 flask-admin 사용 
3. 세션 전용 시크릿 키 생성
   - 웹 애플리케이션은 '세션'이라는 데이터를 사용해서 사용자 정보를 저장. 
   - 이때 사용자에게 부여되는 정보는 암호화됨. 암호화 될땐느 '시크릿 키'라 불리는 랜덤한 문자열 사용
   - 보안을 위해서 시크릿 키는 웹 애플리케이션 작성자이외의 사람이 모르게 해야 함.
   - 세션 전용 시크릿 키는 다음처럼 생성.
   - ```cmd
     $ python -c 'import os,binascii; print(binascii.hexlify(os.urandom(24)))'
     b'~~~~'
     ```
   - '' 안이 세션 전용 시크릿 키. 생성된 시크릿 키는 잠시 뒤에 만들 웹 애플리케이션 전용 스크립트인 flask_admin_server.py에서 사용.
4. 스크립트 생성.
   - flask_admin_server.py 생성. 다음 코드 입력
   - ```python
     from flak import Flask

     import flask_admin
     from flask_admin.contrib import peewee as flask_admin_peewee

     import peewee

     import book_db
     
     app = Flask(__name__)
     
     # 시크릿 키 설정
     app.config['SECRET_KEY']= '~~~' #위에서 생성한 시크릿 키

     class PublisherAdmin(flask_admin_peewee.ModelView):
        """publisher 테이블 관리 화면 전용 클래스"""
        column_display_pk=True
        column_sortable_list=('id','name','is_active')
        column_filters = column_sortable_list
        column_editable_list=('name','is_active')
        form_columns = column_sortable_list

        def on_model_change(self,form,model,is_created):
            if is_created:
                model.save(force_insert=True)
    
     ```