## 파이썬 클래스의 메서드
    1. 일반 메서드(인스턴스 메서드)  : self인자로 시작
    2. 정적 메서드(static method) 
       -  @staticmethod , 인스턴스를 만들지 않아도 호출 가능
    3. 클래스 메서드(class method) 
        - @classmethod  , 인스턴스를 만들지 않아도 호출 가능, 첫 인자가 클래스 객체
-   static method (누적 공유) 
    -   선언과 동시에 주소가 생성되어 bind된다 (공유변수 or 누적값)
        - static, class, struct, union, userFunction.

- instance method (객체 단위 생성)
```python
class M:
    @staticmethod    
 #생성 시 바로 M과 M.a()의 주소가 S.S영역에 고정
    def a():
        pass
        
class Y:
    def b(self):    
#생성 시 Y의 주소만 S.S 영역에 생성, 객체 선언을 해야 b 생성
        pass
##==========
M.a()
# m1 =M() m1.a() <-이미 생성된 걸 또? 2중작업, 비효율적
a1= Y();a1.b()
#===========
m1=M(),m2=M(),m3=M() 
#객체가 공유하는 M(), 같은 주소
y1=Y(),y2=Y(),y3=Y() 
#객체당 다른 b 생성 (자유 영역) ,다른 주소
```
 1.일반 메서드(인스턴스 메서드) 
- 인스턴스 객체를 통하여 접근 
- 메서드의 첫인수로 self를 사용
```python
  class MyClass:
    def add(self,a,b):
        return a + b
m1 = MyClass() 
m1.add(10,20)
```
2.정적 메서드(static method)
- 장식자 @staticmethod를 메서드 앞에 반드시 사용
- 인스턴스를 만들지 않아도 호출 가능
- 메서드의 첫인수로 self를 받지 않는다
- 목적: 누적 데이터, 공유 변수 
```python
class MyClass:
    @staticmethod  # @: decorator, 장식자
    def add(a,b):         # 정적 메서드
        return a + b
    
print(MyClass.add(10,20)) 
# 인스턴스 객체 없이 클래스를 통하여 직접 호출 (클래스 명,스태틱 멤버)

m1 = MyClass()
print(m1.add(30,50))     
# 인스턴스 객체를 통하여 호출 가능(가능은 하지만 비권장)

print(id(MyClass),id(m1))
```
3.클래스 메서드(class method) 
- 장식자  @classmethod 를 메서드 앞에 반드시 사용
- 인스턴스를 만들지 않아도 호출 가능, 첫 인자가 클래스 객체
```python
class MyClass:  
    #자기가 자기 자신을 명시 호출할 때)
    cl_mem = '클래스멤버'
    @classmethod
    def add(cls,a,b):    
# 클래스 메서드,  클래스 멤버와 같이 사용, cls는 클래스 객체
        return a + b,cls.cl_mem 
    
print(MyClass.add(10,20)) 
# 인스턴스 객체 없이 클래스를 통하여 직접 호출

m1 = MyClass()
print(m1.add(30,50))      
# 인스턴스 객체를 통하여 호출 가능
```
## 클래스 상속
- 클래스 A에서 상속된 클래스 B가 있다고 할때
  - 클래스 A
    -  기반(Base) 클래스
    -  부모(Parent) 클래스
    -  상위(Super) 클래스
  - 클래스 B
    - 파생(Derived) 클래스
    - 자식(Child) 클래스 
    - 하위(Sub) 클래스
  
### Class Diagram

- 단일 Class

**기본적으로 모든 class는 object를 상속**

|builtins.object|   
|:---:|
|   |
- (기본 상속)

|Class이름|
|:---:|
|멤버 변수|
|멤버 메소드|
 
 ---
 |선조 |
 |:---:|
 |self|
    |
단일 상속
   
    V
|후손 |
|:---:|
| self, super|

---

|선조 1|  선조 2|
|:---:|:---:|
| self|  self  |

    \  /

   다중 상속

     V

|후손|
|:---:|
|self, super.선조1 super.선조2 |

### 다형성 예시
- 2과목 일때
  
|getTot()|
|---|
|(2)|
= a1

-3과목 일때

|getTot()|
|---|
|(3)|

 = b2

- 4과목 일때

|getSum()|
|---|
|(4)|

= c4

- 5과목 일때

|getTot()|
|---|
|(5)|

 = e5
 
- 위 처럼 합 계산을 여러개로 만들어질 때를 방지
- getTot()-> 합 (base Class로 지정)

이때 base : 추상
 
 getTot()를 강제 상속

- 위의 모든 것을 getTot()으로 불러지도록 통일화.
- 불러질때는 하위 개체를 가져오도록, 메소드 명을 통일.

|getTot()|
|---|
|base|

- 위의 것들이 getTot()을 재정의(override)
- 메소드 명 통일 
- 선조를 통해서 후손의 객체 멤버를 호출하겠다.

### override의 예시 
 |선조 |
 |:---:|
 |self|
 |getTot() 9과목 총점|
 
    |
단일 상속

    V

|후손 |
|:---:|
| self, super|
|getTot():super.getTot()+내 과목|


**기능 확장할 때 유용**

- 기능이 하나 = 함수
- 함수의 원형은 = 기능
- 객체 안에 함수가 들어갔을때 = 메소드
- 객체에 함수가 여러개 = 클래스

```python

class A:
    pass
class B(A):
    pass
```
- 단일 상속의 기본 형태

```python

class ances1:
    pass
class ances2:
    pass
class son(ances1,ances2):
    pass
```
- 다중 상속의 기본 형태

**후손은 선조를 알 수 있지만 선조는 후손을 알 수 없음!**

- C에서는 되지만 python에서는 되지 않는 것
    - **후손(형제)끼리는 호출 X, 선조와 후손의 관계만 있음**
- C계열, python에서는 다중 상속 가능, Java에서는 불가능
- 부모(상위,super,base) 클래스 #
  - 단일 클래스와 동일
```python
Class Person:
    def __init__(self,name,phone=None):
        self.name = name               
        self.phone = phone              
        
    def get_info(self):                
        return self.name,self.phone

p = Person('홍길동','010-1234-1234')   
print(p.get_info())                    
print(p.name,p.phone)                   
print(Person.__bases__)                
```
- 결과값
```python
('홍길동', '010-1234-1234')
홍길동 010-1234-1234
(<class 'object'>,)
```

- 자식(하위) 클래스
```python

class Employee(Person):  
 # 상속받은 부모클래스를 괄호안에 표현
    def __init__(self,name,phone,position,salary): 
    # 생성자
    # Person.__init__(self,name,phone) #두가지의 방법.
        super().__init__(name,phone)  
    # 부모 클래스의 생성자를 호출
        self.position = position
        self.salary = salary 
        
    def get_info(self):  
    #선조가 가진 메소드를 재정의 (override)
        ret = super().get_info()
        return ret,self.position,self.salary
```
- super() 메서드 
  - 현재 클래스의 상위(부모) 클래스를 얻어 낸다   
- 예시
```python
m1 = Employee('김','1111','과장',500)
print(m1.get_info())
```
-결과값
```python
(('김', '1111'), '과장', 500)
```
- q6)상속의 선조를 찾아보자.
```python
class My_test: #클래스 생성
    pass
```   
```python
print(dir(My_test))
#결과값
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
```python
print(help(My_test)) #이 때 bulitins.object가 선조!
#결과값
Help on class My_test in module __main__:

class My_test(builtins.object)
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None

```
```python
print(dir(__builtins__)) #object를 확인
print('='*15)

print(help(__builtins__.object)) # The base class of the class hierarchy.
```
### Override
```python
class MyClass:
    def getPrn(self):
        print('현재 클래스가 표현할 수 있는 기본 값')
        
MyClass().getPrn()
m1=MyClass()
m1.getPrn()
#결과값
현재 클래스가 표현할 수 있는 기본 값
현재 클래스가 표현할 수 있는 기본 값
```
```python
class MyClass:  
#상속의 확인, 상속 __str__을 재정의, 명시호출하여 변경
    def __str__(self):
        return '현재 클래스가 표현할 수 있는 기본 값'
MyClass()
m1=MyClass()
m1.__str__()
print(m1) 
#결과값
현재 클래스가 표현할 수 있는 기본 값
현재 클래스가 표현할 수 있는 기본 값
```
- 위와 아래 코드를 비교해보자
```python
class MyClass:
    pass
MyClass()
m1=MyClass()
m1.__str__()
print(m1) #객체를 호출해서 출력하면 원래는 주소가 출력,재정의 하여 __str__이 리턴
print(m1.__str__())
#결과값
<__main__.MyClass object at 0x000001C236A0A880>
<__main__.MyClass object at 0x000001C236A0A880>
```
- int에서 __init__과의 재정의 구조 살펴보기
```python
res = int(300) 
#선조가 object/ __str__ -> __init__으로 받은 초기값을 리턴하도록 재정의
print(res)
print(res.__str__())
```