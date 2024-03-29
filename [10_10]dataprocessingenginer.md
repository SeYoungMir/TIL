## 2. 데이터베이스 기초 활용하기 
### 3. 데이터모델링과 데이터 모델의 개념
1. 데이터 모델 개념
   1. 현실 세계의 다양한 데이터 중 조직에 필요한 데이터를 선별하는 과정임
   2. 데이터 모델링은 개념적 데이터 모델링, 논리적 데이터 모델링으로 나눌 수 있음.
   3. 데이터 베이스 설계는 개념적 데이터 모델링과 논리적 데이터 모델링을 하는 것이라 할 수있음.
   4. 추상화(abstraction)라고 하며, 추출된 데이터들을 데이터 베이스로 저장하는데 있어서도 데이터베이스의 저장 구조를 결정해야함
2. 개념적 모델링
   1. 현실 세계에서 데이터를 추출하여 개념 세계로 옮기는 작업임
   2. 대표적으로 개체-관계 모델을 이용함
   3. 트랜젝션 인터페이스를 설계함
   4. 정규화를 수행하는 단계임
3. 논리적 데이터 모델링 개념
   1. 개념 세계의 데이터를 데이터베이스에 저장할 구조로 표현하는 작업임
   2. 대표적으로 관계 데이터 모델을 이용함
   3. 저장 공간, 응답 시간, 데이터 효율화 등 여러가지를 고려하여 설계함
   4. 반정규화를 수행함
4. 데이터 모델(Data Model)의 구성
   1. 데이터 구조(Data Structure) : 자주 변하지 않는 정적인 특징을 갖고 있음.
   2. 연산(Operation) : 데이터 구조에 따라 개념 세계나 컴퓨터 세계에서 실제로 표현된 값들을 처리하는 작업으로 값이 연산에 의해 계속적으로 변경될 수 있으므로 동적인 특징을 갖고 있음
   3. 제약 조건(Constraint) : 구조적 측면의 제약 사항과 연산을 적용하는 경우 허용할 수 있는 의미적 측면의 제약 사항이 있음.
### 4. 개체- 관계 (E-R)모델
1. E-R 다이어그램
   1. 현실 세계를 개념적으로 모델링한 결과물을 그림으로 표현한 것임
   2. 개념적 구조를 개체-관계 모델을 개체, 속성, 관계로 표현함
   3. 사각형, 개체 간의 관계를 표현하는 마름모, 개체나 관계의 속성을 표현하는 타원과, 각 요소를 연결하는 링크(연결선)로 구성되어 있음.
   4. 일대 일(1:1), 일대 다(1:N), 다대 다(N:M) 관계를 레이블로 표기함
   5. 개체 - 관계 모델(E-R Model : Entity-Relationship Model)이란 1976년 피터 첸(Peter Chen)이 제안한 것으로 개체(entity)와 개체 간의 관계(Relationship)를 이용해 현실 세계를 개념적 구조로 표현하는 방법으로 핵심 요소는 개체, 속성, 관계임
   6. 개체 - 관계 다이어그램(ERD : Entity-Relationship Diagram)이란 개체 - 관계모델을 이용해 현실 세계를 개념적으로 모델링한 결과물을 그림으로 표현한 것임.
2. 개체
   1. 데이터를 가지고 잇는 사람이나 사물, 개념, 사건 등이며, 다른 개체와 구별되는 이름을 가지고 있고, 각 개체만의 고유한 특성이나 상태, 즉 속성을 하나 이상 가지고 있음
   2. 개체 타입(Entity Type)
      - 개체를 고유의 이름과 속성들로 정의한 것
      - 파일 구조의 레코드 타입에 대응됨
   3. 개체 인스턴스(Entity Instance)
      - 개체를 구성하고 있는 속성이 실제 값을 가짐으로써 실체화된 개체로 개체 어커런스(Entity Occurence)라고도 함
      - 파일 구조의 레코드 인스턴스(Record Instance)에 대응됨
3. E-R 다이어그램 구성 요소
    <table>
        <tr>
            <th>기호</th>
            <th>의미</th>
        </tr>
        <tr>
            <td>직사각형</td>
            <td>개체</td>
        </tr>
        <tr>
            <td>마름모</td>
            <td>관개</td>
        </tr>
        <tr>
            <td>타원</td>
            <td>속성</td>
        </tr>
        <tr>
            <td>타원과 선분</td>
            <td>속성(기본키)</td>
        </tr>
        <tr>
            <td>선분</td>
            <td>개체 관계 연결</td>
        </tr>
    </table>