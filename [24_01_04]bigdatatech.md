
# 7. 빅데이터 분석
## 2. 빅데이터 분석에 활용되는 기술
### 4. 스쿱
- 스쿱 소개
  - RDBMS에 있는 데이터를 특별한 전처리 없이 곧바로 HDFS에 적재하거나, 반대로 HDFS에 저장된 데이터를 RDBMS로 제공해야 하는 경우, 둘 사이에서 데이터를 편리하게 임포트하거나 익스포트 해주는 소프트웨어
  - 2009년에 공개, 2012년 아파치 최상위 프로젝트로 승격
  - 스쿱의 두 가지 버전
    - 초기 버전은 CLI 기반으로 스쿱 명령을 실행하는 스쿱 1 클라이언트 버전
    - 두번째 버전인 스쿱 2는 스쿱 서버를 두고 스쿱 클라이언트가 API를 호출하는 방식으로 스쿱 1을 확장한 서버 버전
<table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://sqoop.apache.org</td>
    </tr>
    <tr>
        <td rowspan=5>주요 구성 요소</td>
        <td>Sqoop Client</td>
        <td>하둡의 분산 환경에서 HDFS와 RDBMS 간의 데이터 임포트 및 익스포트 기능을 수행하기 위한 라이브러리로 구성</td>
    </tr>
    <tr>
        <td>Sqoop Server</td>
        <td>스쿱 2 의 아키텍처에서 제공, 스쿱 1의 분산된 클라이언트 기능을 통합해 REST API로 제공</td>
    </tr>
    <tr>
        <td>Import/Export</td>
        <td>임포트 기능을 RDBMS의 데이터를 HDFS로 가져올 때 사용하며, 반대로 익스포트 기능은 HDFS의 데이터를 RDBMS로 내보낼 때 사용</td>
    </tr>
    <tr>
        <td>Connectors</td>
        <td>임포트 및 익스포트에서 사용될 다양한 DBMS의 접속 어댑터와 라이브러리를 제공</td>
    </tr>
    <tr>
        <td>Metadata</td>
        <td>스쿱 서버를 서비스하는데 필요한 각종 메타 정보를 저장</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>Hiho,Talend,Kettle</td>
    </tr>
</table>