## 2. 데이터베이스 기초 활용하기
### 1. 데이터베이스 필요성
1. 데이터와 정보
   1. 데이터(data)는 현실 세계에서 단순히 관찰되거나 측정하여 수집된 사실(fact)이나 값(value)으로 자료라고도 함
   2. 정보(information)은 데이터를의사 결정에 유용하게 활용할 수 있도록 처리하여 체계덕으로 조직한 결과물임
   3. 정보 처리(information processing)은 데이터에서 정보를 추출하는 과정으로, 데이터를 상황에 맞게 분석하거나 해석하여 데이터 간의 의미 관계를 파악하는 것임
2. 정보 시스템
   1. 정보 시스템(Information System) : 조직 운영에 필요한 데이터를 수집하여 저장해두었다가 필요할 때 유용한 정보를 만들어 주는 수단
   2. 데이터베이스(Database) : 정보 시스템 안에서 데이터를 저장하고 있다가 필요할 때 제공하는 역할을 담강함
   3. 경영 정보 시스템(MIS : Management Information System) : 기업의 경영 관리에 필요한 의사 결정용 정보 시스템임
   4. 의사 결정 지원 시스템(DSS :Decision Support System) : 복합적이고 광범위한 의사 결정을 위해 사용되는 정보 시스템임
3. DBMS 정의
   1. DBMS(DataBase Management System)이란 사요아와 데이터베이스 사이에서 사용자의 요구에 따라 정보를 생성해주고 데이터베이스를 관리해주는 소프트웨어를 말함
4. DBMS의 종류 및 특징
   <table>
        <tr>
            <th>종류</th>
            <th>저작자</th>
            <th>주요 용도</th>
        </tr>
        <tr>
            <td>Oracle</td>
            <td>Oracle</td>
            <td>대규모, 대량 데이터의 안정적 처리</td>
        </tr>
        <tr>
            <td>MS_SQL</td>
            <td>Microsoft</td>
            <td>중소 규모 데이터의 안정적 처리</td>
        </tr>
        <tr>
            <td>MySQL</td>
            <td>MySQL AB,Oracle</td>
            <td>오픈 소스 RDBMS</td>
        </tr>
        <tr>
            <td>SQLite</td>
            <td>D.Richard Hipp</td>
            <td>스마트폰, 태블릿 PC 등의 Embedded Database용</td>
        </tr>
        <tr>
            <td>Mongo</td>
            <td>MongoDB Inc.</td>
            <td>오픈 소스 NoSQL 데이터베이스</td>
        </tr>
   </table>
5. DBMS의 필수 기능
   1. 정의(Definition) 기능: 모든 응용 프로그램들이 요구하는 뎅이터 구조를 지원하기 위하여 DB에 저장될 데이터의 유형과 구조에 대한 정의, 이용 방식, 제약 조건 등을 명시하는 기능
   2. 조작(Manipulation) 기능 : 데이터 검색, 갱신, 삽입, 삭제 등을 체계적으로 처리하기 위하여 사용자와 데이터베이스 사시의 인터페이스 수단을 제공하는 기능
   3. 제어(Control) 기능 : 데이터의 정확성과 안전성을 유지하는 기능(무결성, 보안, 병행 수행 제어, 회복 등)