# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축 - 이어서
- 한 문장을 토큰화하는 가장 간단한 방법은 문자열 안의 공백(whitespace)문자를 단어 구분자(delimiter;또는 구분 문자)로 사용하는 것.
- 파이썬에선 표준 라이브러리의 메서드인 split 사용. 내장 클래스 str 뿐만 아니라 str 클래스에서 인스턶스화 된 str 객체는 이 메서드를 지원. 다음은 메서드 사용 예시
- ```python
  >>> sentence = """Thomas Jefferson began building Monticello at the age of 26."""
  >>> sentence.split()
  >>> str.split(sentence)
  # 결과는 Thomas/Jefferson/began/building/Monticello/at/the/age/of/26. 으로 분리
  ```
- 예제에서 보듯이, 이 파이썬 내장 메서드는 단순한 문장을 잘 토큰화. 유일한 실수라면 '실수'라면 문장 끝의 토큰 "26."에 마침표가 포함되어 있다는 점. 보통은 마침표 같은 문장 호를 의미 있는 토큰과 분리. "26."라는 토큰은 컴퓨터 언어에서 부동소수점 수 26.0을 표현하는 데는 완벽하게 합당하지만, 이것을 개별적인 토큰으로 인정한다면 다른 어떤 문장의 중간에 등장하는 "26"이라는 단어와는 구분되는 어떤 토큰이 되어 버림. 좋은 토큰 생성기라면 "26","26!","26?","26."에서 여분의 문장 부호를 제거, 이들이 모두 "26"이라는 단어에 속하게 만들어야 함. 그리고 좀 더 정교한 토큰 생성기는 문장 끝의 문장부호를 개별적인 토큰으로 산출. 그러면 문장 수준의 분할기나 문장 경계 검출기가 문장의 끝을 식별 가능.
- 일단 지금은 이 불완전한 토큰 생성기를 그대로 사용, 문장 부호나 기타 문제점은 나중에 해결.
- 다음으로 할 일은 각 단어를 나타내는 수치 벡터 표현을 만드는 것. 이런 벡터를 원핫 벡터(one-hot vector)라고 부름. 이런 원핫 벡들의 순차열(sequence)는 원래의 원문 텍스트를 온전히 표현. 여기서 핵심은 , 주어진 텍스트가 이제는 수치적인 자료 구조(2차원 수치 배열)로 변환된다는 점. 즉, NLP의 첫번째 문제인 단어들을 수치로 변환하는 문제가 여기서 해결.
- ```python
  >>> import numpy as np
  >>> token_sequence=str.split(sentence)
  >>> vocab = sorted(set(token_sequence))
  >>> num_tokens = len(token_sequence)
  >>> vocab_size = len(vocab)
  >>> onehot_vectors =np.zeros((num_tokens,vocab_size),int)
  >>> for i, word in enumerate(token_sequence):
  ...   onegot_vectors[i,vocab.index(word)] = 1
  >>> ' '.join(vocab)
  >>> onehot_vectors
  ```
- 나열된 1들과 0들이 바로 토머스 제퍼슨에 관한 예제 문장의 원핫 단어 벡터들인데, 뭐가 뭔지 알아채기 힘듦.
- Pandas 패키지의 DataFrame을 이용하면 이런 자료를 좀 더 쉽게 파악 가능.
- Pandas는 1차원 배열을 Series 라는 객체로 감쌈. 이 객체는 여러 유용한 기능을 제공. Pandas는 목록들의 목록, 2차원 NumPy 배열, 배열들의 배열, 사전들의 사전 같은 내포된 자료 구조를 다룰때 유용.