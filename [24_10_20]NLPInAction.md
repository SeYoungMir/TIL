# 1.NLP 기초.
## 3. TF-IDF 벡터
### 1. 단어 모음
- 긴 문장으로 다른 예제를 시험
- 연(kite)에 관한 영어 위키 페이지의 문단 일부로 테스트.
- NLPIA패키지에 이 텍스트가 포함, 텍스트를 불러와서 용어 빈도를 계산
- ```python
  >>> from collections import Counter
  >>> from nltk.tokenize import TreebankWordTokenizer
  >>> tokenizer = TreebankWordTokenizer()
  >>> from nlpia.data.loaders import kite_text
  >>> tokens = tokenizer.tokenize(kite_text.lower())
  >>> token_counts = Counter(tokens)
  >>> token_counts
  ```
  - TreebankWordTokenizer는 "kite."처럼 마침표가 포함된 토큰들을 산출. 이 토큰 생성기는 주어진입력 문자열이 하나의 문장이라고 (즉, 사용자가 문서를 미리 개별 문장들로 분할해서 한 문장씩 공급한다고)가정하기 때문에 문자열의 제일 끝에 있는 문장 부호만 무시.
  - TreebankWordTokenizer와는 달리 spaCy의 파서는 문장 분할과 토큰화, 그리고 기타 여러 처리를 함께 진행하기 때문에 더빠르고 정확함. 따라서 개인 프로젝트에서는 여기서 사용하는 NLTK 구성요소 대신 spaCy를 사용하는 것이 나을 수 있음.
- 빈도 분석 결과를 보면 상위 토큰 중에 불용어나 문장 부호가 많음을 알 수 있음. 이 페이지가 관사나 접속사 등의 불용어와는 관련이 적으므로, 불용어를 제거.
  - ```python
    >>> import nltk
    >>> nltk.download('stopwords',quite=True)
    >>> stopwords = nltk.corpus.stopwords.words('english')
    >>> tokens = [x for x in tokens if x not in stopwords]
    >>> kite_counts = Counter(tokens)
    >>> kite_counts
    ```
- 단어 출현 횟수 결과를 보면 이 문서에 관해 짐작할 수 있는 내용이 있음. kite, wing ,lift는 모두 이 문서에 중요한 단어들. 이 문서의 출처를 알지 못하는 상태에서 구글 같은 어떤 지식 데이터 베이스에서 이 문서를 우연히 발견했어도, 용어 빈도들로부터 이 문서가 "flight" , "lift"와 관련된 아마도 "kites"를 설명하는 문서임을 프로그래밍적으로 추론 가능
- 한 말뭉치의 여러 문서에 대해 이런 빈도 분석을 실행 시 더욱 흥미로운 추론이 가능.
- 다른 여러 문서에서도 이와 비슷한 용어 빈도들이 나온다면, 해당 말뭉치의 모든 문서가 연이나 연날리기에 관한 문서들일 가능성이 있으며, 아마 모든 문서가 "string"이나 "wind"를 자주 언급, 따라서 모든 문서에서 용어 빈도 TF("string")와 TF("wind")가 높게 나올 것임.
- 이런 수치들을 수학 연산에 좀 더 적합한 형태로 가공.