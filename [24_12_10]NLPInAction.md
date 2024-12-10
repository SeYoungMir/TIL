# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 4. 주성분 분석(PCA)
#### 4. 절단된 SVD를 이용한 문자 메시지 잠재 의미 분석
- scikit-learn의 TruncatedSVD 모형을 시험. 이것이 LSA에 대한 좀 더 직접적인 접근 방식
- 모형에서는 scikit-learn PCA 모형이 숨겻던 세부 사항을 어느 정도 직접 살펴볼 수 있음. 이 모형은 희소 행렬을 ㅈ다루므로, 자료 집합의 덩치가 큰 경우에는 TruncatedSVD 대신 PCA를 사용하는 것이 처리 속도 면에서 유리. TruncatedSVD의 'SVD'부분은 TF-IDF 행렬을 세 개의 행렬로 분할. 그리고 TruncatedSVD의 'Truncated' 부분은 TF-IDF 행렬에 대한 정보가 적은 차원들을 폐기.
- 폐기된('절단된') 차원들은 말뭉치의 문서들 전체에서 그 분산이 작은'주제(단어 빈도들의 일차 결합)'에 해당. 이런 폐기된 차원들은 말뭉치의 전반적인 의미에 별로 기여하지 않는 주제들. 이런 주제들은 모든 문서에서 고르게 쓰이는 불용어나 기타 단어들을 많이 담고 있음.
- 예제에서는 TruncatedSVD를 이용, 단어들을 16개의 가장 흥미로운 주제들, 즉 TF-IDF 벡터들의 분산이 가장 큰 단어 조합들에 해당하는 16개의 주제로 축약.
- ```python
  from sklearn.decomposition import TruncatedSVD
  svd = TruncatedSVD(n_components = 16, n_iter=100)
  svd_topic_vectors = svd.fit_transform(tfidf_docs.values)
  svd_topic_vectors = pd.DataFrame(svd_topic_vectors,columns=columns,index=index)
  svd_topic_vectors.round(3).head(6)
  ```
- TruncatedSVD가 산출한 주제 벡터들이 PCA 모형이 산출한 것들과 정확히 일치함.
- 이는 반복 횟수(n_iter)를 기본보다 훨씬 크게 잡았고 각 단어(열)의 TF-IDF 빈도들을 0에 대해 중심화한(각 빈도에서 평균을 빼서)덕분임.