# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 3. gensimn.word2vec 모듈 사용법
- 어휘가 작으면 단어 벡터 모형의 위력도 그만큼 줄어든다는 점에 주의. 해당 단어 벡터가 존재하지 않는 단어들을 포함한 문서에 대해서는 NLP 파이프라인이 좋은 성과를 내지 못함. 따라서 단어 벡터 모형의 크기는 개발 도중에만 제한하는 것이 바람직. 직접 예제를 실행해서 본문의 결과와 동일한 결과를 얻으려면 미리 훈련된 word2vec 모형 전체를 적재해야함에 주의.
- gensim.KeyedVectors.most_similar() 메서드는 주어진 단어 벡터와 가장 가까운 단어 벡터를 효율적으로 찾아줌. 키워드 인수 positive에 단어들의 목록을 지정하면 이 메서드는 해당 단어 벡터들을 더한 것에 해당하는 단어 벡터들을 검색. 따라서 도입부의 비유 질문의 답을 구할 수 있음. 단어 벡터를 빼려면 negative 인수를 사용. topn 인수는 메서드가 돌려줄 결과의 개수를 지정.
- 전통적인 유의어 사전들과는 달리 word2vec의 유의어 관계는 두 단어의 거리를 뜻하는 하나의 연속값(실수) 점수로 정의. word2vec 자체가 하나의 연속 벡터 공간 모형이기 때문.
- word2vec의 단어 벡터는 고차원이고 각 성분이 연속값이기 때문에 주어진 단어의 의미를 완전한 범위에서 포착 가능. 단어 벡터로 비유 질문은 물론, 액어법(한 단어가 한 문장의 여러 위치에서 서로 다른 의미로 쓰이는 것)까지도 처리할 수 있는 것은 이 때문.
- ```python
  word_vectors.most_similar(positive=['cooking','potatoes', topn=5)
  word_vectors.most_similar(positive=['germany','france', topn=1)
  ```
- 한편, gensim 라이브러리는 무관한 단어들을 찾는 수단도 제공. doesnt_match()메서드가 그것.
- ```python
  word_vectors.doesnt_match("potatoes milk cate computer".split())
  ```
- 위 메서드는 주어진 단어들에서 다른것들과의 거리가 가장 먼 단어 하나를 선택해서 반환.