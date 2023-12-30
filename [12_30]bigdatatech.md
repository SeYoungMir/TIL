# 7. 빅데이터 분석
## 2. 빅데이터 분석에 활용되는 기술
### 1. 임팔라
- 임팔라 소개
  - 2008년 하이브가 맵리듀스를 대체하는 SQL on Hadoop의 도구로 자리 잡음.
  - 생태계에서는 하이브의 배치성 분석에 만족하지 못하고, 빅데이터 분석을 인메모리 기반의 실시간 온라인 분석으로까지 확대되길 원함.
  - 이에 대한 변화는 구글에서 먼저 시작, 관련 기술이 적용된 드레멜(Dremel) 논문을 2010년 발표, 이 논문의 영향을 받은 클라우데라는 곧바로 임팔라(Impala) 개발에 착수, 2012년 10월 실시간 빅데이터 분석 질의가 가능한 임팔라를 오픈소스로 발표
  - 임팔라의 기본 요소
<table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://impala.apache.org</td>
    </tr>
    <tr>
        <td rowspan=6>주요 구성 요소</td>
        <td>Impalad</td>
        <td>하둡의 데이터노드에 설치되어 임팔라의 실행 쿼리에 대한 계획, 스케줄링, 엔진을 관리하는 코어 영역</td>
    </tr>
    <tr>
        <td>Query Planner</td>
        <td>임팔라 쿼리에 대한 실행 계획을 수립</td>
    </tr>
    <tr>
        <td>Query Coordinator</td>
        <td>임팔라 잡리스트 및 스케줄링을 관리</td>
    </tr>
    <tr>
        <td>Query Exec Engine</td>
        <td>임팔라 쿼리를 최적화해서 실행, 쿼리 결과를 제공</td>
    </tr>
    <tr>
        <td>StateStored</td>
        <td>분산 환경에 설치되어 있는 Impalad의 설정 정보 및 서비스를 관리</td>
    </tr>
    <tr>
        <td>Catalogd</td>
        <td>임팔라에서 실행된 작업 이력들을 관리,  필요 시 작업 이력을 제공</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>Tez,Spark SQL, Drill, Tajo</td>
    </tr>
</table>

- 임팔라 아키텍처
  - 임팔라의 아키텍처는 하둡의 분산 노드에서 대규모 실시간 분석을 위해 Impalad, Statestored, Catalogd라는 컴포넌트 설치.
  - Impalad는 HDFS의 분산 노드 상에서 실행 계획과 질의 작업을 수행하는 데몬
  - Statestored는 Impalad의 기본 메타 정보부터 각 분산 노드에 설치되어있는 Impalad를 관리하는 역할
  - Catalogd는 Impalad와 Statestored와 통신하면서 임팔라 SQL의 실행과 변경 이력 관리
- 임팔라 아키텍처 
  - 임팔라 1
    - 임팔라
      - Impalad
        - Query Planner
        - Query Coordinator
        - Query Exec Engine
      - Statestored
      - Catalogd
    - DataNode
  - 임팔라 2
    - 임팔라
      - Impalad
        - Query Planner
        - Query Coordinator
        - Query Exec Engine
  - 임팔라 3
    - 임팔라
      - Impalad
        - Query Planner
        - Query Coordinator
        - Query Exec Engine
- 임팔라 1에서 하이브Metastore,임팔라 Shell, JDBC/ODBC 클라이언트와 연결