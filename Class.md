# 클래스 (Class)
  - 모든 클래스는 __builtin__모듈에 있는 object 클래스의 하위 클래스가 된다.
  - object 클래스는 생성자, 소멸자, 연산 메소드(연산 overload),__str__등  클래스로 만들어진 속성 및 기능을 편리하게 사용할 수 있는 메소드를 제공한다.
 - class UserName(object): 로 사용된다.

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
- q05) 다음과 같은 주소록을 클래스로 구현해보자.
   - case 01) 생성자로 값을 전달하고 출력 (생성과 동시에 값 전달)
     - 클래스 이름:My_Address
     - 레코드 설계(한 줄 단위)

   | name 이름   | addr 주소 | phone 전화번호  |  클래스명|
   |---|---|---|---|
   | 홍길동  |서울  |02-000-0000 |a1 |
    |정길동 | 인천 | 031-000-000| a2|
    |박길동 | 부산  |054-000-0000| a3|

    - 방법:
    - 방을 만들어놓고 변경 (초기값 -> 변경)
    - 방을 만들때부터 추가 (기본값 = 변경예정 값)
```python
class My_Address:
    #생성자 명시 :멤버 변수를 초기화하면서 객체를 생성할 때 단 한번만 명시 호출
    def __init__(self,name,addr,phone): #생성자
        self.name=name
        self.addr=addr
        self.phone=phone
        
    def prn(self): #출력
        print(f'{self.name} \t {self.addr} \t {self.phone} \n')
        

a1 = My_Address('홍길동','서울','02-000-0000')
a2 = My_Address('정길동','인천','031-000-0000')
a3 = My_Address('박길동','부산','054-000-0000')

a1.prn()
#print 했을때 none이 나오는 이유:return이 없기 때문에
a2.prn()
a3.prn()

#이 경우에는 특정 부분 출력, 추출, 변경이 불가능함. 기능 설계에 따라 member 변경.
```
- case 02) 생성자로 값을 전달하고 출력, 값을 변경해보자
```python
#조건 1) 초기값 대입후 전체 출력
#조건 2) 홍길동의 이름을 '최길동'으로 변경 후 출력
#조건 3) 박길동의 주소 '부산'을 '제주도'로 변경 후 출력
#조건 4) 정길동의 번호 '031-000-0000'을 '010-0000-0000'으로 변경 후 출력
# get과 set을 이용한다.
#설계 : 값 전달 및 변경 set 멤버 변수로 결합, 값 리턴은 get 멤버 변수로 사용 
class My_Address02:
    def __init__(self,name,addr,phone):
     #생성자, 멤버변수 초기화 
        self.name=name
        self.addr=addr
        self.phone=phone
        
    def prn(self): 
        print(f'{self.name}\t{self.addr}\t{self.phone}\n')
    #1)이름 변경 후 리턴하는 메소드 추가
    
    def setName(self,name):
        self.name = name 
    #전달받은 name 값으로 self.name 값 전달 및 변경
    def getName(self) :
        return self.name
    #2)주소 변경 후 리턴하는 메소드 추가
    
    def setAddr(self,addr):
        self.addr = addr 
    #전달받은 addr 값으로 self.addr 값 전달 및 변경
    def getAddr(self) :
        return self.addr
    #2)전화번호 변경 후 리턴하는 메소드 추가
    
    def setPhone(self,phone):
        self.phone = phone 
     #전달받은 phone 값으로 self.phone 값 전달 및 변경
    def getPhone(self) :
        return self.phone
#조건 1) 초기값 대입후 전체 출력
a1 = My_Address02('홍길동','서울','02-000-0000')
a2 = My_Address02('정길동','인천','031-000-0000')
a3 = My_Address02('박길동','부산','054-000-0000')

a1.prn() 
a2.prn()
a3.prn()
#조건 2) 홍길동의 이름을 최길동으로 변경 후 출력
a1.setName('최길동')
print(a1.getName())
a1.prn() #전체 레코드로 확인
#조건 3) 박길동의 주소 '부산'을 '제주도'로 변경 후 출력
a3.setAddr('제주도')
print(a3.getAddr())
a3.prn() 
#조건 4) 정길동의 번호 '031-000-0000'을 '010-0000-0000'으로 변경 후 출력
a2.setPhone('010-0000-0000')
print(a2.getPhone())
a2.prn() 
print(dir(a1))
print(help(a1.setPhone))
print(help(a1.getPhone))
print(help(a1))
```
- bulitins.object <- 기본적으로 내장되어 상속

- My_Address02(name, addr, phone) <생성자 표시
  

1. 멤버 접근 : 클래스 멤버와 인스턴스 멤버
    1. 클래스 멤버
```python
class MyClass:
    cl_mem = 100         # 클래스 멤버
    cl_list = [1,2,3,4]  # 클래스 멤버
    a = 'Hi'             # 클래스 멤버

# 클래스 객체를 통해서  직접 접근    (static) (값을 전달하는 변수 외부 노출 X, 일반적 경우)
print(MyClass.cl_mem)
print(MyClass.cl_list)
print(MyClass.a)    

# 변경
MyClass.cl_mem = 300
print(MyClass.cl_mem)

# 인스턴스 객체를 통해서 접근 (non -static) (단순 전달일때 권장, 복잡하지 않고 단순할때)
m1 = MyClass()   #  인스턴스의 생성
print(m1.cl_mem)
m1.cl_mem = 500
print(m1.cl_mem)       # 500
print(MyClass.cl_mem)  # 300

m2 = MyClass()   #  인스턴스의 생성
print(m2.cl_mem)
m2.cl_mem = 700
print(m2.cl_mem)       # 700
print(m1.cl_mem)       # 500
print(MyClass.cl_mem)  # 300
```
2.인스턴스 멤버의 구현과 접근 : 클래스의 메서드 내에 구현한 멤버

#### 생성자 메서드의 구현
```python
class MyClass2:
    def __init__(self,a,b): 
# 생성자 메서드,인스턴스 객체를 생성할 때 자동으로 호출, 인스턴스 멤버 초기화 
# 변수명을 self 대신 다른 이름으로 써도 가능하다 
# self는 파이썬 내장 예약어는 아님
#제일 첫번째를 무조건 자기 자신으로 잡기 때문
        print('MyClass2 생성자가 호출됨')
        print('__init__ :',self,a,b)
        
m1 = MyClass2(10,20)    # 인스턴스 생성    
print('m1:       ',m1)  
```
- 결과값
```python
MyClass2 생성자가 호출됨
__init__ : <__main__.MyClass2 object at 0x0000021B19104850> 10 20
m1:        <__main__.MyClass2 object at 0x0000021B19104850>
```
- keyword에서 self 확인
```python
import keyword
print(keyword.kwlist)
#키워드에는 존재하지 않음
self=200
self  
```
- self는 변수 취급 됨, 그러나 함수 내에서 특별한 별칭을 가진 연산자!
3. 인스턴스 멤버의 생성과 초기화 : 생성자 메서드에 구현
```python
class MyClass2:
    def __init__(self,var1): 
    # 생성자 메서드, 인스턴스 메서드, 
    # 첫인자는 인스턴스 자신 self(this)=현재 오브젝트를 지칭하는 연산자 
        print('MyClass2 생성자가 호출됨')
        self.in_mem = 0        # 인스턴스 멤버
        self.in_list = [0]     # 인스턴스 멤버
        self.a = var1          # 인스턴스 멤버

m1 = MyClass2(50)    # 인스턴스의 생성
print(m1.in_mem)     
# 인스턴스의 멤버의 접근, 인스턴스를 통해서 접근가능
print(m1.a)
m1.in_mem = 1        # 인스턴스 멤버의 값을 변경
m1.a = 80
print(m1.in_mem)     # 1 
print(m1.a)          # 80
#m1와 m2 비교, 
m2 = MyClass2('Hi')   # 인스턴스의 생성
print(m2.in_mem)      # 0 
print(m2.a)           # 'Hi'

print(m1.in_mem)     # 1 
print(m1.a)          # 80
```

4. 인스턴스 메서드의 구현 : 생성된 인스턴스를 통해서 호출이 가능 <<생성자와 소멸자 확인>>
```python
class MyClass2:
    def __init__(self,var1): 
    # 생성자 메서드, 인스턴스 메서드, 첫인자는 인스턴스 자신
        print('MyClass2 생성자가 호출됨')
        self.in_mem = 0         #인스턴스 멤버를 초기화 
        self.in_list = [0]     
        self.a = var1         
        
    def set(self,var1,var2):  
    #초기화가 되어있는 멤버변수의 값 전달 및 변경 하기 메소드
        print('set 메서드가 호출됨')
        self.in_mem = var1  #인스턴스 멤버를 변경    
        self.a = var2         #인스턴스 멤버를 변경     
         
    def get(self):            #리턴을 하기 위한 메소드 
        print('get 메서드가 호출됨')
        return self.in_mem,self.a
    
    def __del__(self):   
    # 소멸자 명시    
    #명시 안되어있으면 기본 소멸자 호출, 명시 된 경우 내장 소멸자 호출
        print('MyClass2 소멸자가 호출됨')
        
m1 = MyClass2(0)  
print(m1.in_mem,m1.a)  

m1.set(30,40)    
print(m1.in_mem,m1.a)   

a,b = m1.get()    
print(a,b)             

del m1 
```
- 결과값
```python
MyClass2 생성자가 호출됨
0 0
set 메서드가 호출됨
30 40
get 메서드가 호출됨
30 40
MyClass2 소멸자가 호출됨
```
   
