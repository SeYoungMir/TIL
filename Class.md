# 클래스 (Class)
  ## 파이썬의 클래스 관련 용어
    1. 클래스(class): class 문으로 정의하며, 멤버와 메서드를 가지는 객체, 새로운 이름 공간을 갖는 단위
    2. 클래스 객체(class object): 클래스와 같은 의미
    3. 클래스 인스턴스:클래스를 호출하여 생성된 객체
    4. 클래스 인스턴스 객체: 클래스 인스턴스와 같은 의미
    5. 멤버: 클래스 혹은 클래스 인스턴스 공간에 정의 된 변수
    6. 메서드 : 클래스 공간(heap 공간 =class영역= 자유 영역공간)에 정의된 함수, def 사용
    7. 속성(Attribute):멤버와 메서드 전체를 가리킨다
    8. 상속: 상위 클래스의 속성과 행동을 그대로 받아들이고 추가로 필요한 기능 작성
    9. Instance of ~~의 것
   
### 클래스의 생성 기본
```python
class UserName: #class {클래스 이름}:
    value,function....
```
- 클래스 생성, 선언(함수, 변수 포함)
```python

class Simple:
    pass

print(simple) 
```
- 결과값
```bash
<class '__main__.Simple'>
```
- 인스턴스 클래스 생성
```python
s1 = Simple()
s2 = Simple()

print(f'{s1}\n{s2}')
```
- 결과값
```bash
<__main__.Simple object at 0x000001C235B01F10>
<__main__.Simple object at 0x000001C236EBA6A0>
```
### self 연산자
- q1) U_class라는 이름으로 합을 구하는 클래스를 선언해보자.
- self -> 현재 오브젝트를 지칭하는 연산자
```python
class U_class:
    a=0  #멤버변수 선언
    b=0
    
    def ssum(a,b): 
        #self가 없으면 본인을 포함하지 않음.오류 발생(첫번째 a가 self로 인지)
        # self.a = a
        # self.b = b 
        #전역변수를 멤버변수에 대입, 위와 같이 설정 하면 제대로 출력됨
        #return self.a+self.b <멤버변수를 가져옴 (멤버 변수)
        return a+b  
        #self는 메소드 매개인자로 첫 인자는 클래스의 주소를 가진 의미로 self 명시
    def sum(self,a,b,/): 
        #이 때 a,b는 지역변수            
        #self가 없으면 본인을 포함하지 않음.오류 발생(첫번째 a가 self로 인지)
        #/를 추가하면 indexing의 뜻, 순서를 지켜라.
        return a+b 
        
       
         
r = U_class()
print(r) #객체의 주소를 16진수로 리턴
print(dir(r)) #목록 확인
print(help(r.sum)) #메소드 확인법 확인
print(help(r.ssum)) 
print(r.sum(100,200)) #메소드 호출
print(id(r)) #주소 호출
print(hex(id(r))) #주소를 16진수로 바꾸어 확인
```

- q2)객체를 생성할 때 값을 전달하는 생성자를 사용하자.
```python
class U_class01:
    def __init__(self,num): 
    #__init__을 호출하도록, 생성자
        print(num)
        
r=U_class01(100) 
#__init__으로 값 전달.클래스는 객체를 생성하면서 값 전달
```
- q3) q2랑 동일하게 int 클래스에 객체를 생성하면서 값을 100 전달해보자
```python
print(dir(int))
print(help(int.__init__))
#help(int) # __int__가 __init__ 대신 사용됨

r=100 
#기본 자료형은 값을 대입 , r=int(100) 와 동일 
print(r)
```

- q4)self 키워드로 멤버 변수를 접근해보자
``` python
class U_class03: 
    a=0 
    #클래스 멤버변수는 멤버 메소드에서 self로 접근(호출)할 수 있다.
    b=0
    def setsum(self,a,b,/):  #이 때 a,b는 지역변수 (<-함수안에 들어있는 변수,메소드)
        self.a = a
        self.b = b 
    #전역변수 (<-멤버,지역변수이기도 함, self로 접근 가능하므로 전역임)를 멤버변수에 대입, 이렇게 하면 제대로 출력됨
    def getsum(self): 
    #self < 자기 주소를 지칭, 자기 주소 영역 내에서 지칭할때는 self.
    #self가 없으면 오류 (특수한 경우가 없으면 self를 반드시 단 한번 가져야한다)
        return self.a+self.b
my_res =U_class03();
my_res.setsum(100,200)
print(my_res.getsum())
print('-'*15)
print(dir(my_res))
print('-'*15)
print(my_res)
print(id(my_res))  
#참조관계, 시작 주소를 줌 <4byte마다 1개의 주소이므로 이를 index하여 찾아갈 수 있음.
```