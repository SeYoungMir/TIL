# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 2. film 테이블에서 아이템 추출
   - 생성된 데이터베이스 모델을 사용해서 film 테이블에서 아이템 추출.
1. 인터렉티브 셸에서 데이터베이스 내용 확인
   - 장고 환경에서 확인하지 않고, 간단하게 인터렉티브 셸을 사용해서 확인. 다음 명령어를 실행해서 인터렉티브 셸로 들어감
   - ```cmd
     $ python manage.py shell
     ```
   - 다음과 같이 입력해서 데이터베이스 내용확인
   - ```python
     In [1]: # film/,models.py 읽어들이기
     In [2]: from film import models
     In [3]: # sakila 데이터베이스의 film 테이블에서 film_id=10의 내용 추출
     In [4]: film = models.Film.objects.get(film_id=10)
     In [5]: film.film_id

     In [6]: film.title
     In [7]: # sakila 데이터베이스에서 film 테이블의 앞 데이터 3개 추출
     In [8]: films = models.Film.objects.all()[:3]
     In [9]: # 장고의 models을 딕셔너리로 변환하는 유틸리티 읽어 들이기
     In [10]: from django.forms.models import model_to_dict
     In [11]: # 변환해서 내용 확인해보기
     In [12]: [model_to_dict(film) for film in films]
     ```
     - 해당 코드처럼 실행 시 데이터베이스에서 아이템이 추출된 것을 확인 가능.