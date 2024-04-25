# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 4. 플라스크 플러그인:Flask-RESTful 사용
2. 플라스크 애플리케이션 생성- 해설
   - db.py에서 'sakila 데이터베이스의 film테이블 전용 모델'인 Film 클래스 읽어들임
   - 단일 아이템 출력 클래스 부분은 film 테이블에서 film_id를 지정, 하나의 데이터를 추출, 출력할 수 있게 해 주는 클래스 정의. 이는 마지막의 /film/`<int:film_id>`(이 때 `<int:film_id>`는 int 자료형의 숫자)라는 URL 경로와 연결
   - get이라는 이름으로 메서드 지정 시 HTTP 프로토콜의 GET 메서드 호출 될 때 실행. Film.get 메서드의 매개변수 film_id에 해당하는 데이터를 film 테이블에서 추출, film.to_dict 메서드를 사용해 딕셔너리 형식으로 변환해 응답
   - film_id에 해당하는 데이터가 없으면 film.get 메서드는 Film.DoesNotExist 예외 발생. 이 때는 abort 메서드 사용, HTTP 상태 코드 404 응답, descriptrion에는 그때 출려갈 메시지 지정.
   - film 테이블에서 여러 개의 데이터를 추출, 출력할 수 있게 해 주는 클래스 정의, 이는 /films 라는 URL 경로와 연결.