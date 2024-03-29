# 6. 빅데이터 탐색
## 2. 빅데이터 탐색에 활용되는 기술
### 3. 우지 - 이어서
- 우지 아키텍처
  - 우지 클라이언트에서 작성한 워크플로는 우지 서버로 전송되어 메타화되고 RDBMS에 저장됨
  - 우지 서버에 있는 Coordinator는 우지에 등록된 워크플로를 스케줄링해주며, 이 때 워크플로 엔진이 Action 노드와 Control 노드의 정보를 해석하면서 관련 태스크를 하둡의 클러스터에서 실행시킴
  - 주요 Action Task로는 하이브, 피그, 스쿱(Sqoop) 등이 있고 관련 Action은 최종적으로 하둡의 맵리듀스 프로그램을 기반으로 작동
  - 실행 중인 태스크 라이프 사이클을 우지 서버가 시작부터 종료까지 추적하면서 모니터링 정보를 제공함
  - 하둡 2.x부터는 얀을 기반으로 더욱 다양한 애플리케이션을 실행할 수 있게 되었고, 우지에서도 이를 지원하기 위한 다양한 태스크 Action들이 추가되고 있음.
  - 우지 아키텍처
    - 우지 클라이언트
      - REST API
      - Workflow Submission
    - 우지 서버
        - Coodinator& Polling
      - RDBMS
        - Workflow Definitions
        - Workflow Running
      - 하둡
        - Launcher Job
          - Map Task
        - Actual Job
          - 맵/리듀스
          - 하이브/피그
          - 스쿱
          - 스파크
- 우지 활용 방안
  - 우지를 활용해 후처리 작업을 정의, 프로세스화
  - 적재된 데이터를 External > Managed > Mart로 이동시키기 위해 다양한 하이브 QL들이 이용, 이를 약속된 시간에 따라 스케줄링해서 실행. 이 때 우지의 워크플로 활용
  - 우지 활용 방안
    - External 영역
      - 스마트카 상태 데이터
    - HBase 
      - 운전자 운행 데이터
    - 우지 - 워크플로 1...N
      - 하이브 Action 1,2,...N
    - Managed 영역
      - 스마트카 상태 데이터
      - 운전자 운행 데이터
      - 스마트카 마스터 데이터
      - 차량용품 구매이력 데이터
    - 우지 - 워크플로 2...N
      - 하이브 Action 1,2,..N
    - Mart 영역
      - 분석주제 1,2...N
    - 스마트카의 빅데이터 웨어하우스 구축을 위한 단계별 워크플로 기능 제공
    - 워크플로를 주기적으로실행 및 관리하기 위한 Coordinator 기능 제공