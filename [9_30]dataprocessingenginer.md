### 3. 객체 지향 프로그래밍 - 이어서
22. 접근 지정자
    1.  상속을 하기 전까지는 publi, private 2가지 접근 지정자를 사용하였다
    2.  접근 지정자 protected는 상속을 받은 클래스는 public 처럼 사용이 가능하고 상속을 받지 않은 클래스는 private같이 외부에서 접근을 하지 못한다.
23. 상속 관계의 생성자 소멸자
    1.  자식 클래스가 호출될 때 부모 클래스도 호출됨
    2.  부모 클래스 생성자가 먼저 실행되고 자식 클래스 생성자가 실행됨
    3.  자식 클래스의 소멸자가 먼저 실행되고 부모 클래스의 소멸자가 실행됨
    - 상속 관계에서 생성자와 소멸자
      - 객체가 생성될 때
        - 부모 생성자 실행
        - 자식 생성자 실행
      - 객체가 소멸될 때
        - 자식 소멸자 실행
        - 부모 소멸자 실행
    - 상속 관계 생성자 소멸자 실행 순서
        ``` C++
        class Point {
            int x, y;
            
            public:
                Point(){
                    cout << "Point 생성자() " << endl; // 부모 생성자 실행
                }
                ~Point() {
                    cout << "Point 소멸자()" << endl; //부모 소멸자 실행
                }
        };

        class Shape : public Point {
            int width,height;
            
            public:
                Shape(){
                    cout << "Rectangle 생성자() " << endl;//자식 생성자 실행
                }
                ~Shape(){
                    cout << "Rectangle 소멸자() " << endl;// 자식 소멸자 실행 
                }
        };
        int main()
        {
            shape s; // 객체 s 생성
            return 0;
        }
        ```
24. 재정의(Overriding)
    1.  상속받은 멤버함수의 변경 시 사용함
    2.  자식 클래스가 필요시 상속된 멤버 함수를 재정의함
    3.  멤버함수의 헤더는 그대로 두고 몸체만 교체하는 것임
    4.  부모 클래스의 멤버 함수와 같은 함수여야함
    5.  기본 클래스에서 제공되는 인터페이스의 내용이 클래스가 구체화되면서 하위 클래스에서 그 내용이 변경될 수 있도록 하기 위한 방법임
    6.  재정의 예제
        ```C++
        class Car{
            public:
                int getSpeed() // 부모의 getSpeed()함수 재정의
                {
                    return 30;
                }
        };
        class Taxi: public Car{ // Car클래스 상속
            public:
                int getSpeed()
                {       //자식의 getSpeed()함수 재정의
                    return 50;
                }
        };
        int main()
        {
            Taxi taxi;  //taxi 객체 생성
            cout << "현재속도: " << taxi.getSpeed()<<endl;  //taxi.getSpeed()호출
            return 0;
        }
        ```
25. 예외처리
    1.  예외발생
        -  프로그램에 잘못된 코드나 부정확한 데이터가 입력될 수 있음.
        -  예상하지 못한 일 즉, 프로그램이 실행되는 동안에 발생하는 예기치 않은 에러를 예외(exception)이라 부름
        -  error 발생 시 오류처리 후 계속적인 실행이 가능하게 하는 것을 예외처리(Exception handling)라 함
        -  예외가 발생하는 상황 예제
        ```C++
        #include<iostream>
        using namespace std;

        void main(){
            int sum,um2,num1 = 10, num2 = 0 ; //0으로 나누기(에러발생)
            sum = num1 / num2;
            cout << sum << endl;
        }
        ```
    2. 전통적인 예외처리 방식
       - if - else를 통한 조건 검사를 하는 방식임
       - 사과를 나누어 나누는 사람의 수가 0일때 예외처리가 됨
       - 전통적인 예외처리 예제
        ```C++
        #include<iostram>
        using namespace std;

        void main(){
            int apple;
            int people;
            cout << "사과 개수 입력:" << ;
            cin >> apple;
            cout <<"사람 수 입력:";
            cin >> people;

            if(people == 0){
                cout << "사람의 수가 0명입니다 " << end;
            }
            else{
                cout << "한 사람당 사과는 " << apple/people <<"입니다" << endl; 
            }
        }    
        ```
    3. 예외 처리기
       -   C++ 에서는 언어 차원에서 예외 처리를 지원함
       -   try,throw,catch의 키워드를 사용함
       -   try 블록은 예외가 발생할 가능성이 있는 문장에 들어감
       -   예외 조건이 감지되면 throw 문장이 실행되어 예외를 던짐
       -   throw 키워드 뒤에 던져질 예외를 지정함
       -   예외가 던져지면 catch 문으로 점프함
       -   catch 에는 자신이 처리할 예외 타입을 지정한 후 예외처리 코드를 기술함
       -   C++의 예외처리 기본 구조
            ```C++
            try{
                //예외가 발생할 수 있는 코드
                if(예외 조건)
                    throw 예외;
            }
            catch (매개변수){
                //예외 처리 코드
            }
            ```
        - C++의 예외처리 예제
            ```C++
            #include<iostream>
            using namespace std;

            void main(){
                int apple,people,result;

                try{
                    cout << "사과 개수 입력:" << ;
                    cin >> apple;
                    cout <<"사람 수 입력:";
                    cin >> people;
                    if(people == 0){
                        throw people;
                        result = apple /people;
                        cout << "한 사람당 사과는 " << result <<"입니다" << endl; 
                    }
                }
                catch(int e){
                    cout<<"사람의 수가"<< e << "명입니다."<<endl;
                }
            }
            ```
            예외발생 프로세스
              - 예외가 발생하지 않았을 때 프로세스
                - try > 결과로 바로 점프
              - 예외가 발생하엿을 때 프로세스
                - catch문으로 들어가서 throw된 people 받아서 출력
        4. 다중 catch 예외처리
           -   하나의 try 블록은 여러개의 throw 예외처리를 할 수 있음
           -   각 예외는 다른 값을 던질 수 있음
           -   예외 처리 블록을 만나지 못하면 try 블록을 또 다시 감싸고 있는 좀 더 큰 try 블록에 해당하는 예외처리 블록에서 예외 처리부를 찾게 됨
           -   예외 처리 블록의 예외 선언에 $\cdots$를 기술하면 이 예외 처리 블록은 모든 종류의 예외를 받아 처리할 수 있음.
           -   예외 처리 블록 안에서 throw ; 하고 하면 현재 예외를 그대로 상위 예외 처리 블록으로 다시 전달함
           -  다중 예외처리 예제
            ```C++
            #include<iostream>
            using namespace std;

            void main(){
                int apple,people,result;

                try{
                    cout << "사과 개수 입력:" << ;
                    cin >> apple;
                    cout <<"사람 수 입력:";
                    cin >> people;
                
                    if(people < 0) throw "negative"
                    if(people == 0) throw people;
                    result = apple /people;
                    cout << "한 사람당 사과는 " << result <<"입니다" << endl;
                }
                catch(const char *e){
                    cout<<"사람의 수가"<< e << "명입니다."<<endl;
                }
                catch(int e){
                    cout<<"사람의 수가"<< e << "명입니다."<<endl;
                }
            }
            ```