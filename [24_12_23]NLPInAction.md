# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 5. 잠재 디리클레 할당(LDiA)
#### 3.LDiA +LDA = 스팸 분류기
- 예제에서 시험 집합(test set;시험용 자료 집합)에 대해 90% 이상의 정확도를 획득, 자료 집합의 절반만 훈련에 사용.
- 그러나 자료 집합이 크지 않아서 특징들이 동일 선상에 놀여 있다는 경고 발생. 이런 상황은 LDA에게 '과소결정(under-determined)'문제, 즉 미지수가 방정식보다 많은 연립방정식 문제에 해당. train_test_split로 말뭉치를 분할한 탓에 주제-문서 행렬의 행렬식(determinant)이 0에 가까워짐. 필요하다면 LDiA의 n_components(주제 수)를 낮추어서 이 문제를 '해결'할 수도 있지만, 그러면 서로의 일차결합인(동일 선상에 있는)주제들이 하나로 묶이는 경향이 생김.
- LDiA 모형을 TF-IDF 벡터에 기초한 훨씬 고차원의 모형과 비교. TF-IDF 벡터는 훨씬 많은 특징으로 구성, 예제 문자 메시지 말뭉치에서 어휘의 단어(고유 용어)는 3000개 이상.
- 실제 스팸 메시지는 비교적 적으므로 일반화가 나쁘고 과대적합이 발생할 가능성이 큼. 이는 LDiA와 PCA가 도움이 되는 상황.
- ```python
  from sklearn.feature_extraction.text import TfidfVectorizer
  from nltk.tokenize.casual import casual_tokenize
  tfidf = TfidfVectorizer(tokenizer=casual_tokenize)
  tfidf_docs = tfidf.fit_transform(raw_documents=sms.text).toarray()
  tfidf_docs = tfidf_docs - tfidf_docs.mean(axis=0)

  X_train,X_test,Y_train,Y_test = train_test_split(tfidf_docs,sms.spam.values,test_size=0.5,random_state=271828)
  lda=LDA(n_components=1)
  lda=lda.fit(X_train,Y_train)
  round(float(lda.score(X_train,Y_train)),3)
  round(float(lda.score(X_test,Y_test)),3)
  ```
- TF-IDF 기반 모형의 훈련 집합 정확도는 100%로 완벽, 그러나 시험 집합 정확도는 저차원 주제 벡터들로 훈련했을때보다 훨씬 못함.
- 스팸 분류기에 중요한 것이 시험 집합 정확도. 이 문제를 해결하기 위한 것이 주제 모형화(잠재 의미 분석)
- 주제 모형화는 작은 훈련 집합으로도 모형을 잘 일반화, 훈련집합과는 다른 단어들이 쓰인(그러나 주제는 비슷한)메시지들도 잘 처리.