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