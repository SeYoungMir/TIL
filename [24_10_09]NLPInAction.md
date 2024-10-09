# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 6. 표제어 추출
- 단순한 어간 추출보다 품사에 기초한 표제어 추출이 더 나은(better) '어근'을 식별할 수 있는 이유는 better라는 단어를 생각해보았을 때 알기 쉬움.
- 어간 추출기는 어미 "er"을 제거, "bett" 또는 "bet" 같은 어간을 산출. 그렇게 하면 "better"는 "bets"나 "Bet's" 처럼 전혀 다른 의미의 단어들과 묶임. 반면 표제어 추출기는 "better"를 "betterment","best" 같은 의미상으로 가까운 단어들과 묶음. 심지어는 "good","goods"등과 묶을 수도 있음.
- 이런 이유로, 대부분의 응용에서는 표제어 추출기가 어간 추출기보다 나음. 현실적으로 어간 추출기는 대규모 정보 검색 응용 프로그램(키워드 기반 문서 검색 등)에만 사용. 정보 검색용 파이프라인에서 어간 추출기의 차원 축소 및 재현율 향상 능력이 꼭 필요한 경우여도, 어간 추출 단계 바로 앞에 표제어 추출 단계를 배치, 더 나은 결과를 획득 가능. 어떤 단어의 표제어는 유효한 영어 단어이므로, 표제어 추출기의 출력은 어간 추출기의 입력으로 유효. 어간 추출기 앞에 표제어 추출기를 두면, 어간 추출기만 사용했을 때보다 차원이 더 많이 축소, 정보 검색 재현율도 증가.
- 파이썬에서 단어의 표제어를 식별하는 방법은 NLTK 패키지에 WordBetLemmatizer라는 표제어 추출기 사용. 이 표제어 추출기는 좀 더 정확한 표제어 추출을 위해 주어진 단어의 품사 정보도 요구.
- ```python
  >>> nltk.download('wordnet')
  >>> from nltk.stem import WordNetLemmatizer
  >>> lemmatizer = WordNetLemmatizer
  >>> lemmatizer.lemmatize("better") # 인수 생략 시 명사를 뜻하는 "n" 적용
  >>>lemmatizer.lemmatize("better", pos="a")
  >>>lemmatizer.lemmatize("good",pos="a")
  >>>lemmatizer.lemmatize("goods",pos="a")
  >>>lemmatizer.lemmatize("goods",pos="n")
  >>>lemmatizer.lemmatize("goodness",pos="n")
  >>>lemmatizer.lemmatize("best",pos="a")
  ```