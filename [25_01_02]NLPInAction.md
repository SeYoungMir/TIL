# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 8. 주제 벡터의 위력
- 예시로, 구글 지도(Google Maps)에서 위도와 경도로 어떤 위치를 찾는 것은 어렵지 않음. 위도와 경도는 하나의 21차원 벡터에 해당. 에를 들어 위도와 경도로 주어진 한 지점과 가장 가까운 커피숍을 찾으려면, 그냥 그 지점에서 시작해서 점차 범위를 넓혀 가면서 커피숍을 찾으면 됨. 이를 프로그램으로 구현하는 것도 가능함. 그냥 주어진 지점을 중심으로 정사각형 형태의 경계 상자(bounding box)를 생성, 그 경계 상자의 크기를 점점 키우면서 그 정사각형 안에 속하는 특징점을 찾으면 됨. 그러나 초평면들과 초입방체들이 존재하는 고차원 공간에서 그런 경계 상자를 상상하기란 쉽지 않음.
- 제프리 힌턴의 말 "14차원 공간의 초평면들을 다루는 방법은 그냥 3차원 공간을 시각화하고 그것이 14차원이라고 외치는 것이다" 애벗이 1884년 발표한 플랫랜드를 어린 시절에 읽은 사람이라면 고차원의 세계를 좀 더 잘 상상할 수도 있음. 어쩌면 3차원 세상에서 벗어나 한 차원 높은 세상에서 3차원 세상을 내려다보는 능력을 가진 사람도 있음 .플랫랜드처럼 고차원 공간의 단어들을 3차원 세계에 투영한 그림자를 다시 2차원 그래프로 시각화하면 고차원 공간을 이해하는 데 도움이 됨. 앞에서 나온 TF-IDF 벡터들의 3차원 산점도를 나타낸 그림이 그런 예. 그리고 3장의 3차원 단어 모음 벡터들이 나오는 예제로 돌아가 해당 어휘에 단어를 하나 더 추가해 4차원의 텍스트 의미 세계를 만든 후 그것을 시각화해봐도 ㄷ재미있을 것.
- 4차원이라는 것을 상상. 주목할 것은 3차원에서 단지 차원이 하나 더 늘어났을 뿐이어도, 2차원에서 3차원으로의 변화에 비해 복잡도가 지수적으로 커진다는 것. 마찬가지로 , 2차원에서 3차원으로의 변화는 1차원 세계(직선)에서 2차원 세계(평면 도형들의 세계)로의 변화에 비해 복잡도 증가가 지수적.