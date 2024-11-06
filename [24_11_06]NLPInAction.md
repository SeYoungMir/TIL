# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
- 이번 챕터에서 기계인 컴퓨터가 자연어 텍스트의 '뜻(의미)'를 이해하게 만들 것.
- 이전 챕터에서 배운 TF-IDF(용어 빈도와 역문서 빈도의 곱)벡터는 주어진 단어들이 특정 문서에서 얼마나 중요한지 추정하는 데 도움이 됨. 이전 챕터에서 우리는 TF-IDF 벡터들로 이루어진 하나의 행렬을 이용해 각 단어가 전체 말뭉치 중 한 문서에서 얼마나 의미가 있는지 파악하는 방법 탐색.
- 이러한 TF-IDF '중요도'점수들은 개별 단어 뿐만 아니라 짧은 단어열, 즉 n-그램에도 적용. n-그램에 대한 이런 중요도 점수는 특정 단어들로 이루어진 정확한 문구로 문서를 검색할 때 유용.
- 예전 NLP 연구자들이 단어 조합의 의미를 드러내고 그러한 의미를 표현하는 벡터를 계산하는 알고리즘 하나를 고안. 잠재 의미 분석(latent semantic analysis,LSA)이 바로 그것. 이 도구를 이용하면 단어들의 뜻을 벡터 형태로 표현 가능, 문서 전체의 뜻도 표현 가능.
- 이번 챕터에서는 의미론적 벡터(semantic vector; 의미 벡터)라고도 하는 주제 벡터(topic vector)를 공부. 주제 벡터는 TF-IDF벡터의 가중 빈도들을 이용해서 구한 주제 '점수'들을 성분으로 하는 다차원 벡터. 이 점수들을 계산할 때는 정규화된 용어 빈도들 사이의 상관관계를 이용해 같은 주제의 단어들을 한데 묶음.
- 이 주제 벡터들은 용도가 다양. 특히 의미에 기초해서 문서를 검색하는 의미 기반 검색에 사용.
- 대부분의 경우 의미 기반 검색의 결과가 키워드 검색(TF-IDF 검색)의 결과보다 훨씬 나음. 종종 의미 기반 검색은 딱 맞는 단어들로 질의문을 구성하지 않는 경우에도 검색자가 찾고자 했던 바로 그 문서 반환
- 의미 벡터(주제 벡터)를 이용하면 주어진 문장이ㅏ 문서, 또는 말뭉치(문서 모음)의 주제를 가장 잘 나타내는 단어들과 n-그램들을 식별 가능. 그리고 그런 단어들의 벡터와 상대적 중요도를 이용해 주어진 문서에 대해 가장 의미있는 단어들, 즉 문서의 의미를 가장 잘 요약하는 일단의 핵심어(키워드)들을 탐색 가능.
- 마지막으로 두 문서(또는 문장, 말뭉치)의 핵심어들을 비교, 두 문서의 의미가 얼마나 가까운지 추정 가능.
- 단어들의 일차 결합(선형 결합)을 성분으로 하는 주제 벡터가 문서의 의미를 상당히 잘 표현한다는 점을 학습.