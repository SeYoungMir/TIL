# 7. 빅데이터 분석
## 7. 분석 파일럿 실행 5단계 - 머하웃과 스파크 ML을 이용한 머신러닝
### 2. 스파크 ML 분류 - 스마트카 상태정보 예측/분류
- 데이터 마이닝의 분류에 사용될 데이터셋은 스마트카 상태 정보, 하이브의 Manage 영역에 테이블로 데이터 적재
- 스마트카의 주요 장치(타이어, 라이트, 엔진, 브레이크 등)에 대한 상태를 기록한 값으로, 차량의 상태를 진단하기 위한 중요한 변수
- 이 값들을 이용해 차량의 정상/비정상을 분류하는 모델 생성, 분류 모델을 운행 중인 스마트카에 적용, 차량의 안전 상태를 실시간으로 점검하는 머신 러닝 분석이 목표
- 분류 모델 사용 알고리즘은 나이브 베이지안, 랜덤 포레스트, 로지스틱 회귀 등 존재, 프로젝트에서는 랜덤 포레스트 사용
  - 랜덤 포레스트란, 학습을 통해 각각의 특징을 가지는 여러 개의 의사결정 트리를 앙상블로 구성하는 알고리즘, 단일의사결정 트리와 달리 모델의 오버피팅을 최소화하면서 일반화 성능을 향상시킨 머신러닝 기법
  - 최종 분류값은 평균이나 과반수 투표 방식 등을 이용
- 분류기의 학습은 과거 수 개월의 스마트카 운행 데이터를 스파크 머신러닝 분류기에 입력, 분류기를 훈련(학습)시킴.
- 학습이 끝나면 스마트카의 상태를 판단할 수 있는 Classify(or Model) 프로그램이 생성, 이 프로그램 안에는 과거의 데이터로부터 학습해 찾아낸 분류 패턴들이 로직화
- 이 Classify 프로그램을 운행 중인 스마트카 시스템에 적용, 발생하는 데이터를 Classify 프로그램이 분석, 과거의 이상 패턴과 유사한 데이터가 발생하는지 실시간 분류 및 예측
- 데이터에 대한 이해와 전처리 능력만 있으면 머신러닝(딥러닝) 프레임워크를 이용해 AI 프로그램을 어렵지 않게 구현 가능
- 알고리즘 자체보다 모델 학습에 필요한 데이터의 확보와 전처리가 성능에 절대적인 영향을 끼치므로 더 중요
### 3. 머하웃과 스파크 ML을 이용한 군집 - 스마트카 고객 정보 분석
- 데이터 마이닝 중 3번째인 군집 분석 진행
- 사용될 데이터셋은 "스마트카고객 마스터정보"
- 하이브의 External 영역의 테이블에 2600여명 적재
- 데이터셋에는 스마트카의 차량 번호, 차량 용량, 차량 모델 정보와 스마트카 사용자의성별, 나이, 결혼, 직업, 거주지역 정보존재.
- 군집분석은 이러한 속성 정보를 벡터화, 유사도 및 거리 계산, 데이터의 새로운 군집을 발견하는 마이닝 기법
- 군집분석은 RDBMS로는 분석이 어려울만큼 대규모, 사람이 직관적으로 파악하기 어려운 데이터셋을 초기 분석하는 데 자주 사용
- 군집분석도 다양한 알고리즘을 선택적 적용 가능. Canopy,K-Means, Pusszy K-Means 등을 데이터의 특성에 맞게 적용
- 파일럿 프로젝트에서는 머하웃을 이용한 Canopy 분석, 대략적인 군집 개수 파악, 스파크 ML의 K-Means를 이용해 군집 분석 진행
- K-Means의 분석 결과로는 N개의 군집별로 스마트카 차량 정보 리스트 확인, 군집된 차량들 사이에 어떠한 공통적인 특징이 있는지 분석.