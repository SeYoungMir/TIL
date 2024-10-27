# 1.NLP 기초.
## 3. TF-IDF 벡터
### 3. 지프의 법칙
- 다음은 브라운 말뭉치에서 지프의 법칙을 실험하는 코드
  - ```python
    >>> nltk.download('brown')
    >>> from nltk.corpus import brown
    >>> brown.words()[:10]
    >>>brown.tagged_words()[:5]
    >>>len(brown.words())
    ```
- 브라운 말뭉치의 단어는 100만을 넘고, 가장 자주 쓰이는 것을 출력.
  - ```python
    >>> from collections import Counter
    >>> puncs = set((',','.','--','-','!','?',':',';','''',"''",'(',')','[',']'))
    >>> word_list = (x.lower() for x in brown.words() if x not in puncs)
    >>> token_counts = Counter(word_list)
    >>> token_counts.most_common(20)
    ```
- 용어 빈도들을 살펴보면 브라운 말뭉치 역시 지픅 예측한 로그 관계를 따르는 것으로 보임. 빈도순으로 1위인 단어 "the"는 2위 단어 "of"보다 약 두 배 자주 쓰이고 3위 단어인 "and"보다는 약 세 배 자주 쓰임. 이 결과를  신뢰하지 못한다면 NLPIA 패키지의 예제 코드를 직접 실행할 것.
- 정리하자면, 충분히 큰 말뭉치의 단어들에 그 빈도에 따라 순위를 매기면(가장 자주 나온 단어가 1위, 그 다음이 2위,... 등등), 순위와 빈도가 대략반비례 관계임을 알 수 있음.즉 1위 단어는 2위 단어보다 두 배 자주 나오고 3위 단어보다는 약 세 배, 4위 단어보다는  네 배 자주 나옴.
- 이러한 관계를 이용 시 말뭉치가 충분히 크다고 할 때 주어진 한 단어가 임의의 한 문서에 몇 번이나 출현할 지 예측 가능.