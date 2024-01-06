# 7. 빅데이터 분석
## 2. 빅데이터 분석에 활용되는 기술
### 3. 머하웃 - 이어서
- 머하웃 아키텍처
  - 머하웃은 하둡의 분산 환경위에 맵리듀스를 기반으로 고급 분석을 지원하는 라이브러리 ㅐ키지
  - 하둡 클러스터 관점에서 보면 머하웃의 머신러닝 알고리즘이 맵리듀스에서 작동하도록 구현되었기 때문에 선형 확장으로 대규모(테라급 이상) 머신러닝 작업이 가능한 아키텍처를 가지고 있음.
  - 주요 관련 라이브러리로는 추천, 분류, 군집이 있음
  - 머하웃 아키텍처 구조
    - HDFS
    - YARN
    - 맵/리듀스
    - 머하웃 라이브러리
      - 추천(Recommendation)
      - 분류(Classification)
      - 군집(Clustering)
- 머하웃 활용 방안
  - 머하웃으로는 추천 라이브러리를 활용해 "차량용품 구매 이력 데이터"를 분석하고 스마트카 운전자 가운데유사 그룹 간의 구매 선호도에 따라 차량용품을 추천하는 작업을 함
  - 스마트카 고객 마스터 정보를 대상으로 군집 분석 진행, 고객군의 적정 개수 파악하는데 황용
  - 머하웃 활용 구조
    - 머하웃 라이브러리 
      - 추천(Recommendation)
      - 분류(Classification)
      - 군집(Clustering)
    - 스마트카 데이터셋 - Managed 영역
      - 스마트카 상태 정보
      - 이상 운행 패턴 정보
      - 운전자 운행 정보
      - 차량용품 구매이력 정보
      - 긴급점검 필요 차량 정보
      - 스마트카 고객 마스터 정보
    - 스마트카 고객 정보를 군집 분석
    - 차량용품 구매이력 분석으로 스마트카 운전자에게 상품 추천