# 1.NLP 기초.
## 3. TF-IDF 벡터
### 1. 단어 모음
- 짧은 문장에서는 순서 없는 단어 모음도 문장의 원래 의도에 관한 정보를 상당히 많이 유지.
- 단어 모음의 정보로도 스팸 검출, 감정(긍정,행복 등) 분석 같은 상당히 강력한 일을 할 수 있음. 풍자나 냉소 같은 미묘한 의도검출 역시 가능.
- 단어 모음은 단어들이 뒤죽박죽 담겨 있는 하나의 자루(bag)이지만 , 문장의 의미에 관한 정보가 꽤 많이 들어 있음. 자루 안의 단어들을 어떤 의미 있는 순서로 정렬 시 단어들을 고찰하기가 좀 더 쉬워짐.
- 단어들을 빈도순으로 정렬, Counter 객체에는 이런 용도에 맞는 most_common()이라는 메서드 존재.
  - ```python
    >>> bag_of_words.most_common(4)
    ```
- 어떤 문서가 한 문서에 출현한 횟수를 용어 빈도(term frequency; 용어 도수)라고 부르고, 흔히 TF로 줄여서 표기. 응용에 따라서는 단어 출현 횟수를 해당 문서에 있는 모든 단어의 수로 나누어서 정규화.
-  앞의 결과에서, 예제 문장에 가장 자주 출현한 토큰 4개는 "the",",","harry","faster" 이며, 정관서 "the"와 문장 부호 ","는 문장의 의도에 관한 정ㄷ보를 그리 많이 담고 있지 않음.
-  문서에는 이런 별 정보 없는 토큰들이 대단히 많음. 이번 장의 여러 예제에는 이런 토큰들을 비롯한 여러 표준 영어 불용어들과 문장 부호들을 무시. 예시의 경우, 이들을 제외하면 "harry"와 "faster"가 가장 자주 등장한 토큰.
-  다음은 Counter 객체(bag_of_words 변수)에서 "harry" 의 용어 빈도를 조회, 전체 토큰 수로 정규화하는 예시
   - ```python
     >>> times_harry_appears = bag_of_words['harry']
     >>> num_unique_words = len(bag_of_words)
     >>> tf = times_harry_appears/ num_unique_words
     >>> round(tf,4)
     ```
- 정규화된 용어 빈도라는 개념은 단어 출현 횟수를 문서의 길이로 "길들인" 것. 단어 빈도를 길들여야 하는 이유를 예를 들면, 짧은 문장 A에서 "dog"이라는 단어는 3회, 책 하나 길이의 문서 B에서는 100회 등장한다고 하면, "dog"의 중요도는 둘에서 꽤 다르기 때문.
- 다음은 단어 빈도뿐만 아니라 단어가 포함된 문서의 길이도 고려, 단어의 중요도를 추정하는 공식
  - $TF("dog",documentA)=3/30=0.1$
  - $TF("dog",documentB)=100/5800000=0.00017$
- 위와 같은 수치들은 단어 "dog"을 기준, 두 문서의 특징을 비교하는 데 유용. 단순한 단어 출현 횟수가 아니라 그것을 문서의 길이로 나눈 '정규화된 용어 빈도'로 문서를 표현시 말뭉치 안에서의 문서의 특징을 좀 더 잘 표현할 수 있음.
- 정규화된 용어 빈도는 주어진 단어가 그 문서에서 상대적으로 얼마나 중요한지도 말해줌. 앞의 예제 문장의 경우, 비교적 짧은 문장인데도 "Harry"가 두번, "faster"가 세 번이나 나왔다는 것에서 그 문장에서 해리의 속도가 대단히 중요함을 말해줌.
- 다소 작위적이어도, 이 예는 주어진 단어의 존재, 또는 부재만 알려주는 이진값(비트)보다 단어의 출현 횟수가 문장의 의미를 파악하는 데 도움이 된다는 점을 표시.
