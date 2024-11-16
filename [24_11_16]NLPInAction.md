# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 1. 단어 빈도에서 주제 점수로
#### 5. LDA 분류기
- 다음은 문자 메시지들을 스팸 또는 비스팸으로 분류하는 LDA 모형을 '훈련'하는 코드
- ```python
  import pandas as pd
  from nlpia.data.loaders import get_data
  pd.options.display.width=120
  sms = get_data('sms-spam')
  index = ['sms{}{}'.format(i,'!'*j) for (i,j) in zip(range(len(sms)),sms.spam)]
  sms = pd.DataFrame(sms.values,columns=sms.columns, index = index) 
  sms['spam'] = sms.spam.astype(int)
  len(sms)
  sms.span.sum()
  sms.head(6)
  ```
- 출력에서는 훈련 자료 집합의 문자 메시지는 총 4,837개, 스팸은 638개.
- 위 문자 메시지들을 토큰화, TF-IDF 벡터로 변환
- ```python
  from sklearn.feature_extraction.text import TfidfVectorizer
  from nltk.tokenize.casual import casual_tokenize
  tfidf_model = TfidfVectorizer(tokenizer = casual_tokenize)
  tfidf_docs= tfidf_model.fit_transform(raw_documents=sms.text).toarray()
  tfidf_docs.shape
  sms.spam.sum()
  ```
- nltk.casual_tokenize의 토큰화 함수로 토큰화한 결과, 어휘의 단어 수는 9,232개. 이는 전체 문자 메시지 수의 약 두 배, 스팸 메시지 수의 약 15배.
- 이는  이 단어들 자체에는 주어진 메시지가 스팸인지 아닌지에 관한 정보가 그리 많이 들어 있지 않다는 뜻. 일반적으로 단순 베이즈 분류기는 자료 집합의 분류명 붙은 견본 수보다 어휘의 단어 수가 훨씬 크면 잘 작동하지 않음. 그런 경우에는 의미 분석 기법들이 유용.
- LDA로 스팸 메시지들을 분류. sklearn.discriminant_analysis.LinearDiscriminantAnalysis의 LDA 모형을 사용할 수도 있지만. 예제에서는 이진 분류의 무게중심들만 계산하면 모형의 '훈련'이 가능. 