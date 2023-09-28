### 3. 객체 지향 프로그래밍 - 이어서
15. 멤버함수의 중복정의(오버로딩 : overloading)
    1.  멤버함수도 함수이므로 중복정의가 가능함
    2.  중복정의는 이름은 같지만 인수의 타입이나 숫자가 다른 것임
    3.  타입이 같은 형태의 중복 정의는 할 수 없음. 아래 표의 6번은 2번과 같은 타입으로 충돌이 발생
    4.  중복 함수 생성 예제
        ```C++
        class Car
        {
            public:
                bool key;
                int spped;

                void setSpeed(); // 1. 인수 없는 함수
                void setSpeed(int n); // 2. 하나의 정수형 인수를 가진 함수 생성
                void setSpeed(double s); // 3. 하나의 더블형 인수를 가진 함수 생성
                void setSpeed(int n, double s); // 4. 두 개의(정수, 더블) 인수르 가진 함수 생성
                void setSpeed(double s, int n); // 5. 두 개의 (더블, 정수) 인수를 가진 함수 생성
                void setSpeed(int s); //6. : 2 와 같은 타입의 인수를 가진 함수이므로 중복 정의 안됨 에러발생
        }
        ```
16. 반환형이 다른 중복 함수
    1.  반환형이 다르더라도 인수의타입과 숫자가 같을 경우 중복이 불가능함
    2. 함수의 중복은 인수의 타입이 중요함
    3. 반환형이 다른 중복 예제
        <table>
            <tr>
                <td>void setSpeed(){...}; <br> int setSpeed(){ ...};</td>
                <td>반환형이 다르지만 인수의 수와 타입이 같으므로 중복 불가</td>
            </tr>
            <tr>
                <td>void setSoeed(){int s}; <br> int setSpeed(){double n};</td>
                <td>반환형은 다르지만 인수의 타입이 다르므로 중복 가능</td>
            </tr>
        </table>
    4. 함수의 중복정의와 사용 예제
        ```C++
        #include<iostrean>
        using namespace std;

        class Car{
            boolkey;
            int speed;
            string color;

            public:
                void setSpeed(int s) { // 정수형 인수를 가진 함수
                    speed = s;
                }
                void setSpeed(double s){ //더블 인수를 가진 함수
                    speed = s;
                }
                int getSpeed(){
                    return speed;
                }
        };
        int main()
        {
            Car myCar;      //객체 생성
            myCar.setSpeed(80);     //정수형 인수 객체 초기화
            cout << "차의 속도:" << myCar.getSpeed() << endl; // 정수형 리턴
            myCar.setSpeed(100.0); // 더블형 인수 객체 초기화
            cout << "차의 속도 :" << myCar.getSpeed() << endl; //더블형 리턴
            return 0;
        }
        ```
17. 생성자
    1.  객체가 생성될 때 호출됨
    2.  기본 자료형으로 변수를 선언할 때 선언과 동시에 값을 주는 것을 초기화라 함. 객체를 생성할때 초깃값을 주는 것이 생성자.
    3.  생성자명은 클래스명과 동일하며 반환형이 없음
    4.  생성자의 객체를 선언(생성)할 때 컴파일러에 의해 자동으로 호출됨. 객체의 초기화란 멤버변수의 초기화를 의미함
    5.  생성자(constructor): 객체가 생성될 때에 필드에게 초기값을 제공하고 필요한 초기화 절차를 실행하는 멤버 함수임
    6.  생성자 기본 구조
        ```C++
        class Car
        {
            public:
                Car(){ //생성자 정의
                }
        }
        ```
    7.  생성자 특징
        - 클래스 이름과 동일하며 반환값이 없음
        - 객체 생성과 동시에 실행이 되기에 외부 접근이 가능하도록 public 이어야 함
        - 중복 정의할 수 있음
        - 정의하지 않을 경우 컴파일러는 외부에서 접근이 가능한 비어있는 디폴트 생성자를 자동으로 추가함
        <table>
            <tr>
                <th>생성자가 없는 클래스</th>
                <th>생성자 자동 추가</th>
            </tr>
            <tr>
                <td>class Car {
                <br>  &nbsp&nbsp bool key;
                <br>  &nbsp&nbsp int speed;
                <br>  &nbsp&nbsp string color
                <br>};
                </td>
                <td>class Car {
                <br>  &nbsp&nbsp bool key;
                <br>  &nbsp&nbsp int speed;
                <br>  &nbsp&nbsp string color
                <br>public:
                <br>Car(){&nbsp&nbsp&nbsp&nbsp&nbsp}
                <br>};
                </td>
            </tr>
        </table>
    8.   기본 생성자 예제
        ```C++
        class Car
        {
                bool key;
                int speed;
                string color;
            public:
                Car()  // 기본(Default) 생성자
                {
                    key = true; //멤버변수 초기화
                    speed = 10;
                    color = "white";
                }
        };

        int main()
        {
            Car myCar;  // 객체의 생성과 동시에 기본(Default) 생성자
            return 0;
        }
        ```
18. 소멸자
    1.  객체가 소멸될 때 자동으로 호출됨
    2.  객체를 정리해주는(리소스를 해제한다든지 하는 작업) 멤버변수임
    3.  객체가 파괴될 때(더이상 사용되지 않을때, 파괴될 때) 자동 호출됨
    4.  소멸자 함수는 멤버함수임
    5.  소멸자 함수명도 생성자처럼 클래스명과 같으며 함수명 앞에 ~ 기호가 붙음
    6.  소멸자는 반환값이 없음
    7.  소멸자는 전달 매개변수(인수)를 지정할 수 없으며 오버로딩도 할 수 없음.
    8.  정의하지 않을 경우 컴파일러는 외부에서 접근이 가능한 비어있는 디폴트 생성자를 자동으로 추가함
    9.  소멸자 기본 구조
    ```C++
    class Car
    {
        public:
            ~Car()  //소멸자 정의
            {                
            }
    };
    ```