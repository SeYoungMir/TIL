# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 5. word2vec 대 Glove
- word2vec이 NLP에 혁신을 가져오긴 했지만, 반드시 역전파를 이용해서 훈련해야하는 신경망에 의존한다는 한꼐가 있음. 일반적으로 역전파는 경사 하강법을 이용해서 비용함수를 직접 최적화하는 것보다 덜 효율적.
- 제프리 패닝턴이 이끄는 스탠퍼드 대학교의 NLP 역구팀은 word2vec이 효과적인 이유를 파악, word2vec의 훈련에서 최적화되는 비용함수가 어떤 것인지 밝히는 연구를 시작. 그들은 단어 공동 출현 횟수를 계산,정방행렬 형태로 기록, 그 행렬에 SVD(특잇값 분해)를 적용, word2vec으로 산출한 것과 동일한 두 개의 가중치 행렬 획득. 여기서 핵심은 공동 출현 행렬(co-occurence matrix)을 동일한 방식으로 정규화. 그러나 어떤 경우에는 word2vec 모형이 스탠퍼드 연구팀이 SVD 접근 방식으로 도달한 전역 최적해로 수렴하지 못하는 경우도 존재. 연구팀은 이러한 직접적인 최적화 방법에 GloVe라는 이름을 붙임. 이 이름은 이 기법이 말뭉치 전체('전역')에 대한 단어 공동 출현 빈도의 전역 벡터(global vector)들을 최적화한다는 점에서 비롯
- GloVe는 word2vec의 은닉 가중치 행렬과 출력 가중치 행렬에 해당하는 행렬들을 훨씬 짧은 시간으로 산출 가능. 즉 GloVe는 word2vec만큼이나 정확한 언어 모형을 좀 더 빠르게 산출 가능.
- GloVe는 텍스트 자료를 좀 더 효율적으로 활용함으로써 처리 속도를 높임. 그리고 GloVe는 더 작은 말뭉치로 훈련해도 여전히 수렴 가능. 더 나아가서, SVD 알고리즘들은 수십년에 걸쳐 개선되고 조율되었기 때문에, GloVe는 디버깅과 알고리즘 최적화 면에서 한발 앞서있음.
- word2vec의 단어 내장들은 역전파로 갱신한 가중치들로 형성, 신경망 역전파 알고리즘들은 GloVe가 사용하는 SVD 같은 좀 더 성숙한 최적화 알고리즘들보다 덜 효율적.
- 단어 벡터를 이용한 의미 추론이라는 개념을 대중화한 것은 word2vec이지만, 지금 단어 벡터 모형을 훈련 시 word2vec보다는 GloVe를 사용하는 것이 좀 더 바람직. word2vec보다는 GloVe가 벡터 표현들의 전역 최적해를 찾아낼 (좀 더 정확한 단어 벡터 모형을 산출할)가능성이 더 큼. GloVe의 장점은 다음과 같음
  - 훈련이 빠름
  - RAM과 CPU 효율성이 좋음(더 큰 말뭉치 처리 가능)
  - 자료를 좀 더 효율적으로 사용(말뭉치가 작을 때 도움이 됨)
  - 같음 훈련 자료로 훈련했을 때 word2vec보다 더 정확한 결과를 제공.