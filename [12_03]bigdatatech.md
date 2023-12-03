# 5. 빅데이터 적재 II - 실시간 로그/분석 적재
## 2. 빅데이터 실시간 적재에 활용하는 기술
### 3. 스톰 - 이어서
- 스톰 아키텍처
  - 스톰의 아키텍처 이해 위해서는 먼저 Nimbus와 Supervisor의 역할을 알아야 함
  - Nimbus는 자파 프로그램으로 구성된 Topology Jar를 배포하기 위해 주키퍼로부터 Supervisor 정보를 알아냄
  - 그 후 해당 Topology Jar파일을 각 Supervisor에 전송, Supervisor는 해당 Node에서 Worker,Executor를 생성, Spout과 Bolt가 실행되기 위한 Task 할당
  - Supervisor가 정상적으로 배포 시, External Target Application 1 에서 발생한 데이터가 Spout을 통해 유입되기 시작, 이를 Bolt가 전달받아 데이터를 분산 처리하고, 처리 결과는 Bolt를 통해 타깃 시스템인 External Target Application 2로 전송
  - Task, Executor 개수를 증가시키면서 대규모 병렬 처리 가능, Spout와 Bolt의 성능 향상
  - 스톰의 아키텍처는 매우 견고한 장애 복구 기능도 제공.
  - 만약 특정 Supervisor가 생성한 Worker 프로세스에 심각한 문제가 발생해 종료되면 Supervisor는 새로운 Worker 프로세스를 다시 생성, 이 때 처리 중이던 데이터들(튜플)은 이전 수신지로 롤백, Topology가 다시 정상적으로 복구되면 롤백 시점부터 다시 처리하면서 데이터의 정합성 보장
  - 스톰 아키텍처
    - Nimbus
    - 주키퍼
    - Node1
      - Supervisor
        - Worker
          - Executor 
            - Task
                > External Target App 1
            - Spout
          - Executor
            - Task
            - Bolt
          - Executor
            - Task
            - Bolt
                > External Target App 2
    - Node2
      - Supervisor
        - Worker
          - Executor 
            - Task
            - Spout
          - Executor
            - Task
            - Bolt
- 스톰 활용 방안
  - 스톰은 파일럿프로젝트에서 스마트카 운전자의 실시간 운행 정보를 대상으로 데이터라우팅과 스트리밍 처리에 활영
  - 일단 카프카의 Spout를 통해 유입되는 모든 운전자의 운행 정보 데이터는 두 개의 Bolt(HBase Bolt, Redis Bolt)로 나눠져서 처리, HBase Bolt는 모든 운행 정보를 정제 없이 HBase 서버에 곧바로 적재, 레디스 Bolt는 에스퍼라는 룰 엔진이 감지한 이상 운행 패턴의 정보만 레디스 서버에 적재
  - 운전자 운행 로그 400KB/1초
  - 플럼
  - 카프카
  - 스톰
    - Spout
      - Bolt
        - Bolt > HBase
        - Bolt > 레디스
      - 실시간 운행 로그 데이터 병렬 처리
      - 실시간 운행 로그 데이터 분석 결과 처리