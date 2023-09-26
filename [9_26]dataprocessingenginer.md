### 3. 객체 지향 프로그래밍 - 이어서
9. 클래스란
   1.  C++에서 클래스를 선언하는 예약어는 class임
   2.  객체를 만들기 위해 필요한 틀을 클래스라 할 수 있음
   3.  클래스는 하나만 있어도 객체를 여러개 찍어낼 수 있음
   4.  Class 예
   ```C++
   class 클래스명{
                  멤버변수 : 현재 상태
                  
                  멤버함수 : 행동
   };
   ```
   5.  Class 설정
   <table>
        <tr>
            <th>텔레비전</th>
            <th colspan=2>상태</th>
            <th colspan=2>변수/함수</th>
        </tr>
        <tr>
            <td rowspan= 9>텔레비전</td>
            <td>전원</td>
            <td>ON</td>
            <td>bool switch</td>
            <td>True</td>
        </tr>
        <tr>
            <td>볼륨</td>
            <td>15</td>
            <td>int volume</td>
            <td>15</td>
        </tr>
        <tr>
            <td>채널</td>
            <td>7</td>
            <td>int channel</td>
            <td>7</td>
        </tr>
        <tr>
            <td>색상</td>
            <td>흰색</td>
            <td>string color</td>
            <td>white</td>
        </tr>
        <tr>
            <td colspan=2>전원 ON/OFF</td>
            <td colspan=2>switch(){....}</td>
        </tr>
        <tr>
            <td colspan=2>볼륨 올리기</td>
            <td colspan=2>volumeUP(){...}</td>
        </tr>
        <tr>
            <td colspan=2>볼륨 줄이기</td>
            <td colspan=2>volumeDown(){...}</td>
        </tr>
        <tr>
            <td colspan=2>채널교체</td>
            <td colspan=2>setChannel(){...}</td>
        </tr>
        <tr>
            <td colspan=2>색상변경</td>
            <td colspan=2>setColot(){...}</td>
        </tr>
   </table>
10. 객체란
    1.  사물을 관찰한 후 데이터 추상화함
    2.  현실세계의 사물을 데이터적인 측면과 기능적인 측면을 통하여 정의함
    3.  실제 세계를 모델링하여 소프트웨어로 구현하는 방법임
    4.  객체는 상태와 행동으로 이루어짐
    5.  객체지향 프로그래밍에서는 자료와 이의 처리 동작을 하나로 묶어서 다룰수 있는 객체(object)라는 개념을 도입함
    6.  프로그램은 처리하는 절차보다도 동작되는 자료에 중점을 둔 객체, 객체 간의 상호관계로 표현함
11. 접근 지정자
    1.  클래스는 크게 클래스 선언과 클래스 멤버함수 정의로 구성되어 있음
    2.  클래스 선언에는 멤버변수와 멤버함수 원형을 정의함
    3.  멤버함수 정의는 클래스 선언 밖에서 따로 이루어짐
        <table>
            [접근 지정자]
            <tr>
                <th>구분</th>
                <th>클래스 내 접근</th>
                <th>클래스 외에서의 접근</th>
            </tr>
            <tr>
                <td>private</td>
                <td>O</td>
                <td>X</td>
            </tr>
            <tr>
                <td>public</td>
                <td>O</td>
                <td>O</td>
            </tr>
        </table>
    4. private :
       - 해당 멤버가 속한 클래스의 멤버함수에서만 사용 가능하며, 캡슐화(데이터 은닉)됨
       - 클래스는 접근 지정자가 생략되면 디폴트로 private가 적용됨
       - 일반적으로 멤버 변술르 private으로 설정하여 외부에서 직접 변수 데이터에 접근하는 것을 막음.(데이터 은닉)
    5. public :
       - 객체를 사용할 수 있는 범위라면 어디서나 접근 가능한 공개된 멤버로, 주로 private 멤버를 해당 클래스 외부에서 사용하도록 하기 위한 멤버함수를 정의할 때 사용함
       - public 멤버로 지정하기 위해서는 public: 을 명시적으로 기술하여야 함. 클래스 내의 멤버함수에서는 물론 객체가 선언되어 있는 영역이라면 어디서든지 객체명 다음에 멤버참조 연산자(.)로 연결하여 멤버함수를 사용할 수 있음.
12. 객체 생성과 멤버 접근
    1. 객체 선언
       - 완성된 클래스를 이용하려면 객체를 정의 하여야 함
       - int나 string, double처럼 class도 하나의 타입임
       - Car 클래스 타입의 변수 myCar를 선언함
    2. 객체 선언의 예(정적 선언)
        ```C++
        Car myCar ; //class Car를 이용하여 myCar 객체 선언
        ```
    3. 생성된 객체를 클래스의 인스턴스라 부름
    4. 선언된 객체 myCar에 접근을 하여 멤버를 호출하려면
        ```C++
        myCar.speed=10; //speed 변수는 private로 선언되어 접근이 제한됨
        myCar.onSwitch(); // onSwitch() 함수는 public으로 선언되어 접근이 가능함.
        ```
    5. 객체지향의 개념으로 보면 클래스의 멤버변수를 직접 접근하는 것은 좋지 않으며 멤버함수를 이용하여 간접적으로 접근을 하는 것이 객체 지향의 개념임