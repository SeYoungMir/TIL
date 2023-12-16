# 6. 빅데이터 탐색
## 2. 빅데이터 탐색에 활용되는 기술
### 3. 우지
- 우지 소개
  - 하이브, 피그, 스파크 등을 이용해 빅데이터의 처라, 탐색, 분석하는 과정은 복잡한 선후행 관계를 맺고 반복적으로 진행
  - 대규모 빅데이터 시스템에서는 수집 및 적재된 수백 개 이상의 데이터셋을 대상으로 다양한 후처리 잡(Job)이 데이터 간의 의존성을 지켜가며 복잡하게 실햄됨
  - 이 같은 복잡한 데이터 파이프라인 작업을 위해 방향성 있는 비순환그래프(DAG : Direct Acyclic Graph)로 잡의 시작, 처리, 분기, 종료점 등의 액션(Action) 등을 정의하는 워크플로가 필요해짐
  - 이것이 바로 아파치 우지(Apache Oozie)
  - 우지는 2008년 Yahoo! 에서 개발, 2010년 오픈소스로 공개, 2011년에 아파치 오픈소스에 인큐베이션, 2012 아파치 최상위 프로젝트로 승격, 2023년 12월 5.2.1버전까지 릴리스
<table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://oozie.apache.org</td>
    </tr>
    <tr>
        <td rowspan=6>주요 구성 요소</td>
        <td>Oozie Workflow</td>
        <td>주요 액션에 대한 작업 규칙과 플로우를 정의</td>
    </tr>
    <tr>
        <td>Oozie Client</td>
        <td>워크플로를 Server에 전송하고 관리하기 위한 환경</td>
    </tr>
    <tr>
        <td>Oozie Server</td>
        <td>워크플로 정보가 잡으로 등록되어 잡의 실행, 중지, 모니터링 등을 관리</td>
    </tr>
    <tr>
        <td>Control 노드</td>
        <td>워크플로의 흐름을 제어하기 위한 Start,End,Decision 노드 등의 기능을 제공</td>
    </tr>
    <tr>
        <td>Action 노드</td>
        <td>잡의 실제 수행 태스크를 정의하는 노드로서 하이브, 피그, 맵리듀스 등의 액션으로 구성</td>
    </tr>
    <tr>
        <td>Coordinator</td>
        <td>워크플로 잡을 실행하기 위한 스케줄 정책을 관리</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>Azkaban,Cascading,Hamake,Airflow</td>
    </tr>
</table>