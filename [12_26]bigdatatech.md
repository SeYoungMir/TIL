# 6. 빅데이터 탐색
## 6. 탐색 파일럿 실행 4단계 - 데이터 탐색 기능 구현 및 테스트
- 앞에서 배운 탐색 기술들을 이용해 데이터 마트 형성
- 주로 External에 적재된 데이터를 Managed로 통합하는 하이브 QL 이용
- 일련의 작업들을 우지의 워크플로로 정의해 배치 잡으로 실행
- 총 5개 주제 영역에 대한 데이터 마트 구성, 5개의 우지 워크플로를 휴의 Job Designer에서 작성
- 실제 환경에서는 Data Warehouse와 Mart 영역을 단계별로 분리 구성
- 탐색 단계의 5가지 주제 영역
<table>
    <tr>
        <th></th>
        <th>주제 영역1</th>
        <th>주제 영역2</th>
        <th>주제 영역3</th>
        <th>주제 영역4</th>
        <th>주제 영역5</th>
    </tr>
    <tr>
        <th>주제 영역</th>
        <td>스마트카 상태 모니터링 정보</td>
        <td>스마트카 운전자 운행 기록 정보</td>
        <td>이상 운전 패턴 스마트카 정보</td>
        <td>긴급 점검이 필요한 스마트카 정보</td>
        <td>운전자의 차량용품 구매 이력 정보</td>
    </tr>
    <tr>
        <th>이용할 테이블</th>
        <td>스마트카 마스터 데이터<br>스마트카 상태 정보 데이터</td>
        <td>스마트카 마스터 데이터<br>스마트카 운전자 운행 데이터</td>
        <td>스마트카 운전자 운행기록 정보</td>
        <td>스마트카 상태 모니터링 정보</td>
        <td>스마트카 마스터 데이터 <br>스마트카 차량용품 구매이력 데이터</td>
    </tr>
    <tr>
        <th>워크플로 이름</th>
        <td>Subject 1 - Workflow</td>
        <td>Subject 2 - Workflow</td>
        <td>Subject 3 - Workflow</td>
        <td>Subject 4 - Workflow</td>
        <td>Subject 5 - Workflow</td>
    </tr>
    <tr>
        <th>스케줄러 이름</th>
        <td>Subject 1 - Coordinator</td>
        <td>Subject 2 - Coordinator</td>
        <td>Subject 3 - Coordinator</td>
        <td>Subject 4 - Coordinator</td>
        <td>Subject 5 - Coordinator</td>
    </tr>
    <tr>
        <th>수행 주기</th>
        <td>01:00/1Day</td>
        <td>02:00/1Day</td>
        <td>03:00/1Day</td>
        <td>04:00/1Day</td>
        <td>05:00/1Day</td>
    </tr>
    <tr>
        <th>생성할 마트 테이블</th>
        <td>Managed_SmartCar_Status_Info</td>
        <td>Managed_SmartCar_Drive_Info</td>
        <td>Managed_SmartCar_Stmptom_Info</td>
        <td>Managed_SmartCar_Emergency_Check_Info</td>
        <td>Managed_SmartCar_Item_BuyList_Info</td>
    </tr>
</table>

### 1. 스마트카 상태 정보 데이터 생성
- 로그 시뮬레이터를 이용해 오늘 날짜의 "스마트카 상태 정보 데이터" 셍상. 수행하는 시점의 날짜를 입력,사용
- 파일이 100MB 파일 크기로 생성된 것을 확인, 로그시뮬레이터 종료
### 2. 스마트카 상태 정보 데이터 적재
- 스마트카 상태 정보 데이터를 플럼의 수집 디렉터리로 이동, 플럼이 수집 작업 시작
- 플럼이 수집해서 하둡에 적재 완료 되기까지 약 5~10분 소요
### 3. 스마트카 상태 정보 데이터 적재 확인
- 스마트카 상태 정보가 HDFS에 정상적으로 적재되었는지 확인
- 크기가 65,52MB로 나뉜 파일이 존재하는 지 확인, .tmp파일이 존재 시 아직 플럼에서 적재중인 것
### 4. 스마트카 운전자 운행 로그 생성
- 로그 시뮬레이터를 이용해 오늘 날짜의 100대 "스마트카 운전자 운행 데이터" 생성
- 플럼,카프카,스톰,레디스,HBase 서버가 정상 상태인지 확인, 스톰의 경우 자동 스타트가 안 되는 경우가 있으므로 스톰의 Nimbus,Supervisor 기동 상태 확인.
- 수집/적재 기능이 모두 정상이면 스마트카 실시간 운행 로그 데이터 생성.
### 5. 스마트카 운전자 운행 로그 확인
- 실시간 운행 로그 데이터가 정상적으로 생성되었는지 확인
- 로그는 24시간 기준으로 지속성 생성, tail 명령으로 실시간 로그 기록 확인 가능
### 6. 스마트카 운전자의 운행 데이터 적재 확인
- 모든 운행 데이터가 HBase에 정상적으로 적재되었는지 휴를 통해 확인
- 레디스 CLI를 실행해 과속한 스마트카 차량 정보 확인
- 과속 차량 3대 이상 발견 시 스마트카 운전자 운행 로그 시뮬레이터 종료
