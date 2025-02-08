# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 7. 케라스: 신경망 파이썬 구현
- 케라스 이용, 간단한 XOR 문제를 푸는 신경망 구현
- ```python
  import numpy as np
  from keras.models import Sequential
  from keras.layer import Dense,Activation
  from keras.optimizers as SGD
  #XOR 학습을 위한 입력 견본
  x_train = np.array([[0,0],[0,1],[1,0],[1,1]])
  y_train = np.array([[0],[1],[1],0])
  model = Sequential()
  num_neurons = 10
  model.add(Dense(num_neurons,input_dim=2))
  model.add(Activation('tanh'))
  model.add(Dense(1))
  model.add(Activation('sigmoid'))
  model.summary()
  ```
- model.sumamry()는 각 층의 형태와 가중치 개수(Param #)을 보여줌. 간단히 생각해보면 첫 층은 뉴런이 10개 , 뉴런당 가중치는 세 개(입력의 두 특징에 대한 것 두개와 치우침 가중치 하나).따라서 첫 층이 학습해야 할 가중치는 총 30개, 그 다음 층인 출력 층은 뉴런이 하나뿐. 이 뉴런에 첫 층의 뉴런 10개가 연결. 거기에 치우침 항이 하나 있으므로 가중치는 총 11개
- 여기에 확률적 경사 하강법(SGD)를 적용
- ```python
  sgd=SGD(lr=0.1)
  model.compilte(loss='binary_crossentropy',optimizer=sgd,metrics=['accuracy'])
  ```
  