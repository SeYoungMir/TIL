# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 3. 토큰 개선
- 다음은 NLTK의 RegexpTokenizer라는 함수를 이용, 예제 문장을 토큰화 하는 예시.
- ```python
  >>> from nltk.tokenize import RegexpTokenizer
  >>> tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
  >>> tokenizer.tokenize(sentence)
  ```
- 공백 토큰을 자동으로 제외했다는 점에서, 이 토큰화 함수가 우리의 정규 표현식보다 조금 발전. 이 토큰화 함수는 문장 끝의 후행 문자 부호를 문장 부호가 없는 다른 토큰들과 개별적인 토큰으로 분리.
- NLTK 패키지는 TreebankWordTokenizer라는 토큰화 함수도 제공, 이것은 앞의 함수보다도 강력.
- 펜 트리뱅크 토큰화(Penn Treebank tokenzation)에 기초한 이 토큰화 함수는 영어 단어 토큰화에 흔히 쓰이는 다양한 규칙을 담고 있음.
- 예를 들어 이 토큰화 함수는 문장 끝 부호(?!.;,)를 인접 토큰들과 분리하면서도 소수점이 있는 수치는 하나의 토큰으로 유지.
- 또한 이 토큰 생성기는 영어의 축약형 단어들을 위한 규칙들도 갖추고 있음. 예를 들어 "wasn't"는 ["was","n't"]로 토큰화. 이는 어간 추출 같은 nLP 파이프라인의 이후 단계들에 도움이 되는 기능. 이 토큰화 기능에 관해서는 http://www.nltk.org/api/nltk.tokenize.html#module-nltk.tokenize.treebank를 참고.
- 다음은 이 함수를 사용하는 예제
- ```python
  >>> from nltk.tokenize import TreebankWordTokenizer
  >>> sentence = """Monticello wasn't designated as UNESCO World Heritage Site untill 1987."""
  >>> tokenizer = TreebankWordTokenizer()
  >>> tokenizer.tokenize(sentence)
  ```
