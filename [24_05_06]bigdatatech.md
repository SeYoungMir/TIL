# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 1. 장고를 사용해서 웹 API 만들기
5. settings.py의 내용 변경 - 코드 해설
   - 프로젝트 이름(django_film_api/django_film_api/)바로 아래의 settings.py 파일에서 장고 통합 설정 실행
   - DEBUG부분은 장고 디버그 객체. True로 설정 시 개발 서버 화면을 출력할 때 오류가 있으면 화면에 오류의 원인이 나오게 됨. 참고로 장고로 만든 웹 애플리케이션을 외부로 공개할 때는 이를 False로 해 두는 것이 좋음(해킹 수단으로 사용될 수 있음)
   - ALLOWED_HOSTS 부분은 장고를 사용한 웹 애플리케이션을 호스트할 머신의 호스트 이름을 넣음 *을 지정하면 아무것이나 괜찮다는 의미. ALLOWED_HOSTS 정의에 포함되지 않은 호스트 머신에서 애플리케이션 실행 시 (위 부분 False로 설정 시)Bad Request(400)이라는 오류 출력
   - INSTALLED_APPS 부분에서는 웹 애플리케이션에서 사용할 모듈을 지정. 기본적으로 다음과 같이 설정되어 있으며, 따로 수정하지 않아도 됨.
     - 'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    - 그 바로 아래 부분에서는  장고 REST 프레임워크를 사용할 수 있게 djangorestframework 라이브러리 활성화
    - 장고 REST 프레임워크를 사용한 웹 애플리케이션에서 요청 필터 기능을 사용할 수 있게 django-filters 라이브러리를 활성화. 필터 기능을 활성화하면 데이터베이스 필터 값을 지정해서 해당 값에 해당하는 데이터만 데이터베이스 테이블에서 필터링해서 추출할 수 있음.
    - 다음 코드는 python manage.py startapp film 명령어로 만든 film 애플리케이션을 활성화. 장고에는 '프로젝트'와 '애플리케이션'이라는 개념이 있음. django-admin startproject django_film_api 명령어로 만든 django_film_api 디렉터리의 내용이 '프로젝트', 프로젝트는 '애플리케이션'이라는 단위로 기능을 구현해서 사용하게 됨.
    - 예를 들어 DVD 가게를 관리하는 웹 애플리케이션을 만들 때는 고객 관리 기능과 DVD 상태 관리 기능을 따로따로 구분할 수 있음. 이와 같은 경우 각각 애플리케이션이라는 단위로 이를 나눠서 만들 수 있음.
    -  모든 기능을 하나의 애플리케이션으로 만들 수도 있지만, 기능을 나눌 수 있다면 애플리케이션으로 나누는 것이 보수하기 쉬움.
    -  film.apps.FilmConfig는 django_film_api/film/app.py의 FilmConfig 클래스를 지정. 이 클래스는 pyrhon manage.py startapp film 명령어를 실행했을 때 film 디렉터리를 기반으로 자동 생성된 것.
    -  REST_FRAMEWORK = 부분은 위에서 활성화한 장고 REST 프레임워크의 설정.
    -  DEFAULT_FILTER_BACKENDS는 위에서 활성화한 필터 기능 중에서 기본으로 사용할 라이브러리. 이를 지정하지 않으면 필터 기능을 따로따로 사용하겠다고 선언해야 함. 대부분 2개 지정해주면 됨(직접 필터 기능을 구현하고 기본으로 사용하겠다고 선언할 때는 여기에 모듈을 추가)
    -  DATABASES = 부분은 웹 애플리케이션에서 사용할 데이터베이스와 접근 정보 지정. 로컬에 있는 MySQL 내부의 sakila 데이터베이스 지정.