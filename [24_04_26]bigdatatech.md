# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 4. 플라스크 플러그인:Flask-RESTful 사용
2. 플라스크 애플리케이션 생성- 해설 - 이어서
   - def `__init__`(self,*args,**kwargs): 부븐 에서는 Resource 클래스의 `__init__` 메서드를 오버라이드. *args,**kwargs를 사용해서 모든 매개변수를 추출, 일반적인 매개 변수와 키워드 매개 변수를 각각 args,kwargs 변수에 저장
     - 함수와 메서드의 매개 변수 *args
       - 함수의 매개 변수를 *args라고 작성하면 키워드 매개 변수 이외의 모든 매개 변수가 args 변수에 튜블 형식으로 들어옴
       - 다음과 같은 함수를 정의하고 fun(1,2,'a','b') 형태로 함수 호출 시 args 변수에 (!,2,'a','b')라는 튜플 반환
       - ```python
         def func(*args):
            print(args)
         ```
    - 함수와 메서드의 매개 변수 **kwargs
      - 함수의 매개 변수를 **kwargs라고 작성하면 모든 키워드 매개 변수가 kwargs 변수에 딕셔러니 자료형으로 반환
      - 다음과 같은 함수를 정의하고 func(one=1,two=2,three=3) 형태로 함수 호출 시 kwargs 변수에 {'one':1,'two':2,'three':3}이라는 딕셔너리 반환
      - ```python
        def func(**kwargs):
            print(kwargs)
        ```
  - /films?page=2처럼 URL 매개 변수로 page를 지정할 수 있게 URL 매개 변수를 파싱하는 reqparse.RequestParser 함수를 호출
  - self.parser.add_argument 메서드를 사용해서 파싱 대상 URL 매개 변수인 page를 지정, page 매개 변수는 숫자로 다룰 것이므로 type=int 라고 지정
  - page 매개 변수가 없을 때는 page=1을 지정했을 때와 똑같이 동작하도록 기본값 default=1을 지정, 마지막으로 super().`__init__` 메서드는 부모 클래스인 Resource의 `__init__` 메서드를 호출하는 것. 꼭 작성해야 하는 코드임.
  - 이때 매개변수 args를 *args, 키워드 매개변수 kwargs를 **kwargs로 언팩해서 전달
    - 변수 언팩
      - 변수 args에 (1,2,3)이라는 튜플 형식의 값이 들어있을 때, func 함수에 func(*args)라는 형태로 전달하면 func(1,2,3)형태로 실행했을 때처럼 처리(args 변수의 값이 전개되어 전달)
      - 변수 kwargs에 {'one':1,'two':2,'three':3}라는 딕셔너리 형식의 값이 들어있을 때, func 함수에 func(**kwargs)라는 형태로 실행했을 때 처럼 처리(kwargs 변수의 값이 전개되어 전달)
      - 이처럼 변수에 * 또는 **를 붙여 함수를 호출하는 것을 '변수 언팩' 이라 함
  - def get(self): 부분처럼 get이라는 이름으로 메서드 지정 시 HTTP 프로토콜의 GET 메서드가 호출될 때 실행
  - Film.select 메서드를 사용, film 테이블의 데이터 추출 가능. 이어서 order_by 메서를 사용해서 데이터를 film_id 순서로 오름차순 정렬
  - paginate 메서드 사용, film 테이블의 데이터를 self.ITEMS_PER_PAGE 변수의 값(5)으로 나누고, URL 매개 변수 page로 전달된 페이지 번호(args[page])부분을 추출. 이어서 이 결과를 films 변수에 저장
  - 리스트 내포를 사용해 각각의 데이터에 to_dict 메서드를 적용한 다음 응답
    - 리스트 내포
      - 리스트 내포는 리스트를 생성할 때 for 반복문 내부에 넣어 사용하는 것을 의미. 다음 for 반복문 예시를 참고
      - 최종적으로 1부터 3까지의 숫자에 2를 곱한 값을 가진 squares 리스트 생성
      - ```python
        squares=[]
        for i in [1,2,3]:
            squares.append(i*2)
        ```
      - 따라서 squares 에는 [2,4,6]이 들어감. 리스트 내포를 사용 시 다음과 같은 코드로도 구현 가능
      - ```python
        squares =[i*2 for i in [1.2.3]]
        ```
      - 기본적인 형식은 <리스트의 최종 요소> for <반복변수> in <리스트>
      - api.add_resource 부분은 FilmItem 클래스를 /film/(film_id)와 연결
      - (film_id) 부분을 `<int:film_id>`로 작성하면 film_id가 int 자료형의 변수로 전달, 이 코드로 인해 예를 들어 /film/10이라는 URL 경로로 접근하면 film_id에 10이 전달
      - apo.add_resource 메서드를 사용, FilmList 클래스를 /film/과 여결. 이 때는 page 등의 URL 매개 변수를 따로 지정하지 않아도 됨.