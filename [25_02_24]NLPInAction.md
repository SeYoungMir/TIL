# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 2. word2vec의 단어 표현 계산
- 신경망의 벡터 표현 학습 방법
  - word2vec 모형의 훈련에는 2장에서 본 기법들이 사용. 예를 들어 입력 단어 $w_t$는 주어진 문장의 $t$번째 토큰을 표현하는 원핫 벡터.
  - 주어진 목표 단어 앞, 뒤로 두 단어씩을 주변 단어로 사용하는 스킵그램 구간(window)의 크기(반경)은 2. 스킵그램 구간이 2인 경우에는 목표 단어를 포함한 5- 그램으로 문장을 토큰화. 문장의 단어마다 하나의 5-그램이 만들어지므로, 10개의 단어로 이루어진 문장은 10개의 5-그램들로 토큰화.
  - 이러한 입력 단어와 그 주변 단어들로 이루어진 훈련 집합으로 신경망을 훈련. 지금처럼 주변 단어가 네 개인 경우에는 각 주변 단어를 입력 단어에 대한 기대 출력으로 삼아서 훈련 과정을 네 번 반복
  - 입력 단어와 주변 단어들 각각은 제 2장에서 배운 원핫 벡터의 형태로 신경망에 입력. 그에 대한 신경망의 출력(예측 결과) 역시 원핫 벡터. 출력층의 노드들(어휘의 단어당 하나씩)은 소프트맥스 활성화 함수를 이용해서 각 출력 단어가 주어진 입력 단어 주변에 등장할 확률을 계산. 그런 다음 출력층은 주어진 입력 단어 주변에 등장할 확률이 가장 큰 단어에 해당하는 성분만 1이고 나머지 성분들은 0인 하나의 원핫 벡터를 출력. 이러한 출력을 사용하면 손실함수(역전파에 사용할)의 계산이 간단.
  - 주어진 입력에 대해 출력 원핫 벡터와 손실함수를 계산, 그로부터 역전파를 진행. 연결 가중치들을 학습하는 과정이 모두 끝나면 가중치들은 단어의 의미를 반영하게 됨. 애초에 신경망이 주어진 단어 주변에 나타날 확률이 높은 단어들을 잘 예측하도록 훈련되었으므로, 그리고 신경망의 입력과 출력이 원핫 벡터의 형태이므로, 가중치 행렬의 각 행은 어휘의 각 단어 주변에 나타날 가능성이 큰 단어들을 말해 줌. 그리고 주변에 나타나는 단어들이 비슷한 두 단어는 그 의미나 쓰임새도 비슷할 것이라고 가정할 수 있음. 결과적으로 가중치 행렬의 각 행은 각 단어의 의미를 반영.
  - 일단 훈련이 끝나면 신경망의 출력층은(즉, 신경망의 예측 능력 자체는) 별 쓸모가 없음. 우리에게 중요한 것은 입력층과 은닉층을 연결하는 가중치들. 입력 단어를 표현한 원핫 벡터와 이 가중치 행렬을 곱한 것이 바로 단어 벡터 내장(word vector embedding)임.