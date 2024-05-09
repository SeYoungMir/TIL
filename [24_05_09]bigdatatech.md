# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 2. film 테이블에서 아이템 추출
2. views.py 변경 - 이어서
   - 각 애플리케이션 디렉터리의 views.py에는 특정 URL에 접근했을 때 호출할 처리를 정의
   - 여기에서 정의한 클래스와 함수는 이후의 django_film_api/django_film_api/urls.py 파일에서 URL 경로를 연결할 때 사용.
   - from film 부분은 django_film_api/film/models.py 임포트
   - class LanguageSerializer 부분은 language 테이블의 데이터를 직렬화 하기 위한 클래스
     - 직렬화(serialize)란?
       - 객체의 내용을 바이트열 또는 특정 형식을 가진 문자열로 변환하는 것을 직렬화(serialize)
       - 장고 REST 프레임워크는 serializers.ModelSerializer 클래스를 상속, 직렬화 클래스를 정의, 어떤 데이터 모델이 가진 데이터를 JSON 형식으로 변환. 장고 REST 프레임워크의 직렬화와 관련된 자세한 내용은 하단 문서 참고
         - Serializers - 장고 REST 프레임워크 [[URL](http://www.django-rest-framework.org/api-guide/serializers/)]
     - model = models.Language 부분에서 이러한 직렬화를 models.Language 클래스와 연결
     - fields 부분에서 직렬화로 추출,출력할 필드 지정. `'__all__'`이라고 지정 시 모든 필드를 나타냄. 특정 필드만 지정하고 싶을 때는 fields=('name',)처럼 튜플 형식으로 지정.
     - class FilmSerializer 부분은 film 테이블의 데이터를 직렬화 하기 위한 클래스
     - language=LanguageSerializer 부분은 film 테이블 내부의 language_id 필드에서 참조할 language 테이블의 데이터를 직렬화해서 저장할 수 있게 위에서 정의한 LanguageSerializer의 인스턴스를 LanguageSerializer 메서드로 생성.
     - models = models.Film 부분에서 이러한 시리얼 라이저를 models.Film 클래스와 연결.
     - fields 부분은 이러한 시리얼 라이저로 추출해서 출력할 필드로 모든 것 지정.
     - 이상 데이터 베이스의 각 테이블 전용 시리얼 라이저 정의.
     - class FilmViewSet 부분은 장고 REST 프레임워크의 ViewSet 정의.
       - 장고 REST 프레임워크의 ViewSet
         - /film이라는 URL 경로에 접근할 때의 처리로 Film/ViewSet 클래스가 연결
         - 이 때 HTTP 메서드 GET(추출),POST(생성),PUT(변경),DELETE(제거)에 따라서 호출될 메서드를 따로 정의하지 않아도 queryset에서 지정한 쿼리 객체와 serializer에서 지정한 시리얼라이저 클래스를 통해서 연결된 데이터베이스 테이블(film 테이블)의 데이터 추출, 생성, 변경, 제거가 이뤄지게 할 수 있음. 이와 관련된 내용은 하단 문서 참고
           - ViewSets - 장고 REST 프레임워크 [[URL](http://www.django-rest-framework.org/api-guide/viewsets/)]