## 의사결정나무 모델:회귀 나무(Regression Tree)
### Keywords
- 분산감소량
- 정지규칙
- 가지치기
### 의사결정 모델 회귀 나무
- Decision tree 모델(의사결정 나무 모형)
  - 전체데이터 분할을 나무로 표현
- Pruning(가지치기)
- 해석 및 활용
- Decision Tree 모델의 특징
### 회귀 나무
- 회귀 나무(Regression Tree)의 분리규칙 탐색
  - 분산의 감소량
    - 각 그룹(자식 노드)내에서의 목표 변수의 분산이 작을수록, 그룹 내 이질성이 작은 것으로 볼 수 있음.
    - 자식 노드로 분리했을 때, 분산의 감소량이 가장 커지도록 하는 분리규칙을 탐색
  - ANOVA 의 F 통계량
    - F값이 클수록 그룹(자식 노드)간에 평균차이가 있다는 것이므로, 그룹 간 이질성이 큰 것으로 볼 수 있음.
    - F값이 가장 커지게 되는 분리규칙을 탐색
- 정지규칙과 가지치기
  - 의사결정나무의 과적합 방지 방법
    - 지나치게 많은 마디를 가지는 의사결정나무는 새로운 자료에 적용할 때 예측 오차가 매우 커지는 과적합(overfitting)상태가 됨
    - 이를 방지하기 위한 방법으로 정지규칙 또는 가지치기 방법을 사용함.
    - 정지규칙(stopping rule)
      - 다음의 경우에 더 이상 분리하지 않고 나무가 성장을 멈추도록 함.
        - 모든 자료의 목표변수 값이 동일할 때
        - 마디에 속하는 자료의 개수가 일정 수준보다 적을 때
        - 뿌리마디로부터의 깊이가 일정 수준 이상일 때
        - 불순도의 감소량이 지정된 값보다 적을 때
      - 가지치기(pruning)
        - 성장이 끝난 나무의 가지를 제거하여 적당한 크기를 가지도록 함
        - 적당한 크기를 결정하는 방법은 검증용 자료(validation data)에 대한 예측 오류가 가장 작은 나무 모형을 찾는 것이 일반적이며,이 과정은 의사결정나무 모형 알고리즘 내에 자동화 되어있는 경우가 많음.
- 의사결정나무 모형 특징
<table>
    <tr>
        <th>장점</th><th>단점</th>
    </tr>
    <tr>
        <td>이해하기 쉬운 규칙을 생성함:if-then-else방식<br>특성변수 및 목표변수 둘 다 연속형, 범주형 자료 모두 취급함<br>데이터의 전처리가 거의 필요하지 않음<br>이상치에 덜 민감<br>모형에 가정이 필요없는 비모수적 모형</td>
        <td>훈련결과가 불안정함<br>모든 분할은 축에 수직임<br>나무가 깊어질수록 과적합으로 예측력이 저하되며,해석이 어려워짐</td>