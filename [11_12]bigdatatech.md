# 2. 빅데이터 파일럿 프로젝트
## 2. 빅데이터 파일럿 아키텍처 이해
### 4. 처리 / 탐색 레이어
- 하둡에 적재된 데이터는 하이브를 이용해 정제/변형/통합/분리/탐색 등의 작업을 수행, 데이터를 정형화된 구조로 정규화해 데이터 마트를 만듦
- 가공/ 분석된 데이터를 외부로 제공하기 위해 스툽을 이용, 필요시 분석/응용 단계에서도 사용함
- 처리/탐색 프로세스를 복잡도를 낮추고 자동화하기 위해 우지의 워크플로로 프로세스를 구성, 데이터의 품질을 높임.
### 5. 분석/응용 레이어
- 처리/ 탐색을 통해 데이터 정규화, 데이터 마트 생성
- 요구사항 1, 2 에 해당하는 스마트카의 상태 점검과 운전자의 운행 패턴을 빠르게 분석하기 위해 임팔라 or 제플린 이용
- 머하웃과 스파크 ML로 스마트카 분석을 위해 군집, 분류/예측, 추천 등을 진행
- R로 통계분석 진행
- 텐서플로로 딥러닝 모델 만들어 플라스크로 서비스 API 제공

* 빅데이터 기술 접근법
  - 플랫폼 전문가 : 하둡 에코시스템 설치 및 구성
  - 수집/적재 전문가: 대규모 데이터 연동 및 통합
  - 처리/ 탐색 전문가: 데이터 모델 설계 및 처리
  - 분석/ 응용 전문가 : 도메인 분석 및 인사이트 도출
  - 4개의 전문가 영역의 공통적 특징 : 하둡 에코시스템에 대한 기본 아키텍처와 핵심 기술 반드시 이해
* 빅데이터 과학자
  * 데이터 과학자는 통계 , 수학, 엔지니어링, 프로그래밍, 리더십, 커뮤니케이션 등 모든 경험과 지식을 갖춰야하므로, 만능 데이터 과학자를 찾기 보다는 분야별 전문가가 협업하면서 각자의 역할과 서로의 업무 영업을 이해하는 것이 아직은 최선.
### 6. 하드웨어 아키텍처
- 빅데이터의 하드웨어 아키텍처는 3V(Volume, Vairety, Velocity) 관점에서 구성함. 이 때 서버 네트워크, 디스크, 랙 등을 3V 관점에서 면밀히 검토해서 설계하고 규모를 산정해야함
- 프로젝트 초기 3V를 고려한 대규모 하드웨어를 구성해 기존 인프라에 배치해야하므로 보안, 성능, 처리량, 확장성, 안정성등을 다각적으로 검토해야함.
<table>
    <tr>
        <th>3V</th>
        <th>하드웨어 아키텍처 수립</th>
    </tr>
    <tr>
        <td>Volume(크기)</td>
        <td>얼마나 많은 데이터가 발생하는가?</td>
    </tr>
    <tr>
        <td>Velocity(속도)</td>
        <td>얼마나 자주 데이터가 발생하는가?</td>
    </tr>
    <tr>
        <td>Variety(다양성)</td>
        <td>얼마나 다양한 데이터가 발생하는가?</td>
    </tr>
</table>

- 파일럿 프로젝트의 하드웨어 아키텍처가 위의 표의 빅데이터 3V 요건을 모두 만족할 수 없음.
- 파일럿 프로젝트에서는 빅데이터의 성능 및 확장성 테스트를 위한 벤치마킹 불가능, 대신 다양한 기술과 기능들을 응용해보고, 향후 대규모 빅데이터 환경에서도 빠르게 적응할 수 있도록 함.
- 메모리에 대한 리소스 사용률이 높으므로, 파일럿 프로젝트를 수행할 때는 불필요한 프로그램을 중지해 여유 메모리를 확보해야함.
- 고사양 아키텍처를 기준으로 서버는 다음과 같음
- 데스크톱 PC
  - OS
  - 오라클 버추얼 박스
    - 리눅스 가상 서버 1
      - Hadoop Management Nodes
      - Hadoop Data Nodes
      - HBase Management
      - PostgreSQL
    - 리눅스 가상 서버 2
      - Hadoop DataNode
      - HBase Region
      - 우지
      - 플럼
      - 레디스
      - 하이브/스파크
      - 스톰
      - 휴
      - 제플린
      - 카프카
      - 주키퍼
    - 리눅스 가상 서버 3
      - Hadoop DataNode
      - HBase Region
      - Cloudera Management
      - 임팔라
      - 스쿱