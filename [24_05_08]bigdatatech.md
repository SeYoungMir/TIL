# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 2. film 테이블에서 아이템 추출
2. views.py 변경
   - django_film_api/film/views.py를 다음처럼 변경
   - ```python
     """API 전용 뷰"""
     from rest_framework import serializers, viewsets

     # film/models.py 읽어들이기
     from film import models

     # models.py의 Language 모델 데이터를 JSON으로 변환하는 클래스
     Class LanguageSerializer(serializers.ModelSerializer):
        """Language 시리얼라이저"""
        class Meta:
            model = models.Language # models.Language와 연결
            fields = '__all__' # 모든 필드 출력
     # models.py의 Film 모델 데이터를 JSON으로 변환하는 클래스
     class FilmSerializer(serializers.ModelSerializer):
        """Film 시리얼라이저"""
        #language 필드에는 위의 LanguageSerializer 적용
        language = LanguageSerializer()

        class Meta:
            model = models.Film # models.Film과 연결
            fields = '__all__' # 모든 필드 출력
     # /films의 URL에서 호출될 클래스
     class FilmViewSet(viewsets.ModelViewSet):
        """Film 전용 Viewset"""
        # Film 모델에서 쿼리 객체 추출, queryset에 설정(필수)
        queryset = models.Filmobjects.all()

        # 직렬화 해당 지정(필수)
        serializer_class = FilmSerializer
        
        # 옵션
        filter_fields = '__all__'
        ordering_fields = '__all__'
        search_fields = ('title',)
     ```