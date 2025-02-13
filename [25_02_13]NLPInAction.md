# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 1. 의미 기반 질의와 비유
- 단어 벡터의 위력을 가늠할 수 있는 간단한 예를 살펴보자. 예를 들면 마리 퀴리가 생각이 나지 않을 때, 그에 대한 일반적인 인상만으로 다음과 같은 검색어로 웹을 검색할 수 있다.
  - she invented something to do with physics in Europe in the early 20th century
- 이 문장으로 구글이나 빙(Bing)을 검색해도 마리 퀴리에 대한 문서의 링크가 뜨지는 않을 것임. 구글 검색은 남녀를 포함한 유명 물리학자의 목록을 담은 페이지로의 링크를 제시할 가능성이 큼.
- 그러나 일단 '마리 퀴리'혹은 'Marie Curie'를 발견하면, 구글이나 빙은 그 사실을 기억, 그래서 다음에 어떤 과학자를 찾을 때는 구글이나 빙이 좀 더 나은 결과를 제시.
- 단어 벡터를 이용 시 "woman","Europe","physics","scientist","famous"같은 단어들의 의미를 모두 결합한 단어나 이름을 찾을 수 있음. 이는 앞의 질의문으로 "Marie Curie"라는 토큰에 좀 더 가까이 접근할 수 있음을 뜻함. 단어 벡터들이 맞추어져 있다면, 이런 검색을 위해 해야 할일은 결합하고자 하는 단어들의 단어 벡터를 모두 더하는 것.
- ```python
  answer_vector = wv['woman'] + wv['Europe'] + wv['physics'] + wv['scientist']
  ```
- 의미 기반 질의를 실제로 이런 벡터 연산의 형태로 수행하는 방법을 살펴볼 수 있음. 심지어는 다음처럼 단어 벡터에서 성별에 대한 편향을 빼서 답을 구하는 것도 가능.
- - ```python
  answer_vector = wv['woman'] + wv['Europe'] + wv['physics'] + wv['scientist'] - wv['male'] - 2* wv['man']
  ```
- 단어 벡터에서는 위와같이 woman에서 man을 빼버릴 수도 있음.