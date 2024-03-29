## 3. 적재 파일럿 실행 1단계 - 적재 아키텍처
### 1. 적재 요구사항
- 플럼의 HDFS Sink
  - 플럼에서 가장 중요한 컴포넌트
  - 플럼의 Source에서 읽어들인 데이터를 하둡에 적재, 이 때 플럼의 HDFS Sink 에서 다양한 옵션과 기능들을 사용 가능
  - 기본 기능은 수집한 데이터를 HDFS의 특정 경로에 적재하는 것. 적재할 때 사용될 파일 타입, 파일명, 배치 크기, 생성 파일 크기 등의 정보를 설정. 이 때 사용하는 옵션은 주변 환경과 요구사항에 따라 최적화. 수집되는 데이터 양과주기, 포맷, 향후 분석 형태 등을 고려
- HDFS의 파티션 적재
  - HDFS의 적재 경로를 하이브에서 인지할 수 있는 특정한 구분값(날짜, 시간, 코드 등)으로 파티셔닝함
  - 파티션은 주로 날짜별 디렉터리로 만들어 관리, 업무코드 + 날짜를 조합해서 고유한 파티션 경로를 구성함. 향후 적재한 데이터를 하이브에서 사용하는데, 데이터 조회 시 전체 파일을 스캔하지 않고 파티션 조건에 해당하는 디렉터리만 직접 참조하고 수정할 수 있어 효율성이 좋아짐. 유사한 기능으로 하이브의 버킷이 있음
## 4. 적재 파일럿 실행 2단계 - 적재 환경 구성
- 하둡 설치
## 5. 적재 파일럿 실행 3단계 - 적재 기능 구현
- 하둡 스마트카 상태 정보 로그 파일 적재 기능 구현
- SmartCar 에이전트 수정
## 6. 적재 파일럿 실행 4단계 - 적재 기능 테스트
- 하둡 스마트카 상태 정보로그파일이 정상적으로 적재되었는지 확인, 플럼에 인터셉터 추가, 관련 conf 수정
- 플럼의 사용자 정의 Interceptor 추가
- 플럼의 Conf 파일 수정
- SmartCar 로그 시뮬레이터 작동
- 플럼 이벤트 작동
- HDFS 명령어 확인
