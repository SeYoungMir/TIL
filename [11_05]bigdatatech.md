# 1. 빅데이터 이해하기
## 6. 빅데이터 구현 기술
- 적재 기술
  - 수집한 데이터를 분산 스토리지에 영구 또는 임시로 적재하는 기술
  - 빅데이터의 부산 저장소의 4가지 유형
    - 대용량 파일을 영구적으로 저장하기 위한 HDFS(Hadoop Distributed File System)
    - 대규모 메시징 데이터전체를 영구 저장하기 위한 NoSQL(HBase, Mongo DB, Casandra 등)
    - 대규모 메시징 데이터 일부만 임시 저장하기 위한 인메모리 캐시(Redis, Memcached, Infinispan 등)
    - 대규모 메시징 데이터 전체를 버퍼링 처리하기 위한 Message Oreiented Middleware(Kafka,RabbitMQ, ActiveMQ등)
  - 수집된 데이터의 성격에 따른 빅데이터 적재 저장소 차이
    - HDFS : 대용량 파일의 적재
      - 실시간 및 대량으로 발생하는 작은 메시지의 경우 파일 수가 기하급수적으로 늘어나 관리노드와 병렬 처리의 효율성 감소
    - 데이터의 성격에 따라 NoSQL, 인메모리 캐시, MoM 등을 선택적으로 사용할 수 있는 아키텍처링 필요
    - 빅데이터가 적재될 때에는 추가적 전처리 작업 수행 가능, 다음에 있을 탐색/분석 단계를 위해 비정형(음성, 이미지, 텍스트, 동영상 등)데이터를 정형 데이터(스키마가 있는 구조) 로 가공하거나 개인정보로 의심되는 데이터를 비식별하 처리 하는 작업 선행됨
    - 데이터 크기나 비즈니스 요건에 따라 HDFS에 적재 한 후 수행하는 후처리 작업으로도 가능
    <table>
        <tr>
            <th>6V</th>
            <th>적재 기술</th>
            <th>중요성</th>
        </tr>
        <tr>
            <td>Volume</td>
            <td>대용량 데이터(테라바이트 이상) 적재
            <br>대규모 메시지(1,000TPS 이상) 적재</td>
            <td>상</td>
        </tr>
        <tr>
            <td>Variety</td>
            <td>정형/반정형/비정형 데이터 수집
            </td>
            <td>중</td>
        </tr>
        <tr>
            <td>Velocity</td>
            <td>실시간 스트림 데이터  적재</td>
            <td>상</td>
        </tr>
        <tr>
            <td>Veracity</td>
            <td>데이터의 품질과 신뢰성을 확보해 적재</td>
            <td>상</td>
        </tr>
        <tr>
            <td>Visualization</td>
            <td>N/A</td>
            <td>하</td>
        </tr>
        <tr>
            <td>Value</td>
            <td>N/A</td>
            <td>하</td>
        </tr>
    </table>

  - 빅데이터 적재 기술은 6V 관점에서 데이터의 크기, 속도, 진실성을 효과적으로 처리해야 함.
  - 다양성의 경우 원천 데이터를 다양한 형식으로 변환해 적재 가능하지만 데이터의 일관성과 성능 측면에서 트레이드오프가 발생할 수 있어 주의할 필요 있음
  - 시각화 및 가치는 탐색/분석 단계에서 주로 활용되므로 적재 단계에서는 크게 신경쓸 필요 없음.
  - 적재 단계 관련 소프트웨어로는 분산 파일 시스템으로 하둡, NoSQL 저장소로는 Hbase, 분산 캐시 저장소로는 레디스(Redis), 메시징 저장소로는 카프카(Kafka)등이 있음.