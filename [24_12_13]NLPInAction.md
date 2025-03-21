# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 4. 주성분 분석(PCA)
#### 5. 스팸 분류에 대한 LSA의 정확도
- 고윳값(벡터의 비례 또는 길이)들을 무시하는 것은 주제 벡터 공간을 경계 짓는 초입방체(hypercube)를 "바로 세우는 (square up)"것에 해당. 그러면 모형은 모든 주제를 동일한 정도로 중요하게 처리. 
- 이 기법을 SVD 구현에 사용하고 싶다면 SVD 또는 절단된 SVD를 계산하기 전에 모든 TF-IDF 벡터를 $L^2-노름$으로 정규화하면 됨. scikit-learn의 PCA 구현은 자료를 '중심화','백화'함으로써 이러한 정규화를 수행
- 이런 정규화를 적용하지 않으면, 자주 언급되지 않은 주제들이 실제보다 약간 더 큰 가중치를 받게 됨. '스팸성'은 전체 메시지의 13%만 언급하는 드문 주제, 스팸성에 해당하는 개별 주제들은 이 정규화(고윳값 무시)에 의해 더 큰 가중치를 받음. 결과적으로 해당 주제들은 스팸성같은 미묘한 특성들과 좀 더 강하게 연관
  - 의미 분석을 위한 알고리즘은 LSA,PCA,SVD,절단된SVD,LDiA 등으로 다양. 어떤 알고리즘의 어떤 구현을 사용하든 중요한 것은 먼저 BOW 벡터나 TF-IDF 벡터들을 정규화해야 함. 그렇게 하지 않으면 주제들의 비례계수 차이가 커짐. 주제들의 비례꼐수 차이가 크면 모형이 미묘하고 드문 주제들을 구별하는 능력이 감소. 
##### LSA와 SVD의 개선
- 의미 분석과 차원 축소에 특잇값 분해가 유용하다는 점이 밝혀지면서 연구자들은 특잇값 분해 알고리즘을 더욱 확장하고 개선. 그런 개선안들은 대부분 비 NLP 문제를 위한 것, 하지만 다른 문헌들에서 그런 개선안들을 마주칠수도 있으므로 간단 언급. 다음 세 개선안은 추천시스템에서 NLP 내용 기반 추천 엔진과 함께 쓰이는 행동 기반 추천 엔진에 종종 쓰임. 그리고 NLP의 품사 통계 분석에도 쓰인 바 있음.
- 사실 그 어떤 행렬 인수분해 기법이나 차원 축소 기법이라도 자연어의 용어 빈도들에 적용하는 것이 가능, 따라서 언젠가 의미 분석 파이프라인에서 이 개선안들의 좋은 용도를 찾을 수 있음. 소개 개선안은 다음과 같음.
  - 이차 판별 분석(quadratic dicsriminant analysis,QDA)
  - 무작위 투영(random projection)
  - 비음수 행렬 인수분해(nonnegative matrix factorization, NMF 또는 음수 미포함 행렬 분해)
- QDA는 LDA의 한 대안. QDA는 선형(일차)변환이 아니라 이차 다항식 변환 행렬을 산출. 이 변환 행렬이 정의하는 벡터 공간을 이용, 벡터들을 여러 분류로 분해. LDA와는 달리 QDA의벡터 공간에서 부류들을 가르는 경계는 사발이나 반구, 하프 파이프같은 이차 곡면
- 무작위 투영은 SVD와 비슷한 행렬 분해 및 변환 접근 방식, 알고리즘이 확률적(비결정론적)이기 때문에 실행할 때마다 다른 해답이 나옴. 그렇지만 이런 확률적 성격 덕분에 알고리즘을 여러 대의 컴퓨터에서 병렬로 수행하기가 쉬움. 그리고 이 알고리즘을 여러 번 실행하면 SVD의(그리고 LSA의 )결과보다 나은 결과가 나오기도 함. 그러나 NLP 문제에는 무작위 투영이 거의 쓰이지 않으며, 널리 쓰이는 구현(NLP의 Spacy나 NLTK 패키지 같은)도 없음. 만일 이 기법을 NLP에 적용하고 싶다면, 꽤 많은 코드를 직접 구현해야함.
- 대부분의 경우에는 이런 개선안들보다는 효과가 이미 검증된 SVD 알고리즘에 기초한 LSA를 사용하는 것이 나음.