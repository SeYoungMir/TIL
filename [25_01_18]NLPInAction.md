# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 3. 치우침 단위
##### 퍼셉트론의 훈련
- 우리는 자료에 기초한 예측으로 기본적인 '무대'를 설치. 이 무대에서 벌어지는 주된 공연이 바로 기계 학습. 앞의 예제에서는 그냥 임의로 정한 가중치들로 퍼셉트론의 출력을 계산. 그러나 신경망의 핵심은 그러한 가중치들을 신경망이 스스로 학습하게 하는 것. 이를 위해서는 주어진 견본 예측 결과에 기초, 가중치들을 바람직한 값 쪽으로 "슬쩍 밀어 옮기는" 수단이 필요.
- 퍼셉트론은 주어진 입력에 대한 추측이 맞았는지 틀렸는지(또는 얼마나 틀렸는지)에 대한 함수에 기초해서 가중치들을 증가하거나 감소함으로써 학습. 그런데 학습을 시작하려면 가중치들의 초기값을 정해야 함. 가중치들을 초기화하는 간단한 방법은 그냥 난수를 사용하는 것. 일반적으로는 정규 분포에서 추출한 0에 가까운 난수들로 가중치들을 초기화. 앞에서도 이야기했지만 가중치들이 모두(치우침 가중치 포함) 0이면 출력도 0
- 그러나 가중치들을 0에 가까운 다양한 값들로 초기화하면, 뉴런에 너무 큰 능력을 주는 경로를 만들지 않고도 옳은 족 또는 그른 쪽으로 나아갈 수 있는 발판이 생김.