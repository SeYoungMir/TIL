# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 3. 치우침 단위
##### 컴퓨터의 논리 학습
- 앞의 결과, 무작위 가중치들이 뉴런에 별 도움이 되지 않았음을 추측 가능, 네 가지 추측 중 세 개가 틀리고 하나만 정답. 이 뉴런은 아직 졸업할 때가 되지 않음. 다시 견본들에 대해 그냥 1과 0을 출력하는 대신 예측 결과에 따라 가중치들을 갱신하는 과정을 반복
- ```python
  for iteration_num in range(5):
    correct_answers=0
    for idx,sample in enumerate(sample_data):
        input_vector = np.array(sample)
        weights = np.array(weights)
        activation_level = np.dot(input_vector,weights)+(bias_weight*1)
        if activation_level > activation_threshold:
            perceptron_output=1
        else:
            perceptron_output=0
        new_weights=[]
        for i,x in enumerate(sample):
            new_weights.append(weights[i]+(expected_results[idx]-perceptron_output)*1)
            weights=np.array(new_weights)
        print('{}correct answers out of 4, for iteration {}'.format(correct_answers,iteration_num)
  ```
- 위와 같은 코드를 실행 시 퍼셉트론이 내부 루프에서 가중치들을 갱신하며 퍼셉트론은 자료 집합으로부터 논리합 개념을 학습. 첫 반복에서는 퍼셉트론이 총 네 질문 중 무작위 추측의 하나보다 두개 더 많은 세 개를 맞춤
- 두 번째 반복에서는 정답 수가 감소, 이는 가중치들이 너무 크게 갱신되어서 정답 영역을 벗어난 탓. 다행히 세 번째 방법에서는 다시 정답 영역으로 복귀, 네 번째 반복에서는 두 특징과 결과 사이의 관계(논리합)을 완전히 터득. 각 견본에 대한 오차가 0이므로 갱신과정을 반복해도 가중치들이 더 개선되지는 않음.
- 이것이 앞에서 말한 수렴(convergence)상태. 모형의 오차 함수가 최솟값에 도달하거나 적어도 어떤 고정된 값을 유지할 때 그 모형을 가리켜 "수렴했다" 혹은 "수렴 상태에 도달했다"라고 할 수 있음.
- 그런데 아무리 반복해도 수렴에 도달하지 못할 때도 있음. 예를 들어 신경망이 자료 집합에 존재하는 관계들을 만족하는 최적의 가중치들 주변을 왕복하는 진동 상태에 빠지기도 함.
- 다음에는 신경망이 최적이라고 "생각하는" 가중치들에 목적함수(objective function)혹은 손실함수(loss function)이 어떤 식으로 영향을 미치는지 살핌.