# 1.NLP 기초.
## 3. TF-IDF 벡터
### 4. 주제 모형화-
- IDF라는 이 '희소성(rarity)' 측도를 용어 빈도들에 대한 가중치로 적용. 우선, "and"라는 단어가 있는 문서의 수를 체크.
    - ```python
      >>> num_docs_containing_and=0
      >>> for docs in [intro_tokens,history_tokens]:
      ...   if 'and' in doc:
      ...       num_docs_containing_and += 1
      ```
- "kite"와 "china"에 대해서도 이런식으로 문서 수를 계산, 다음으로 두 문서에서 "China"의 TF 계산
  - ```python
    >>> intro_tf['china']=intro_counts['china]/intro_total
    >>> history_tf['china']= history_counts['china]/history_total
    ```
- "kite"와 "and"의 TF들도 같은 방식으로 계산, 세 단어의 IDF를 계산. 앞에서 TF들을 구할때처럼 문서별로 사전 객체를 두고 IDF를 저장.
  - ```python
    >>> num_docs=2
    >>> intro_idf={}
    >>> history_idf={}
    >>>  intro_idf['and']=num_docs/num_docs_containing_and
    >>>  history_idf['and']=num_docs/num_docs_containing_and
    >>>  intro_idf['kite']=num_docs/num_docs_containing_kite
    >>>  history_idf['kite']=num_docs/num_docs_containing_kite
    >>>  intro_idf['china']=num_docs/num_docs_containing_china
    >>>  history_idf['china']=num_docs/num_docs_containing_china
    ```
- 연을 소개하는 문서에 대한 각 단어의 TF에 IDF라는 가중치를 곱해서 TF-IDF 점수를 계산
  - ```python
    >>>  intro_tfidf={}
    >>>  intro_tfidf['and']=intro_tf['and']*intro_idf['and']
    >>>  intro_tfidf['kite']=intro_tf['kite']*intro_idf['kite']
    >>>  intro_tfidf['china']=intro_tf['china']*intro_idf['china']
    ```
- 같은 방식으로 연의 역사에 관한 문서에 대해서도 TF-IDF 계산.