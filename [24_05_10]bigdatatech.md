# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 2. film 테이블에서 아이템 추출
2. views.py 변경 - 이어서
   - queryset 부분은 위에서 ViewSet과 연결된 테이블에서 데이터를 추출할 때 SQL 쿼리 조합을 만드는 객체. 기본적으로는 models.py에서 정의한 데이터베이스 모델 전용 클래스의 objects.all 메서드 호출.
   - serializer_class 부분은 시리얼라이저 클래스 지정. 시리얼라이저로 사용할 클래스 이름 FilmSerializer 지정
   - 옵션 부분은 각각 데이터베이스 테이블에서 필터링해서 데이터를 추출할 때 대상이 되는 필드를 filter_fields 변수로 지정. 모든 필드를 대상으로 할 때는 `'__all__'`로 지정.
   - 데이터베이스 테이블의 데이터를 정렬할 때 사용할 필드를 ordering_fields 변수에 지정. 
   - 데이터베이스 테이블의 데이터를 검색할 때 사용할 필드를 search_fields 변수에 지정.예제에서는 title 필드만 검색할 것이므로 'title'로 지정, 필드는 튜플 자료형으로 지정.
   - django_film_api/django_film_api/urls.py를 다음과 같이 변경.
   - ```python
     """URL 라우팅 정의"""
     from django.conf.urls import url,include
     from rest_framework import routers
     from film import views
     router = routers.DefaultRouter()

     # /films의 URL에 views.FilmViewSet 연결
     router.register(r'films',views.FilmViewSet)

     urlpatterns = [
        url(r'^',include(router.urls)),
     ]
     ```
   - 프로젝트 디렉터리의 urls.py에는 특정 URL 경로와 해당 URL 경로에 접근할 때 호출할 처리를 클래스 또는 함수로 지정.