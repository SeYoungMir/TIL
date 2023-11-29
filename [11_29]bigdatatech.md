# 5. 빅데이터 적재 II - 실시간 로그/분석 적재
## 2. 빅데이터 실시간 적재에 활용하는 기술
### 1. HBase
- HBase 소개
  - NoSQL 데이터베이스들은 데이터를 키/값(Key/Value) 구조로 단순화하고, 칼럼 또는 도큐먼트 형식의 제약 사항이 적은 스키마 모델로 만들어 고성능 쓰기/읽기가 가능하다는 공통점
  - HBase는 하둡 기반의 칼럼 지향(Column-Oriented) NoSQL 데이터베이스로서, 스키마 변경이 자유롭고, 리전이라는 수십~ 수백 대의 분산 서버로 샤딩과 복제 등의 기능을 지원해 성능과 안정성을 보장하는 특징을 띰
  - 특히 하둡의 확장성과 내고장성을 그대로 이용할 수 있어 대규모 실시간 데이터 처리를 위한 스피드 레이어 저장소에 주로 사용
  - 구글의 BigTable 논문을 모델로 삼아 2006년 말에 개발이 시작, 2008에 하둡의 서브 프로젝트가 됨
- HBase의 기본 요소
<table>
    <tr>
        <td colspan=2>공식 홈페이지</td>
        <td>http://hbase.apache.org</td>
    </tr>
    <tr>
        <td rowspan=7>주요 구성 요소</td>
        <td>HTable</td>
        <td>칼럼 기반 데이터 구조를 정의한 테이블, 공통점이 있는 칼럼들의 그룹을 묶은 칼럼 패밀리와 테이블의 로우를 식별해서 접근하기 위한 로우키로 구성</td>
    </tr>
    <tr>
        <td>HMaster</td>
        <td>HRegion 서버를 관리, HRegion들이 속한 HRegion 서버의 메타 정보를 관리 </td>
    </tr>
    <tr>
        <td>HRegion</td>
        <td>HTable의 크기에 따라 자동으로 수평 분할이 발생, 이 때 분할된 블록을 HRegion 단위로 지정</td>
    </tr>
    <tr>
        <td>HRegionServer</td>
        <td>분산 노드별 HRegionServer가 구성되며, 하나의 HRegionServer에는 다수의 HRegion이 생성되어 HRegion을 관리</td>
    </tr>
    <tr>
        <td>Store</td>
        <td>하나의 Store에는 칼럼 패밀리가 저장 및 관리되며, MemStore와 HFile로 구성</td>
    </tr>
    <tr>
        <td>MemStore</td>
        <td>Store 내의 데이터를 인메모리에 저장 및 관리하는 데이터 캐시 영역</td>
    </tr>
    <tr>
        <td>HFile</td>
        <td>Store 내의 데이터를 스토리지에 저장 및 관리하는 영구 저장 영역</td>
    </tr>   
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>BigTable,Cassandra,MongoDB</td>
    </tr>
</table>
