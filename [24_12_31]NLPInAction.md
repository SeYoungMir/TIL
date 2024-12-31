# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 7. 피드백에 기초한 방향 조정
#### 1.선형 판별 분석(LDA)
- 오차가 0이라는 것은 별로 대단한 일은 아님. 이는 단지 이 모형이 자료에 과대적합했다는 의미. 문서가 몇천 개 정도인 말뭉치에 대해 모형이 모든 정답을 '암기'하는 것은 그리 놀라운 일은 아님. 좀 더 의미 있는 정확도를 위해 모형에 교차 검증 수행
- ```python
  from sklearn.model_selection import cross_val_score
  lda=LDA(n_components=1)
  scores = cross_val_score(lda,tfidf_docs,sms.spam,cv=5)
  "Accuracy:{:.2f}(+/-{:.2f})".format(scores.mean(),scores.std()*2)
  ```
- 결과에서 이 모형이 그리 좋은 모형이 아님. 예제는 훈련집합에 대해 모형이 좋은 성과를 낸다고 해서 좋아할 필요가 없음을 보여줌.
- cross_val_score 함수가 반환한 정확도 76%가 진짜로 맞는 수치인지 확인하기 위해 자료 집합의 3분의 1을 시험집합으로 사용, 직접 정확도 측정
- ```python
  from sklearn.model_selection import train_test_split
  X_train,X_test,Y_train,Y_test = train_test_split(tfidf_docs,sms.spam,test_size=0.33,random_state=271828)
  lda=LDA(n_componets=1)
  lda.fit(X_train,Y_train)
  lda.score(X_test,Y_test).round(3)
  ```
- 시험 집합 정홗도가 유사함. 자료 표집(sampling;표본 추출)에 운이 따르지 않은 것으로 보이며, 이 모형은 나쁜, 과적합된 모형이라고 할 수밖에 없음.
- 다음은 LSA를 LDA와 결합하면 모형의 정확도가 올라가는지, 특히 훈련에 사용하지 않은 새로운 문자 메시지를 잘 분리하는지 살펴봄
- ```python
  X_train,X_test,Y_train,Y_test = train_test_split(pca_topicvectors.values,sms.spam,test_size)=0.3,random_state=271828)
  lda=LDA(n_componets=1)
  lda.fit(X_train,Y_train)
  lda.score(X_Test,Y_test).round(3)
  lda=LDA(n_componets=1)
  scores=cross_val_score(lda,pca_topicvectors,sms.apam,cv=10)
  "Accuracy:{:.3f}(+/-{:.3f})".format(scores.mean(),scores.std()*2)
  ```