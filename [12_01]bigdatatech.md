# 5. 빅데이터 적재 II - 실시간 로그/분석 적재
## 2. 빅데이터 실시간 적재에 활용하는 기술
### 2. 레디스
- 레디스 소개
  - 레디스(Redis)는 분산 캐시 시스템이면서 NoSQL 데이터베이스처럼 대규모 데이터 관리 능력도 갖춘 IMDG(In-Memory Data Grid) 소프트웨어
  - 레디스는 키/값 형식의 데이터 구조를 분산 서버 상의 메모리에 저장하면서 고성능의 응답 속도 보장
  - 다양한 데이터 타입을 지원, 데이터를 구조화해서 저장할 수 있어 단순 키/값 이상의 데이터 복잡성도 처리 가능.
  - 인메모리 인메모리 데이터를 영구적으로 저장할 수 있는 스냅샷 기능 제공
  - 데이터 유실에 대비, AOF(Append Only File) 기능으로 정합성 보장
  - NoSQL 데이터베이스의 주요 특징인 데이터의 샤딩(Sharding)과 복제(Replication)도 지원하고 있어 높은 성능이 필요한 서비스에서 많이 사용됨
  - 알려지기 시작한 것은 2009년 초반, 그 후로 많은 기능과 성능 보완, 빠르게 버전업
  - 2023년 12월 기준 안정 버전이 7.2 버전 까지 릴리즈됨
- 레디스의 기본 요소
<table>
    <tr>
        <td>공식 홈페이지</td>
        <td colspan=2>http://redis.io</td>
    </tr>
    <tr>
        <td rowspan=5>주요 구성 요소</td>
        <td>Master</td>
        <td>분산 노드 간의 데이터 복제와 Slave 서버의 관리를 위한 마스터 서버</td>
    </tr>
    <tr>
        <td>Slave</td>
        <td>다수의 Slave 서버는 주로 읽기 요청을 처리하고, Master 서버는 쓰기 요청을 처리</td>
    </tr>
    <tr>
        <td>Sentinel</td>
        <td>레디스 3.x부터 지원하는 기능, Master 서버에 문제가 발생할 경우 새로운 Master를 선출하는 기능</td>
    </tr>
    <tr>
        <td>Replication</td>
        <td>Master 서버에 쓰인 내용을 Slave 서버로 복제해서 동기화 처리</td>
    </tr>
    <tr>
        <td>AOF/Snapshot</td>
        <td>데이터를 영구적으로 저장하는 기능, 명령어를 기록하는 AOF와 스냅샷 이미지 파일 방식을 지원</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=2>BSD</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=2>jBoss Infinispan,MemCached,MamBase</td>
    </tr>
</table>

- 레디스 아키텍처
  - 레디스의 아키텍처는 3.x 부터 HA 기능이 강화. 클러스터의 완성도 높아짐. 요구사항과 데이터의 샤딩 및 복제 구성 방식에 따라 세가지 아키텍처 구성이 가능함
    - Single Master
      -  클라이언트
         -  Write$\dArr$/Read$\uArr$
      -  Master
      - 개발과 테스트 환경에 주로 사용, 설치하기가 쉽고 단일 서버만으로도 빠른 응답 속도와 안정적인 기능 제공. 소규모이면서도 중요도 비교적 낮은 시스템 간의 데이터 공유에 종종 사용
    - Single Master/MultiSlave
      - 클라이언트
        - Write$\dArr$
      - Master
        - Replication
      - Slave 1/2
        - Read$\uArr\uArr$
      - Master인 쓰기 노드와 Slave인 읽기 노드로 분리 구성, Master에 쓰여진 데이터는 복제를 통해 Slave 노드로 복제, 데이터 정합성 유지. Single Master로만 구성된 아키텍처와 비교하였을 때 쓰기/읽기 노드를 분리, 전체적 성능 향상. 읽기 노드를 추가해서 성능 극대화 가능
    - HA Master/MultiSlave
      - 3.x버전부터 지원되는 HA 클러스터링 구조.
      - 앞선 Single Master/MultiSlave의 두가지 문제점
        - 첫번째는 Master 서버 장애 발생 시 쓰기 요청 실패, 데이터 유실이 발생할 수 있는 취약한 구조
        - 두번째는 클라이언트가 쓰기 노드와 읽기 노드를 알고 있어야 하므로 클라이언트 프로그램에 복잡도 발생
      - 문제점 극복 위해 레디스 3.x 부터 Sentinel이라는 노드 모니터링/ 제어 컴포넌트 추가
        - Sentinel이 노드들을 모니터링하고 있다가 Master 노드에 문제가 발생하면 Slave 노드 중 하나를 Master 노드로 지정, 문제가 된 Master 노드와 연결을 끊으면서 HA 기능 제공