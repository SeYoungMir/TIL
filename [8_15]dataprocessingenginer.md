## 3. 정적 테스트
1. 프로그램을 실행하지 않고 소스 코드를 대상으로 분석하는 것
2. 워크스루, 인스펙션, 코드 검사 등
   - 워크스루 : SW 개발자의 작업 내역을 전문가들이 검토
   - 인스펙션 : SW 개발 단계에서 산출된 결과물의 품질을 평가
## 4. 동적 테스트
1. 프로그램 실행하여 SW 개발의 모든 단계에서 테스트를 수행하는 것
2. 블랙박스 테스트, 화이트 박스 테스트
* 참고
  * 서비스 제공 소프트웨어의 특성 및 유형
    * 신규 개발 소프트웨어 - 새로운 서비스 제공을 목적으로 개발되며, 일반적으로 초기 개발 단계, 확장 단계 , 기능 고도화 단계 등으로 진행됨
    * 기능 개선 소프트웨어 - 기존 서비스 기능에서 사용자 편의성 개선, 응답 속도 개선, 화면 UI(User Interface)개선, 업무 프로세스 개선 등의 목적으로 개발되는 소프트웨어임
    * 추가 개발 소프트웨어 - 기존 서비스 제공 시스템에 업무 환경의 변화, 산업 환경의 변화, 법/제도의 개정 등으로 인해 새로운 기능을 추가로 개발하는 소프트웨어를 말함.
    * 시스템 통합 소프트웨어 - 각각 별도로 서비스되는 시스템을 원스톱(One-Stop) 서비스 제공을 위해 업무 기능 및 데이터 등을 통합하여 개발하는 소프트웨어임
## 5. 화이트박스 테스트
1. 개요
   1. 원시 코드의 논리적인 모든 경로를 테스트하여 테스트 케이스 설계
   2. 테스트 과정의 초기에 적용
   3. 모듈 안의 작동을 직접 관찰
   4. 모든 문장을 한 번 이상 실행
2. 종류
   1. 기초 경로 검사 : 논리적 복잡성을 측정
   2. 제어 구조 검사
      - 조건 검사 : 프로그램 모듈 내에 있는 논리적 조건을 테스트
      - 루프 검사 : 반복 구조에 초점을 맞춰 실시
      - 데이터 흐름 검사 : 변수 사용의 위치에 초점을 맞춰 실시
3. 검증 기준
   1. 문장 검증 기준 : 모든 구문이 한 번 이상 수행
   2. 분기 검증 기준 : 모든 조건문이 한 번 이상 수행
   3. 조건 검증 기준 : 모든 조건문에 대해 조건이 True/False인 경우가 한 번 이상 수행
   4. 분기/조건 기준 : 각 조건문에 포함된 개별 조건식의 결과가 True/False인 경우가 한 번 이상 수행