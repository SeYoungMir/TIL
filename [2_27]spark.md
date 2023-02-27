## 스파크로 구축하는 분산처리 빅데이터 플랫폼
### Before we start
- 수집영역
  - 플럼
  - 카프카
  - 스톰(카프카의 발전)
- 적재 영역
  - 하둡(플럼에서) = HDFS
    - Windows에서는 FAT/NTFS
    - Linux에서는 EXT4
    - 구글은 GFS
  - HBASE(카프카/스톰에서), 하둡 DB
- 처리/탐색
  - 하이브
- 분석/활용 영역
  - R/스파크
- 하둡의 기본은 Linux(OS), Java(프로그램),Scala(프로그램)
- 하둡 에코 시스템
  - 기본적으로 Linux, Java를 이용
  - HDFS(Data storage)
  - MapReduce(Data Processing)
  - HBase(NoSQL Database)
  - Pig(Scripting)
  - HCatalog(Metadata Management)
  - Hive(SQL-like Queries)
  - Mahout(Machine Learning, Library <업그레이드 잘 안됨, Tensorflow import) 
  - ZooKeeper(Cluster Coordination(전체 관리))
  - Ambari(Cluster installation & management)
  - Oozie(Workflow Automatization)
  - Scoop(Import & Export of relational data - 데이터 수집)
  - Flume(Import & Export of data flows - 로그 데이터 수집
### 빅데이터 플랫폼 
1. 프로세스
   - 전형적인 빅데이터 처리 과정
     - 데이터 수집 -> 저장 -> 분석 -> 시각화 -> 서비스
2. 오픈 소스 기술
   - 필요한 S/W 기술
     - 하둡 에코시스템에서 제공하는 오픈소스 S/W와 상용 S/W와의 연계를 통해 빅데이터 분석/서비스 시스템 구축
       - 수집(ETL) -> Flume
         - Load Valancing : Collector 분산 , 노드 부하 모니터링
         - Fault Tolerance : 노드 장애 시 다른 노드로 전환 
         - Network Traffic 분산
         - 다수의 Collector에 Traffic 분산 & local Disk 저장
           - Hadoop Network & Hacked Together to HDFS
         - Fire & Forget Agent 서버 실패시 재전송, End to End 전송 보장
         - Management
         - 중앙관리 시스템 : N Agent & N Collect Node
       - 저장 -> HDFS,Hive,Hbase
         - HDFS : 분산파일 시스템
         - Hive : HDFS 기반의 Database, Data는 HDFS에 저장, 스키마 정보는 Mysql에 저장,HiveQL -> SQL Query로 분석(select,groupby,join,union...)
         - HBASE: NoSQL for Hadoop, Data는 HDFS에 저장, 스키마 정보는 Hbase Region Server에서 관리, 노드당 초당 수만개 Rows Insert, 수십만 Rows Read&Scan
       - 분석 -> MapReduce,HiveQL,Pig,R
         - MapReduce : 분산 병렬 처리 시스템
         - HiveQL : SQL Query Language & Dataware House MySQL Query와 유사, HDFS와 HBASE에 저장된 Data 분석 언어
         - Pig : Pig Latin Script Language 
         - Data & Flow 기반의 분산병렬 처리 언어, Hive와 동일하게 HDFS와 HBASE에 저장된 Data 분석
         - R& RHadoop Package 
         - RHadoop 패키지에서 HDFS에 저장된 데이터를 Input으로 해서 통계분석 처리
### 연계 및 수집 Layer
- 요구사항 및 구성 요소 정의
  - 연계 및 수집 요구사항
    - 다양한 데이터 연계 수집
      - 정형 및 비정형 데이터를 모두 연계/수집 할 수 있도록 구성 필요
    - 다양한 환경 지원
      - 내부/그룹사/웹사이트 등 정보 제공처의 다양한 환경을 고려한 구성 필요
    - 대용량 데이터 수집 지원
      - 수집되는 데이터는 상당수가 대용량 데이터일 것으로 예상됨 대용량 데이터를 충분히 수집할 수 있도록 구성 필요
    - 다양한 연계 방식 지원
      - 수집되는 데이터의 특성에 따라 다양한 방식으로 연계/수집 할 수 있도록 구성 필요
    - 다양한 네트워크 구성 지원
      - 내부망, 외부망, 전용선 등 다양한 네트워크를 지원할 수 있도록 구성 필요
    - 소셜/웹 데이터 수집 지원
      - 소셜 및 웹사이트의 데이터 수집을 지원할 수 있도록 구성 필요
    - 수동 데이터 업로드 지원
      - 시스템에 의한 자동 연계 외에 수동으로 데이터 업로드를 지원할 수 있도록 구성 필요
  - 연계 및 수집 구성 요소
    - 데이터 소스
      - 정형 데이터(DB,Excel,XML)
      - 비정형 데이터(File, Web)
    - 네트워크
      - 내부망
      - 전용선
      - 일반 인터넷
      - 오프라인(사람)
    - 데이터 채널
      - 연계를 위한 다양한 소스 채널
      - 유관기관 제공 API
      - Open API
      - 수집 Agent
    - 연계/수집 기술
      - SOA 방식 데이터 수집 기술
      - RDBMS 데이터 Import 기술
      - ETL Tools
      - SFTP, 웹크롤링
      - On-Demand 데이터 업로드
    - 연계/수집 관리 도구
      - 연계/수집한 데이터에 대한 모니터링 및 내역 관리
### 저장 및 처리 Layer
- 요구사항 및 구성 요소 정의
  - 저장 및 처리 요구사항
    - 통합 운영/관리 데이터 저장소
      - 데이터의 저장과 운영에 필요한 통합적인 운영/관리 기능을 지원
    - 분석을 위한 데이터 임시저장소
      - 분석을 위하여 수집된 데이터의 임시저장소로, 분석이 완료된 데이터는 폐기(삭제)함
    - 백업을 위한 데이터 저장소
      - 중요한 자료는 반드시 백업이 필요하며, 이를 위한 백업 저장소의 기능을 지원 해야 함
    - 데이터 가공을 위한 기반
      - 수집된 데이터를 전처리(가공)하여 분석에 활용될 수 있도록 지원
    - 쉬운 데이터 처리
      - 데이터 처리를 쉽게 할 수 있는 SQL 쿼리 지원
    - 대용량 데이터 저장
      - 데이터센터, 그룹사 및 외부로 부터 수집하는 데이터의 양이 증가할 것을 대비하여 대용량 데이터를 충분히 저장할 수 있는 확장성 있는 구성이 필요
    - 다양한 데이터 저장 
      - 분석에 활용되는 데이터의 종류 및 형태(정형/비정형)는 다양하므로 이를 체계적으로 저장할 수 있는 구성을 지원
  - 구성 요소
    - 저장 데이터 형식
      - 정형 데이터
        - RDBMS 
     - 준정형 데이터
       - NoSQL
     - 비정형 데이터 및 원본로그
       - File(로컬 및 분산파일)
    - 대용량 데이터 저장소
     - 분산파일시스템
     - SQL on Hadoop(타조 등)
     - NoSQL(HBase,몽고DB 등)
     - 원본 데이터 저장소 역할
    - 하이브리드 DW
     - 하둡기반의 SQL과 상용 RDBMS/MPP(엑사데이터,그린플럼)가 연계된 통합 DataWarehouse
    - 배치 처리/SQL/CEP
     - 데이터 처리를 위한맵리듀스 및 SQL 쿼리 지원 
     - 실시간 데이터 처리를 위한CEP 지원
    - 데이터 관리 및 연계
     - 메타데이터 관리 
     - 데이터 통합 관리를 위한 운영/관리 시스템
     - R/SAS 등 통계패키지와의 연계
     - OLAP 및 분석 솔루션과의 연계
- 구성도 – 통합 저장 플랫폼 및 특징
  - 다양한 유형의 저장소 구성
    - 빅데이터 공통기반으로 수집되 는 데이터 유형이 다양하기 때문에, 다양한 유형의 데이터를 저장할 수 있는 체계를 구성함
    - 수집된 데이터는 해당 데이터의 포맷에 따라 각각의 저장소에 저장될 수 있도록 구성
  - 하이브리드 DW / SQL 쿼리
    - 데이터 분석 효율의 극대화 및NoSQL DB기반의 분석도구를 활용하기 위하여 NoSQL 데이터를 저장하기 위한 환경 구성
    - 데이터 저장 도구는 서로 다르지만 SQL 쿼리를 모두 지원하는 기술이 요구됨(타조,임팔라 등 SQL on Hadoop)
  - 유연한 데이터 교환 기반 구성
    - RDB/NoSQL/HDFS(File)간의 데이터를 변환하여 저장할 수 있는 기반을 구성하여 제공함
    - 데이터 변환은 분석플랫폼의 데이터 변환 도구를 활용함
  - 관리/운영을 위한 DB 구성
    - 수집되는 다양한 데이터의 저장 및 폐기(삭제)이력을 관리할 수 있는 체계 구성
    - 저장 데이터와 활용채널간의 관계를 관리할 수 있는 체계를 구성
### 분석 및 시각화 Layer
- 주요 분석 기법
  - 텍스트 마이닝
  - 웹 마이닝
  - 오피니언 마이닝
  - 리얼리티 마이닝
  - 소셜 네트워크 분석
  - 분류
  - 군집화
  - 기계학습
  - 감성 분석 등
- 통계/분석 절차
  - 데이터 선정
  - 데이터 정제
  - 데이터 변형
  - 모델링
  - 해석/평가
- 시각화 주요 기능
  - Spatial information flow
  - Clustergram
  - History Flow
  - Facebook Transaction
  - Heat Map
  - R
## Hadoop Ecosystem
### 빅데이터 플랫폼과 하둡 에코시스템
#### 빅데이터 플랫폼
- 인프라
- 연계/수집
- 저장/처리
- 분석
- 서비스/ 시각화
#### 하둡 에코시스템 기술의 이해
1. 대용량 데이터 처리
   - 처리 속도의 발전
     - 1단계 : CPU의 Clock Frequency 늘리기
       - 무어의 법칙 : 동일한 면적의 반도체 직접회로의 트랜지스터의 개수가 18개월에 2배씩 증가
       - CPU Clock 물리적인 한계 : 최대 4Gh
     - 2단계 : Single CPU에서 Multi CPU & Core 
       - 1 CPU -> 2 CPU(최적) -> 4 CPU -> 8 CPU
       - 1 CPU : 1 Core -> 2 Core -> 4 Core -> 6 Core -> 8 Core
     - 3단계 : Single Machine -> Cluster( N대의 Machine을 Network로 연결 ) 
       - 수퍼컴퓨터
       - 하둡 클러스터 -> N대의 범용 컴퓨터를 묶은 클러스터(하둡 HDFS와 맵리듀스)
   - 분산병렬처리를 위한 맵리듀스 프레임워크
     - 구글
       - 2003년 GFS : 구글 분산 파일 시스템 아키텍처
       - 2004년 MapReduce : 구글 맵리듀스 아키텍처
     - 하둡
       - 2006년 2월 더그커팅 : 오픈소스로 하둡(HDFS,MapReduce) 공개
       - 2008년 야후 : 900노드에서 1테라바이트 정렬 : 209초(세계최고기록)
       - Hadoop, Pig, Hive, HBase, Mahout, Zookeeper .... Spark : 하둡에코시스템 및 스팍으로 발전
2. Hadoop Ecosystem
   - 하둡의 3가지 주요 기능
     - < 분산파일시스템 + 분산병렬처리시스템 >
     - MapReduce
     - HDFS
     - YARN
   - 하둡 에코시스템
#### 하둡 분산 파일시스템 -HDFS
1. HDFS의 개요
- 데이터가 단일 물리 머신의 저장 용량을 초과하게 되면 전체 데이터셋을 분리된 여러 머신
에 나눠서 저장할 필요
- 네트워크로 연결된 여러 머신의 스토리지를 관리하는 파일시스템을 분산 파일시스템
- 분산 파일시스템은 네트워크 기반이므로 네트워크 프로그램의 복잡성을 가짐
- 따라서 일반적인 디스크 파일시스템보다 훨씬 더 복잡
- 최고의 난제 중 하나는 특정 노드에 장애가 발생해도 자료가 유실되지 않는 강건한 파일
시스템을 만드는 것
- 하둡은 HDFS라는 분산 파일시스템을 제공
- HDFS는 Hadoop Distributed FileSystem(하둡 분산 파일시스템)의 약어
- 하둡은 범용 파일시스템을 추구하기 때문에 추상화의 개념을 가지고 있음
- 하둡이 로컬 파일시스템이나 아마존의 S3와 같은 다른 스토리지 시스템을 통합하는 방식

2. HDSF의 개념과 설계
- HDFS 설계
  - 매우 큰 파일
    - ‘매우 큰’의 의미는 수백 메가바이트, 기가바이트 또는 테라바이트 크기의 파일을 의미.
    - 최근에는 페타바이트 크기의 데이터를 저장하는 하둡 클러스터
  - 스트리밍 방식의 데이터 접근
    - HDFS는 ‘가장 효율적인 데이터 처리 패턴은 한 번 쓰고 여러 번 읽는 것’이라는 아이디어
    - 데이터셋은 생성되거나 원본으로부터 복사
    - 시간이 흐르면서 다양한 분석을 수행
    - 분석이 전부는 아니지만 첫 번째 레코드를 읽는 데 걸리는 지연 시간보다 전체 데이터셋을 모두 읽을 때 걸리는 시간이 더 중요
  - 범용 하드웨어
    - 하둡은 고가의 신뢰도 높은 하드웨어만을 고집하지는 않는다.
    - 하둡은 노드 장애가 발생할 확률이 높은 범용 하드웨어(여러 업체에서 제공하는 쉽게 구할 수 있는 하드웨어)로 구성된 대형 클러스터에서 문제없이 실행되도록 설계
    - HDFS는 이러한 장애가 발생하더라도 사용자가 장애가 발생했다는 사실조차 모르게 작업을 수행하도록 설계
- HDFS 설계 – 적합하지 않은 분야
  - 빠른 데이터 응답 시간
    - 데이터 접근에 수십 밀리초 수준의 빠른 응답 시간을 요구하는 애플리케이션은 HDFS와 맞지 않음
    - HDFS 는 높은 데이터 처리량을 제공하기 위해 최적화되어 있고 이를 위해 응답   시간을 희생
    - 빠른 응답 시간을 원한다면 현재로서는 HBase (20장 참조)가 하나의 대안이 될 수 있음
  - 수많은 작은 파일
    - 네임노드는 파일시스템의 메타데이터를 메모리에서 관리하기 때문에 저장할 수 있는 파일 수는 네임노드의 메모리 용량에 좌우
    - 파일, 디렉터리, 블록은 각각 150바이트 정도의 메모리가 필요
    - 따라서 파일 수가 백만 개고 각 파일의 블록이 하나면 적어도 300MB의 메모리가 필요
    - 수백만 개의 파일은 괜찮겠지만 수십억 개의 파일은 하드웨어 용량을 넘어서게 딤
  - 다중 라이터와 파일의 임의 수정
    - HDFS는 단일 라이터로 파일을 씀
    - 한 번 쓰고 끝나거나 파일의 끝에 덧붙이는 것은 가능하지만 파일에서 임의 위치에 있는 내용을 수정하는 것은 허용하지 않으며 다중 라이터도 지원하지 않음(하둡 3.0부터는 다중 라이터를 지원
- HDFS 개념 - 블록
  - 블록
    - 물리적인 디스크는 블록 크기란 개념이 있음
    - 블록 크기는 한 번에 읽고 쓸 수 있는 데이터의 최대량
    - 단일 디스크를 위한 파일시스템은 디스크 블록 크기의 정배수인 파일시스템 블록 단위로 데이터를 다룸
    - 파일시스템 블록의 크기는 보통 수 킬로바이트고, 디스크 블록의 크기는 기본적으로 512바이트
    - 사용자는 파일의 크기와 상관없이 파일을 읽고 쓸 수 있으며, 특정 파일시스템에 구애받지도 않음
    - 파일시스템의 블록 수준에서 파일시스템의 유지관리를 수행하는 df나 fsck와 같은 도구
  - HDFS도 역시 블록의 개념
    - HDFS 블록은 기본적으로 128MB와 같이 굉장히 큰 단위
    - HDFS의 파일은 단일 디스크를 위한 파일시스템처럼 특정 블록 크기의 청크(chunk) 로 쪼개지고 각 청크는 독립적으로 저장
    - 단일 디스크를 위한 파일시스템은 디스크 블록 크기보다 작은 데이터라도 한 블록 전체를 점유하지만, HDFS 파일은 블록 크기보다 작은 데이터일 경우 전체 블록 크기에 해당하는 하위 디스크를 모두 점유하지는 않음
    - 예를 들어 HDFS의 블록 크기가 128MB고 1MB 크기의 파일을 저장한다면 128MB의 디스크를 사용하는 것이 아니라 1MB의 디스크만 사용
- HDFS 개념 – 네임노드와 데이터노드
  - 네임노드와 데이터노드 + HDFS 클라이언트
    - HDFS 클러스터는 마스터-워커 master-worker 패턴으로 동작하는 두 종류의 노드(마스터인 하나의 네임노드namenode 와 워커인 여러 개의 데이터노드 datanode 로 구성)
    - 네임노드는 파일시스템의 네임스페이스를 관리한다. 네임노드는 파일시스템 트리와 그 트리에 포함된 모든 파일과 디렉터리에 대한 메타데이터를 유지
    - 이 정보는 네임스페이스 이미지 namespace image 와 에디트 로그 edit log 라는 두 종류의 파일로 로컬 디스크에 영속적으로 저장
    - 네임노드는 또한 파일에 속한 모든 블록이 어느 데이터노드에 있는지 파악
    - 하지만 블록의 위치 정보는 시스템이 시작할 때 모든 데이터노드로부터 받아서 재구성하기 때문에 디스크에 영속적으로 저장하지는 않음
    - HDFS 클라이언트는 사용자를 대신해서 네임노드와 데이터노드 사이에서 통신하고 파일시스템에 접근
    - HDFS 클라이언트는 POSIX( Portable Operation System Interface )와 유사한 파일시스템 인터페이스를 제공하기 때문에 사용자는 네임노드와 데이터노드에 관련된 함수를 몰라도 코드를 작성
    - 데이터노드는 파일시스템의 실질적인 일꾼이다. 데이터노드는 클라이언트나 네임노드의 요청이 있을 때 블록을 저장하고 탐색하며, 저장하고 있는 블록의 목록을 주기적으로 네임노드에 보고
3. 하둡 분산파일 시스템

**분산처리 시스템에서 고려해야할 점**
1. 장애 대응(System, Network)
2. Interface(System, Network)
3. Management


- 하둡 분산 병령 처리 - MapReduce
  1. Case Study : 하둡으로 데이터 분석하기
     - 맵 단계의 입력은 NCDC의 원본 데이터
     - 먼저 데이터셋의 각 행의 타입을 텍스트로 인식하는 텍스트 입력 포맷을 선택
     - 값은 각 행(문자열)이고, 키는 파일의 시작부에서 각 행이 시작되는 지점까지의 오프셋이다. 여기서 키는 의미가 없으므로 무시
     - 맵 함수는 단순
     - 각 행에서 연도와 기온을 추출
     - 맵 함수는 단지 데이터의 준비 단계로, 연도별 최고 기온을 찾는 리듀스 함수를 위해 데이터를 제공하는 역할을 맡음
     - 또한 잘못된 레코드를 걸러주는 작업은 맵 함수에서 수행하는 것이 적합하며, 여기서는 기온 필드의 값이 누락되거나 이상하거나 문제가 있는 레코드를 제거하는 작업을 수행
     - 각 행은 키-값 쌍으로 변환되어 맵 함수의 입력이 된다.
     - 맨 앞의 키는 각 행의 파일 오프셋으로, 맵 함수는 그냥 무시한다. 맵 함수는 연도와 기온(굵은 문자로 표시)을 추출하여 출력으로 방출한다(기온은 정수형으로 변환된다).
     -  각 행맵 함수의 출력이 리듀스 함수의 입력으로 보내지는 과정은 맵리듀스 프레임워크에의해 처리 된다. 이 과정에서 키-값 쌍은 키를 기준으로 정렬되고 그룹화
       - 여기서 맵 함수의 키는 연도고 값은 기온
       - 따라서 리듀스 함수는 다음과 같은 입력을 받게 됨
          - (1949, [111, 78]) 
          - (1950, [0, 22, -11])
   - 연도별로 측정된 모든 기온값이 하나의 리스트로 묶인다. 리듀스 함수는 리스트 전체를 반복하여 최고 측정값을 추출한다.
   - 최종 결과로, 연도별 전세계 최고 기온임
  2. 맵리듀스 데이터 흐름
     - 입력 - 맵 - 셔플 - 리듀스 -출력
     - 단일 리듀스 태스크의 맵리듀스 데이터 흐름
       - 입력 - 스플릿 
       - 맵
       - 셔플 - 정렬 및 복사, 병합
       - 리듀스
       - 출력
     - 다수 리듀스 태스크의 맵리듀스 데이터 흐름
       - 위와 동일하지만 리듀스가 여러개
     - 리듀스 태스크가 없는 맵리듀스 데이터 흐름
       - 리듀스 없이 단순하게 맵, 출력
   - 맵 리듀스 잡(Job)
     - Data Work Flow
     - [하둡 MapReduce] Job DAG : 1번째 Job -> 2번째 Job -> ... -> N번째 Job 
     - 맵/ 리듀스의 반복 
   - 맵 리듀스의 원리
     -  입력: 1~10 계산: SUM 출력: 55
     -  map 1에서는 1,2,3
     -  map 2에서는 4,5,6
     -  map 3에서는 7,8,9,10
     -  reduce에서 세 값의 합을 가져옴
     - 맵 리듀스의 3대 원리
       1. Map
          - sort (부분정렬)
          - group (파티셔닝)
          - sub ( 소계)
       2. Suffle
       3. Reduce
          - merge (전체정렬)
          - by (그룹핑)
          - total (총계)
#### H/W와 N/W 구성 및 인프라 설계
- H/W와 N/W
- 고려 사항
  - Machine
  - OS
  - Hadoop Distribution
- 단계별 구성 절차
  - 1단계 : 개발용
    - 마스터 하나, 슬레이브 6개, 네트워크 스위치 하나
    - 하둡을 본격적으로 도입하기 전 최소 구성으로 개발용 클러스터를 제안
  - 2단계 : 운영 초기
    - 마스터 둘, 슬레이브 9, 네트워크 스위치 2
    - 하둡을 이용한 비즈니스를 즉각 도입하려는 고객에게 제안하는 하둡 클러스터.
    - 클러스터의 가용성과 성능을 보장하는 최소 구성이며, 비즈니스 성장과 함께 확장이 용이
  - 3단계 : 확장
    - 마스터 2
    - Cloudere Manager & NFS Server 1
    - Slave Node * Many * (Racks)
    - 10GB Network Switch * 2 * (Racks)
    - 대용량 데이터 저장/분석 및 서비스를 제공하려는 고객에게 제안하는 대규모 하둡 클러스터.
    - 마스터서버와 네트워크의 이중화 / 마스터 HA를 지원하는 구성으로 Scale-Out 모델 제공
  - 네트워크와 확장
### 데이터 분석을 위한 Hadoop Ecosystem
#### 수집/저장/처리 기술 개요
1. 개요
   - 빅데이터 처리 과정
     - 데이터 소스 - 수집- 저장 - 처리 -분석- 표현
   - 빅데이터 처리 과정별 기술
2. 목표시스템 인프라 구성
3. 소프트웨어 구성
#### 빅데이터 수집 기술
- 수집 개요
  - 정형, 반정형, 비정형
  - 로그 수집기, 크롤러, 센서 데이터 수집기, Open API 등 이용
  - 빅데이터 저장소
- 빅데이터의 주요 수집 기술
<table>
    <tr>
        <th>기술</th>
        <th>개발</th>
        <th>최초 공개</th>
        <th>주요 기능 및 특징</th>
    </tr>
    <tr>
        <td>Sqoop</td>
        <td>아파치</td>
        <td>2009년</td>
        <td>RDBMS와 HDFS(NoSQL) 간의 데이터 연동</td>
    </tr>
    <tr>
        <td>Flume</td>
        <td>Cloudera</td>
        <td>2010년</td>
        <td>방대한 양의 이벤트 로그 수집</td>
    </tr>
    <tr>
        <td>Kafka</td>
        <td>Linkedin</td>
        <td>2010년</td>
        <td>분산 시스템에서 메시지 전송 및 수집</td>
    </tr>
</table>

2. SQOOP
- 개요
  - 하둡과 데이터베이스 간 데이터 이동
  - 양방향 : Import & Export
  - 다양한 DB로부터의 자료 이동 지원
- 특징
  - JDBC(JAVA)드라이버를 통한 연동 : RDBMS(MySQL, PostgreSQL, 오라클)와 NoSQL(몽고DB, Redis)과 같은 다양한 데이터베이스 지원
  - 하둡 에코시스템 (Hive, pig, HBase등)와 연계
  - 스쿱 임포트(Import)
    - RDBMS -> HDFS
  - 하이브 임포트(Import)
    - RDBMS -> HDFS -> Hive Table
  - 스쿱 익스포트(Export))
    - HDFS -> RDBMS

3. Flume
- 개요
  - 오픈 소스 로그 수집 소프트웨어
  - 분산 환경에서 대량의 로그 데이터를 효과적으로 수집 후 전송
- 특징
  - 다양한 로그 데이터 수집 및 모니터링이 가능하며 실시간 전송을 지원
  - 자바로 구현되어 있기 때문에 다양한 운영체제에 설치가 가능
  - 장애에 쉽게 대처 가능
- 배경 및 필요성
  - 기존의 다양한 시스템들과 하둡 사이에 연동하는 방법 개선 필요
- 개요
  - 오픈 소스 로그 수집 소프트웨어
  - 분산 환경에서 대량의 로그 데이터를 효과적으로 수집 후 전송
- 특징
  - 다양한 로그 데이터 수집 및 모니터링이 가능하며 실시간 전송을 지원
  - 자바로 구현되어 있기 때문에 다양한 운영체제에 설치가 가능
  - 장애에 쉽게 대처 가능
- 배경 및 필요성
  - 기존의 다양한 시스템들과 하둡 사이에 연동하는 방법 개선 필요
4. Kafka 
- Kafka 개요
  - 개요
    - 확장성이 좋고 처리량이 높은 분산 메시지 시스템
    - 우수한 메시지 전달 성능을 보장
  - 링크드인과 Kafka
    - 링크드인의 실시간 데이터나 오프라인 데이터를 처리하고 수집
    - 높은 처리량을 유지하면서 병렬처리에 초점을 맞춘 구조
    - 다량의 클라이언트 생성이 가능한 유연성을 제공하고 분산처리를 지원
- Kafka 아키텍처
  - Kafka의 구성
    - Producer, Consumer, Broker
  - 역할 및 처리 과정
    - Kafka의 Broker는 Topic을 기준으로 메시지를 관리
    - Producer는 특정 Topic의 메시지를 생성한 뒤 해당 메시지를 Broker에 전달
    - Topic별로 분류하여 쌓아놓으면, 해당 Topic을 구독하는 Consumer들이 메시지를 가져가서 처리
  - 설계 특성
    - 확장성(scale-out)과 고가용성(High Availability)
- 카프카(Kafka)라는 메시징 분산 스트리밍 플랫폼
  - 카프카는 웹사이트, 어플리케이션, 센서 등에 취합한 데이터를 스트림 파이프라인을 통해 실시간으로 관리하고 보내기 위한 분산 스트리밍 플랫폼
  - 데이터를 생성하는 어플리케이션과 데이터를 소비하는 어플리케이션 간의 중재자 역할을 함으로써 데이터의 전송 제어, 처리, 관리 역할을 한다. 카프카 시스템은 여러 요소(노드)와 함께 구성될 수 있어 카프카 클러스터
  - 다른 메시징 시스템과 마찬가지로 어플리케이션과 서버 간의 비동기 데이터 교환을 용이하게 하고, 하루에 수 조개의 이벤트 처리가 가능하게 하는 역할
  - 카프카는 플랫폼에 서비스를 연결하여 다양한 서비스에서 나오는 데이터 흐름을 실시간으로 제어하는 서비스의 중추역할을 하는 플랫폼
- Kafka의 기본구성 요소
  - Cluster : 여러 대의 컴퓨터들이 연결되어 하나의 시스템처럼 동작하는 컴퓨터들의 집합
  - Producer : 데이터를 만들어내어 전달하는 전달자의 역할
  - Consumer : 프로듀서에서 전달한 데이터를 브로커에 요청하여 메시지(데이터)를 소비하는역할
  - Broker : 생산자와 소비자와의 중재자 역할을 하는 역할
  - Topic : 보내는 메시지를 구분하기
 위한 카테고리화
  - Partition : 토픽을 구성하는 데이터 저장소로서 수평확장이 가능한 형태
- Kafka의 특징
  - 카프카에 여러 전달자(Producer)가 동시에 메시지를 전송할 수 있고 반대로, 여러 소비자(Consumer)에서 동시에 메시지를 읽을 수 있음
  - 한 노드가 메시지를 전송하면 전달자(Producer)와 소비자(Consumer)를 중재하는 브로커에서 전달자가 전달한 메시지를 브로커의 동작에 영향을 주지 않고 처리 속도 및 장애 복구를유지할 수 있게 하기 위해 일정 기간 동안 파일 형태로 저장
  - 스템 트래픽이 높아지면 브로커를 추가해서 클러스터를 확장
  - 처리 속도가 저하되면 소비자(Consumer) 또는 생산자 (Producer)를 추가하여 처리량을 늘릴 수 있음
  - 소비자 (Consumer)가 프로듀서의 메시지 생성속도를 따라가지 못할 때 컨슈머를 그룹으로묶어 프로듀서에서 보내는 속도와 읽는 속도의 균형을 맞춤


#### 빅데이터 저장 기술
- 저장 기술
<table>
    <tr>
        <th>구분</th>
        <th>기술</th>
        <th>최초 개발</th>
        <th>주요 기능 및 특징</th>
    </tr>
    <tr>
        <td rowspan=3>분산파일 시스템</td>
        <td>HDFS</td>
        <td>아파치 </td>
        <td>대표적인 오픈소스 분산파일시스템</td>
    </tr>
    <tr>
        <td>Hive</td>
        <td>페이스북</td>
        <td>HDFS기반의 DataWarehouse</td>
    </tr>
    <tr>
        <td>S3</td>
        <td>아마존 </td>
        <td>아마존의 클라우드 기반 분산 스토리지 서비스</td>
    </tr>
    <tr>
        <td rowspan=3>NoSQL</td>
        <td>HBase</td>
        <td>아파치 </td>
        <td>HDFS기반의 NoSQL</td>
    </tr>
    <tr>
        <td>Cassandra</td>
        <td>A. Lakshman</td>
        <td>ACID 속성을 유지한 분산 데이터베이스</td>
    </tr>
     <tr>
        <td>몽고DB </td>
        <td>10gen</td>
        <td>DB의 수평 확장 및 범위 질의 지원, 자체맵리듀스</td>
    </tr>
</table>

#### HDFS

- HDFS 개요
  - 개발 동기
    - 대용량 파일의 스트리밍 읽기와 쓰기에 뛰어난 성능
    - 전통적인 대용량 SAN, NAS 스토리지를 대체
- HDFS 개요 및 특징
  - 분산 파일시스템 : 개별 디스크와 머신이 지원하는 용량의 한계를   뛰어 넘을 수 있음
  - 클러스터의 머신들은 파일시스템을 구성하는 전체 데이터를 나누어 각각 저장
  - 단일 중앙 서버에 저장된 파일시스템 메타데이터는 블록 데이터의 디렉터리 역할
- HDFS 아키텍처
  - 데이터노드
    - 블록은 한 파일의 분리된 바이너리 파일 조각
    - HDFS에서 블록 데이터를 저장하고 추출하는 기능을 담당하는 데몬
  - 네임노드
    - 파일시스템 메타데이터를 저장하고 파일시스템의 전체 이미지를 관리
    - 데이터노드들은 하트비트(heartbeat)에 자신의 상태를 실어서 주기적으로 네임노드에 보낸다.
      - 네임노드는 데이터노드들의 생존 여부와 가용 블록 등 전체적인 상황을 파악 가능
#### Hive
- 개요
  - SQL을 사용, 데이터 요약, 쿼리 및 분석을 수행, 하둡 기반의 데이터웨어하우스 시스템
  - 페이스북 주도로 개발
- 기본적인 작동 원리
  - 사용자가 SQL 쿼리를 작성하면 이것을 자동으로 맵리듀스 작업으로 변경해서 클러스터에서 실행
- 기본 구성과 특징
  - 실행 부분 : 쿼리->맵리듀스 실행
  - 메타데이터 정보 : Mysql과 같은 RDBMS에 저장
- Hive와 RDBMS의 차이점
  - 작은 데이터일 경우 응답 속도가 느리다.
  - 레코드 단위의 Insert, Update, Delete를 지원하지 않는다.
  - 트랜잭션을 지원하지 않는다.
  - 통계정보를 바로 확인할 수 없다. 
  - 입력값 오류도 바로 확인할 수 없다
- 엔터프라이즈 Data Warehouse
- 기존 RDBMS와 Hive의 결합
  - 데이터를 처리하는 새로운 기술적인 방법 제시
- 데이터 모델
  - 테이블
    - 컬럼 타입 ( int, float, string, boolean )
    - 리스트 : map ( JSON과 유사 )
  - 파티션
    - 테이블은 하나 이상의 파티션 키를 가짐
    - 데이터 접근을 위한 테이블 구조의 최적화(인덱스)
      - Ex) 날짜별 파티션 테이블
  - 버킷
    - 파티션의 데이터는 특정 해쉬 함수에 의해서 버킷으로 분할
    - 특정 범위의 해쉬 파티션(샘플링에 이용)
- 메타스토어(Metastore)
  - 데이터베이스
    - 테이블 목록등의 정보를 가진 네임스페이스
  - 테이블 명세를 저장
    - 컬럼 타입, 물리적 레이아웃
  - 파티션 데이터
    - Derby, Mysql 또는 RDBMS에 저장될 수 있음
- 물리적 레이아웃
  - HDFS에 위치한 Warehouse 디렉토리
  - /user/hive/warehouse
- 테이블은 Warehouse의 서브디렉토리에 저장
  - 파티션은 해당 테이블의 서브디렉토리
- 실제 데이터는 일반파일로 저장됨
  - 특정 구분자로 컬럼을 구분하는 텍스트 파일 또는 순차 파일 형태
  - SerDe 형식, 임의 형식 지원
#### NoSQL
RDBMS와 NoSQL
- CAP 이론을 기준으로 한 RDBMS와 NoSQL의 비교
<table>
    <tr>
        <th>구분</th>
        <th>설명</th>
        <th>적용 예</th>
    </tr>
    <tr>
        <td>RDMBS</td>
        <td>일관성(C)과 가용성(A)를 선택</td>
        <td>트랜잭션 ACID의 보장 (금융 서비스)</td>
    </tr>
    <tr>
        <td>NoSQL</td>
        <td>일관성(C)과 가용성(A) 중 하나를 포기하고, 지속성(P)를 보장</td>
        <td>C+P형 : 대용량 분산 파일 시스템(성능 보장) <br>A+P형 : 비동기식 서비스 (아마존, 트위터 등)</td>
    </tr>
</table>
- RDBMS와 NoSQL의 장 ∙ 단점 및 특성 비교
 <table>
    <tr>    
        <th>특성</th>
        <th>내용</th>
    </tr>
    <tr> 
        <td>無 스키마</td>
        <td>데이터를 모델링 하는 고정된 데이터 스키마 없이 키(Key)값을 이용하여 다양한 형태의 데이터 저장 및 접근 가능<br>데이터 저장 방식은 크게 열(Column),값(Value),문서(Documnet),그래프(Graph) 등의 네 가지를 기반으로 구분 </td>
    </tr>
    <tr>
        <td>탄력성</td>
        <td>시스템 일부에 장애가 발생해도 클라이언트가 시스템에 접근 가능<br>응용 시스템의 다운 타임이 없도록 하는 동시에 대용량 데이터의 생성 및 갱신
        <br>질의에 대응할 수 있도록 시스템의 규모와 성능 확정이 용이하며, 입출력의 부하를 분산시키는 데도 용이한 구조</td>
    </tr>
    <tr>
        <td>질의(Query) 기능</td>
        <td>수십 대에서 수천 대 규모로 구성된 시스템에서도 데이터의 특성에 맞게 효율적으로 데이터를 검색 ,처리할 수 있는 질의 언어, 관련 처리 기술, API제공 </td>
    </tr>
    <tr>
        <td>캐싱(Caching)</td>
        <td>대규모 질의에도 고성능 응답 속도를 제공할 수 있는 메모리 기반 캐싱 기술을 적용하는 것이 중요<br>개발 및 운영에도 투명하고 일관되게 적용할 수 있는 구조</td>
    </tr>
</table>

#### 하이브라드 DataWarehouse
- 하이브리드 DW 구성 및 SQL 쿼리 도구
  - HDFS/HBase
    - Hive(MapReduce)
    - 타조, 임팔라(SQL on Hadoop)
  - RDBMS
    - Oracle DW
    - MS MSSQL
  - MPP
    - Oracle ExaData
    - EMC GreenPlum
  - Raw Data 
    - HDFS에 저장
  - Summary Data
    - Hive, RDBMS, MPP에 통합 저장
  - Batch Processing 
    - MapReduce/Hive SQL
  - Report 
    - RDBMS Query
  - Ad-hoc Query
    - 엑사데이터(제조), 그린플럼(포털)

### 빅 데이터 처리 기술
#### 분산 병렬처리 기술
- 하둡 맵리듀스
  - 분산 병렬 데이터 처리 기술의 표준, 일반 범용 서버로 구성된 군집화 시스템을 기반으로 <키,값> 입력 데이터분할 처리 및 처리 결과 통합 기술, job 스케줄링 기술, 작업 분배 기술, 태스크 재수행 기술이 통합된 분산 컴퓨팅 기술
  - 맵리듀스, Pig, Hive
- SQL on Hadoop
  - 배치처리 중심의 맵리듀스의 한계를 넘기 위해 만들어진 SQL 기반의 자체 쿼리 실행엔진이다.
  - Hive on Tez, Impala, Presto, Spark(SparkSQL)
- 맵 리듀스
  - 하둡 맵 리듀스
    - 맵 : 입력(HDFS) -> Emit (Key, Value) 
    - 셔플 : key로 정렬하여 Reduce로 전송
    - 리듀스 : 개별 key로 묶인 Value의 리스트로 연산 수행 -> 결과 저장(HDFS)
- SQL On Hadoop
  - SQL On Hadoop 개요
    - 정의
      - HDFS에 저장된 데이터를 SQL 혹은 SQL과 유사한 형태로 처리를 요청하고 분산 처리하는 시스템
    - 특징
      - 기존 시스템에서 주로 사용한 SQL형식으로 하둡의 데이터를 분산 처리할 수 있다.
    - RDBMS와 SQL on Hadoop의 선택
      - 빠른 처리가 필요한 비정형 쿼리나 OLTP는 RDBMS를 선택
      - 맵리듀스 대신 자체 엔진을 사용한 실시간 쿼리를 최근에 나온 SQL on Hadoop 기술이 지원
 - SQL On Hadoop의 장점
    - 개발 시간의 단축
      - 맵리듀스 보다 쉬움, 프로젝트 수행 인력을 구하기 쉽다.
    - 기존 DW의 SQL과 유사하다.
      - 기존 프로그램의 상당수는 SQL로 되어 있음, 처리로직을 이해하는데 수월
      - 마이그레이션할 때 필요한 자원이 크게 줄어든다.
    - 직관성
      - 직관성이 높고 반복 과정에 수월하다. 단계적 쿼리 분석을 통해 유용한 분석 방법과 결과를 도출한다
  - Hive on Tez
    - 호튼웍스의 스팅거 프로젝트 -> Hive를 발전키고 성능을 강화
    - MapReduce -> 새로운 MapReduce인 Tez를 지원
    - Hive 쿼리 엔진으로 빠른 응답 속도
  - 드릴(Drill)
    - 구글의 Dremel(일명 BigQuery)의 오픈소스 버전
    - 높은 확장성과 하둡/NoSQL과의 쿼리 인터페이스 지원이 특징
  - SparkSQL(SPark)
    - 스파크(Spark)는 인메모리 기반의 초고속 분산병렬처리 프레임워크. 
    - SparkSQL은 Hive에 저장된 데이터에 SQL 질의를 할 수 있는 것이 특징.
    - 초기 버전은 Hive의 소스코드를 일부 변경한 Spark
  - Impala
    - Hive 사용자를 고려한 빠른 SQL 쿼리 엔진.
    - HDFS나 HBase에 저장된 데이터를 대상으로 분석, 문법은 HiveQL과 동일
  - Presto
    - 페이스북에서 개발
    - 빠른 속도의 검색과 집계가 가능
- 실시간 처리 기술
<table>
    <tr>
        <th>CEP</th>
        <th>ESP</th>
    </tr>
    <tr>
        <td>복합 이벤트의 분석을 통해 패턴에서 중요한 정보를 획득<br>수직적 확장<br>다양한 이벤트 분석이 중요</td>
        <td>실시간 이벤트 데이터의 빠른 분석을 통해 실시간 정보 제공<br>수평적 확장<br>실시간 분석이 중요</td>
    </tr>
</table>

<table>
    <tr>
        <th>구분</th>
        <th>세분</th>
        <th>내용</th>
    </tr>
    <tr>
        <th rowspan=2>CEP</th>
        <td>상용 제품</td>
        <td>Oracle CEP,IBM Webshere Business Event</td>
    </tr>
    <tr>
        <td>Esper</td>
        <td>Java와 .NET을 지원하는 CEP와 이벤트 분석</td>
    </tr>
    <tr>
        <th rowspan=2>ESP</th>
        <td>Storm</td>
        <td>분산 실시간 컴퓨팅 시스템</td>
    </tr>
     <tr>
        <td>S4</td>
        <td>실시간 데이터 프로그램 개발을 위한 플랫폼</td>
    </tr>
</table>

#### Spark Streaming
- 스파크 스트리밍
  - 개요 : 실시간 스트리밍 데이터 처리
  - DStream : 시간별(특정 시간 간격)로 도착한 데이터들의 연속적인 모음
  - 데이터 소스 : Flume, Kafka, HDFS 등
- 주요 아키텍처
  - 마이크로 배치(Micro-Batch)
    - 작은 배치 단위들 위에서 연속적인 흐름에 따라 처리한다.
  - 트랜스포메이션
    - 무상태 트랜스포메이션
    - 상태유지 트랜스포메이션
    - 윈도 트랜스포메이션
  - 결과 연산
    - 화면 출력 : Print()
    - 저장 : Save()
## 빠른 데이터 분석을 위한 Spark
### Spark의 이해
#### Spark 개요
- 하둡 MapReduce 보다 발전된 새로운 분산병렬처리 Framework
  - 저장소는 로컬파일시스템, 하둡 HDFS, NoSQL(Hbase, Redis), RDBMS(오라클,MSSQL)
  - Spark는 분산병렬처리 엔진
- 기존 Hive, Pig, Mahout, R, Storm 등을 모두 대체 가능
  - 분산병렬처리 엔진인 Spark Core를 기반으로
  - 다양한 내장 패키지를 지원
- Spark 특징
  - 하둡 에코시스템 발전의 최고봉
    - 구현 원리 및 아키텍처는 Stinger Initiative와 유사
    - 레코드 기반과 컬럼 기반 데이터 저장이 모두 가능
    - YARN, Hive, Sqoop, Kafka 등 다양한 하둡 에코시스템과 통합
- 구성 요소
  - program
  - Spark Client(app master)
    - RDD graph
    - Scheduler
    - Block tracker
    - Shuffle tracker
  - Cluster manager
  - Spark worker
    - Task threads
    - Block manager
- Process & Scheduling
  - RDD Objects
    - built operator DAG
  - DAGScheduler
    - split graph into stages of tasks
    - submit each stage as ready
  - TaskScheduler
    - launch tasks via clustermanager
    - retry failed or straggling tasks
  - Worker
    - execute tasks
    - store and serve blocks
- Data Process Model
  - HDFS MapReduce
    - Slow due to replication, serialization, and disk IO
  - Spark
    - 10~ 100x faster than network and disk
  - 성능 : Logistic Regression
    - 초기 반복에서는 Hadoop이 빠르나 나중으로 갈 수록 반복 속도는 Spark가 빠름
#### Spark 아키텍처와 구현원리
- 함수형 언어 : Scala
  - 분산병렬처리에 최적화된 함수형 언어의 필요성
    - 구글 MapReduce 프레임워크 : C/C++ 언어
    - 하둡 MapReduce 프레임워크 : Java 6 / Java 7
    - 하둡 Tez 프레임워크 : Java 7 / Java 8
    - Spark Core 프레임워크 : Scala / Java 8
  - 함수형 언어
    - 함수형 언어 vs 절차형 언어 또는 명령형 언어
    - 대표적인 함수형 언어로는 SQL
      - MapReduce의 구현 목표는 분산병렬처리가 가능한 데이터 집계 기능(SQL) 
      - HiveQL, SQL on Hadoop(임팔라, 타조, 프레스토 등)
    - Data Work Flow는 DAG(Directed Acyclic Graph, 방향성 비사이클 그래프)
      - Start -> 입력(Input) -> 처리 -> 분기 -> 처리 -> 병합 -> 처리 -> 결과(Output) -> End
    - 입력이 같으면 결과도 같아야 함
    - 단일 머신에서 병렬처리 & 클러스터에서 분산병렬처리가 가능
    - 명령형 언어이면서 함수형 언어의 특징을 가진 대표적인 언어 : R, Java Script, Python
 - 프로그래밍 아키텍처
    - OS : Linux
      - JVM(자바 가상 머신) : 자바 애플리케이션을 실행하기 위한 가상 머신
      - Java 8 / Scala 프로그래밍 언어 : JVM 기반의 애플리케이션 개발 언어
    - 컴파일 vs 스크립트
      - 컴파일 방식 : 컴파일 후 실행파일(JAR)을 각 머신에 배포해야 함( Compile -> Job Submit )
      - 스크립트 방식 : 컴파일 과정 없이 스크립트를 그 때마다 해석하여 JVM에서 바로 실행( Console)
  - 분산병렬처리 : 프로그래밍 실행 구조
    - 하둡 MapReduce : Java/Pig/Hive에서 컴파일 후 JobTracker에 Submit -> 각 머신에서 실행
    - Spark : 각 머신에 실행 코드를 바로 전송 후 실행
- Data Work Flow
  - Job DAG의 이해
    - [하둡 MapReduce] Job : Input -> Map -> Shuffle -> Reduce -> Output
    - Job DAG : 1번째 Job -> 2번째 Job -> ... -> N번째 Job
- 하둡 MapReduce의 단점
  - Disk I/O가 크다.
  - 네트워크 부하가 크다.
  - 전체 Work을 여러 단계의 Job으로 분리하는 것은 굉장히 어렵고 이해하기도 힘들다.
- 대안 => 스파크
  - 입출력 사이의 중간 과정은 Disk대신 메모리에서 처리.
  - 작업은 단일 Job : 대신 여러 단계의 Stage로 구분해서 내부적으로 실행됨. 
  - 배치성 작업뿐만 아니라 대화형 분석이 가능
  - Data Work Flow : RDD(Resilient Distributed Dataset, 탄력적인 분산 데이터셋) Graph로 유지관리.
  - Input, Map, Shuffle, Reduce, Output을 위한 체계적인 Operator 제공.
  - Operator는 Transformation과 Action로 크게 구분.
  - Action 연산시에만 실제 실행 : 지연 실행(Lazy Evaluation)
  - Persist( )를 요청하면 특정 RDD를 인메모리에 상주시킴.
  - 물리적인 파티션을 직접 관리할 수 있음
- Spark RDD와 인메모리 방식
  - RDD 개요
    - Resilient Distributed Dataset : 탄력적인 분산 데이터셋
    - Resilient : 처리과정에서 일부 데이터가 손상되어서 복구가 가능( 부분 손상 -> 부분 복구 )
    - Distributed : 처리과정에서 데이터를 여러 머신에 분산 저장 => 파티션(Partition)
    - RDD Graph : [Input] -> RDD -> RDD -> ... -> RDD -> [Output]
- Spark 연산 및 대화형 분석
  - Transformation과 Action
    - Transformation은 입력 데이터셋을 단계별 RDD로 변형하는 연산자
    - Action은 결과를 콘솔에서 보거나 HDFS등에 저장하는 연산자
    - Action 연산자를 실행하면 입력 소스에서 데이터를 불러와서 처리하고 그 결과를 보여주거나 저장
    - => 즉 Transformation 연산은 실제 실행되지 않고 Action 연산을 요청할 때에만 실행
    - 이런 방식을 Lazy Evaluation(지연 실행)이라고 부름
  - 특징
    - Pig, Hive 등이 제공하는 연산자보다 직관적이고 효율적인 다수의 연산자를 지원함
    - 주의할 점은 Action을 요청할 때마다 데이터를 입력 소스에서 불러와서 처리함
    - => 원하는 RDD에 persist( ) 메소드로 분산캐싱을 명시하는 방법을 제공
    - 대화형으로 동일한 입력 데이터셋을 처리하고 요약(집계)할 때 효율적임
    - Spark 연산자를 이용한 다양한 라이브러리를 제공
  - 효율적인 대화형 분석 절차
  - 분산캐싱(인메모리)
    - 매번 HDFS나 RDBMS에서 데이터를 불러오는 것은 비효율적이고 시간이 오래 걸림
    - 원하는 특정 RDD를 분산캐싱(다수의 머신에 있는 메모리에 데이터를 상주시킴)할 수 있음
    - 캐싱은 메모리(우선)와 Disk 모두 가능.
    - 직렬화(압축, 컬럼기반) 옵션을 지원
    - 성능 고려 사항
      - DISK
      - RAM
        - 빠르지만 저장 용량이 적음
      - SSD
        - DISK보다 빠름
        - RAM보다 용량이 큼
        - Spark 캐싱에 적합

### 분산 코디네이터
- Zookeeper 아키텍처
  - 일반적인 분산 시스템 구조 : Master <-> N대의 Worker(Slave)
    - Leader/Follower 구조
    - 모든 서버에서 Read/Write 가능
    - 리더가 받아서 다른 Follower에 전달
    - 모든 Zookeeper 서버는 데이터의 복제본을 저장
    - 리더는 시작시 리더선출 알고리즘에 의해서 자동 선정(리더 장애시에도)
    - 이벤트는 리더로 전송되고 모든 서버에 저장될 때 결과가 리턴됨
- Client <-> Server Ensemble Session
- Data Model – Znode( Directory + File )
  - 인메모리 데이터베이스
    - 내구성을 위해 변경내역은 로그로 저장
    - 클라이언트는 파일시스템처럼 사용 가능
  - 데이터는 계층화된 패스노드
    - znode
    - 디렉토리/파일 구조 아님 
      - (데이터를 가지는 디렉토리)
    - 데이터는 key-value로 저장
    - 데이터는 최대 1M 제한
  - 임시 노드
    - 세션이 삭제되면 임시노드도 삭제
  - 시퀀스 노드
  - 고속 처리
    - 초당 50,000번 변경
    - 초당 200,000번 읽기
- API
- Watcher
  - Zookeeper는 Watch 라는 개념을 지원
  - 클라이언트는 특정 znode에 Watch를 설정
    - znode에 변경이 발생하면 클라이언트에 통보
    - 통보후에는 Watch는 삭제됨(주의:필요한 경우 재설정)
  - 서버가 변경시 통보하기 때문에 부하가 적음
    - 클라이언트가 서버에 변경이 되었는지 모니터링 하지 않음
  - 장애처리
  1. 연결된 Zookeeper서버 장애
     - 다른 Zookeeper 서버로 대체
  2. 클라이언트와 Zookeeper와의 연결이 단절될 경우?
     - local notification, 클라이언트에서 예외처리
#### NoSQL
### 빅데이터 분석 프로젝트 -실시간 처리
#### ELK Stack
- ELK Stack : 엘라스틱서치(Elasticsearch), 로그스태쉬(Logstash), 키바나
(Kibana)
  - 엘라스틱서치는 색인과 검색 기능을 맡는 실시간 분산 검색 엔진이며, 
  - 로그스태쉬는 각종 로그를 가져와 JSON형태로 만들어 엘라스틱서치로 전송하고, 
  - 키바나는 엘라스틱서치에 저장된 데이터를 대쉬보드 형태로 사용자에게 보여준다
- 데이터 수집 및 전송 : 로그스태쉬
- 데이터 인덱싱 및 저장 : 엘라스틱 서치
- 데이터 검색과 대쉬보드:키바나
### 빅데이터 관리 프로젝트
#### 오케스트레이션
- 데이터 추출 배치 작업과 데이터 분석 파이프라인은 독립적인 여러 단
계로 구성
- 각 단계마다 다른 기술이 사용
- 파이프라인 작업에 대한 오케스트레이션 및 스케줄링과 같은 복잡한 상호 의존 관계를 나타낼 방법이 필요
- Oozie
  - 하둡에서 사용되는 작업 스케줄링 및 실행 프레임워크
  - 우지서버는 하둡 작업을 직접 실행하지 않고, 하둡 클러스터에 맡기는
아키텍처 덕분에 가벼움
  - 백 개의 액션을 동시에 쉽게 실행
  - 작업 정의와 관련된 모든 파일과 라이브러리는 반드시 HDFS에 저장(action, workflow, coordinator details, bundles 등)
  - 프로세스
    - Client: XML 파일로 정의된 작업을 제출. 처리 과정이 플로우 차트와 비슷
    - Workflow Engine: 기본 실행단위인 액션을 구성하고, 연쇄적으로 함께 실행돼야 하
는 액션을 묶어 워크플로우를 구성
    - Scheduler: 구성된 워크플로우는 코디네이터를 통해서 스케줄링. 관련있는 여러 코디네이터를 번들로 그룹지어 정해진 시간에 실행
- Airflow
  - Python 코드로 워크플로우를 작성하고, 스케줄링, 모니터링하는 플랫폼
  - 워크플로우는 DAG(비순환 방향 그래프) 형태로 나타나고, DAG를 통해실행하고 싶은 Task들의 관계와 종속성을 표현
  - DAG를 정확히 설정해야 Task를 원하는 대로 스케줄링하고, 실행
  - 구성요소
    - Scheduler: 실행해야할 Task를 스케줄링하고, Executor로 작업을 제출
    - Executor: Task를 Worker로 푸시하여 작업을 실행
    - Webserver: DAG 및 Task 동작을 트리거/검사/디버그할 수 있는 사용자 인터페이스 웹서버
    - DAG Directory: Scheduler와 Executor가 읽는 DAG 파일의 폴더
    - Metadata DB: Scheduler, Executor, Webserver의 상태를 저장하는 DB

