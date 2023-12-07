# 5. 빅데이터 적재 II - 실시간 로그/분석 적재
## 2. 빅데이터 실시간 적재에 활용하는 기술
### 4. 에스퍼 - 이어서
- 에스퍼 아키텍처
  - 에스퍼는 CEP(Complex Event Processing) 엔진임
  - 엔진은 단순 자바 라이브러리 프로그램으로 설치와 사용은 매우 간단함
  - 그로 인해 애플리케이션 서버(톰캣, 제이보스, OSGI, 스톰 등) 또는 애플리케이션의 컨텍스트에 에스퍼 라이브러리를 설치하고, 해당 라이브러리를 이용해 CEP 프로그래밍을 하는 단순한 아키텍처를 가지고 있음
    - 에스퍼 아키텍처 1
      - 애플리케이션
      - 자바 환경
      - 애플리케이션 서버
        - Input Adapter
        - 에스퍼 엔진
          - Event Processing Language
          - Core Library
        - Output Adapter
      - 데이터베이스
      - 애플리케이션
      - Alert
      - 대시보드
  - 에스퍼의 EPL(Event Processing Language)을 이용해 대규모 분산 아키텍처를 구성할 때는 룰을 통합 관리하고, 분산 노드에 일관되게 적용하기 위해 다소 복잡한  구성이 필요
  - 이 때 분산된 응용 서버에 에스퍼 엔진을 설치하고 에스퍼 엔진들이 동일한 EPL 룰을 동적으로 일괄 로딩하기 위해 EPL 공유 저장소가 이용됨
    - 에스퍼 아키텍처 2
      - 관리자
        - EPL 등록
      - EPL(Event Processing Language) 공유 저장소
        - EPL 동적 로딩
      - 분산 응용 서버 * n
        - Input Adapter
        - 에스퍼 엔진
          - Event Processing Language
          - Core Library
        - Output Adapter
- 에스퍼 활용 방안
  - 파일럿 프로젝트에서는 운전자의 운행 데이터를 실시간으로 분석하기 위해 에스퍼 EPL을 활용함
  - EPL은 30초동안의 평균 시속을 체크해서 80km/h를 초과하는 운전자 이벤트 정보를 실시간으로 감지할 수 있도록 룰을 정의함. 해당 이벤트 데이터는 감지 즉시 레디스에 적재되어 과속한 차량 정보만 관리할 수 있게 됨
  - 운전자 운행 로그 400KB/1초
  - 플럼
  - 카프카
  - 스톰
    - Spout
    - Bolt
      - 에스퍼 엔진
        - Event Processing Language
        - Core Library
      - 운전자 운행로그 필터링
      - 과속 운행정보 이벤트 감지
    - Bolt 1
    - Bolt 2
      - 레디스