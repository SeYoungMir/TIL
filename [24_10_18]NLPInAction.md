# 1.NLP 기초.
## 3. TF-IDF 벡터
### 1. 단어 모음
 - 앞에서 우리는 텍스트로부터 우리의 첫 번째 벡터 공간 모형을 생성.
 - 각 단어의 원핫 부호화 벡터로 표현, 그 벡터들을 모두 비트별 논리합(OR)으로(또는 절단된 sum으로)결합해서 텍스트를 표현하는 하나의 벡터를 생성.
 - 이러한 이진 단어 모음(bag of words)벡터를 Pandas의 DataFrame 같은 자료 구조에 담으면 문서 검색을 위한 훌륭한 색인.
 - 앞에서 또한 주어진 텍스트에서 단어가 출현한 횟수, 즉 단어 빈도로 이루어진 좀 더 유용한 벡터 표현도 탐색. 이러한 단어 빈도 벡터는 자주 출현한 단어일수록 그 문서의 의미에 더 많이 기여한다는 가정을 깔고 있음.
 - 예를 들어 "cats"나 "gravity" 같은 단어가 많이 나오는 문서보다는 "wing"(날개)과 "rudder"(방향키) 같은 단어가 많이 나오는 문서가 비행기나 항공 산업과 관련된 문제와 연관이 클 것.
 - 그리고 "good","best","joy","fantastic" 같은 긍정적 감정을 표현하는 단어들이 많이 등장하는 문서에는 긍정적'감정'이 담겨 있을 가능성이 큼. 그러나 단순한 규칙들에만 의존하는 알고리즘은 얼마든지 문서의 의미나 감정을 오해해서 엉뚱한 결과를 낼 수도 있음.
 - 간단한 예제를 통해 단어 출현횟수가 어떻게 도움이 되는지 탐색.
   - ```python 
     >>> from nltk.tokenize import TreebankWordTokenizer
     >>> sentence = """The faster Harry got to the store, the faster Harry, the faster, would get home."""
     >>> tokenizer = TreebankWordTokenizer()
     >>> tokens = tokenizer.tokenize(sentence.lower())
     >>> tokens
     ```
  - 위 코드는 주어진 문장의 고유한 단어들의 목록을 출력. 파이썬 사전 자료 구조 (dict)는 이런 목적에 아주 적합. 파이썬 모듈 Counter를 사용하면 각 토큰의 빈도도 간단하게 셀 수 있음.
    - ```python
      >>> from collections import Counter
      >>> bag_of_words = Counter(tokens)
      >>> bags_of_words
      ```
  - 토큰들의 순서가 뒤죽박죽, 이는 파이썬 사전이 키들을 알파벳순으로 정렬하지 않기 때문, 키들의 순서는 저장, 갱신, 조회에 최적화. 일관된 출력을 고려하지 않음. 따라서 원래의 문장에 있던 단어들의 순서에 관한 정보는 모두 제거
    - collections.Counter 객체는 순서 없는 컬렉션(unordered collection)이며, 이런 자료 구조를 자루(bag;또는 가방)나 중복집합(multiset;또는 다중집합)이라고 부르기도 함.
    - 플랫폼과 파이썬 버전에 따라서는 Counter 출력의 토큰들이 알파벳 순이나 문장의 출현 순서로 나타날 수 있음. 그러나 파이썬 표준 사전 자료구조 dict와 마찬가지로, Counter의 토큰(키)들이 어떤 특정한 순서로 나타나리라고 기대해서는 안됨.