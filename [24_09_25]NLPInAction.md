# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 3. 토큰 개선
- 축약형
  - 축약형 "wasn't"를 ["was","n't"]로 분리하는 것이 바람직한 이유는 다음과 같음
  - 구문 트리를 사용하는 문법 기반 NLP 모형 같은 몇몇 응용에서, 구문 트리 파서가 입력을 미리 정해진 구문 규칙들에 기초해서 일관되고 예측 가능한 토큰들로 다룰 수 있으려면 "wasn't"를 was와 not으로 분리할 필요가 있음. 영어에서 축약형 단어를 만드는 규칙은 다양하며, 널리 통용되는 표준적인 규칙도 잇고, 일부만 사용하는 비 표준적인 규칙도 잇음.
  - 축약형 단어를 그 구성 단어들로 분리하면 모든 가능한 축약형 단어를 예측할 필요 없이 그냥 개별 단어의 여러 철자 변형들만 고민하면 되므로, 의존성 트리 파서나 구문 파서를 만들기가 쉬워짐.
    - 트위터나 페이스북 같은 SNS 에서 얻은 비형식적 텍스트 토큰화
      - NLTK 라이브러리에는 casual_tokenize라는 토큰화 함수가 존재.
      - 이 함수는 SNS에서 흔히 볼 수 있는 짧고 비형식적인, 이모티콘들이 난무하는 텍스트, 그러니까 문법과 철자의 관례가 아주 다양한 텍스트를 다루도록 만들어짐.
      - 특히 casual_tokenize 함수는 텍스트에서 사용자 이름을 제거하고 토큰 안에서 반복되는 문자들을 줄이는  데 유용.
    - ```python
      >>> from nltk.tokenize.casual import casual_tokenize
      >>> message = """RT @TJMonticello Best day everrrrr at Monticello. Awesommmmmme day :*)"""
      >>> casual_tokenize(message)
      >>> casual_tokenize(message,reduce_len=True,strip_handles =True)
      ```
    