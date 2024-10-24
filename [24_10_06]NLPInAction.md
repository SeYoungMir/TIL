# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 5. 어휘 정규화
- 어간 추출
  - 어간 추출 때문에 검색 엔진의 '정밀도'가 크게 감소 가능. 즉, 검색 결과에 검색어와 관련이 있는 문서들이 늘어날 뿐만 아니라 무관한 문서들도 늘어날 수 있음.
  - 응용에 따라서는 이런 '가양성(false-positive; 거짓 양성)'비율, 즉 사용자에게 별로 유용하지 않은 페이지들의 비율이 문제가 될 수 있음. 그래서 대부분의 검색 엔진은 대소문자 정규화뿐만 아니라 어간 추출도 비활성화 하는 수단도 제공, 앞에서 언급한 따옴표로 감싸기가 그런 예.
  - 사용자가 "Portland Housing Development software"  처럼 검색 문굴르 따옴표로 감싸는 것은 그 단어들로 이루어진 정확한 문굴로 검색을 수항하라는 것. 예를 들어 "dr house call"이 아니라 "Dr.House's call"을 검색하고 싶을 때는 어간 추출 기능을 끄는 것이 좋음
  - 다음은 후행 s들을 처리하는 간단한 어간 추출기를 순수 파이썬으로(즉, 외부 패키지를 사용하지 않고)구현한 예
  - ```python
    >>> def stem(phrase):
    ...     return ' '.join([re.findall('^(.ss|.*?)(s)?$',word)[0][0].strip("'") for word in phrase.lower().split()])
    >>> stem('houses')
    ```
  - 이 어간 추출함수에 쓰인 짧은 정규 표현식은 다음과 같은 규칙들을 표현.
    - 만일 단어가 둘 이상의 s로 끝나면, 어간은 그 단어 자체이고 접미사는 빈 문자열.
    - 만일 단어가 하나의 s로 끝나면, 어간은 단어에서 s를 제외한 부분이고 접미사는 s
    - 만일 단어가 s로 끝나지 않으면, 어간은 그 단어 자체이고 접미사는 없음.
  - 결과적으로 이 어간 추출 함수는 몇몇 복수형 단어나 소유격 접미사가 붙은 단어에서 어간을 추출
  - 이 어간 추출 함수는 복수형 변화가 단순한 단어들에는 잘 작동, 좀 더 복잡한 경우에는 잘 작동하지 않음. 예를 들어 이 함수의 규칙들은 dishes나 heroes와 같은 단어를 제대로 처리하지 못함. 이런 더 복잡한 경우들을 처리하려면 NLTK 패키지가 제공하는 어간 추출기를 사용하는 것이 좋음.
  - 또한 이 어간 추출 함수는 앞에서 언급한 "Portland Housing"검색의 "housing"같은 예도 처리하지 못함.