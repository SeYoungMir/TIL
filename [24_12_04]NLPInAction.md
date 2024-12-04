# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 4. 주성분 분석(PCA)
#### 2. NLP에서의 PCA
- SVD가 자연어 문서들에는 어떤 효과를 내는가.
- 예제에서는 스팸 또는 비스팸으로 분류된 5,000개의 문자 메시지에 대해 SVD를 적용. 모 대학교의 연구실이 제공한 이 문자 메시지(SMS) 말뭉치는 그 어휘와 주제의 다양성이 비교적 적음.
- 예제는 주제를 16개로 한정, TF-IDF 벡터들에 대해 먼저 scikit-learn의 PCA 모형을 적용, 그런 다음 절단된 SVD 모형을 적용하여 두 방법의 결과에 차이가 있는지 탐색.
- scikit-learn의 절단된 SVD 모형(TruncatedSVD)은 희소 행렬들을 다루도록 설계, 희소 행렬(sparse matrix)이란 대부분의 성분이 같은 값(보통 0 또는 NaN)인 행렬. NLP의 단어 모음 행렬이나 TF-IDF 행렬은 거의 항상 희소 행렬. 대부분의 문서는 어휘의 전체 단어 중 일부만 사용하기 때문. 따라서 대부분의 단어 빈도는 0. (자료를 평활화 하기 위해 '가짜 빈도'를 추가하지 않는 한)
- 희소 행렬은 대부분의 칸이 비어 있고 일부 칸에만 의미 있는 값이 입력된 스프레드 시트와 비슷. scikit-learn의 TruncatedSVD는 메모리 효율성을 위해 의미 없는 칸들을 생략한 자료 구조를 사용, 반면 PCA 모형은 그런 칸들이 실제로 0으로 채워진 밀집 행렬(dense matrix)을 사용. 그래서 PCA 쪽이 계산 속도가 더 빠를 수는 있지만, 대신 메모리를 많이 소비. scikit-learn의 TfidfVectorizer는 희소 행렬을 출력. 그것을 PCA에서 사용하려면 비어 있는 성분들을 모두 채워 조밀한 행렬을 생성해야 함.
- 예제 코드는 NLPIA 패키지의 문자 메시지 자료 집합을 DataFrame으로 적재.
- ```python
  import pandas as pd
  from nlpia.data.loaders import get_data
  pd.options.display.width =120
  sms = get_data('sms-spam')
  index = ['sms{}{}'.format(i,'!'*j) for (i,j) in zip(range(len(sms)),sms.spam)]
  sms.index = index
  sms.head(6)
  ```
- 다음으로 각 메시지의 TF-IDF 벡터를 계산
- ```python
  from sklearn.feature_extraction.text import TfidfVectorizer
  from nltk.tokenize.casual import casual_tokenize

  tfidf = TfidfVectorizer(tokenizer=casual_tokenize)
  tfidf_docs = tfidf.fit_transform(raw_documents=sms.text).toarray()
  len(tfidf.vocabulary_)

  tfidf_docs = pd.DataFrame(tfidf_docs)
  tfidf_docs = tfidf_docs - tfidf_docs.mean()
  tfidf_docs.shape
  sms.spam.sum()
  ```
- 코드의 출력에서 말뭉치의 문자 메시지는 총 4,837개. 토큰화 함수 casual_tokenize는 이로부터 9,232개의 서로 다른 1-그램 토큰을 추출. 4,837개의 메시지 중 스팸은 638개뿐. 이 말뭉치는 햄(보통의 문자 메시지) 대 스팸(광고 혹은 구걸 메시지)의 비율이 8:1인 불균형한 훈련 자료 집합.