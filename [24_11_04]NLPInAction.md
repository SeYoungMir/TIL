# 1.NLP 기초.
## 3. TF-IDF 벡터
### 4. 주제 모형화
#### 4. 여러 TF-IDF 정규화 방법
- 용어- 문서 행렬로서의 TF-IDF 행렬은 수십년 간 정보 조회(검색)의 주춧돌. 그래서 연구자들과 기업들은 검색 결과의 관련성(적합성)을 개선하기 위해 IDF 부분을 최적화 하는 데 많은 시간 투자.
- 다음은 용어 빈도 가중치들을 정규화하고 평활화하는 여러 방법
  - 정규화 없음
  - TF-IDF
  - TF-ICF
  - Okapi BM 25
  - ATC
  - LTU
  - MI
  - PosMI
  - T-Test
  - 카이제곱
  - Lin98a
  - Lin98b
  - Gref94
- 검색 엔진(정보 검색 시스템)은 질의문의 키워드(용어)들로 말뭉치의 문서들을 검색. 사용자가 찾고자 했을 가능성이 큰 문서들을 잘 찾아내는 검색 엔진을 구현하기 위해 위의 여러 정규화 접근 방식을 시험해 볼 필요 있음.
- 검색 결과의 순위를 매길 때 보통의 TF-IDF 코사인 유사도 대신 사용하면 좋을 대안으로는 Okapi BM25 또는 그것의 최신 변형인 BM25F가 있음.