# 3. 빅데이터 수집
## 2. 빅데이터 수집에 활용할 기술
### 3. 플럼
1. 플럼 소개
  - 플럼(Flume)은 빅데이터를 수집할 때 다양한 수집 요구사항들을 해결하기 위한 기능으로 구성된 소프트웨어
  - 데이터를 원천으로부터 수집할 때 통신 프로토콜, 메시지 포맷, 발생 주기, 데이터 크기등의 고민이 생김
  - 플럼은 이러한 고민을 쉽게 해결할 수 있는 기능과 아키텍처를 제공함
  - 플럼은 2011년 클라우데라를 통해 처음으로 소개, 이후 아파치 프로젝트에 기증되어 현재는 아파치 최상위 프로젝트로서 전 세계 수많은 엔지니어들이 사용중.
  - 0.9.x 버전은 Flume -OG로 불리고, 1.x 이후 버전부터 Flume- NG(Next Generation) 으로 이름이 교체. 아키텍처가 크게 바뀜.
  - 플럼 기본 요소
    - 공식 홈페이지 
      - http://flume.apache.org
    - 주요 구성 요소
      - Source
        - 다양한 원천 시스템의 데이터를 수집하기 위해 Avro, Thrift, JMS,SpoolDir, Kafka 등 여러 주요 컴포넌트를 제공, 수집한 데이터를 channel로 전달
      - Sink
        - 수집한 데이터를 Channel로부터 전달받아 최종 목적지에 저장하기 위한 기능으로 HDFS,Hive,Logger,Avro,ElasticSearch,Thrift 등을 제공
      - Channel
        - Source와 Sink를 연결, 데이터를 버퍼링하는 컴포넌트. 메모리 ,파일, 데이터베이스를 채널의 저장소로 활용
      - Interceptor
        - Source와 Channel 사이에서 데이터 필터링 및 가공하는 컴포넌트, Timestamp,Host,Regex Filtering 등을 기본 제공, 필요시 사용자 정의 Interceptor를 추가
      - Agent
        - Source ->(Interceptor) -> Channel - >Sink 컴포넌트 순으로 구성된 작업 단위로 독립된 인스턴스로 생성
    - 라이선스
      - Apache 2.0
    - 유사 프로젝트
      - Fluented, Scribe, logstash, Chukwa, NiFi, Embulk 등