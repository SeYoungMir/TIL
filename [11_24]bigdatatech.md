# 4. 빅데이터 적재 I - 대용량 로그 파일 적재
## 2. 빅데이터 적재에 활용하는 기술
### 3. 하둡 활용 방안
- 하둡 활용 방안
    - 스마트카 상태 정보 100MB/1일
    - 수집
    - 플럼
    - 적재
    - 하둡
    - DataNode 1,2,3
        - HDFS
        - 일자별 스마트카 상태 정보
        - 맵&리듀스
    - 스마트카의 상태 정보를 장기 적재
    - 일/주/월/년 단위의 시계열 분석
- 위는 파일럿 프로젝트에서 하둡의 역할 설명
- 스마트카 상태 정보 로그는 비교적 큰 크기(100MB 이상, 실제 환경에서는 GB 이상의 파일을 저장)의 파일, HDFS의 특정 디렉터리에 일자 단위로 파티션해서 적재함
- 일 단위로 분리 적재된 데이터는 일/주/월/년 별로 스마트카의 다양한 시계열 집계 분석을 효율적으로 수행 가능, 데이터를 재적재해야 하는 경우 전체 데이터가 아닌 해당 파티션의 데이터만 재적재 가능한 장점
- 파일럿 환경에서는 일련의 작업 처리 위해 주로 하이브 사용, 대규모 하이브 작업에서는 분산 병렬 처리를 위해 맵리듀스 프로세스가 내부적으로 작동.
- 하이브에서 처리된 결과는 다시 HDFS의 특정 영역(Hive Data Warehouse)에 저장, 이 데이터를 스마트카의 고급 분석으로까지 확장해서 사용함
### 4.주키퍼
- 주키퍼 소개
  - 수십~ 수천 대의 서버에 설치되어 있는 빅데이터 분산 황경을 더욱  효율적으로 관리하기 위해 서버 간의 정보를 쉽고 안전하게 공유해야함
  - 공유된 정보를 이용해 서버 간의 중요한 이벤트(분산 락, 순서 제어, 부하 분산, 네임 서비스 등)을 관리하면서 상호 작용을 조율해 주는 코디네이터 시스템이 분산 코디네이터인 아파치 주키퍼(Apache Zookeeper)
  - 주키퍼는 하둡,HBase, 카프카, 스톰 등의 분산 노드 관리에 사용 중
  - 최초 하둡의 서브 프로젝트로 시작, 아파치 최상위 프로젝트로  승격, 독립적으로 발전 중
- 주키퍼의 기본 요소
  <table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://zookeeper.apache.org</td>
    </tr>
    <tr>
        <td rowspan=5>주요 구성 요소</td>
        <td>Client</td>
        <td>주키퍼의 ZNode에 담긴 데이터에 대한 쓰기, 읽기, 삭제 등의 작업을 요청하는 클라이언트
        </td>
    </tr>
    <tr>
        <td>ZNode</td>
        <td>주키퍼 서버에 생성되는 파일 시스템의 디렉터리 개념, 클라이언트의 요청 정보를 계층적으로 관리(버전, 접근 권한, 상태, 모니터링 객체 관리 등의 기능 지원)</td>
    </tr>
    <tr>
        <td>Ensemble</td>
        <td>3대 이상의 주키퍼 서버를 하나의 클러스터로 구성한 HA 아키텍처</td>
    </tr>
    <tr>
        <td>Leader Server</td>
        <td>Ensemble 안에는 유일한 리더 서버가 선출되어 존재, 클라이언트의 요청을 받은 서버는 해당 요청을 리더 서버에 전달, 리더 서버는 모든 팔로워 서버에게 클라이언트 요청이 전달되도록 보장</td>
    </tr>
    <tr>
        <td>Follower Server</td>
        <td>Ensemble 안에서 한 대의 리더 서버를 제외한 나머지 서버, 리더 서버와 메시지를 주고받으면서 ZNode의 데이터를 동기화, 리더 서버에 문제가 발생할 경우 내부적으로 새로운 리더를 선출하는 역할을 수행</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>Chubby,Doozerd,Consul</td>
    </tr>
</table>