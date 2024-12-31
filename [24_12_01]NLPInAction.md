# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 4. 주성분 분석(PCA)
- 시각화 예제는 10,000차원 이상의 문서-단어 벡터들이 아니라 3차원의 자료점들을 사용. 10,000차원보다는 3차원이 시각화하기 훨씬 쉬움. 파이썬의 경우 Matplotlin의 Axes3D 클래스를 이용 시, 3차원 자료점들을 보기 좋은 그래프로 손쉽게 표현 가능.
- NLPIA 패키지의 소스 코드(http://github.com/totalgood/nlpia)를 보면 다음 그림과 같은 회전 가능한 3차원 그래프를 생성하는 방법을 학습 가능.
- 다음 그림에 표시된 3차원 산점도 또는 '점 구름(point cloud)'은 이전의 그래프들처럼 BOW 벡터들의 화살표 머리를 표시한 것이 아니라 어떤 실제 물체의 표면을 3차원으로 스캔해서 얻은 자료점들을 표시. 자료의 성격이 전혀 달라도, 예제는 LSA의 작동 방식을 이해하는 데 도움. 예제를 통해 문서-단어 벡터같은 고차원 벡터를 다루기 전에 먼저 저차원 벡터들을 조작하고 표시해보는 방법 학습 가능.
- 3차원 점들이 어떤 물체를 스캔한 것인지 짐작이 가지 않음. 2차원으로만 표시된 그림과 달리, 프로그램에서 3차원 그래프를 이리저리 회전해 보면 원래의 물체를 추측 가능. 또한 ,그래프의 자료점들을 이리저리 회전해 보면 물체의 점들이 x,y,z축들에 좀 더 잘 정렬되는 방향을 탐색 가능. 3차원 점들을 회전함에 따라 x,y,z축 방향으로의 분산이 어떻게 변하는 지도 생각해보길 바람.
- ![alt text](image-7.png)