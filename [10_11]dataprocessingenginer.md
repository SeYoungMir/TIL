## 2. 데이터베이스 기초 활용하기 
### 4. 개체- 관계 (E-R)모델 - 이어서
4. E - R 다이어그램 예
    - 강의
      - 교수(1)
        - 교번(기본키)
        - 이름
        - 학과
      - 학생(N)
        - 학번(기본키)
        - 이름
        - 학과
5. 개체 관계 유형
   1. 이항 관계 : 개체 타입 두 개가 맺는 관계
   2. 삼항 관계 : 개체 타입 세 개가 맺는 관계
   3. 순환 관계 : 개체 타입 하나가 자신과 맺는 관계
6. 매핑 관계
   1. 일대일(1:1)관계
    - 개체 A가 다른 개체 B의 개체 인스턴스 하나와 관계를 맺는 것
    - - 강의
      - 교수(1)
        - 교번(기본키)
        - 이름
        - 학과
      - 학생(1)
        - 학번(기본키)
        - 이름
        - 학과
   1. 일대다(1:N)관계
    - 개체 A가 다른 개체 B의 개체 인스턴스 여러개와 관계를 맺는 것
    - - 강의
      - 교수(1)
        - 교번(기본키)
        - 이름
        - 학과
      - 학생(N)
        - 학번(기본키)
        - 이름
        - 학과
   2. 다대다(N:M)관계
    - 개체 A의 여러 개의 인스턴스가 다른 개체 B의 여러 인스턴스와 관계를 맺는 것
    - - 강의
      - 교수(N)
        - 교번(기본키)
        - 이름
        - 학과
      - 학생(M)
        - 학번(기본키)
        - 이름
        - 학과
### 5. 데이터베이스 정규화(Normalization)
1. 데이터베이스 정규화 개녀
   1. 데이터베이스 설계 시 발생하는 이상(Anomaly) 현상( 데이터에 삽입, 수정, 삭제 연산)의 발생을 최소화함
   2. 데이터의 중복으로 인하여 삽입, 삭제, 업데이트 연산 시 이상 증상을 최소화함으로 데이터의 안정성을 최대화함
   3. 데이터베이스를 설계한 후 설계 결과물을 검증하기 위해 사용함
2. 이상(Anomaly) 현상
   1. 삽입(Insert) 이상 : 데이터 삽입 시 불필요한 데이터가 같이 삽입되는 현상
   2. 삭제(Delete) 이상: 데이터 삭제 시 삭제하지 않아야 할 데이터가 연쇄적으로 삭제되는 현상
   3. 업데이트(Update) 이상 : 데이터 업데이트 시 정보가 모순되는 현상
3. 데이터베이스 정규화 단계
   1. 1 정규형 (1 NF) : 도메인 원자값
      - 릴레이션에 속한 모든 속성의 도메인이 더 이상 분해되지 않는 원자값(atomic value)으로만 구성되어 있었을 때임
   2. 2 정규형 (2 NF) : 부분 함수 종속 제거
      - 릴레이션이 제 1 정규형에 속하고 기본키가 아닌 모든 속성이 기본키에 완전 함수 종속되면 제 2 정규형임
   3. 3 정규형 (3 NF) : 이행적 함수 종속 제거
      - 릴레이션이 제 2 정규형에 속하고 기본키가 아닌 모든 속성이 기본키에 이행적 함수 종속이 되어 지울 때임
   4. BCNF 정규화 (BCNF) : 결정자 함수 종속 제거
      - 릴레이션의 함수 종속 관계에서 모든 결정자가 후보키이면 보이스/코드 정규형임
   5. 4 정규화 (4 NF) : 다치 종속 제거
      - 릴레이션이 보이스/코드 정규형을 만족하면서 함수 종속이 아닌 다치 종속(MVD : Multi Valued Dependency)을 제거하면 제 4정규형임
   6. 5 정규화 (5 NF) : 조인 종속 제거
      - 릴레이션이 자신의 프로젝션에 대한 조인의 결과가 자신과 같을 때임.