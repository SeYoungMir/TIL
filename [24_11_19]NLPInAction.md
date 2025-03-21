# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 2. 잠재 의미 분석(LSA)
- 잠재 의미 분석은 가장 오래되고 가장 널리 쓰이는 차원 축소 기법인 SVD(singular value decomposition; 특잇값 분해)에 기초한 알고리즘. SVD는 '기계 학습'이라는 용어가 등장하기 훨씬 오래 전부터 널리 쓰임. SVD는 주어진 행렬을 세 개의 정방행렬로 분해. 세 정방행렬 중 하나는 대각 행렬.
- SVD의 한 용도는 행렬의 역을 구하는 것. 하나의 행렬을 그보다 더 간단한 세 정방행렬로 분해해서 전치, 다시 곱하면 역행렬이 나옴. 세상에는 역행렬이 필요한 알고리즘이 많으므로, 크고 복잡한 행렬의 역행렬을 비교적 간단하게 계산하는 알고리즘이 대단히 유용할 수 있음.
- SVD는 트러스 구조의 응력과 변형도를 분석하는 등의 여러 건축, 기계 공학 문제에 유용. 전기 공학의 회로 분석에도 유용. 내용 기반 NLP 추천 엔진과 함께 실행되는 행동 기반 추천 엔진을 위한 데이터 과학에도 SVD가 사용.
- LSA는 SVD를 이용해서 TF-IDF 용어- 문서 행렬을 더 간단한 세 행렬로 분해. 세 행렬을 곱하면 다시 원래의 행렬. 이는 큰 정수의 소인수 분해와 비슷. 행렬을 분해해서 그대로 복원하는 것은 별 의미가 없음 . TF-IDF 행렬을 SVD를 통해서 더 간단한 세 행렬로 분해 시 원래의 TF-IDF 행렬에 관한 유용한 정보를 얻을 수 있으며, 이를 이용해서 세 행렬을 절단(truncate;특정 행들과 열들을 제거)한 후 다시 결합함으로써 문서를 표현하는 벡터 공간의 차원을 줄일 수 있음. 
- 그러한 축소된 행렬들을 곱한 결과는 원래의 TF-IDF 행렬과 같지 않음. 그러나 원래의 행렬보다 문서를 더 잘 표현. 새 문서 표현 행렬은 문서의 본질 또는 '잠재 의미(latent semantic)'을 담고 있음. 이러한 '정수'파악 능력 덕분에 SVD는 압축 같은 다른 분야들에서도 사용. 자료를 압축한다는 것은 자료에서 잡음을 제거하고 그 본질만 남기는 것이라 할 수 있음.
- 예를 들어 비트맵 이미지를 JPEG형식으로 압축하면 크기가 10분의 1 정도로 감소, 그래도 원본 이미지의 거의 모든 정보가 남아 있음.
- SVD를 자연어 텍스트에 적용, 텍스트의 본질을 뽑아 내는 것이 이번 절의 잠재 의미 분석(LSA), LSA는 숨겨진, 그리고 발견되길 기다리는 단어들의 의미를 드러냄.