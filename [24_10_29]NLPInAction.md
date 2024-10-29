# 1.NLP 기초.
## 3. TF-IDF 벡터
### 4. 주제 모형화
- 각 문서에서 "kite"가 몇 번이나 출현했는지 세어보자. 이름이 _tf로 끝나는 두 변수는 각 문서의 용어 빈도들을 담을 사전 객체들.
  - ```python
    >>> intro_tf = {}
    >>> history_tf = {}
    >>> intro_count = Counter(intro_tokens)
    >>> intro_tf['kite']/intro_total
    >>> history_counts = Counter(history_tokens)
    >>> history_tf['kite']= history_counts['kite']/history_total
    >>> 'TF of "kite" in intro:{:.4f}'.format(intro_tf['kite'])
    >>> 'TF of "kite" in history{:.4f}'.format(history_tf['kite'])
    ```
- 두 문서의 "kite" 출현 횟수는 약 두 배 정도 차이가 남. 그렇다고 첫 문서가 둘째 문서보다 연에 관한 내용이 두 배인 것은 아님. 수치들을 좀 더 관찰.
- 두 문서에서 "and"의 빈도를 확인.
- ```python
  >>> intro_tf['and']=intro_counts['and']/intro_total
  >>> history_tf['and']= history_counts['and']/history_total
  >>> print("intro tf",intro_tf['and'],"history_tf",history_tf['and'])
  ```
- 결과에서 두 문서 모두 "and"가 "kite"만큼이나 자주 등장, 그렇다고 이 말뭉치에서 접속사 "and"가 "kite"만큼 중요하진 않음. 이는 이전에 "the"의 해리에 관한 말뭉치와 같음.
- 주어진 단어가 문서에서 얼마나 중요한지 보려면 IDF가 필요.
- IDF의 개념은 "이 토큰이 이 문서에 등장하는 것이 얼마나 이상한 일인지" 생각하는 것이 좋음. 어떤 용어가 이상하게도 한 문서에만 자주 등장, 말뭉치의 나머지 문서들에는 나오지 않는다면, 그 용어는 그 문서에 아주 중요한 단어. 그 용어는 그 문서의 주제를 말해주는 단어일 수 있음 .이것이 주제 분석(topic analysis)의 첫걸음.
- 한 용어의 IDF는 전체 문서 수를 그 용어가 출현한 문서 수로 나눈 것. "and"와 "kite"의 IDF는 같음.
- "China"라는 단어는 "and"와 "kite"의 IDF의 두배.
