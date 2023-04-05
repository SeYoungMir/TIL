## 특성 공학: 개요, 특성 선택(Feature Selection) 방법론
### Keywords
- 특성선택
- 특성 추출
- Filter 방식
- Wrapper 방식
### 특성 공학
- 특성 공학
  - 머신 러닝 알고리즘에 사용되는 입력데이터에 해당하는 특성변수들에 대한 처리
  - 데이터의 양과 질에 따라 머신러닝의 성능이 달라짐
  - 사전 변수 선별
    - 사전에 알기가 힘듦
- 특성 선택
  - 전체 특성변수 중 최적의 조합을 선택하는 문제
- 특성 추출 
  - 특성변수들을 적절하게 조합하여 새로운 특성변수를 만드는 문제
### 특성 공학 2
- 특성 공간 차원 축소의 필요성
  - 모델의 해석력 향상.
  - 모델 훈련시간의 단축
  - 차원의 저주 방지
  - 과적합(overfitting)에 의한 일반화 오차를 줄여 성능 향상
- 특성공학의 방법론은 크게 특성 선택(feature selection)방법과 특성 추출(feature extraction)방법으로 구분할 수 있음.
### 특성 선택(feature selection)방법론
- 특성 선택(feature selection)
  - 주어진 특성 변수들 가운데 가장 좋은 특성변수의 조합만 선택함
  - 불필요한 특성 변수를 제거함
  - Filtering ,Wrapper,Embedded 방식으로 분류할 수 있음
    - Filtering - ranking을 매긴 후 높은 것 일부 선택
    - Wrapper - 일부 set을 후보, model에 적합(fitting),결과 평가 반복하며 optimal한 조합 선택
    - embedded - 모델이 자체적으로 해석, 모델에 넣어서 변수선택.
  - Filter 방식:각 특성변수를 독립적인 평가함수로 평가
    - 각 특성변수 $X_i$와 목표변수($Y$)와의 연관성을 측정한 뒤, 목표변수를 잘 설명할 수 있는 특성 변수만을 선택하는 방식.
    - $X_i$와 $Y$의 1:1 관계로만 연관성을 판단.
    - 연관성 파악을 위해 t-test,chi-square test,information gain 등의 지표가 활용됨
  - Wrapper 방식: 학습 알고리즘을 이용
    - 다양한 특성변수의 조합에 대해 목표변수를 예측하기 위한 알고리즘을 훈련하고, cross-validation 등의 방법으로 훈련된 모델의 예측력을 평가함. 그 결과를 비교하여 최적화된 특성변수의 조합을 찾는 방법
    - 특성변수의 조합이 바뀔 때 마다 모델을 학습함.
    - 특성변수에 중복된 정보가 많은 경우, 이를 효과적으로 제거함
    - 대표적인 방법으로는 순차탐색법인 forward selection, backward selection, stepwise selection 등이 있음
  - Filter 와 Wrapper의 장단점 비교
<table>
    <tr><th><br></th><th>장점</th><th>단점</th></tr>
    <tr><th>Filter</th><td>계산 비용이 적고 속도가 빠름</td><td>특성 변수간의 상호작용을 고려하지 않음</td></tr>
    <tr><th>Wrapper</th><td>특성변수 간의 상호작용을 고려함 <br> 주어진 학습 알고리즘에 대해 항상 최적의 특성변수 조합을 찾음</td><td>모델을 학습해야 하므로, 계산 비용이 크고 속도가 느림<br>과적합(overfitting)의 가능성있음.</td></tr>
</table>

  - Embedded 방식: 학습 알고리즘 자체에 feature selection을 포함하는 경우
    - Wrapper 방식은 모든 특성변수 조합에 대한 학습을 마친 결과를 비교하는 데 비해, Embedded 방식은 학습 과정에서 최적화된 변수를 선택한다는 점에서 차이가 있음.
    - 대표적인 방법으로는 특성변수에 규제를 가하는 방식인 Ridge,Lasso,Elastic net등이 있음.
