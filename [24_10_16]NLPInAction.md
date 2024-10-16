# 1.NLP 기초.
## 2. 단어 토큰화
### 3. 감정 분석
#### 2. 단순 베이즈 모형
- ```python
  >>> from sklearn.naive_bayes import MultinomialNB
  >>> nb = MultinomialNB()
  >>> nb = nb.fit(df_bows,movies.sentiment>0)
  >>> movies['predicted_sentiment'] = nb.predict_proba(df_bows)*8 - 4
  >>> movies['error'] = (movies.predicted_sentiment - movies.sentiment).abs()
  >>> movies.error.mean().round(1)
  >>> movies['sentiment_ispositive']=(movies.sentiment>0).astype(int)
  >>> movies['predicted_ispositve']=(movies.predicted_sentiment>0).astype(int)
  >>> movies['''sentiment predicted_sentiment sentiment_ispositive predicted_ispositive'''.split()].head(8)
  >>> (movies.predicted_ispositive == movies.sentiment_ispositive).sum()/len(movies)
  ```
  - 위와 같은 몇줄 안되는 코드와 대량의 자료로 꽤 괜찮은 감정 분석기를 만들 수 있음.
  - VADER 접근 방식이라면 몇천 개의 단어를 선정하고 각각에 감정 점수를 매겨야 했을 것. 그러나 예제에서는 분류명이 붙은 텍스트를 공급하기만 하면 됨.
  - 이것이 기계학습과 NLP의 위력. 이 단순 베이즈 모형이 영화평이 아니라 상품평 같은 완전히 다른 종류의 감정 점수를 예측하게 하면 부정확함.
  - 이런 감정 분석기를 실제로 구축할 때는 용도에 맞게 훈련 자료를 분리하는 것이 중요(시험용 자료 집합을 따로 떼어 놓는 것도 중요.)
  - 앞에서 단순 베이즈 분류기가 영화평을 '추천'혹은 '비추천' 중 하나로 분류하게 했고. 추천/비추천을 그냥 무작위로 선택하게 한다면 평균 절대 오차는 약 4, 단순 베이즈 기반 감정 분석기의 평균 절대 오차는 2.4로 무작위 선택보다 약 두배 정도 나음. 
  - 이 모형을 상품평에 적용하는 예제
  - ```python
    >>> products = get_data('hutto_products')
    ...     bags_of_words=[]
    >>> for text in products.text:
    ...     bags_of_words.append(Counter(casual_tokenize(text)))
    >>> df_product_bows = pd.DataFrame.from_records(bags_of_words)
    >>> df_product_bows = df_product_bows.fillna(0).astype(int)
    >>> df_all_bows = df_bows.append(df_product_bows)
    >>> df_all_bows.columns
    >>> df_product_bows = df_all_bows.iloc[len(movies):][df_bows.columns]
    >>> df_product_bows.shape
    >>> df_bows.shape
    >>> products[ispos] = (products.sentiment>0).astype(int)
    >>> products['predicted_ispositive'] = nb.predict(df_product_bows.values).astype(int)
    >>> products.head()
    >>> (products.pred == products.ispos).sum()/len(products)
    ```
- 최종 결과에서 베이즈 모형은 주어진 상품평이 '추천'에 해당하는지 아닌지를 그리 잘 예측하지 못함. 기대 이하의 성과가 나온 이유 중 하나는 상품평 텍스트에 대해 casual_tokenize 함수를 실행해서 얻은 어휘에 원래의 영화평 어휘에는 없던 토큰이 2546개 존재하기 때문.
- 이는 영화평 어휘의 약 10% 에 해당. 이전 훈련 단순 베이즈 모형에는 새 토큰들에 대한 가중치나 감정 점수가 들어있지 않음. 또한 단순 베이즈 모형은 VADER보다 부정어를 잘 다루지 못함. 부정 표현을 제대로 처리하게 하려면 부정어("not"나 "never")와 그것이 수식하는 단어를 n-그램으로 묶어서 토큰화해야함.
- 이후 내용들에서도 이 기계 학습 모형을 계속 개선, 또한 각 개선 단계에서 VADER와 비교, 모형이 얼마나 나아졌는지 측정.