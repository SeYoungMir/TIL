## 2. 데이터베이스 기초 활용하기 - 이어서
### 2. 논리적 데이터모델링
1. 논리적 데이터 모델링 개념
   1. E-R 다이어그램으로 표현함
   2. 개념적 구조를 선택한 데이터베이스 관리 시스템에 따라 사용자 입장에서 데이터베이스에 저장할 형태로 표현한 데이터베이스의 논리적인 구조임
   3. 관계 데이터 모델, 계층 데이터 모델, 네트워크 데이터 모델 등이 있음.
2. 관계 데이터 모델
   1. 논리적 구조가 2차원 테이블 형태임
   2. 키(Key)를 이용하여 관계를 표현함
   3. 관계형 데이터모델이라고 부름
   4. 일반적 형태(테이블)의 데이터베이스는 관계형 데이터 모델임
    <table>
        <tr>
            <th>이름</th>
            <th>학과</th>
            <th>과목</th>
            <th>강의실</th>
        </tr>
        <tr>
            <td>박명수</td>
            <td>소프트웨어과</td>
            <td>C언어</td>
            <td>101</td>
        </tr>
        <tr>
            <td>김길수</td>
            <td>전자과</td>
            <td>전자회로</td>
            <td>203</td>
        </tr>
        <tr>
            <td>남기선</td>
            <td>전자과</td>
            <td>전자회로</td>
            <td>203</td>
        </tr>
    </table>
3. 계층 데이터 모델
   1. 논리 구조가 트리형태임
   2. 상하관계가 존재하는 모델임
   3. 부모-자식 개체가 있음
   4. 1:N의 관계만 표현이 가능함
   5. 개체는 사각형으로 나타내고 개체들 간의 관계는 링크(연결성)로 나타냄
   6. 데이터의 삽입, 삭제, 수정, 검색이 쉽지 않은 단점이 있음.
      - 이름
        - 학교
          - 교수
            - 교번
            - 이름
          - 학생
            - 학번
            - 이름
4. 네트워크 데이터 모델
   1. 논리 구조가 그래프 형태임
   2. 1:N,N:M 의 관계를 형성함
   3. 두 개체 간의 관계를 여러 개 정의할 수 있어 관계를 이름으로 구별함
   4. 각 관계를 화살표를 이용하여 각 관고ㅖ를 이름으로 구별할 수 있음
   5. 1:N(일대 다) 관계의 개체들을 각각 오너(Owner)와 멤버(member)라고 부름
      - 학교 > 강의실 배정 > 학생
      - 학생 > 수강 > 교수
      - 교수 > 강의 > 학생
