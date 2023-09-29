### 3. 객체 지향 프로그래밍 - 이어서
19. this 포인터
    1.  this는 현재 코드를 실행하는 현재 객체를 가리키는 포인터임
    2.   this는 컴파일러에 의해 자동으로 생성이 되며 명시적으로 선언할 필요가 없음.
    3.   멤버변수를 사용할 때 컴파일러는 암묵적으로 this$\rarr$를 붙임
    4.   암묵적 this 포인터
        ```C++
        void setSpeed(int s)
        {
            this -> speed = s;  //컴파일 시 암묵적으로 생성된 this →
        }
        ```
    5.   암묵적으로 this 포인터가 생성은 되나 내부 함수에같은 이름의 변수가 있을 경우 this$\rarr$는 붙지 않음
    6.   this 포인터 예제
        ```C++
        //this 포인터를 사용하지 않을때
        class Car
        {
            bool key;
            int speed;

            public:
            void setSpeed(int speed){
                speed = speed;
            }
            int getSpeed(){
                return speed;
            }
        };
        int main()
        {
            Car car;
            car.setSpeed(100);
            cout << car.getSpeed();
            return 0;
        }
        ```
        ```C++
        -838993460 //setSpeed 값이 아닌 값이 지정됨
         ```
         ```C++
         // this 포인터를 사용할 때
         class Car
        {
            bool key;
            int speed;

            public:
            void setSpeed(int speed){
                This->speed = speed;
            }
            int getSpeed(){
                return speed;
            }
        };
        int main()
        {
            Car car;
            car.setSpeed(100);
            cout << car.getSpeed();
            return 0;
        }
         ```
         ```C++
         100 //올바른 값
         ```
20. 상속의 정의
    1.  상속은 코드를 재사용하기 위한 중요한 기법임
    2.  기존 클래스의 속성과 기능을 이어받아 자신의 기능을 추가하는 기법임
    3.  상속을 통하여 기존 클래스의 필드아 메소드를 재사용
    4.  기존 클래스의 일부 변경도 가능함
    5.  상속은 이미 작성된 검증된 소프트웨어를 재사용을 할 수 있게 해줌
    6.  신뢰성 있는 소프트웨어를 손쉽게 개발, 유지 보수 코드의 중복을 줄일 수 있음.
    7.  상속 기본구조
        ```C++
        class Car
        {
            int speed;
        }
        class taxiCar : public Car //Car 클래스를 taxiCar 클래스가 상속
        {
            int meter;
        }
        ```
    8. 상속관계 도식
       - taxiCar : 자식 클래스
         - int meter
         - Car : 부모 클래스
           - int speed;
    9. 상속관계 예제
        ```C++
        class Car { //Car 클래스
            int speed;
            bool switch;
        
            public:
                void setSpeed(int s){ //setSpeed 멤버 함수
                    speed += sl
                }
                void setSwitch(int sw){ //setSwitch 멤버 함수
                    switch = sw;
                }
        };
        class taxi : public Car{ //Car 클래스 상속
            int meter
            
            public:
                void setMeter(int m){
                    meter=m;
                }
        };

        int main()
        {
            taxi taxi;
            taxi.setSwitch(True); // 부모클래스 멤버 함수 호출
            taxi.setSpeed(10); // 부모클래스 멤버 함수 호출
            taxi.setMeter(100); // 자식클래스 멤버 함수 호출
            retrun 0;
        }
        ```
    21. 상속이 필요한 이유
        1.  상속을 사용하면 중복 코드를 줄일 수 있음
        2.  공통적인 클래스의 중복을 최소화 할 수 있음
        3.  공통 부분이 하나로 정리되어 관리가 쉬움
        4.  유지보수도 쉽고 변경도 쉽게 할 수 있음
        5.  중복되는 클래스는 부모클래스에 모음
        - 예시( 상속 클래스 관계)
          - 부모 클래스
            ```C++
            class 캐릭터{
                변수
                행동()
            }
            ```
          - 자식 클래스
            - 
            ```C++
            class 전사{
                전사변수
                전사행동()
            }
            ```
            - 자식의 자식 클래스
                ```C++
                class 전사2차전직{
                    전사2차변수
                    전사2차행동()
                }
                ```
            ```C++
            class 마법사{
                마법사변수
                마법사행동()
            }
            ```
            ```C++
            class 사제{
                사제변수
                사제행동()
            }
            ```