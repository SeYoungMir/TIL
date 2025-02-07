# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 6. 흔들어서 탈출
- 주어진 훈련 견본의 오차를 취합, 그 오차(비용)곡면을 따라 내려가서 최적의 가중치들을 찾는다는 개념은 충분히 이해. 다수의 훈련 견본에 대해 오차를 측정해서 가중치들을 갱신하는 방식을 배치 훈련 방식이라고 부름. 배치(일괄 단위,batch)는 한 번의 훈련 주기에 사용하는 자료점(견본)들의 집합으로, 많은 경우 전체 훈련 자료의 한 부분집합.
- 하나의 배치에 대한 오차 곡면은 일정, 배치가 달라지면 오차 곡면도 달라짐. 무작위로 초기화한 가중치들은 그 오차 곡면의 한 지점을 정의. 그 지점에서 기울기를 따라 아래쪽으로 하강 시 극소점에 해당하는 구덩이에 빠질 수 있음. 그러면 진정한 최소점을 구할 수 없고. 이런 함정을 벗어나는 방법은 크게 두 가지.
- 하나는 확률적 경사 하강법(stochastic gradient descent, SGD)를 사용하는 것. 확률적 경사 하강법에서는 모든 훈련 견본을 처리한 후 기울기들을 갱신하는 대신 각각의 훈련 견본에 대해 가중치들을 갱신. 또한 훈련 견본들의 순서를 매번 무작위로('확률적으로')뒤섞음. 매번 입력과 그 정답이 달라지므로 오차 곡면은 매번 달라지나, 그 곡면을 따라 내려가면서 가중치들을 갱신하는 건 원래의 경사 하강법과 동일. 그러나 확률적 경사 하강법은 주어진 견본 하나에 대해 그런 갱신을 수행. 즉, 한 훈련 주기의 끝에서 모든 오차를 취합한 후 일괄적으로 가중치들을 갱신하는 것이 아니라, 개별 견본의 출력과오차를 구할때마다 가중치들을 갱신을 수행함.
- 견본들을 거치면서 이런 과정이 반복되면 가중치들이 다양한 극소점과 곡면상의 굴곡을 지나 진짜 최소점을 향해 나아가게 됨. 만일 모형이 제대로 조율되지 않았거나 훈련 자료가 일괄적이지 않으면 확률적 경사 하강법을 적용해도 모형이 수렴하지 못하고 같은 곳을 계속 맴돌게 됨. 그러면 모형은 아무것도 배우지 못함. 그러나 실제 응용에서 확률적 경사 하강법은 대부분의 경우 극소점들을 극복하는데 상당히 효과적임이 판명.
- 이 접근 방식의 한 가지 단점은 느리다는 것. 모든 훈련 견본을 순전파로 처리 후, 역전파를 한 번 수행하는 것도 느린 과정임을 생각하면, 견본마다 순전파와 역전파를 반복하는 것이 얼마나 느린지를 짐작 가능.