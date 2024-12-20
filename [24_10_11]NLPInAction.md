# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 7. 용법
- 검색 기반 챗봇에서는 재현율보다 정밀도가 더 중요, 어간 추출이나 기타 정규화를 적용하지 않는 엄격한 검색을 먼저 수행, 원하는 결과를 찾지 못했을 때만 어간 추출이나 기타 정규화를 적용한 검색을 수행하는 것이 바람직. 그러면 정규화된 토큰 부합들이 비정규화된 토큰 부합들보다 낮은 점수 획득.
  - 여기서 핵심은, 관심 있는 단어들의 여러 용법과 대소문자 구성을 담은 텍스트를 충분히 확보할 수 있다면, 굳이 어간 추출과 표제어 추출을 사용할 필요가 없다는 사실.
  - 요즘은 NLP 자료 집합이 넘쳐나는 만큼, 생소한 전문 용어가 많이 쓰이는 과학이나 기술, 문학의 아주 특화된 작은 분야에 관한 텍스트를 다루는 것이 아닌 한, 필요한 텍스트를 충분히 확보하지 못하는 경우는 드물 것.
  - 이는 영어의 경우, 영어 이외의 언어에서는 여전히 표제어 추출이 유용할 것. 스탠퍼드 대학교의 정보 검색 교과 과정에는 어간 추출과 표제어 추출이 아예 제외, 이는 영어에서 어간 추출과 표제어 추출을 해 봤자 재현율 증가는 무시할 만한 수준, 정밀도는 크게 감소하기 때문
### 3. 감정 분석
- NLP 파이프라인이 처리하는 토큰이 단일 단어이든, 아니면 n-그램이나 어간, 표제어이든, 각 토큰에는 어떤 정보가 담겨 있음. 단어의 감정(sentiment;또는 정서), 즉 그 단어가 불러일으키는 전반적인 느낌은 그러한 정보의 중요한 일부. 단어 조합이나 문구, 문장 등에 담긴 강점을 분류하고 측정하는 것은 감정 분석(sentiment analysis; 또는 감성 분석, 정서 분석)이라고 부름.
- 감정 분석은 NLP의 일반적인 응용 중 하나. 여러 기업에서 NLP 기술자에게 요구하는 주된 작업이 이 감정 분석.
- 기업은 사용자가 자사 제품을 어떻게 생각하는지 알고 싶어함. 그래서 많은 기업은 사용자의 의견을 받는 수단을 제공할 때가 많음. 아마존이나 Rotten Tomatoes 등에서 볼 수 있는 별점 평가 방법(star rating)처럼 고객이 어떤 제품이나 서비스에 관해 느끼는 바를 수치 자료의 형태로 수집하는 방법도 있음. 그러나 좀 더 자연스러운 방법은 사용자가 자신의 언어로 느낌을 말하게 하는 것. 사용자에게 빈 종이(빈 텍스트 입력란)를 주고 제품에 관한 의견을 적으라고 요청하면 좀 더 상세한 피드백을 획득 가능.
- 예전에는 담당자(사람)가 사용자 의견을 모두 직접 읽어야 했음. 자연어 텍스트에 담긴 감정과 정서를 이해할 수 있는 것은 사람뿐이라는 생각 때문.
- 그러나 한 사람이 수천 개의 평가를 읽다보면 지루해져서 실수를 저지르기 쉬움. 사람은 피드백을 읽는 데 아주 서투름, 특히 비판이나 부정적 의견을 잘 처리하지 못함. 그리고 대체로, 담당자의 인간적인 방어막과 필터를 통과할 정도로 능숙하게 의견을 전달하는 고객은 그리 많지 않음.