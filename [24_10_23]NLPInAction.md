# 1.NLP 기초.
## 3. TF-IDF 벡터
### 2. 벡터화
#### 1. 벡터 공간
- 그래프를  그리는 데 사용하는 모눈종이나 픽셀들이 격자 형태로 배치 된 디지털 이미지를 상상하면 2차원 벡터 공간을 이해하는 데 도움이 됨.
- 한 2차원 벡터의 x,y 좌표를 뒤집으면, 벡터 계산 과정을 뒤집지 않아도 선형대수 문제의 답이 뒤집힘.
- 모눈 종이와 이미지는 x축과 y축이 서로 수직인 직선적 유클리드 공간의 예. 그리고 이번 장에서 이야기하는 벡터들은 모두 직교좌표계 공간, 즉 공간의 모든 축이 직선이고 서로 직교하는 유클리드 공간에 존재.
- 지도나 지구본의 위도와 경도는 지도 위의 한 위치가 위도와 경도라는 두 성분으로 서술, 지도도 2차원 벡터 공간. 그러나 하나의 위도 경도 쌍은 지구의 울툴불퉁한 표면을 근사(approximation)한 구면의 한 위치를 표시. 즉 위도 경도 벡터 공간은 직교 좌표계가 아님. 2차원 위도 경도 벡터 공간 같은 비유클리드 공간에서는 두 점의 거리(유사도)를 계산하기가 좀 더 까다로움. 위도 경도 좌표를 이용, 서울과 뉴욕의 거리를 계산한다 가정.
- 2차원 벡터를 표현하는 한 방법은, 벡터의 머리(뾰족한 화살표 끝)는 벡터 공간에서 벡터가 나타내는 위치에 해당. 
- 그림에서 세 개의 벡터 머리들은 언급한 세 좌표쌍에 해당. 벡터의 꼬리는 항상 원점(0,0)
- 3차원 벡터공간으로는 우리가 사는 물리적인 3차원 세상의 위치나 속도를 좌표 성분 x,y,z로 이루어진 3차원 벡터로 표현. 또한, 지구 표면의 장소들을 곡면 공간의 위도-경도-고도 쌍으로 표현할 수 있는데, 이 역시 3차원 벡터.
- 필요하다면 차원을 더 확장 가능. 예를 들어 5차원 벡터나 10차원 벡터, 5000차원 벡터역시 가능.
- 차원이 어떻든 선형대수 벡터 연산들은 기본적으로 동일. 물론 차원이 높으면 계산에 시간이 더 걸림. 소위 '차원의 저주' 문제가 발생 가능하며, 이에 관한 자세한 논의는 뒤에서 살펴봄.
