### 3. 객체 지향 프로그래밍 - 이어서
13. 객체의 동적생성
    1.  new와 delete를 이용하여 동적으로 변수나 배열을 생성할 수 있음
    2.  객체지향 관점에서 객체도 동적으로 생성할 수 있음
    3.  메모리 할당 요청(new)이 있을 경우 메모리가 있다면 요청이 승인되어 메모리가 할당됨
    4.  사용이 끝나면 메모리를 반납(delete)함. 반납을 하지 않더라도 에러는 발생하지 않지만 메모리 누수가 발생함
    5.  C언어는 malloc(), free() 로 동적 메모리를 할당함
    6.  C++언어는 new,delete로 동적 메모리를 할당함
    7.  객체의 동적 생성 및 접근 예제
        ```C++
        class Car //클래스(Car 생성)
        {
            public:
                bool key;
                int speed;

            speedUp{.....}
            int main() //메인 (main)함수
            {
                Car *pCar = new Car; //동적 객체 생성
                pCar->key = true; // 객체의 멤버벼수 접근
                pCar -> speed = 100;
                pCar -> speedUp(); // 객체의 멤버함수 접근
                return 0;
            }
        }
        ```
14. 접근자와 설정자
    1.  객체지향의 핵심은 클래스 안에 멤버변수를 감추는 것임
    2.  멤버변수가 public: 되는 것은 되도록 피해야 함
    3.  외부에서 멤버변수에 접근하고 싶을 경우 접근자와 설정자를 이용함
    4.  접근자는 멤버변수를 반환하는 return 형으로 메소드 명 앞에 get을 붙임
    5.  설정자는 멤버변수에 데이터를 기입하는 것으로 메소드명 앞에 set을 붙임
    6.  예) 접근자 : int getSpeed(), 설정자 : void setSpeed()
    7.  접근자 설정자 예제
        
        ```C++
        [설정자(Set)]
        class Car
        {
            bool key;
            int speed; //멤버변수 speed값 100

            public:
            void setSpeed(int s){  //전달받은 100을 s에 넣음
                speed = s; // s를 speed에 대입
            }
            int main()
            {
                Car car;
                Car.setSpeed(100); // setSpeed() 함수에 100 값 전달
                return 0;
            }
        }
        ```
        ```C++
        [접근자(get)]
        class Car
        {
            bool key;
            int speed; //리턴할 speed

            public
            int getSpeed(){ //호출받은 함수 int 리턴 타입
                return speed; // speed를 리턴
            }

            int main()
            {
                Car car;
                Car.getSpeed(); // :getSpeed() 함수 호출
                return 0  // speed값 리턴
            }
        }

        ```
        