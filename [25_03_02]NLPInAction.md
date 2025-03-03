# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 3. gensimn.word2vec 모듈 사용법
- 다양한 기업이 미리 훈련된 단어 벡터 모형을 공개, 유명 NLP 라이브러리들은 그런 미리 훈련된 모형을 효율적으로 활용할 수 있는 API를 다양한 언어로 제공. 구체적인 예제를 체험. 예제들은 인기 있는 gensim 라이브러리를 사용.
- NLPIA 패키지를 이미 설치했다면, 미리 훈련된 word2vec 모형을 다음 두 명령으로 내려받을 수 있음.
  - ```python
    from nlpia.datra.loaders. import get_data
    word_vectors = get_data("word2vec)
    ```
- 직접 해보는 쪽을 선호 시 웹에서 구글이 구글 뉴스 문서들로 미리 훈련한 word2vec 모형을 담은 GoogleNews-vectors-negative300.bin.gz 파일을 낼여받은 후 다음 명령들을 실행해서 직접 적재 가능.
- ```python
  from gensim.models.keyedvectors import KeyedVectors
  word_vectors = KeyedVectors.load_word2vec_format('파일 경로/GoogleNews-vectors-negative300.bin.gz',binary=True)
  ```
- 위 단어 벡터들은 메모리를 대단히 많이 차지. 가용 메모리가 부족하거나 단어 벡터 모형이 적재되길 기다리는 시간이 지루하다면 limit 인수를 지정해서 메모리에 적재될 단어 수를 제한하는 것도 한 방법. 다음은 구글 뉴스 말뭉치에 가장 자주 등장한 단어 20만개만 적재하는 예.
- ```python
  from gensim.models.keyedvectors import KeyedVectors
  word_vectors = KeyedVectors.load_word2vec_format('파일 경로/GoogleNews-vectors-negative300.bin.gz',binary=True, limit=200000)
  ```