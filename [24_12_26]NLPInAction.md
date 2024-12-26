# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 6. 거리와 유사도
- 거리를 측정하는 방법이 많은 것은 거리 측정이 그만큼 중요하기 때문임. 이러한 쌍별 거리(pairwise distance)들은 scikit-learn에도 구현되어 있음. 위상 기하학 같은 특별한 수학 분야나 통계학, 공학에서는 이외에도 다양한 측정 방법을 사용. 참고로 다음은 sklearn.metrics.pairwise 함수가 지원하는 여러 거리 측정 방식
- ```python
  'cityblock','cosine,','euclidean','l1','l2','manhattan','braycurtis','canverra','chebyshev','correlation','dice','hamming','jaccard','kulsinski','mahalanobis','matching','minkowski','rogerstandimoto','russellrao','seuclidean','sokalsneath','sqeuclidean','yule'
  ```
- 거리를 유사도 점수로부터 계산할 때도 많고, 반대로 유사도 점수로부터 거리를 계산할 때도 많음. 일반적으로 거리는 유사도 점수에 반비례. 그리고 유사도 점수는 최소 0, 최대 1의 범위일 때가 많음.다음은 이러한 관계를 만족하는 변환 공식
- ```python
  similarity = 1. /(1.+distance)
  distance = (1./simliarity)-1
  ```
- 유사도 점수 뿐만 아니라 거리도 0과 1 구간일 때는 다음처럼 뺄셈을 이용해서 변환하는 것이 일반적
- ```python
  similarity = 1. - distance
  distance = 1. - similarity
  ```
- 코사인 거리는 범위가 이와는 다름. 두 벡터의 각 거리(angular distance)는 두 벡터의 최대 각도(도 단위로는 180, 라디안 단위로는 $\pi$)를 분모로 하는 분수로 표하는 것이 관례. 그런 경우 코사인 유사도와 코사인 거리는 서로의 역수.
- ```python
  import math
  angular_distance = math.acos(cosine_similarity)/math.pi
  distance = 1. /similarity -1.
  similarity = 1. -distance
  ```
- '거리'와 '길이'를 '거리함수(metric;또는 계량)'과 혼동 다수. 거리와 길이가 실제로 유효하고 유용한 거리함수일 때가 많긴 하지만, 모든 거리 또는 길이가 거리 함수인 것은 아님. 진지한 수학 교과서나 집합론 교과서에서 거리 함수를 '거리 함수(distance function)'나 '거리 측도(distance measure)'라고 부르기도 한다는 점이 혼동 가중.