# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 4. 주성분 분석(PCA)
#### 3. PCA를 이용한 문자 메시지 잠재 분석.
- 할인 상품 광고나 불법 제품 광고 같은 거래(deal) 관련 스팸에 나올 만한 단어들("half","off"등등)의 점수가 높은 주제들을 탐색
- ```python
  pd.options.display.max_columns=12
  deals = weights['!;):) half off free crazy deal noly $ 80%'.split()].round(3)*100
  deals
  ```
- 주제 4,8,9는 거래 관련 단어들에 대한 점수의 합이 비교적 큰 양수이므로 거래를 뜻하는 주제일 가능성이 있음. 반면 0,3,5는 해당 점수 합이 비교적 큰 음수이므로 아마도 거래와는 상반된 주제. 주제 4,8,9의 점수가 비슷하기 때문에 딱 하나를 거래를 대표하는 주제라고 부르기는 어려움.
  - 토큰화 함수 casual_tokenize는 "80%"를 ["80","%"]로, 
"\$80million"을 ["$","80","million"]으로 분리. 따라서 LSA나 2-그램 토큰화를 사용하지 않는 한, NLP 파이프라인은 그냥 "80"이라는 토큰을 공유, 무관한 단어 조합들인 둘을 구분하지 못함.
- 이처럼 주제의 의미를 파악하는 것이 LSA의 어려운 점 중 하나. LSA는 단어들 사이의 일차 관계만 허용. 그리고 현실적으로 말뭉치가 그리 크지 않을 때가 많기 때문에, 사람이 의미를 파악하기 어려운 단어 조합들도 많이 나옴. PCA는 그냥 9,232개의 단어 빈도들의 분산이 가장 커지는 조합을 찾을 뿐이며, 따라서 사람이 보기에는 전혀 다른 여러 주제의 여러 단어가 하나의 차원(주성분)으로 합쳐지는 일이 발생.