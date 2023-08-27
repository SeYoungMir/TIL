* 참고
  * 코드 리팩토링 종류 - 이어서
    3. 데이터 구성
       1. Change Reference to Value : 불변성을 띄고 관리하기 어려운 참조 객체는 값을 객체로 바꿈
       2. Encalpsulate Field Public : 필드가 있는 경우 그 필드를 private로 만들고 접근자를 제공함
       3. Replace Magic Numver with Symbolic Constant : 특별한 의미를 갖는 술자가 있으면 상수를 만들고 이름을 지음
       4. Replace Record with Data Class : 레코드 구조에 대한 인터페이스가 필요할 때 그 레코드를 위한 데이터 객체를 만듦
       5. Replace Type Code with Subclass : 클래스 동작에 영향을 미치는 변경 불가능한 타입 코드가 있으면 서브클래스로 바꿈
       6. Replace Type Code with Class : 클래스의 동작에 영향을 미치지 않는 숫자로 된 타입 코드가 있으면 숫자를 클래스로 만듦
       7. Self Encapsulate Field :  필드에 직접 접근하는데 필드에 대한 결합이 이상해지면 그 필드에 대한 get set 메서드를 만들고 접근함
       8. Replace Array with Object : 배열의 특정 요소가 다른 뜻을 가지고 있다면 배열을 각각의 요소에 대한 필드를 가지는 객체로 바꿈
       9. Replace Data Value with Object : 추가적인 데이터나 동작을 필요로 하는 데이터 아이템이 있을 경우 데이터 아이템을 객체로 바꿈
       10. Replace Type Code with State/Strategy : 클래스의 동작에 영향을 미치지만 서브 클래싱을 할 수 없을 때 타입 코드를 스테이트 객체로 바꿈
       11. Encapsulate Collection : 컬렉션을 리턴하는 메서드가 있으면 해당 메서드가 읽기전용 뷰를 리턴하도록 만들고 add/remove 메서드를 제공함
       12. Change Value to Reference : 동일한 인스턴스를 여러 개 가진 클래스가 있고 여러 동일한 인스턴스를 하나의 객체로 바꾸고 싶으면 그 객체를 참조 객체로 바꿈
       13. Change Bidirectional Association to Unidirectional : 서로 링크를 갖는 두 개의 클래스에서 한 쪽이 다른 한 쪽을 더 이상 필요로 하지 않을 때 불필요한 링크를 제거함
       14. Duplicate Observed Data : GUI 컨트롤에서만 사용 가능한 도메인 데이터가 있고 도메인 메서드에서 접근이 필요한 경우 해당 데이터를 도메인 객체로 복사하고 옵저버를 두어 데이터를 동기화함
   4. 조건문 단순화
      1. Rename Method : 메서드의 이름이 그 목적을 드러내지 못하면 메서드의 이름을 바꿈 
      2. Introdice Null Object null : 체크를 반복적으로 하는 null 값은 null 객체로 대체함
      3. Decompose Conditional : 복잡한 조건문이 있으면 조건, then, else 부분에서 메서드를 추출함
      4. Introduce Assertion : 코드의 한 부분이 프로그램의 상태를 나타내고 있으면 assertion을 써서 가정을 명시적으로 만듦
      5. Remove Control Flage: 일련의 boolean 식에서 컨트롤 플래그 역할을 하는 변수가 있는 경우 break 또는 return을 대신 사용함
      6. Consolidate Conditional Expression : 같은 결과를 나타내는 일련의 조건 테스트가 있는 경우 그것을 하나의 조건식으로 결합하여 뽑아냄
      7. Consolidate Duplicate Conditonal Fragments : 동일한 코드 조각이 조건문의 조건 분기 안에 있는 경우 동일한 코드를 조건문 밖으로 옮김
      8. Replace Nested Conditonal with Guard Clauses : 메서드가 실행 경로를 불명확하게 하는 조건 동작을 가지고 있는 경우 모든 특별한 경우에 대해 보호절을 사용함
      9. Replace Conditional with Ploymorphism : 객체의 타입에 따라 다른 동작을 선택하는 조건문을 가지고 있는 경우 조건문의 각 부분을 서브클래스에 있는 오버라이딩 메서드로 옮기고 원 메서드를 abstract로 만듦
   5.  일반화
       1.  Pull Up Field : 두 서브클래스가 동일한 필드를 가지고 있다면 그 필드를 수퍼클래스로 옮김
       2.  Push Down Field : 어떤 필드가 일부 서브클래스에 의해서만 사용된다면, 그 필드를 관련된 서브클래스로 옮김
       3.  Pull Up Method : 동일한 일을 하는 메서드를 여러 서브클래스에서 갖고 있다면 이 메서드를 슈퍼클래스로 옮김
       4.  Push Down Method : 슈퍼 클래스에 있는 동작이 서브 클래스 중 일부에만 관련되어 있다면 해당 동작과 관련된 서브클래스로 옮김
       5.  Pull Up Constructor Body : 서브 클래스들이 대부분 동일한 몸체를 가진 생성자를 갖고 있다면 슈퍼클래스에 생성자를 만들고 서브클래스 메서드에서 이것을 호출함
