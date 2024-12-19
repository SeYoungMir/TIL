# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 5. 잠재 디리클레 할당(LDiA)
#### 2. 문자 메시지 말뭉치에 대한 LDiA 주제 모형
- LDiA가 산출한 주제들은 사람이 좀 더 이해하기 쉽고 "설명하기" 쉬움. LDiA는 함께 자주 출현한 단어들을 같은 주제로 묶기 때문. 이는 사람이 단어와 주제의 관계를 생각하는 방식과 비슷. LSA(SVD)가 원래 떨어져 있던 것들을 계속 떨어뜨려 놓는다고 하면 LDiA는 원래 가까이 있던 것들을 계속 가까이 두려 함.
- 두 개가 비슷한 방식이라고 생각할 수 있겠지만 그렇지 않음. 둘에 깔린 수학 공식들은 그 최적화 대상이 다름. 즉 둘은 목적함수(objective function)가 다르며, 따라서 다른 목표에 도달. 고차원 공간에서 가까이 있던 벡터들이 그것을 축소한 저차원 공간에서도 가까이 있게 하기 위해 LDiA는 공간을(따라서 그 안의 벡터들을) 비선형적인 방식으로 비틀고 일그러뜨림. 원래의 공간이 3차원이고 그것을 2차원으로 '투영'하는 경우가 아닌 한, LDiA의 이러한 변환을 시각화하기 어려움.
- 스팸 또는 비스팸 분류명이 붙어있는 몇천개의 문자 메시지들로 이루어진 자료 집합에 LDiA를 적용. 우선 할 일은 문자 메시지(문서)들의 TF-IDF 벡터들을 생성, 그로부터 주제 벡터를 계산하는 것. 여기서는 이전 예제들처럼 문자 메시지의 스팸성을 분류하는 데 사용할 주제를 단 16개로 한정 주제의 수(차원 수)를 낮게 유지한면 과대적합을 줄이는 데 도움
- LDiA는 정규화된 TF-IDF 벡터가 아니라 원본 BOW 빈도 벡터에 대해 작동. 다음은 scikit-learn을 이용해 BOW 벡터들을 손쉽게 구하는 방법을 보여주는 예제 코드
- ```python
  from sklearn.feature_extraction.text import CountVectorizer
  from nltk.tokenize import casual_tokenize
  np.random.seed(42)

  counter = CountVectorizer(tokenizer = casual_tokenize)
  bow_docs = pd.DataFrame(counter.fit_transform(raw_documents=sms.text).toarray(),index =index)
  column_nums, terms = zip(*sorted(zip(counter.vocabulary_.values(),counter.vocabulary_.keys())))
  bow_docs.columns = terms
  ```
- 확인 삼아 첫 문자 메시지('sms0')의 단어 모음 출력.
- ```python
  sms.loc['sms0'].text
  bow_docs.loc['sms0'][bow_docs.loc['sms0']>0].head()
  ```
- 위 단어 모음들에 대해 LDiA를 적용해서 주제 벡터들을 산출
- ```python
  from sklearn.decomposition import LatentDirichletAllocation as LDiA
  ldia = LDia(n_components=16,learning_method='batch')
  ldia = ldia.fit(bow_docs)
  ldia.components_.shape
  ```
- 마지막 출력에서 LDiA는 9,232개의 단어들을 16개의 주제(LDiA의 어법으로는 성분(component))에 할당. 어휘의 처음 몇 단어가 16개의 주제에 어느정도씩이나 할당되었는지 탐색. 예제를 실행했을때 다른 수치가 나올 수 있음