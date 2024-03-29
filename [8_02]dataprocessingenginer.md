## 2. 인터페이스 기능 구현하기
### 1. 인터페이스 기능 구현 정의
#### 1. 모듈 세부 설계서
1. 컴포넌트 명세서
   - 컴포너느 명세서는 컴포넌트의 개요 및 내부 클래스의 동작, 인터페이스를 통한 외부와 통신하는 명세를 정의하며, 실제 코드 수준의 명칭이나 설계 수준의 논리적인 클래스 명칭을 사용하기도 함
     - 컴포넌트 명세서 예시
        <table>
            <tr>
                <th>컴포넌트ID</th>
                <th>CR-COM-002</th>
                <th>컴포넌트 명</th>
                <th>인사발령</th>
            </tr>
            <tr>
                <td>컴포넌트 개요</td>
                <td colspan=3>각 사의 인사발령을 수행하고 관계사와 필수 정보를 공유하는 컴포넌트임</td>
            </tr>
            <tr>
                <th colspan=4>내부 클래스</th>
            </tr>
            <tr>
                <td>ID</td>
                <td>클래스명</td>
                <td colspan=2>설명</td>
            </tr>
            <tr>
                <td>CR-CLASS-01</td>
                <td>발령이력 관리</td>
                <td colspan=2>발령형태에 따른 발령이력을 개인 이력관리에 등록함</td>
            </tr>
            <tr>
                <td>CR-CLASS-02</td>
                <td>인사마스터 관리</td>
                <td colspan=2>가장 최근의 이력을 인사마스터에 반영함. 이전 정보는 갱신함</td>
            </tr>
            <tr>
                <td>CR-CLASS-03</td>
                <td>인터페이스 호출</td>
                <td colspan=2>발령사항을 인터페이스를 통해 관계사와 공유함</td>
            </tr>
            <tr>
                <th colspan=4>인터페이스 클래스</th>
            </tr>
            <tr>
                <td>ID</td>
                <td>인터페이스 명</td>
                <td>오퍼레이션 명</td>
                <td>구분</td>
            </tr>
            <tr>
                <td rowspan=3>IF-HR-001</td>
                <td rowspan=3>인사정보 전송 인터페이스</td>
                <td>대상 추출</td>
                <td>전달 대상</td>
            </tr>
            <tr>
                <td>정보 전송</td>
                <td>전달 행위</td>
            </tr>
            <tr>
                <td>결과 확인</td>
                <td>전달 결과</td>
            </tr>
        </table>
2. 인터페이스 명세서
   - 인터페이스 명세서는 컴포넌트 명세서에 명시된 인터페이스 클래스의 세부 조건 및 기능을 명시한 명세서이며, 명칭, 설명, 사전/후 조건, 인터페이스 데이터 및 인터페이스 후 성공 여부를 반환받는 값이 정의 되어 있음
     - 인터페이스 명세서 예시
        <table>
            <tr>
                <th>인터페이스 ID</th>
                <td>IF-HR-001</td>
                <th>인터페이스 명</th>
                <td>인사정보 전송 인터페이스</td>
            </tr>
            <tr>
                <th>오퍼레이션 명</th>
                <td colspan=3>인터페이스 대상 선정</td>
            </tr>
            <tr>
                <th>오퍼레이션 개요</th>
                <td colspan=3>관계사와 인터페이스 할 대상(정보)를 선택함</td>
            </tr>
            <tr>
                <th>사전 조건</th>
                <td colspan=3>과장 이상 정규직만 선택</td>
            </tr>
            <tr>
                <th>사후 조건</th>
                <td colspan=3>전송 이후 상대 시스템의 결과값을 업데이트</td>
            </tr>
            <tr>
                <th>파라미터</th>
                <td colspan=3>발령구분, 발령정보</td>
            </tr>
            <tr>
                <th>반환값</th>
                <td colspan=3>Success/Fail</td>
            </tr>
        </table>
### 2. 인터페이스 구현
#### 1. 인터페이스 구현 도구
1. 데이터 통신을 통한 인터페이스 구현
   - 주로 JSON 및 XML형식의 데이터 포맷을 사용
     1. JSON(Java Script Object Notation)
        - "속성-값 쌍" 또는 "키-값 쌍"으로 이루어진 데이터 오브젝트를 전달하기 위해 인간이 읽을 수 있는 텍스트를 사용하는 개방형 표준 포맷이다. 비동기 브라우저/서버 통신(AJAX)을 위해, 넓게는 XML을 대체하는 주요 데이터 포맷임. 특히, 인터넷에서 자료를 주고 받을 때 그 자료를 표현하는 방법으로 알려져 있음. 자료의 종류에 큰 제한은 없으며 , 특히 컴퓨터 프로그램의 변수값을 표현하는 데 적합함
     2. XML
        - W3C에서 개발된, 다른 특수한 목적을 갖는 마크업 언어를 만드는데 사용하도록 권장하는 다목적 마크업 언어. XML은 SGML의 단순화된 부분집합으로, 다른 많은 종류의 데이터를 기술하는데 사용할 수 있음. 주로 다른 종류의 시스템, 특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 HTML의 한계를 극복할 목적으로 만들어짐.
2. 인터페이스 엔티티를 통한 인터페이스 구현
   - 인터페이스가 필요한 시스템 사이에 별도의 인터페이스 엔티티를 두어 상호 연계하는 역할을 함
   - 송신 시스템
     - Write
       - 송신 인터페이스 테이블
   - DB Connection
     - Data Transfer(Procedure,Job)
   - 수신 시스템
     - Choose Data & Use
       - 송신 인터페이스 테이블