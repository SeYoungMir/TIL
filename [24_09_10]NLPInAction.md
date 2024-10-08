# 1.NLP 기초.
## 2. 단어 토큰화
### 1. 어간 추출 개요
- 텍스트에서 특징을 추출하는 것이 어려운 이유를 보여주는 예로 어간 추출(stemming)을 들 수 있음. 어간 추출은 한 단어의 여러 변형을 동일한 '통' 혹은 군집으로 묶는 것을 말함
- 아주 똑똑한 사람들이 단어의 여러 어형 변화를 오직 그 철자에만 기초해서 묶는 알고리즘을 개발하는데 평생을 바쳤다. 그것이 얼마나 어려운 일일까.
- 예를 들면 "ending"에서 동사화 접미사 "ing"을 제거하면 "ending"을 포함한 여러 변형을 대표하는 "end"가 남는데, "running"에서 "run"을 추출하려면 "ing"가 아니라 n이 붙은 "ning"을 제거해야함.
- 게다가 "sing"에 대해 이런 방법을 적용하면 "s"라는 글자 하나만 남음으로 주의해야 한다.
- 복수형을 단수형으로 바꾸기 위해 "s"를 제거할 때도 비슷한 일이 벌어짐. "words"에서 "s"를 제거해서 "word"를 얻는 것은 좋지만 "bus"나 "lens"에는 이런 방법이 통하지 않음. 한 단어 또는 단어의 한 부분에 있는 개별 글자가 단어의 의미에 관한 정보를 제공하고, 글자 하나 때문에 단어의 의미가 전혀 달라질 수 있다.
- 이번 장에서는 단어 철자 난제들을 전통적인 어간 추출 접근 방식으로 해결 , 우리의 NLP 파이프라인을 좀 더 똑똑하게 만듦
- 나중에 통계적 군집화 접근 방식에서는 대상 영역의 단어들을 담은 대량의 자연어 텍스트만 있으면 됨. 접근 방식이 텍스트 자료의 단어 사용 통계량으로부터 '의미론적 어간'들(구체적으로는, 표제어나 동의어 같은 좀 더 유용한 단어들의 군집)을 밝혀내므로, 사람이 정규 표현식을 작성하거나 어간 추출 규칙을 작성할 필요가 없음.