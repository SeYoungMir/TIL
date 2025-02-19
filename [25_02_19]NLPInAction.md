# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
- 다음 코드를 참조
- ```python
  from nlpia.book.examples.ch06_nessvectors import *
  nessvector('Marie_Curie').round(2)
  ```
- 예제에 쓰인 '성질 벡터(ness-vector)'들을 생성하는 방법은 예제 GitHub 저장소의 예제 스크립트([링크](https://github.com/totalgood/nlpia/blob/master/src/nlpia/book/examples/ch06_nessvectors.py))를 참고. 이 예제 스크립트의 접근 방식을 word2vec 어휘의 임의의 단어나 n-그램과 임의의 '성질들'에 적용 가능.
- 미콜로프는 단어들을 수치 벡터로 표현하는 방법을 고민하는 도중에 word2vec 알고리즘을 고안. 그는 앞에 나온 것 같은 덜 정확한 단어 감정 계산 방식에 만족할 수 없었고, 비유 질문의 예에 나온 것 같은 벡터 지향적 추론(vector-oriented reasoning)을 가능하게 하는 벡터 표현을 원함. 이는 그냥 컴퓨터에 적합한 수치들로 이루어진 단어 벡터에 수학 계산을 적용해서 얻은 수치들을 다시 사람이 이해할 수 있는 단어로 환원하는 개념. word2vec의 단어 벡터들을 더하고 뺌으로써 그 벡터들이 나타내는 단어들에 관한 어떤 추론을 수행 가능.
- LSA를 이용해서 문서 전체로부터 얻은 주제 벡터들은 문서 분류나 의미 기반 검색, 군집화에 적합. 그러나 LSA가 산출한 주제-단어 벡터들은 짧은 문구나 복합어 수준의 의미 분석, 분류, 군집화에 사용하기에는 정확하지 않음. 좀 더 정확하고 재미있는 단어 벡터들을 얻으려면 단층 신경망을 훈련해야함.