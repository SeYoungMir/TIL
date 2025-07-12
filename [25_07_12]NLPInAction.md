# 2. 더 깊은 학습: 신경망 적용
## 7. 단어 순서를 고려한 의미 분석: 합성곱 신경망
### 4. 다시 텍스트로
#### 1. 케라스로 합성곱 신경망 구현: 자료 준비
- ```python
    def collect_expected(dataset):
        """자료 집합에서 목푯값들만 뽑아서 따로 저장"""
        expected = []
        for sample in dataset:
            expected.append(sample[0])
        return expected
    ```
- 이제 앞의 두 함수를 이용, 자료 집합을 토큰화, 벡터화하고 목푯값 목록을 획득
- ```python
  vectorized_data = tokenize_and_vectorize(dataset)
  expected = collect_expected(dataset)
  ```
- 이렇게 해서 기본적인 자료 전처리가 종료. 여기서는 그냥 전처리된 자료 집합의 80%를 훈련용, 20%를 시험용으로 사용. 앞에서 내려받은 자료 집합의 train/ 과 test/ 폴더에 훈련용 자료와 시험용 자료가 각각 들어 있다는 점도 기억. 자료는 많을수록 좋음. 이들을 활용해보는 것도 좋음
- 이 자료 집합뿐만 아니라 공개된 대부분의 자료 집합에서는 자료 집합 관리자가 이런 식으로 훈련용 자료와 시험용 자료를 폴더를 나누어서 담아둔 경우가 많음. 이런 폴더들의 기본적 목적은 해당 자료 집합을 사용한 논문의 결과를 정확히 재현할 수 있게 하는 것.
- 다음 목록은 앞에서 마련한 단어 벡터들과 해당 목푯값들을 훈련 집합과 시험 집합으로 나누는 코드. 훈련 집합은 훈련을 위한 견본들(x_train)과 해당 목푯값들, 즉 '정답'들(y_train)으로 구성되고 시험 집합은 시험을 위한 견본들(x_test)과 해당 목푯값들(y_test)로 구성됨.
- 훈련 과정에서는 x_train의 견본들에 대해 모형이 산출(예측)한 결과와 y_train 의 해당 목푯값을 비교하고 그 오차를 이용해서 모형의 가중치들을 갱신. 시험 과정에서는 x_test의 견본들에 대해 모형이 산출한 결과와 y_test의 해당 목푯값을 비교해서 모형의 정확도를 측정
- ```python
  split_point=int(len(vectorized_data)*.8)
  x_train = vectorized_data[:split_point]
  y_train = expected[:split_point]
  x_test = vectorized_data[split_point:]
  y_test = expected[split_point:]
  ```
