## 4. 데이터 조작 프로시저 최적화하기
### 1. 데이터 조작 프로시저 성능 개선
#### 1. APM(Application Performance Manangement) 도구의 이해
1. APM 정의
   - 운영 중인 시스템에 대한 가용성 확보, Minimum Down Time 등의 최소화를 통한 안정적 시스템 운영을 위하여, 부하량과 접속자 파악 및 장애 진단 등의 목적을 둔 모니터링 도구
2. APM 유형
   1. Resource monnitoring
      - CPU,Memory,Network,Disk 등 모니터링
      - Nagios,Zabbix,Cacti 등이 대표적 오픈 소스
   2. End to End monitoring
      - 비즈니스 트랜잭션 관리 및 최종 사용자에 대한 모니터링
      - VisualVM이 대표적 오픈소스, 제니퍼, 파로스, 시스마스터는 대표 상용제품
#### 2. SQL 처리 흐름
1. 구문 분석 단계
   1. 사용자가 실행한 SQL문이 데이터베이스에서 처음 사용된 문장인지 이미 사용된 문장인지를 공유 풀 영역을 검색하여 확인
   2. 이미 사용된 문장이라면 구문분석 작업을 할 필요가 없고, 처음 사용되었다면 구문분석 작업 필요
   3. 구문분석 단계에서 SQL 문의 문법이 제대로 작성되었는지를 분석
2. 실행단계
   1. 구문분석이 정상 실행되면 서버 프로세스는 메모리 영역의 데이터베이스 버퍼 캐시 영역을 검색하여 해당 테이블이 다른 사용자의 다른 SQL문에 의해 이미 데이터버퍼 캐시영역에 존재하는지 검색
   2. SQL문의 캐시 영역에 존재하지 않을 경우, 해당 데이터 파일로부터 테이블을 읽어 데이터 버퍼 캐시영역에 저장
3. 인출단계
   1. 실행단계 종료 후 서버프로세스는 데이터버퍼 캐시 영역에서 관련 테이블 데이터를 읽어 사용자의 클라이언트 화면에 출력
   2. 단,SELECT 문을 실행하는 경우에만 인출단계가 실행되고 UPDATE,INSERT,DELETE문은 인출단계 실핼되지 않음
#### 3.TKPROF
1. TKPROF 개념
   - SQL Trace를 통해 생성된 Trace 파일을 분석이 가능한 형식으로 전환하여 출력
2. TKPROF 문법
    ```sql
    TKPROF tracefile outputfile
    
    [SORT=parameters][PRINT=number][EXPLAIN=username/password]
    ```
    1. tracefile : SQL Trace에 의해 생성된 통계정보를 가진 유저 덤프 파일명
    2. outputfile : TKPROF가 읽기 가능한 텍스트 파일로 생성할 파일명
    3. sort : 지정된 option에 ASC 순으로 SQL문을 정렬
    4. print : 지정된 수의 SQL 문에 대해서만 TRACE 결과를 출력
    5. explain : SQL문의 EXCUTIONPLAN(실행 계획)을 수립하고 저장

3. TKPROP 통계 정보 설명
<table>
    <tr>
        <th>로우/칼럼</th>
        <th>설명</th>
    </tr>
    <tr>
        <td>Parse</td>
        <td>SQL문이 파싱되는 단계에 대한 통계</td>
    </tr>
    <tr>
        <td>Execute</td>
        <td>SQL문의 실행 단계에 대한 통계</td>
    </tr>
    <tr>
        <td>Fetch</td>
        <td>SQL문이 실행되면서 페치된 통계</td>
    </tr>
    <tr>
        <td>count</td>
        <td>SQL문이 파싱/실행/페치가 수행된 횟수</td>
    </tr>
    <tr>
        <td>cpu</td>
        <td>parse,execute,fetch가 실제로 사용한 CPU 시간</td>
    </tr>
    <tr>
        <td>elapsed</td>
        <td>작업의 시작에서 종료시까지 실제 소요된 시간</td>
    </tr>
    <tr>
        <td>disk</td>
        <td>디스크에서 읽혀진 데이터 블럭의 수</td>
    </tr>
    <tr>
        <td>query</td>
        <td>메모리 내에서 변경되지 않은 블럭을 읽거나 다른 세션에 의해 변경되었으나 아직 커밋되지 않아 복사해 둔 스냅샷 블럭을 읽은 블럭 수</td>
    </tr>
    <tr>
        <td>current</td>
        <td>현 세션에서 작업한 내용을 커밋하지 않아 오로지 자신에게만 유효한 블럭을 액세스한 블럭 수</td>
    </tr>
    <tr>
        <td>rows</td>
        <td>SQL문을 수행한 결과에 의해 최종적으로 액세스된 로우의 수</td>
    </tr>
</table>