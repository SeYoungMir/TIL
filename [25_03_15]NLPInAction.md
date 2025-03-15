# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 8. 단어 관계의 시각화.
- 유의어나 반의어 같은 단어들 사이의 관계는 NLP의 강력한 수단. 그리고 이런 관계들을 시각화하면 흥미로운 점 발견 가능. 단어 벡터를 2차원으로 시각화 시도
- 구글 TensorBoaRD의 단어 내장 시각화 기능을 사용할 수도 있음.
- 시각화 예제는 우선 구글 뉴스 말뭉치 word2vec 모형을 사용. 이 말뭉치에는 미국의 여러 주 (state)이름과 도시 이름이 나옴 NLPIA 패키지에는 구글 뉴스 word2vec 모형의 단어 벡터들을 손쉽게 적재하는 기능 포함. 이를 사용.
- ```python
  import os
  from nlpia.loaders import get_data
  from gensim.models.word2vec import KeyedVectors
  wv = get_data('word2vec')
  len(wv.vocab)
  ```
  - 구글 뉴스 word2vec 모형은 엄청나게 큼. 단어수가 300만에 각 단어 벡터의 차원은 300, 모형 전체는 약 3GB의 메모 리 차지. 가용 메모리가 충분하지 안거나 적재 시간을 줄이기 위해 limit 인수를 이용해 적은 수의 고빈도 용어들만 적재하는 방법도 있음.
- 예제 코드는 구글이 구글 뉴스 기사에 기초한 거대한 말뭉치로 훈련한 word2vec 모형들을 담은 압축 파일을 내려받고 그 모형의 단어 벡터들을 gensim의 KeyedVectors 형식의 객체 wv로 적재. wv에는 300만개의 word2vec 벡터가 담겨 있음. 구글 뉴스 기사들에는 여러 지명과 인명이 포함
