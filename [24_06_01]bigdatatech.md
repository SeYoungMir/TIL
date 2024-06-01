# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 2. peewee와 flask-admin 사용 
2. 데이터베이스 조작 전용 스크립트 - 이어서
   - ```python
     """데이터베이스 모델"""
     import datetime

     import peewee
     from playhouse.pool import PooledMySQLDatabase

     db = PooledMySQLDatabase(
        'book_db',
        max_connections=8,
        stale_timeout=10,
        user='root')
     
     class BaseModel(peewee.Model):
        """공통 부모 모델"""
        created_at = peewee.DateTimeField(default=datetime.datetime.utcnow)
        updated_at = peewee.DateTimeField()

     def save(self,*args,**kwargs):
        self.updated_at=datetime.datetime.utcnow()
        super().save(*args,**kwargs)
        
        class Meta:
            database= db
     class Publisher(BaseModel):
        id = peewee.IntegerField(primary_key=True)
        name = peewee.CharField()
        is_active = peewee.BooleanField()

        class Meta:
            db_table = 'publisher'
     ```
   - 위 코드는 ORM 라이브러리 peewee를 사용해서 데이터베이스의 테이블 정의를 만든 모델 파일.
   - 이전 장에서 peewee를 사용해 데이터베이스의 모델 전용 파일을 만드는 방법을 다뤘으므로 해당 부분 참고
   - db 부분에서는 데이터베이스 접근과 관련된 정보를 가진 db 객체 생성.
   - class BaseModel 부분에서는 book_db 데이터베이스와 데이터베이스 테이블 모델을 연결할 수 있게 공통 정의를 나타내는 부모 클래스 셍성
   - class publisher 부분에서는 publisher 테이블의 모델 정의. id 필드는 출판사 ID를 정수로 저장할 수 있도록 peewee.IntergerField 메서드로 정의. id 필드는 publisher 테이블의 프라이머리 키(데이터 베이스 내부에서 레코드를 유일하게 식별하기 위해 사용하는 키)이므로 primary_key=True로 지정.
   - name 필드에는 출판사 이름을 문자열로 저장, peewee.CharField 메서드로 정의
   - is_active 필드는 출판사 데이터의 활성화 상태를 나타내는 필드. True 또는 False로 지정할 것이므로 peewee.BooleanField 메서드로 정의. 이 값은 데이터베이스에 저장될 때 각각 1과 0으로 변경되어 저장.
   - 이 모델을 publisher 테이블과 연결할 수 있게 Meta 클래스의 db_table 필드를 'publisher'로 지정.
   - peewee를 사용해서 데이터베이스 테이블의 전용 모델을 만들 때 필드 정의하는 방법은 다음 사이트 참고
     - peewee:Models and Fields[[URL](http://docs.peewee-orm.com/en/latest/peewee/models.html)]