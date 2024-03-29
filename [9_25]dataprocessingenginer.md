### 3. 객체 지향 프로그래밍 - 이어서
4. 객체 지향의 필요성
   1. 객체지향의 목적 : 코드 분석과 변경이 용이한 장점을 가지고 있음
   2. 기존의 절차 지향적 프로그래밍이 유지관리가 어려운 점을 해결하기 위하여 객체 지향적 프로그래밍이 나오게 됨
   3. 객체 지향 프로그래밍은 변경이 생기면 수정사항에 해당하는 객체들간의 관계만 변경하면 절차지향적 프로그래밍에 비해 손쉽게 변경이 가능함
   4. 지속적으로 사용하는 프로그램일 경우 객체 지향으로 프로그래밍을 하면 코드의 재사용이 가능하여 유지비를 낮출 수 있음.
5. 객체 지향
   1. class는 형상을 만들 수 있는 틀이라고 한다면, 그 틀에 무언가를 부어서 만들어지는 것(new 로 생성되는 것)을 객체라 함
   2. 프로그래밍에서는 현실 세계를 모두 반영하기 힘들기 때문에 필요한 것들로 구성을 하여 원하는 결과를 얻도록 개발을 하는 것. 즉 객체, 속성, 메소드를 정의하고 객체와의 관계를 정의하는 과정이 추상화에 해당함
6. 객체지향 방법론
   1. 소프트웨어 시스템을 구성하는 요소를 인터페이스와 데이터를 포함한 객체의 단위로 나누고, 객체간의 메시지 전달을 통해 문제를 해결함
   2. 실 세계의 문제를 직접 묘사할 수 있는 장점 및 재사용성에 의해 빠른 소프트웨어의 개발 및 생산성의 증대에 도움을 줄 수 있음
   3. 객체지향 프로그램에서는 객체의 구성 및 객체 간의 통신을 정의하는 것이 중요함
   4. 객체지향의 기본 키워드
      1. 객체(Object) : 실세계에 존재하는 모든 사물을 표현함
      2. 클래스(Class) : 객체를 프로그램으로 표현할 수 있도록 만든 언어적 도구
      3. 인스턴스(Instance) : 프로그램에서 클래스를 통해 만든 실제의 실행 객체
7. 객체지향 설계의 고려사항
   1. 객체의 정의 및 객체간의 통신에 대해 정의한 것
   2. 캡슐화, 추상화, 상속 및 다형성 등의 핵심 개념을 적용함
8. 객체지향의 특징
   1. 캡슐화(Encapsulation)
      - 데이터와 함수 등 객체와 관련된 것을 하나로 묶는 것
      - 정보 은닉(Information hiding)과 함께 연관 지어 사용되는 개념
      - 외부에서 알아야 할 필요가 없는 데이터와 연산을 외부에서 보이지 않게 숨겨 자세한 실행 흐름을 드러나지 않게 함
   2. 추상화(Abstraction)
      - 인터페이스(Interface)와 구현(Implementation)을 분리하는 것
      - 객체가 가진 특성 중 필수 속성만으로 객체를 묘사하고 유사성을 표현하며, 세부적인 상세 사항은 각 객체에 따라 다르게 구현되도록 함
      - C++ 언어는가상 함수를 통한 클래스의 상속을 통하여 추상화를 제공함.
      - 기능 추상화와 자료 추상화가 있음
   3. 상속(Inheritance)
      - 기존에 정의된 클래스를이용하여 새로운 클래스를 정의할 수 있도록 함.
      - 클래스에 상, 하 관계를 맺을 수 있도록 하고 하위 클래스는 상위 클래스에서 정의한 모든 내용을 수정 없이 사용 가능하도록 정의함
      - 상위 클래스(Super Class), 기본 클래스(Base Class), 부모 클래스(Parent Class), 하위 클래스(Sub Class), 유도 클래스(Derive Class), 자식 클래스(Child Class)로 구성되어 있음 
   4. 다형성(Polymorphism)
      - 서로 다른 타입에 대해 동일한 방식으로 접근할 수 있도록 하나의 인터페이스를 제공하는 것
      - 같은 방식으로 접근하지만 서로 다른 표현을 함.