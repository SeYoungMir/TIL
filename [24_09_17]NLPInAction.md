# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축 - 이어서
- 예제 코드에서 주목할 또 다른 점은 이진 희소 벡터를 dict, 즉 파이썬의 사전 자료 구조(또는 단어와 이진값의 쌍을 담는 임의의 자료 구조)에 저장하면 공간이 그리 낭비되지 않는다는 것. 이진 사전 자료 구조는 값이 1인 항목만 저장하므로, 어휘의 단어가 수천 개이든 수만 개이든 상관없이 실제로 문서에 출현한 단어에 대해서만 저장 공간이 소비.
- 만일 단어 모음 벡터를 일련의 0들과 1들로 명시적으로 표현 시 공간 낭비가 대단히 심할 것. 예를 들어 어휘의 단어가 10만 개이면, 예제 문장의 단어 10개를 제외한 나머지 9,990개의 단어에 대해 쓸데없이 0들을 저장해야 함. 예제 문장을 그런 밀집(dense;희소의 반대, 즉 조밀한)이진 벡터로 표현한다면 약 100KB의 저장 공간이 필요. 사전 자료 구조는 문장에 없는 단어, 즉 이진 벡터의 성분이 0인 단어는 그냥 '무시'하므로 단 몇 바이트로 10단어 문장을 표현할 수 있음. 그리고 사전 자료 구조의 각 항목에 해당 단어가 어휘의 몇 번째 단어인지를 말해 주는 정수 색인 값을 담는다면, "26."이나 "Jefferson"같은 단어 문자열 또한 일일히 저장할 필요가 없으므로 저장 공간을 더욱 줄일 수 있음.
- 그런 좀 더 효율적인 형태의 사전으로 Pandas 패키지의 Series가 있음. 그리고 Series를 Pandas의 DataFrame으로 감싸면, 토머스 제퍼슨에 관한 텍스트의 이진 벡터 '말뭉치(corpus)'에 더 많은 문장을 추가할 수 있게 됨. 그리고 그런 식으로 DataFrame(말뭉치의 텍스트들에 대응되는 벡터들의 테이블)에 더 많은 문장과 해당 단어 모음 벡터를 추가할 수록 희소한 벡터 표현과 밀집 단어 모음 표현의 차이가 점점 커짐.
- ```python
  >>> import pandas as pd
  >>> df = pd.DataFrame(pd.Series(dict([(token,1)for token in sentence.split()])),columns=['sent']).T
  >>> df 
  ```
- 그럼 이 말뭉치에 문장 몇 개를 더 추가해서 DataFrame이 어떻게 성장하는지 확인 가능.
- DataFrame은 문서 검색을 위한 '역색인(inverse index)' 접근을 위해 행 색인과 열 색인을 모두 제공.(이런 기능은 이를테면 잡학상식 퀴즈의 답을 빠르게 찾는 데 유용).행 색인으로는 특정 문서에 대한 행에 접근 가능, 열 색인으로는 그 문서의 특정 단어에 대한 성분(칸)에 접근 가능.
- ```python
  >>> sentences = "Thomas Jefferson began building Monticello at the age of 26.\n"""
  >>> sentences += """Construction was done mostly by local masons and carpenters.\n"""
  >>> sentences += "He moved into the South Pavilion in 1770.\n"
  >>> sentences += """Turning Monticello into a neoclassical masterpiece was Hefferson's obsession."""
  >>> corpus = {}
  >>> for i , sent in enumerate(sentences.split('\n')):
  ...     corpus['sent{}'.format(i)] = dict((tok,1)for tok in sent.split())
  >>> df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
  >>> df[df.columns[:10]]
  ```
- 위 예제를 실행해서 출력을 훑어보면 이 문장들이 사용하는 단어가 거의 겹치지 않음을 알 수 있음. 두 문장 이상에 쓰인 단어는 "Monticello"가 유일. 문서들을 비교하거나 비슷한 문서를 검색하려면, 파이프라인에서 이런 중복 단어들을 식별할 수 있어야 함. 두 문장의 유사도를 측정하는 한 가지 방법은 이런 중복 토큰들의 개수를 내적을 이용해서 세는 것임.