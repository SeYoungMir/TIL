# 1. 빅데이터 이해하기
## 6. 빅데이터 구현 기술
- 빅데이터 아키텍처는 역할별로 수집, 적재, 처리 및 탐색, 분석 및 응용이라는 6개의 레이어로 나눌 수 있음


- 전처리
  - 수집 단계
    - 역할
      - 내·외부 데이터 연동
      - 내·외부 데이터 통합
    - 활용 기술
      - Crawling, FTP, OpenAPI, RSS, Log Aggregation, DB Aggregation, Streaming
  - 적재 단계
    - 역할
      - 대용량/실시간 데이터 처리
      - 분산 파일 시스템 저장
    - 활용 기술
      - Distributed File, No-SQL, Memory Cached , Message Queue
  - 처리 단계
    - 역할 
      - 데이터 선택, 변환, 통합, 축소
      - 데이터 워크플로 및 자동화
    - 활용 기술
      - Structured Processing,Unstructured Processing,WorkFlow, Scheduler
- 후처리
  - 탐색 단계
    - 역할
      - 대화형 데이터 질의
      - 탐색적 Ad-Hoc 분석
    - 활용 기술
      - SQL Like,Distributed Programming , Exploration Visualization
  - 분석 단계
    - 역할
      - 빅데이터 마트 구성
      - 통계 분석, 고급 분석
    - 활용 기술
      - Data Mining, Machine Learning, Analysis Visualization
- 활용
  - 응용 단계
    - 역할
      - 보고서 및 시각화
      - 분석 정보 제공
    - 활용 기술
      - Data Export/Import, Reporting, Business Visualization
- 구축 순서도 통상 수집 > 적재 > 처리 및 탐색 > 분석 및 응용 순으로 진행된
- 이 중 처리및 탐색 단계와 분석 및 응용 단계는 필요시 반복 진행하면서 데이터의 품질과 분석 수준을 향상시킴
- 빅데이터 아키텍처의 요소 기술들은 10~20개정도, 발생하는 데이터의 6V(Volume, Variety, Velocity , Veracity, Visualization, Value) 요건과 중요도에 따라 최적화된 아키텍처 구성