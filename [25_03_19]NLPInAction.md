# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 8. 단어 관계의 시각화.
- ```python
    import numpy as np
    np.linalg.norm(wv['Illinois']-wv['Illini'])
    cos_similarlity = np. dot(wv['Illinois'],wv['Illini'])/np.linalg.norm(wv['Illinois'])*np.linalg.norm(wv['Illini'])
    cos_similarity
    1-cos_similarity
  ```
- 위 수치들은 두 단어의 의미가 그냥 적당히 가까운 정도임을 말해 줌.
- 그럼 미국의 주들과 도시들에 대한 word2vec 단어 벡터들을 모두 뽑고 그 거리들을 이용해서 2차원 의미 지도를 생성. 그러려면 KeyedVectors 객체에 담긴 word2vec 모형의 어휘에서 주 이름과 도시 이름을 뽑아낼 수 있어야함.