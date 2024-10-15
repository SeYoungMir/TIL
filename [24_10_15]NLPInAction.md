# 1.NLP 기초.
## 2. 단어 토큰화
### 3. 감정 분석
#### 2. 단순 베이즈 모형
- VADER의 단점에서 벗어나기 위한 방법으로 기계 학습에 기초한 감정 분석기를 사용하는 방법이있음
- 단순 베이즈 모형은 주어진 문서 집합에서 목표변수(출력 변수)를 예측하는 키워드를 찾으려 함. 
- 감정 분석의 경우 목표(target) 변수는 평가하고자 하는 감정. 즉 감정 분석에서 단순 베이즈 모형은 해당 감정을 예측하는 단어들을 찾음. 단순 베이즈 모형의 내부 계수들에 의해 단어 또는 토큰들이 그에 상응하는 감정 점수들에 대응. 이때 중요한 것은, VADER같은 규칙 기반 감정 분석기와는 달리 사람이 개별 단어들에 대해 일일이 감정 점수를 지정해 둘 필요가 없다는 것.
- 컴퓨터는 미리 만들어진 어휘집에 의존하지 않고 임의의 문제에 대해 "최선의" 감정 점수를 탐색
- 다른 모든 기계 학습 알고리즘처럼, 단순 베이즈가 제대로 자동화하려면 훈련 자료가 필요. 감정 분석의 경우 긍정적 감정 내용에 대한 분류명이 붙은 대량의 텍스트 문서를 구해야 함.
- 후토와 동료들이 VADER를 구축할 때 만든 네 종류의 감정 자료 집합을 사용하면 되며, 이 자료 집합들은 NLPIA에 포함. 다음은 이를 활용하는 예
- ```python
  >>> from nlpia.data.loaders import get_data
  >>> movies = get_data('hutto_movies')
  >>> movies.head().round(2)
  >>> movies.describe().round(2)
  ```
- 다음으로, 모든 영화평 텍스트를 토큰화해서 각각에 대해 단어 모음 생성, 이전에 했던 것처럼 Pandas 의 DataFrame에 모든 단어 모음 벡터를 넣음.
  ```python
  >>> import pandas as pd
  >>> pd.set_option('display.width',75)
  >>> from nltk.tokenize import casual_tokenize
  >>> bags_of_words = []
  >>> from collections import Counter
  >>> for text in movies.text:
  ...   bags_of_words.append(Counter(casual_tokenize(text)))
  >>> df_bows = pd.DataFrame.from_records(bags_of_words)
  >>> df_bows = df_bows.fillna(0).astype(int)
  >>> df_bows.shape
  >>> df_bows.head()
  ```
- 위 코드로 단순 베이즈 모형이 자연어 텍스트에 담긴 감정을 예측(추론)하는 데 필요한 모든 자료를 구축, 감정 분석을 진행.