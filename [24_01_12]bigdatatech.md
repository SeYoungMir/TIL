# 7. 빅데이터 분석
## 8. 분석 파일럿 실행 6단계 - 스쿱을 이용한 분석 결과 외부 제공
- 빅데이터 시스템에서 탐색 및 분석한 결과는 외부 업무시스템에 제공되어 중요한 의사결정 포인트로 활용될 수 있어야 함
- 그를 위해 빅데이터의 HDFS에 저장된 데이터를 외부 시스템의 저장소(RDBMS)로 제공할 수 있어야하는데, 이때 스쿱을 이용할 수 있음.
- 외부시스템의 저장소(RDBMS)에 있는 데이터를 HDFS로 가져오기를 할 때도 스쿱을 이용할 수 있음.
- 파일럿 프로젝트에서는 분석한 결과를 외부 RDBMS에 제공하는 내보내기 기능을 사용해봄
### 1. 스쿱의 내보내기 기능 -이상 운전 차량 정보
- 6장의 데이터 탐색에서 3번째 주제 영역 탐색의 결과로 "스마트카 이상 운전 차량" 결과를 도출, 해당 데이터를 하이브의 Managed 영역 테이블로 저장
- 스쿱을 이용, "이상 운전 차량 정보" 데이터셋을 PostgreSQL로 내보내기
- PostgreSQL서버는 클라우데라의 CM에 기본으로 설치된 데이터베이스 활용
- 스쿱의 Export 기능은 일/주/월/연별 주기적으로 수행해야하는 배치성 작업.
- 이를 위해 휴의 우지 워크플로에서 스쿠브이 작업 노드를 이용, 정기적 스쿱 Export작업 실행 가능
- 스쿱을 활용할 때 주의할 점
  - 일반적으로 RDBMS는 중요 업무 시스템의 온라인 서빅스 저장소로 사용
  - 스쿱의 대규모 Export/Import 맵(Map)작업들이 RDBMS에 연결되면 큰 오버헤드 발생 가능
  - 이를 통해 100대의 서버에서 동시에 Map 작업 생성 ,RDBMS로 연결된 JDBC 작업 수행 가능.
  - 이로 인해 RDBMS의 자원 점유율이 커지고 이를 사용하는 중요 온라인 시스템 서비스에 영향이 갈 수 있음
  - 스쿱의 실행 옵션 중 --split-by 또는 --num-mappers를 이용,문제를 최소화