# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 4. 주성분 분석(PCA)
#### 3. PCA를 이용한 문자 메시지 잠재 분석.
- scikit-learn의 PCA 모형을 문자 메시지들에 적용. 앞에서 3차원 말 자료점들을 2차원 평면에 투영하기 위해 PCA 모형 사용.
- 이번에는 9,232차원의 TF-IDF 벡터들을 16차원의 주제 벡터들로 줄이는 데 PCA 모형 사용
- ```python
  from sklearn.decomposition import PCA
  pca = PCA(n_components=16)
  pca = pca.fit(tfidf_docs)
  pca_topic_vectors = pca.transfrom(tfidf_docs)
  colums = ['topic{}'.format(i) for in range(pca.n_componets)]
  pca_topic_vectors = pd.DataFrame(pca_topic_vectors,columns=columns, index=index)
  pca_topic_vectorss.round(3).head(6)
  ```
- 출력에 나온 주제들이 무엇을 말하는지는 각 주제에 각 단어가 어느정도로 "담겨 있는지"를 보면, 즉 그 주제에 대한 각 단어의 가중치를 보면 짐작 가능. 예를 들면 어떤 주제에 "half"와 "off"의 가중치가 높다면 그 주제는 "half off" 같은 문구가 많이 나오는 메시지들을 요약하는 것이므로 '할인(discount)' 주제라고 부르면 됨.
  - 적합된(fitted)scikit-learn 변환의 가중치들은 해당 객체의 components_ 속성으로 확인 가능.
- PCA 변환의 모든 차원에 단어들을 배정. TfidfVectorizer는 어휘를 각 단어가 색인 번호(열 번호)에 대응되는 사전 자료 구조의 형태로 저장, 먼저 단어들을 적절한 순서로 정렬할 필요가 있음.
- ```python
  tfidf.vocabulary_
  column_nums,terms = zip(*sorted(zip(tfidf.vocabulary_.values(),tfidf.vocabulary_.keys())))
  terms
  ```
- 다음으로 이 열 번호들과 단어 및 그 빈도들, 그리고 주제들로 Pandas의 DataFrame 객체를 만들고 , 각 주제의 각 단어 점수(가중치)를 보기 좋은 표 형태로 표시
- ```python
  weights = pd.DataFrame(pca.components_,columns=terms,index=['topic{}'.format(i) for i in  range(16)])
  pd.options.display.max_columns=8
  weights.head(4).round(3)
  ```
- 주제(행)에는 그냥 번호만 붙어 있음. 각 주제가 실제로 무엇에 관한 것인지 알려면 단어들의 가중치를 살펴 봐야함. 예제의 목표는 스팸을 걸러내는 것이므로 , 스팸에 관련된 주제들에 집중.