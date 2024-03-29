# 6. 빅데이터 탐색
## 4. 탐색 파일럿 실행 2단계 - 탐색 환경 구성
- 4개의 소프트웨어 (하이브, 우지, 휴, 스파크) 를 추가 설치함
- 4개의 소프트웨어는 빅데이터의 탐색적 분석을 지원하는 도구로 활용
- *저사양 파일럿 환경: 미사용 수집/적재 서비스를 일지 중지
  - 플럼 서비스
  - 카프카 서비스
  - 스톰 서비스
  - 레디스 서비스
1. 하이브 설치.
2. 우지 설치
3. 휴 설치
4. 스파크 설치
5. 탐색 환경의 구성 및 설치 완료.
## 5. 탐색 파일럿 실행 3단계 - 휴를 이용한 데이터 탐색
- 휴에 접속해 로그인 한 후 휴의 편리한 기능들을 이용해스마트카 데이터를 탐색
1. HDFS에 적재된 데이터 확인
   - 휴의 파일 브라우저 기능을 이용해 HDFS에 적재된 스마트카의 상태 정보 뎅터 확인
   - CLI로 HDFS 명령을 실행할 필요 없이 기본적인 HDFS의 명령들을 웹 UI에서 마우스 클릭만으로 실행 가능
2. HBase에 적재된 데이터 확인
   - 휴의 Data Browsers 기능을 이용해 HBase에 적재된 스마트카 운전자의 운행 정보 확인
3. 하이브를 이용한 External 데이터 탐색
   - HDFS 파일 브라우저로 탐색한 위치는 플럼에서 수집한 데이터를 1차로 적재한 곳, 하이브 External 영역에 해당함.하이브 QL을 이용해 이곳의 데이터를 탐색하기 위해서는 적재된 데이터를 하이브의 테이블 구조와 매핑시킨 메타 정보가 필요함. 
* 하이브의 특징
  * 하이브는 하둡에 적재되어 있는 파일의 메타 정보(파일의 위치, 이름, 포맷 등)를 테이블의 스키마 정보와 함께 메타스토어에 등록, 하이브 쿼리를 수행할때 메타스토어의 정보를 참조, 마치 RDBMS에서 데이터를 조회 및 탐색하는 것 같은 기능을 제공
  * 하이브 쿼리는 RDBMS 쿼리와 외형만 유사할 뿐 내부 메커니즘은 전혀 다름
  * 하이브 QL의 5가지 주요 특징
    1. 하이브 쿼리는 맵리듀스로 변환되어 실행
       - 일부 하이브 쿼리를 제외한 대부분의 하이브 쿼리는 맵 리듀스로 변환되어 하둡의 잡에서 실행 및 관리됨. 하나의 하이브 쿼리는 복잡도에 따라 여러 개의 잡이 순차적으로 만들어지고, 다시 잡 안에서는 데이터의 크기와 조건절에 따라 여러 개의 맵과 리듀스 작업이 생성되어 실행됨
    2. 대화형 온라인 쿼리 사용에 부적합
       - 하이브 쿼리는 맵 리듀스로 변환되어 실행되기 까지는 최소 10~30초 이상의 준비 시간이 필요, 처리량이 높은 대규모 배치 작업에 최적화
       - 극단적인 예는 RDBMS에서 0.5초면 수행되는 가벼운 쿼리를 하이브에서 실행하면 50여초 이상 걸릴 수 있음. 하지만 RDBMS에서 50여분 수행되는 무거운 쿼리를 하이브에서 실행하면 단 50여초만에 수행이 완료될 수 있음
    3. 데이터의 부분적인 수정(Update/Delete) 불가
       - 데이터의 부분적인 수정 불가는 HDFS의 특징, HDFS를 기반으로 작동하는 하이브는 그 특징을 그대로 계승
       - 하이브 테이블에서는 부분 수정 및 삭제 처리를 할 수 없고 전체 데이터를 덮어쓰기 해야 함.
       - 이러한 문제로 하이브로 처리할 데이터를 적재할 때는 특정 파티션 단위로 적재해 필요 시 해당 파티션만 덮어쓴느 방식의 데티어 설계.
       - 하이브 0.14부터는 INSERT,UPDATE,DELETE,MERGE문을 ORC Stored 형식에서 부분적으로 지원
    4. 대규모 병렬분산 처리가 불가능한 경우
       - 하이브는 처리량이 높은 대규모 병렬 분산 처리에 최적화, 일부 요건에 따라 대규모 분산 처리가 어려울 수 있음
       - 예를 들어 RDBMS에서 주로 사용되는 전체 정렬을 단순 하이브 QL로 실행하면 하나의 리듀스만 실행되어 급격한 성능 저하 발생, 또한 대규모 조인이나 그루핑이 발생하면 분산된 노드들끼리 대량의 데이터를 주고받으면서 네트워크 레이턴시가 높아져 응답 속도가 크게 떨어짐. 대용량 하이브 QL을 수행할 때는 데이터의 분산과 로컬리티를 반드시 고려한 쿼리 플랜 수립 필요
    5. 트랜잭션 관리 기능이 없어 롤백 처리 불가
        - 하나의 하이브 쿼리는 여러 개의 잡과 맵리듀스 프로그램으로 실행, 로컬 디스크에 중간 파일들을 만드렁냄
        - 이 때 특정 맵리듀스 작업 하나가 실패하면 이미 성공한 잡들이 롤백 처리되지 않음. 단지 실패한 잡을 재실행하기 위해 노력할 뿐
        - 이러한 기본 원칙으로 인해 하이브에서는 트랜잭션 관리 기능이 존재하지 않음. 하이브 0.14부터는 ACID를 부분적으로 지원하고 있으나 제약사항이 많아 자주 사용되지는 않음
 - 하이브가 SQL과 유사한 인터페이스를 제공하기 시작하면서 하둡 에코시스템들이 급성장하게 됨, 빅데이터 벤더들은 하이브의 단점을 극복한 소프트웨어들을 만들기 시작함. 관련 제품으로 임팔라, 테즈(Tez), 스파크 SQL, 드릴(Drill) 등이 있음. 이 제품들의 공통적인 특징은 인메모리 또는 DAG(Directed Acyclic Graph) 기술로 대용량의 배치 처리에 대해서도 빠른 응답속도를 보장한다는 것.
 - 최근 동향은 해당 제품들이 하이브를 완전히 대체하지는 못하고, 하이브리드 형태로 하이브와 공존 중. 빅데이터의 특성상 장시간에 걸친 배치성 잡에는 하이브 사용, 빠른 의사결정이 필요한 잡에는 임팔라, 테즈 등을 선택적 사용
 - 