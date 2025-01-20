# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 3. 치우침 단위
##### 컴퓨터의 논리 학습
- 앞의 예는 가중치 갱신 방식을 보여주기 위한 것이었을 뿐이고, 해당 수치들에 특별한 의미는 없음. 이번에는 이를 실제 문제에 적용. 간단한 장난감 문제이긴 하지만, 분류명('정답')이 붙은 견본들만으로 컴퓨터에게 어떤 개념을 가르친다는 것이 어떤 것인지 잘 보여줌. 이 예제의 목적은 컴퓨터가 논리합(logical OR)의 개념을 이해하게 만드는 것. 논리합은 주어진 피연산자 중 하나라도 참이면 참이고, 둘 다 거짓일때만 거짓인 연산. 간단한 문제이기 때문에 모든 가능한 입력 견본을 우리가 직접 나열 가능(실제에서는 극히 드문 일). 견본들(sample_data)은 각각 두 개의 피연산자로 구성, 분류명(expected_results)들은 해당 두 연산자들의 논리합 결과
- ```python
  sample_data = [[0,0],[0,1],[1,0],[1,1]]
  expected_results = [0,1,1,1]
  activation_threshold= 0.5
  ```
- 훈련 과정에는 몇 가지 도구가 필요. 우선, 내적은 앞에서처럼 NumPy로 구하면 됨. 그리고 가중치들을 초기화하는 데는 ranmdom 패키지 사용.
- ```python
  from random import random
  import numpy as np
  weights = np.random.random(2)/1000
  weights
  ```
- 또한 치우침 가중치도 설정.
- ```python
  bias_weight =np.random.random()/1000
  bias_weight
  ```
- 일단은 초기 가중치들(난수로 설정한)로 예제의 견본들을 예측
- ```python
  for idx, sample in enumerate(sample_data):
    input_vector = np.array(sample)
    activation_level = np.dot(input_vector,weights+(bias_weight * 1))
    if activation_level > activation_threshold:
        perceptron_output = 1
    else :
        perceptron_output = 0
    print('Predicted {}'.format(perceptron_output))
    print('Expected {}'.format(expected_results[idx]))
    print()
  ```