## 머신러닝 모델의 검증 및 평가
### Keywords
- 과대적합
- 훈련자료
- 검증자료
- 평가자료
- 교차검증
- 편향
- 분산
### 머신러닝 모델의 분석 절차
- 모델 기반 지도학습 알고리즘의 일반적인 분석 절차
  - 주어진 데이터 전처리 및 탐색
  - 적절한 모델을 선택
  - 주어진 데이터로 모델을 훈련시킴
  - 훈련된 모델을 적용하여 새로운 데이터에 대한 예측을 수행
  - 과대적합(과적합)을 이해하고 잘 컨트롤하는것이 머신러닝의 성공 여부 결정
- 과대적합(overfitting)의 문제
  - 주어진 자료는 거의 완벽한 예측이 가능하지만 미래의 새로운 자료에 대한 예측력이 떨어지는 문제.
  - 복잡한 알고리즘을 사용하여 데이터를 훈련하는 경우, 과대적합 문제를 항상 염두에 두어야 함
### 머신러닝 모델의 검증 및 평가
- 모델의 검증 및 평가 개요
  - 모델 평가의 필요성
    - 과대적합을 막고 일반화 오차를 줄이기 위해서는 새로운 데이터에 얼마나 잘 일반화 될지를 파악해야 함
    - 모델 적합에 사용된 자료를 평가를 위해 재활용하지 않고, 평가만을 위한 데이터를 확보할 필요가 있음.
- 모델 검증 및 평가를 위한 데이터의 구분: Hold-out 방식
  - 주어진 자료를 다음의 세 그룹으로 랜덤하게 분할 한 뒤, 주어진 목적에 따라 각각 모델의 훈련, 검증, 평가에 활용함
  - 1. 훈련 데이터(Training data)
    - 모델의 학습을 위해 사용되는 자료
  - 2. 검증 데이터(Validation data)
    - 훈련 자료로 적합되는 모델을 최적의 성능으로 튜닝하기 위해 사용되는 자료
    - 훈련에 필요한 하이퍼파라미터(hyperparameter)를 조정하거나, 변수 선택(model selecting) 등에 이용.
    - Training data의 일부를 분할해 형성
  - 3. 평가 데이터(Test data)
    -  훈련 및 검증 자료로 적합된 최종 모형이 미래에 주어질새로운 자료에 대하여 얼마나 좋은 성과를 갖는지를 평가하는데 사용되는 자료.
 - 모델 검증 및 평가를 위한 데이터의 구분:K-fold 교차검증(Cross-validation)방식
   - 자료의 수가 충분하지 않은 경우에는 훈련데이터에서 너무 많은 양의 데이터를 검증 또는 평가 데이터에 뺏기지 않도록 교차검정(cross-validation)기법을 사용.
   - 자료를 균등하게 $k$개의 그룹으로 분할 한 뒤 각$j$에 대하여, $j$번째 그룹을 제외한 나머지$k-1$개 그룹의 자료를 이용하여 모델을 적합
   - $j번째 그룹의 자료에 적합된 모델을 적용한 뒤 예측 오차를 구함.
   - $j=1,\cdots,k$에 대하여 위의 과정을 반복한 뒤$k$개의 예측오차의 평균을 구함
   - 예측오차의 평균값을 기준으로 모델의 검증 또는 평가를 수행
### 과대적합
- 과대적합
  - Test Error가 Training Error보다 너무 높은 경우
- 과소적합
  - 모형이 단순해서 fitting이 안 좋은 경우
### 일반화 오차 및 편향-분산 트레이드 오프
- 편향-분산 트레이드 오프(Bias-Variance Trade off)
  - 모델의 복잡한 정도에 따라 훈련 데이터와 평가 데이터의 예측오차는 일반적으로 모델이 복잡해질수록 편향은 낮아지고 분산은 높아지는 경향이 있음
  - 모델이 복잡해지면 과소적합은 떨어지지만 과대적합은 높아지는 경향
  - 모델이 단순해지면 과소적합과 과대적합이 모두 높아지는 경향
  - 모델이 가장 좋을 때는 과대적합이 최소, 과소적합이 낮아지는 형태.
  - 편향은 모델이 변형되었을 때 실제 자료를 얼마나 잘 맞추는 지에 대한 지표
  - 분산은 자료가 바뀌었을 때 모델이 얼마나 바뀌는 지에 대한 지표
  - 일반화 오차는 편향의 제곱과 분산의 합,결과적으로 일반화 오차가 가장 낮은 값이 최적의 모델 복잡도
- 과대 적합을 막기 위한 방법
  - 훈련 데이터를 많이 확보
  - 모델의 복잡도를 낮춤
    - 특성 변수의 수를 줄이거나 차원 축소
    - 파라미터에 규제(regulation)을 적용