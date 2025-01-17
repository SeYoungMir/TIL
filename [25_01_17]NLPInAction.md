# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 3. 치우침 단위
- 다음 그림은 심층 학습에 쓰이는 인공 뉴런의 입$\cdot$출력을 뇌의 생물학적 뉴런이 주고받는 신호에 비유해서 깔끔하게 도식화 한 것. 잠깐 생각해보면 우리는 생물학적 뉴런들을 이용, 자연어 처리에 관한 문서를 읽으면서 심층학습을 학습중.
- ![alt text](image-9.png)
- 퍼셉트론을 수학적으로 다룰 때는 출력을 $f(x)$ 로 표기. 퍼셉트론의 출력은 다음 식의 문턱값 활성화 함수로 정의
- $f(\vec{x})$ 
$
\begin{cases}
    1   \space if  \sum^{n}_{i=0} > threshold  \newline
    0   \space else
\end{cases}
$
- 우리의 퍼셉트론은 아직 아무것도 학습하지 않음. 그렇지만 우리는 이미 뭔가 상당히 중요한 성과를 거둚. 자료를 입력했을 때 그에 대한 출력을 산출하는 하나의 '모형(model)'을 정의했다는 것 자체가 커다란 한 걸음. 아직은 가중치들이 제대로 설정되지 않아서 모형이 틀린(즉, 우리가 원하는 것과는 다른) 출력을 낼 때가 많지만, 가중치들이 제대로 설정되면 상황이 달라질 것. 그리고 가중치들을 제대로 설정하는 과정이 신경망의 학습

##### 파이썬의 뉴런
- 앞에서 설명한 뉴런의 출력을 파이썬으로 계산하는 것은 간단한 일. 그냥 두 벡터의 성분을 각각 곱해서 더하면 됨 .그러나 다음처럼 NumPy의 dot 함수를 이용. 두 벡터의 내적을 구하는 것이 효율적.
- ```python
  import numpy as np

  example_input={1,.2,.1,.05,.2}
  example_weights=[.2,.12,.4,.6,.90]

  input_vector = np.array(example_input)
  weights = np.array(example_weights)
  bias_weight=.2

  activation_level=np.dot(input_vector,weights)+(bias_weight * 1)
  activation_level
  ```
- 이제 문턱값을 적용, 활성화 함수의 결과와 비교하면 뉴런의 최종 출력을 산출 가능. 문턱값은 0.5로 지정
- ```python
  threshold= 0.5
  if activation_level >= threshold:
    perceptron_output=1
  else:
    perceptron_output=0

  perceptron_output
  ```
- 주어진 입력 견본(example_output)과 가중치 집합(example_weight)에 대해 이 퍼셉트론은 1을 출력. 여기서는 가중치들을 미리 고정시켰지만, 신경망 학습에서는 자료 견본과 그에 대한 '정답'의 쌍들로 이루어진 훈련 집합을 ㅗ신경망을 훈련, 가중치들을 동적으로 갱신. 그러한 훈련 과정을 거친 후에는 퍼셉트론에 새로운 입력을 제시, 그 입력에 대한 답을 추측하게 함. 그러한 추측을 예측(predict)라고 부르기도 함.