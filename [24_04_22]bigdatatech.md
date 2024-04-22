# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 3. 데이터베이스 연결
3. iPython을 사용한 아이템 추출
   - 실제로 데이터베이스에서 아이템 추출
   - 표준 인터렉티브 셸 대신 여러 가지 보조 기능이 있는 iPython의 인터렉티브 셸 사용.
   - pip install 명령어 사용, iPython 설치. 이어서 iPython 실행, 데이터베이스조작 테스트
   - ```cmd
     $ pip install ipython
     $ ipython
     ```
   - ```python
     # film_id = 10에 해당하는 아이템 추출
     from db import Film
     film=Film.get(Film,film_id==10)
     film.film_id
     film.tilte
     film.to_dict()
     # 데이터 3개 추출
     films=Film.select().limit()
     [film.to_dict() for film in films]
     ```
  - 결과 학인 시 sakila 데이터베이스의 film 테이블에서 아이템을 적절하게 추출했다는 것으 롹인 가능, 확인 완료 후 CTRL +D 키로 셸 명령어 입력 상태에서 벗어남.