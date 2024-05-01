# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 1. 장고를 사용해서 웹 AI 만들기
3. 장고 ORM 모델 정의
   - sakila 데이터베이스의 film 테이블과 대응되는 장고 ORM 모델 정의. 장고에는 실제 데이터 베이스의 내용을 기반으로 데이터베이스를 자동으로 생성해주는 기능 있음.
   - 다음 명령어 실행해서 데이터베이스 모델의 기본 형태 생성
   - ```cmd
     $ python manage.py inspectdb
     ```
4. models.py의 내용 변경
   - 위의 명령어로 출력된 파일 참고, django_film_api/film/models.py의 내용을 다음 코드처럼 변경
   - ```python
     """데이터베이스 모델"""
     from django.db import models
     
     class Language(models.Model):
        """language 테이블 전용 모델"""
        language_id = models.AutoField(primary_key=True)
        name = models.CharFiled(max_length=20)
        last_update = models.DateTimeField()
        
        def __str__(self):
          return '%s %s' %(self.language_id,self.name)
        class Meta:
          managed = False
          db_table = 'language'
      
      class Film(models.Model):
        """film 테이블 전용 모델"""
        film_id = models.SmallIntergerField(primary_key = True)
        title = models.CharField(max_length=255)
        description = models.TextField(blank=True,null=True)
        release_year = models.PositiveSmallIntegerField(blank=True,null=True)
        language =models.ForeignKey('Language',models.DO_NOTHING)
        length = models.SmallIntergerField(blank=True,null=True)
        last_update = models.DateTimeField()
      
        class Meta:
          managed = False
          db_table = 'film'
     ```