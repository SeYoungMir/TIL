# 6. 빅데이터 탐색
## 2. 빅데이터 탐색에 활용되는 기술
### 2. 스파크
- 스파크 소개
  - 하이브는 복잡한 맵 리듀스를 하이브 QL로 래핑해 접근성을 높일 수 있었지만 맵 리듀스 코어를 그대로 사용함으로써 성능 면에서는 만족스럽지 못했음.
  - 그로 인해 반복적인 대화형 연산 작업에서는 하이브가 적합하지 않았고, 이러한 하이브의 단점을 극복하기 위한 다양한 시도 중 하나가 스파크
  - 스파크는 UC 버클리의 AMPLab에서 2009년 개발, 2010년 오픈소스로 공개, 2013년 6월 아파치 재단으로 이관, 최상위 프로젝트가 됨
  - 빅데이터 분야에서 가장 핫한 기술중 하나로 2023년 12월 기준 3.5.0까지 릴리스 됨
  <table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://spark.apache.org</td>
    </tr>
    <tr>
        <td rowspan=7>주요 구성 요소</td>
        <td>Spark RDD</td>
        <td>스파크 프로그래밍의 기초 데이터셋 모델</td>
    </tr>
    <tr>
        <td>Spark Driver/ Executors</td>
        <td>Driver는 RDD 프로그램을 분산 노드에서 실행하기 위한 Task의 구성, 할당, 계획 등을 수립하고, Executor는 Task를 실행 관리하며, 분산 노드의 스토리지 및 메모리를 참조</td>
    </tr>
    <tr>
        <td>Spark Cluster Manager</td>
        <td>스파크 실행 환경을 구성하는 클러스터 관리자로 Mesos, YARN, Spark Standalone이 있음</td>
    </tr>
    <tr>
        <td>Spark SQL</td>
        <td>SQL 방식으로 스파크 RDD 프로그래밍을 지원</td>
    </tr>
    <tr>
        <td>Spark Streaming</td>
        <td>스트리밍 데이터를 마이크로 타임의 배치로 나누어 실시간 처리</td>
    </tr>
    <tr>
        <td>Spark MLib</td>
        <td>스파크에서 머신러닝 프로그래밍(군집,분류,추천등)을 지원</td>
    </tr>
    <tr>
        <td>Spark GraphX</td>
        <td>다양한 유형의 네트워크(SNS,하이퍼링크 등)구조 분석을 지원</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>Impala,Tajo,Tez</td>
    </tr>
</table>