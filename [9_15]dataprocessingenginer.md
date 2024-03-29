## 4. 보안 기능 - 이어서
9. 소프트웨어 보안 입력 데이터 검증 및 표현
    <table>
        <tr>
            <th>보안 약점</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>널(Null)포인터 역참조</td>
            <td>Null 값으로 설정된 중요 변수의 메모리 주소 값을 참조했을 때 발생하는 보안 취약점</td>
        </tr>
        <tr>
            <td>부적절한 자원 해제</td>
            <td>사용되는 리소스 자원을 적절하게 해제하지 못하면 리소스 자원의 누수 등이 발생하고, 리소스 자원이 부족하여 새로운 입력에 처리 못하게 되는 보안 취약점</td>
        </tr>
    </table>
## 5. 캡슐화
1. 개요
   1. 중요한 데이터를 은닉하기 위한 확장 개념이라고 볼 수 있으며, 캡슐화는 객체들의 내부와 외부 간의 분리 역할을 수행하고 사용자에게 상세 구현을 감추고 필요 사항만 보이게 함으로써, 객체의 속성과 메소드를 다른 객체가 접근할 수 없도록 하기 때문에 메시지 수신에 의해 요구된 작업을 수행함
   2. 따라서 소프트웨어의 부품의 재사용 증대와, 소프트웨어의 수정, 시럼, 유지 보수성이 향상되는 효과가 있음
2. 캡슐화 개념도
   
   &nbsp; 보호막
    ```C
     Attribute
         int a;
         char
    ```
    ```C
    Method
        load();
        save();
    ```
    ```C
        Interface
    ```
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\darr$ &nbsp; $\uarr$ &nbsp;

    메시지 &nbsp; 송수신
    
    1. 중요한 프로그램의 데이터와 프로그램의 기능성을 충분하지 못하게 캡슐화 하였을 때 인가되지 않은 사용자에게 프로그램 내부의 데이터 누출이 가능해지는 보안약점임
    2. 예로 Private 배열에 Public Data가 할당되거나, Public Method부터 반환된 Private 배열 등이 있음
 3. 소프트웨어 보안 캡슐화
    <table>
        <tr>
            <th>보안 약점</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>잘못된 세션에 의한 정보 노출</td>
            <td>잘못된 통신 세션에 의해 권한우없는 사용자에게 데이터 노출이 일어날수 있는 보안 취약점</td>
        </tr>
        <tr>
            <td>제거되지 않고 남은 디버그 코드</td>
            <td>프로그램 디버깅을 위해 작성된 코드를 통해 권한이 없는 사용자 인증이 우회되거나, 또는 중요 정보에 접근이 가능해지는 보안 약점</td>
        </tr>
        <tr>
            <td>시스템 데이터 정보 노출</td>
            <td>사용자가 볼 수 있는 에러 처리 메시지나 오류가 스택 정보에 시스템 내부 데이터나 내부 로직 등 디버길 관련 정보가 공개되는 보안 취약점</td>
        </tr>
    </table>