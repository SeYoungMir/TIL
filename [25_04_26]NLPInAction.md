# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 10.doc2vec을 이용한 문서 유사도 추정
- word2vec의 개념을 단어가 아니라 문구나 문장, 문서 전체로 확장 가능. 즉, 기존 단어들에 근거해서 다음 단어를 예측함으로써 단어벡터들을 학습한다는 착안을 문장이나 문단, 문서 벡터의 학습으로 확장할 수 있음. 이 경우에는 예측 시 이전 단어들뿐만 아니라 문장과 문단을 나타내는 벡터도 고려. 그런 벡터들은 예측을 위한 추가 입력으로 간주. 그런 식으로 훈련을 진행하면 모형은 말뭉치로부터 문서나 문다느이 표현을 학습.
- doc2vec도 점진적 학습이 가능. 즉, 훈련을 마친 모형에 새로운 문서들을 입력, 새로운 문서 벡터들을 생성할 수 있음. 추론 단계(inference stage)에서 알고리즘은 동결된 단어 벡터 행력과 해당 가중치들로 새 문서 벡터들을 계산, 문서 행렬에 추가.
- 이런 식으로 추론한 문서 벡터는 해당 문서의 의미를 반영. 이런 문서 벡터들을 예를 들어 말뭉치에서 의미가 비슷한 문서들을 찾는 등의 다양한 용도로 활용 가능.