### 클래스 연습
1. 1. 클래스 선언
   2. 객체 생성
   3. 멤버 호출
#### [Step 01:  클래스 선언 ]
```python
class Test: 
    # object의  후손 클래스가 되어 선조의 메소드들을 참조하고 있다.   
    #object <- Test
    def empty(self):
       self.data = [] 
    #리스트 객체를 초기화

    def add(self, x):
       self.data.append(x) 
    # x를 리스트 객체에 추가

```
#### [Step 02:  클래스 객체 생성  ] 
``` python
if __name__ == '__main__':
    my01 = Test()
 #__init__()가 내부 호출되면서 메모리에 Test클래스가 로드되어 생성된다.
    my02 = Test()
```
#### [Step03 :  멤버 호출]
```python
    my01.empty() #data 객체가 초기화된다.
    my02.empty()
    for  i in range(1,6): # 1 ~ 6 -1
        my01.add(i) 
        #data 객체에 1~5까지 추가된다
    print(my01.data) #출력
    print(my02.data) #빈 객체 출력
    print(my01, my02) #객체 주소 출력
    my03= my01 
    #my01에 있는 주소를 my03에 대입
    print(my03.data) 
    #my01에서 참조되는 곳을 참조하기 때문에 같은 데이터를 출력하게 된다.
    print(my01, my03) 
    #동일한 주소가 출력된다.
```
### 정적 변수 static 변수 와 클래스.멤버변수를 비교해보자
 - 멤버는 클래스.멤버
 - static 메소드로 선언 ->@staticmethod 선언

- q1) 이름 , 주소 , 전화 번호를 관리하는 Address 라는 클래스를 선언해서 변수로 값을 저장해 보자
 - 정적 변수 = static 변수  =  클래스.멤버변수
``` python
class Address:
    name="Dominica" #멤버
    addr = "seoul" #멤버
    tel ="02-0000-000" #멤버
    def prn(self):  # 멤버 메소드
        print(Address.name, Address.addr, Address.tel) 
        #print(self.name, self.addr, self.tel) 
# 클래스.멤버변수 -> static 형식 호출! (파이썬에서만)
        
if __name__ == '__main__':
    print(Address.name, Address.addr, Address.tel)
    Address.name ="1111111111111" 
    # 공유변수이므로 이를 넣어주면 둘 다 변함(static값)
    print(Address.name, Address.addr, Address.tel)

    a1 = Address() 
    #최초에는 Dominica가 출력, 이후에 111111~이 되는 이유는 static 형식으로 사용
    a1.prn()
```
#### object 클래스에서 상속받은 속성값을 사용해 보자.
   - `class type(object) = __class__`
