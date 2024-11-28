# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 2. 잠재 의미 분석(LSA)
#### 3. 특잇값 분해
##### 2. 특잇값 행렬 S
- 시그마 행렬이라고 부르는 행렬 $S$는 주제의 '특잇값(singular value)'들로 이루어진 대각행렬. 이 특잇값들은 새 의지(주제) 벡터 공간의 각 차원이 얼마나 많은 정보를 담고 있는지를 말해 줌. 
- 대각 행렬이란 왼쪽에서 오른쪽으로의 대각선에 있는 성분들 이외의 성분들은 모두 0인 행렬. 즉, 이 행렬은 대각선 성분들만 중요, 그래서 NumPy는 $S$를 2차원 자료 구조가 아니라 그냥 하나의 1차원 배열로 저장, 저장 공간을 절약.
- 필요하다면 numpy.diag 함수를 이용, 배열을 원래 형태로 복원 가능. 다음 예제는 이 함수 사용.
- ```python
  s.round(1)
  S=np.zeros((len(U),len(Vt)))
  pd.np.fill_diagonal(S,s)
  pd.DataFrame(S).round(1)
  ```
- 행렬 $U$ 처럼 행렬 $S$도 말뭉치의 여섯 단어와 여섯 주제에 관한 정보를 담고 있음. 기본적으로 행과 열의 수는 둘 다 주제의 수 $p$.
- 예제 코드는 이 행렬에 성분들이 모두 0 인 열벡터를 다섯 개 추가, 열이 총 11개가 되게 했는데, 11은 말뭉치의 문서 수를 의미.
- 이렇게 한 이유는 이 행렬을 다음에 이야기할 오른쪽 특이 벡터 행렬 $V^T$(행의 수가 문서의 수와 같은)와 곱할 수 있게 하기 위한 것. 지금 단계에서 대각행렬 S의 첫 대각성분은 말뭉치에 관한 가장 중요한 정보(통계학에서 말하는 "설명된 분산(explained variance)")를 담고 있으며, 오른쪽 아래 끝으로 갈수록 덜 중요한 정보에 해당. 따라서 오른쪽 아래 끝부터 왼쪽 위 끝으로 올라가면서 대각 성분들을 점차 제거(0으로 설정)함으로써 주제 모형의 차원을 축소 가능. 단 , 주제 모형의 축소때문에 NLP 파이프라인의 전반적인 오차가 의미 있는 수준으로 증가 시 축소를 멈추어야 함.
  - NLP를 비롯한 대부분의 응용에서는 주제 모형의 분산 정보를 유지할 필요가 없음. 이후에 NLP 파이프라인으로 처리할 문서들은 현재의 주제 모형과는 다른 주제들을 담고 있을 가능성이 크기 때문. 따라서 대부분의 경우에는 이 $S$ 행렬의 대각성분들을 모두 1로 설정, 단위 행렬과 유사한 모습으로 변형. 그런 $S$ 행렬은 그냥 문서-문서 행렬 $V^T$를 단어- 주제 행렬 $U$와 곱할 수 있는 형태로 만드는 역할을 함. 이렇게 하면 ,$S$ 행렬을 어떤 새로운 문서 벡터들의 집합과 곱했을 때, 그 벡터들이 원래의 주제 혼합(분포)쪽으로 기울어지는 현상이 발생하지 않음.