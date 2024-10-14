# 1.NLP 기초.
## 2. 단어 토큰화
### 3. 감정 분석
#### 1. VADER - 규칙 기반 감정 분석기
- 조지아 공과대학(GA Tech)의 후토와 길버트는 최초의 성공적 감정 분석 알고리즘 중 하나인 VADER 알고리즘 고안. VADER는 Valence Aware Dictionary for sEntiment Reasoning(감정 추론을 위한 결합가 인식 사전)의 머릿글자를 딴 것
- 여러 NLP 패키지가 이 알고리즘(또는 그 변형)을 구현
- NLTK의 경우 nltk.sentiment.vader가 VADER 알고리즘을 구현한 것. 
- 후토 자신은 vaderSentiment라는 파이썬 패키지를 관리중. 예제는 이 패키지를 사용
- 아래의 예제를 실행하려면 먼저 터미널 또는 명령 프롬프트에서 pip install vaderSentiment를 실행, vaderSentiment 패키지를 설치해야 함. NLPIA에는 vaderSentiment가 포함되지 않음.
- ```python
  >>> from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
  >>> sa = SentimentIntensityAnalyzer
  >>> sa.lexicon
  >>> sa.polarity_scores(text=)
  >>> [(tok,score) for tok,score in sa.lexicon.items() if "" in tok]
  >>>sa.polarity_scores(text="python is very readable and it's great for NLP")
  ```
- 위와 가은 규칙 기반 접근 방식이 앞에서 예로 든 사용자 의견들을 평가하는 방법 예제는 다음과 같음
- ```python
  >>> corpus = ["예제 문장들"]
  >>> for doc in corpus:
  ...   scores = sa.polarity_scores(doc)
  ...   print('{:+}:{}'.format(scores['compound'],doc))
  ```
- VADER의 유일한 단점은 문서의 모든 단어가 아니라 약 7,500개 단어만 고려한다는 점. 만약 문서의 모든 단어로 감정 점수를 측정해야한다면, 할 일이 엄청나게 증가. 모든 단어의 감정 점수를 일일히 기입하거나, SentimentIntensityAnalyzer.lexicon의 사전 자료 구조에 수많은 커스텀 단어들을 직접 추가해야함. 기본적으로 규칙 기반 접근 방식은 대상 자연어를 이해하지 않으면 불가능. 언어를 이해하지 못하면 사전(어휘집)에 점수들을 집어넣지도 못할 것이기 때문.