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