# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 5. 잠재 디리클레 할당(LDiA)
#### 4. 주제가 32개인 LDiA
- 주제의 수를 늘려서 더 고차원의 모형을 시험. 앞에서 LDiA가 LSA(PCA)보다 못한 정확도를 낸 것은 아마도 주제가 충분치 않았기 때문일 것. 이번 예제는 단어들을 32개의 주제에 할당(n_components = 32)
- ```python
  ldia32 = LDiA(n_components=32, learning_method='batch')
  ldia32 = ldia32.fit(bow_docs)
  ldia32.components_.shape
  ```
- 다음으로, 말뭉치의 모든 문서(문자메시지)에 대해 새로운 32차원 주제 벡터 생성
- ```python
  ldia32_topic_vectors=ldia.transform(bow_docs)
  columns32 = ['topic{}'.format(i) for i in range(ldia32.n_components)]
  ldia32_topic_vectors = pd.DataFrame(ldia32_topic_vectors,index=index,columns=columns32)
  ldia32_topic_vectors.round(2).head()
  ```
- 이전보다 행렬이 더 희소, 즉, 주제들이 더 깔끔하게 분리
- 마지막으로, 32차원 LDiA 주제 벡터들로 LDA 모형(분류기)을 다시 훈련하고 훈련 집합과 시험 집합에 대한 정확도 측정.
- ```python
  X_train,X_test,Y_train,Y_test = train_test_split(ldia32_topic_vectors,sms.spam,test_size=0.5,random_state=271828)
  lda=LDA(n_components=1)
  lda=lda.fit(X_train,Y_Train)
  sms['ldia32_spam']=lda.predict(ldia32_topic_vectors)
  X_train.shape
  round(float(lda.score(X_train,Y_train)),3)
  round(float(lda.score(X_test,Y_test)),3)
  ```
- 주제(성분) 수를 늘린 것이 동일 선상 문제를 피하기 위한 것은 아님을 주의. 주제 수를 늘리거나 줄여도 동일 선상 문제가 사라지거나 생기는 것이 아님. 동일선상 문제는 바탕 자료 집합 자체에 존재. 동일 선상 관련 경고를 제거하고 싶다면 해당 중복 단어 벡터들을 명시적으로 제거, 또는 합성 단어들을 문자 메시지들에 삽입해서 자료 집합에 '잡음'을 추가해야 함. 말뭉치에 중복 단어 벡터가 존재하거나 특정 단어 쌍들이 자주 함께 등장한다면, 주제 수를 변경하는 것은 동일 선상 문제에 아무런 도움이 되지 않음.
- 주제의 수가 많으면 주제들을 좀 더 정확하게 반영할 수 있음. 그리고 적어도 예제의 자료 집합에 대해서는 주제 수를 늘리면 주제들의 선형 분리가 더 좋아짐. 그러나 분류 정확도는 여전히 PCA+LDA의 96%에 미치지 못함. 이는 PCA가 SMS 주제 벡터들을 좀 더 효율적으로 분산시켰음을, 즉 스팸인 메시지들과 스팸이 아닌 메시지들 사이의 간격이 커서 초평면이 두 부류를 좀 더 잘 가를 수 있었음을 뜻함.
- scikit-learn이나 gensim의 디리클레 할당 모형 구현 코드를 살펴보는 것도 학습에 도움. 두 패키지의 LDiA에 대한 API는 LSA에 대한 API들(sklearn.TruncatedSVD 와 gensim.LsiModel)과 비슷함. 이후에 문서 요약을 이야기할 때 관련 예제를 제시. 설명하기 쉬운 주제들을 산출하는 것이 LDiA의 장점. 이는 문서 요약 같은 응용에 도움이 됨. 그리고 LDiA의 주제 벡터들은 선형 분류에도 그리 나쁘지 않음.
  