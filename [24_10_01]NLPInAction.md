# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 4. n-그램을 이용한 어휘 확장
- 불용어
  - 문장에 따라 불용어들이 담은 의미의 양이 다를 수 있음. 어떤 문장은 불용어들의 절반을 제거해도 문장 전체의 의미가 크게 달라지지 않음. 예를 들어 관사(정관사, 부정관사)나 전치사가 없어도, 심지어는 be 동사가 없어도 문장을 이해할 수 있을 때가 있음. 수화(수어)로 의사소통을 한다거나, 또는 종이 쪽지에 뭔가를 급하게 메모할 때 항상 생략하는 단어처럼, 흔히 통용되는 불용어가 이 경우에 해당.
  - 그런 "표준적인"불용어들의 상세한 목록은 NLTK에 정의된 목록을 살펴보는 것이 빠르고 효과적.
    - ```python
      >>> import nltk
      >>> nltk.download('stopwords')
      >>> stop_words=nltk.corpus.stopwords.words('english')
      >>>len(stop_words)
      >>>stop_words[:7]
      >>>[sw for sw in stopwords if len(sw) == 1]
      ```
  - 1인칭 문장들이  계속 나오는 문서는 상당히 지루할 수 있음. 그리고 NLP의 관점에서 더욱 중요한 것은 그런 문서는 정보량이 적을 수 있음. NLTK의 불용어 목록은 위의 예에 나온 1인칭 대명사들을 포함한 여러 인칭 대명상화 기타 대명사를 포함. 또한, 예제의 마지막 출력의 NLTK 불용어 목록 중 한 글자 짜리 불용어들은 왜 이런 불용어들이 필요한지 NLTK 토큰 생성기와 포터(porter)어간 추출기를 많이 사용하다 보면 저절로 알게 됨. 
  - 이런 한 글자 토큰들은 NLTK 토큰화 함수와 어간 추출기를 이용해서 축약형 단어를 처리할 때 나타남.
    - scikit-learn이 사용하는 영어 불용어 집합은 NLTK의 것과 상당히 다름. scikit-learn의 불용어는 nltk의 불용어가 153개일 때 기준 318개이며, 같은 코드를 파이썬 3.9와 NLTK 버전 3.2.5로 다시 실행 시 179가 출력. 이는 불용어를 걸러내지 않는 것이 좋을 수 있는 또 다른 이유이며 불용어들을 걸러 내면 같은 결과 재현이 어려울 수있음.
  - 여러개의 불용어 목록을 함께 사용하는 방법도 있음. 자연어 텍스트의 정보를 얼마나 폐기할 것인가에 따라서는 여러 불용어의 합집합을 사용할 수도 있고, 교집합을 사용할 수도 있음.
  - 다음은 scikir-learn(버전 0.19.2)의 불용어들과 NLTK(버전 3.2.5)의 불용어들의 합집합과 교집합
  - ```python
    >>> from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words
    >>> len(sklearn_stop_words)
    >>> len(stop_words)
    >>> len(stop_words.union(sklearn_stop_words))
    >>> len(Stop_words.intersection(sklearn_stop_words))
    ```