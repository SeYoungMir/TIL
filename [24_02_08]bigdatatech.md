# 3. 크롤러 및 스크레이핑 개발 환경 준비와 파이썬 기본
## 3. 파이썬 기초
### 7. 함수와 클래스
1. 함수
   - 함수 정의는 def 구문으로 함.
   - 함수 정의하기
   ```python
   def 함수():
    # 처리 내용 작성
   ```
   - 다음 언어처럼 매개 변수를 지정할 수 있으며, 반환할 값을 지정할 수도 있음. 매개변수는 기본 값을 지정할 수 있음.
   - 매개 변수 지정한 예시
   ```python
   def sum(a, b=0):
        result = a + b
        print(result)
        return result
    
   result = sum(2,3) # 5가 출력, 동시에 5가 반환  
   ```
   - 파이썬은 매개 변수와 리턴값의 자료형을 따로 지정할 수없음.
   - 그러나 주석(자료형 노테이션)을 붙일수는 있음
   - 주석을 지정한 예
   ```python
   def sum(a : int, b: int) -> int:
        result = a + b
        print(result)
        return result
    
   result = sum(2,3) # 5가 출력, 동시에 5가 반환  
   ```
   - 주석(Annotation)
     - 어디까지나 주석, 실행할 때 자료형을 확인하거나 하는 기능이 없음
     - 에디터 등에서 소스 코드를 작성할 때 경고를 띄워주거나 자동 완성 기능 등에서 자료형 정보를 알려주므로 꽤 편리, 활용하기 좋음
2. 클래스
   - class 구문으로 클래스를 정의
   - 클래스에는 변수와 메서드를 정의할 수 있음
   - 특징점으로 메서드의 첫 번째 매개 변수로 self 지정, 메서드 호출할 때에는 self 지정하지 않음.
   - 생성자는 `__init__` 이라는 이름 사용
   - 클래스 정의하기
   ```python
   class Shop:
        name = ""
        businessHours = ""
        def __init__ (self,name,busineessHours):
            self.name = name
            self.businessHours = businessHours
        def detail(self):
            print("가게 이름: "+ self.name + ", 영업시간: " + self.businessHours)
    shop = Shop("투썸", "9:00-19:00")
    shop.detail() # 결과 print
   ```
   - 클래스를 상속받고 싶을때는 다음처럼 작성
   ```python
   class BookStore(shop)
   ```
3. 모듈
   - 모듈은 다른 프로그램에서 코드를 재사용할 수 있게 유용한 클래스와 함수를 모아놓은 것.
   - 하나의 모듈은 하나의 파이썬 파일에 해당
   - 모듈을 읽어 들일때는 다음처럼 파일 앞에 import 구문 작성
   ```python
   import <모듈 파일 이름>
   ```
   - 추가로 모듈 내부에 있는 특정 함수나 특정 클래스만 읽어들일 수도 있음.
   - 다음처럼 작성하면 math 모듈에서 cos,sin,tan만 읽어들임
   ```python
   from math import cos,sin,tan
   ```