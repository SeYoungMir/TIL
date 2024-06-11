# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
5. 스크립트 수정
   - 출력된 기본 형태 참고, 자동으로 생성된 book_db/book/models.py를 다음처럼 수정
   - ```python
     from django.db import models

     class BaseModel(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            abstract = True
            managed = False

     class Publisher(BaseModel):
        id = models.IntergerField(primary_key=True)
        name = models.CharField(max_length=128)
        is_active = models.BooleanField()

        def __Str__(self):
            return "{}:{}".format(self.id,self.name)
        
        class Meta:
            managed =False
            db_table = 'publisher'
     ```
   - 애플리케이션 디렉터리 아래에 있는 models.py 파일들에는 데이터베이스 테이블의 데이터 모델을 정의.