# 7. 빅데이터 분석
## 3. 분석 파일럿 실행 1단계 - 분석 아키텍처
### 3. 분석 아키텍처
- 스마트카의 5가지 데이터셋을 앞서 소개한 임팔라, 제플린, 머하웃, 스마크 ML을 이용해 다양한 고급 분석을 수행, 3개의 분석 소프트웨어가 하이브의 데이터 웨어 하우스의 데이터셋의 직접 접근해서 분석 작업.
  - 스마트카 데이터셋
    - 스마트카 상태 정보
    - 운전자 운행 정보
    - 이상 운행 패턴 정보
    - 점검이 필요한 차량 정보
    - 차량 용품 구매 정보
    - 스마트카 고급 분석 결과
  - 데이터분석
    - 임팔라
      - Impala SQL
    - 제플린
      - Spark-SQL
      - Spark-ML 분류
      - Spark-ML 군집
    - 머하웃
      - 군집
      - 추천
    - 분석 결과 제공
      - 스쿱
        - Export
  - 휴 - Impala Editor
    - 스마트카 Impala Editor
  - 제플린 - Notebook
    - 상습 과속 지역을 Spark-SQL 분석
    - 분석 결과를 제플린 차트로 출력
  - 스파크 ML - 분류 라이브러리
    - 머신러닝 감독 학습
    - 랜덤 포레스트 알고리즘 활용
    - 스마트카 상태정보 예측 모델
  - 스파크 ML 군집 라이브러리
    - 머신러닝 감독학습
    - 랜덤 포레스트 알고리즘 활용
    - 스마트카 상태 정보 예측 모델
  - 머하웃 - 추천 라이브러리
    - 스마트카 사용자 기반 협업 필터링
    - 사용자 간 유사성으로 상품을 추천
  - 스쿱 - 분석 결과 Export
    - HDFS의 저장된 분석 결과를 외부 RDBMS에 제공
1. CM에서 임팔라를 추가 설치하면 휴의 Editors 메뉴에 Impala Editor가 추가. 이 Impala Editor를 통해 기존 탐색 단계에서 사용했던 "스마트카 상태 정보" 및 "운전자 운행 정보" 데이터셋에 대한 하이브 배치 쿼리를 임팔라의 실시간 쿼리로 바꿔 빠른 분석을 수행
2. 제플린의 Notebook을 활용해 웹 브라우저에서 스파크 -SQL로 "운전자 운행 정보" 데티어셋을 분석, "상습 과속 지역"과 "지역별 상습 과속 차량"등을 분석. 분석 결과는 제플린에서 제공하는 다양한 차트로 시각화
3. 머하웃의 추천 라이브러리 명령어에 입력 데이터로 "차량 정보 구매 정보" 데이터셋을 지정, 상품 평가 정보에 대한 운전자의 취향을 분석해서 취향이 비슷한 운전자에게 구매 가능성이 높은 상품을 추천
4. 스파크 ML의 분류 라이브러리로 "스마트카 이상 징후"를 예측하기 위한 모델을 만듦. 트레이닝 데이터로 "스마트카 상태 정보" 데이터셋을 이용, 알고리즘으로 랜덤 포레스트를 선택. 최종적으로 트레이닝된 분류 모델(Classify)을 애플리케이션에 적용
5. 스파크ML의 군집 라이브러리를 이용, "스마트카 운전자의 운행" 데이터셋에 대해 K개의 군집(초기 K값은 머하웃의 Canopy 활용)으로 형성되는 K-means를 적용. 이를 통해 탐색 단계에서는 식별되지 않은 새로운 운행 패턴을 발견해 분석
6. 스쿱의 CLI 명령 중 익스포트 기능을 이용, HDFS에 저장된 분석 결과 데이터를 외부의 RDBMS(PostgreSQL)에 제공
