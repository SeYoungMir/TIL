# 6. 빅데이터 탐색
## 2. 빅데이터 탐색에 활용되는 기술
### 4. 휴
- 휴 소개
  - 빅데이터 탐색 / 분석은 장기간의 반복 작업이면서 그 과정에 있어 많은 도구들이 활용됨
  - 주로  하둡을 기반으로 하이브, 피그, 우지, 스쿱, 스파크  등이 해당, 이를 일반 분석가 또는 업무 담당자들이 각 서버에 직접 접속해 사용하기에는 어려움이 많음
  - 빅데이터 기술이 성숙해지면서 이러한 기술의 복잡도를 숨기고 접근성과 편의성을 높인 소프트웨어들이 만들어짐, 그 중 하나가 바로 클라우데라에서 만든 휴(Hue)
  - 휴는 다양한 하둡의 에코시스템의 기능들을 웹 UI로 통합 제공.
  - 오픈소스로 깃허브에 공개되어 있으며, 2023년 12월 기준 공식 사이트에서 5.0 버전까지 릴리스
<table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://gethue.com</td>
    </tr>
    <tr>
        <td rowspan=6>주요 구성 요소</td>
        <td>Job Designer</td>
        <td>우지의 워크플로 및 Coordinator를 웹UI에서 디자인</td>
    </tr>
    <tr>
        <td>Job Browser</td>
        <td>등록한 잡의 리스트 및 진행 상황과 결과 등을 조회</td>
    </tr>
    <tr>
        <td>Hive Editor</td>
        <td>하이브 QL을 웹 UI에서 작성, 실행,관리</td>
    </tr>
    <tr>
        <td>Pig Editor</td>
        <td>피그 스크립트를 웹 UI에서 작성, 실행,관리</td>
    </tr>
    <tr>
        <td>HDFS Browser</td>
        <td>하둡의 파일 시스템을 웹 UI에서 탐색 및 관리</td>
    </tr>
    <tr>
        <td>HBase Browser</td>
        <td>HBase의 HTable을 웹 UI에서 탐색 및 관리</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>NDAP,Flamingo,Ambari</td>
    </tr>
</table>