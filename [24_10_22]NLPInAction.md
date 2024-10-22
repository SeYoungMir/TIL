# 1.NLP 기초.
## 3. TF-IDF 벡터
### 2. 벡터화
- 다음은 벡터 공간의 원점에 해당하는 모든 성분이 0인 벡터
  - ```python
    >>> from collections import OrderedDict
    >>> zero_vector = OrderedDict((token,0) for token in lexicon)
    >>> zerco_vector
    ```
- 말뭉치의 문서마다 이 기준 벡터를 복사해서 각 성분을 해당 용어 빈도로 갱신해서 세 문서의 벡터들을 생성.
  - ```python
    >>> import copy
    >>> doc_vectors-[]
    >>> for doc in docs:
    ...     vec = copy.copy(zero_vector)
    ...     tokens = tokenizer.tokenize(doc.lower())
    ...     token_counts = Counter(tokens)
    ...     for key, value in token_counts.items():
    ...         vec[key] = value / len(lexicon)
    ...     doc_vectors.append(vec)
    ```
- 이렇게 해서 문서당 하나씩 세 개의 벡터가 생성. 이 벡터들을 어떻게 활용하는가? 이 문서 표현 용어 빈도 벡터는 말 그대로 벡터. 벡터에 적용되는 갖가지 수학 연산을 적용 가능. 따라서. 벡터와 벡터 공간을 공부하는 것이 필요.

#### 1. 벡터 공간
- 벡터는 선형 대수의 기본적 구성 요소. 벡터는 순서 있는 수치 목록, 이 수치들은 벡터 공간에서 그 벡터의 위치를 말해주는 좌표성분들로 해석 가능. 이러한 해석에서 하나의 벡터는 공간의 한 장소(위치)를 서술. 또는 벡터로 방향이나 속력, 두 위치 사이의 거리를 나타낼 수 있음.
- 벡터 공간(vector space)는 그 공간 안에 나타날 수 있는 모든 가능한 벡터의 집합. 벡터의 성분 개수는 해당 벡터 공간의 차원 수. 따라서 성분이 두 개인 벡터는 2차원 벡터 공간에 놓이고, 성분이 세 개인 벡터는 3차원 벡터 공간에 놓임.