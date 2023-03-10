## 머신러닝의 개요
### 머신러닝과 인공지능의 차이점
- 머신러닝은 데이터로부터 학습하여 지식을 획득
- 인공지능은 지식을 획득한 후, 그것을 활용함
<table>
    <tr>
        <th></th><th>머신러닝</th><th>인공지능</th>
    </tr>
    <tr>
        <td>주요 활동</td><td>학습을 통한 지식의 획득</td><td>지식의 획득과 활용</td>
    </tr>
    <tr>
        <td>구현과 실현</td><td>데이터로부터의 학습 실현</td><td>복잡한 문제 해결을 위한 지능의 구현</td>
    </tr>
    <tr>
        <td>개발 목표</td><td>스스로 학습하는 알고리즘 개발</td><td>인간을 닮은 지능적인 시스템의 개발</td>
    </tr>
</table>

### 머신러닝 과정에서의 고려 사항
- 머신러닝 구상과정에서의 고려 사항들
  - 주어진 데이터로부터 원하는 답을 찾을 수 있을까?
  - 문제 해결을 위해 데이터가 충분한가?
  - 어떤 머신러닝 기법을 적용하면 좋을까?
  - 추출할 데이터의 특성은 무엇인가?
  - 머신러닝의 결론은 무엇으로 설정할 것인가?
  - 생성된 출력을 실제 응용에 어떻게 사용할 것인가?


### 머신러닝의 주요 종류들
- 신경망(Neural Network):
  - 생물의 신경 네트워크 구조와 기능을 모방한 모델
- 클러스터링(Clustering):
  - 주어진 데이터를 클러스터라는 부분 집합들로 분리하는 것
- 분류(Classification):
  - 주어진 데이터를 비슷한 것들끼리 분류하는 것
- 의사결정 트리(Decision Tree):
  - 트리 구조 형태의 예측 모델로 의사를 결정하는 모델
- 나이브 베이즈(Naive Bayes):
  - 베이즈 정리를 바탕으로 한 조건부 확률 모델 분류
### 머신러닝의 활용 분야
<table>
    <tr>
        <th>활용분야</th><th>응용</th>
    </tr>
    <tr>
        <td>영상인식</td><td>문자인식, 물체인식</td>
    </tr>
    <tr>
        <td>얼굴인식</td><td>Facebook에서의 얼굴 인식</td>
    </tr>
    <tr>
        <td>음성인식</td><td>Bixby,Siri,Alexa등</td>
    </tr>
    <tr>
        <td>자연어 처리</td><td>자동 번역, 대화 분석</td>
    </tr>
    <tr>
        <td>정보 검색</td><td>스팸 메일 필터링</td>
    </tr>
    <tr>
        <td>검색 엔진</td><td>개인 맞춤식 추천 시스템</td>
    </tr>
    <tr>
        <td>로보틱스</td><td>자율주행 자동차, 경로 탐색</td>
    </tr>
</table>

- 머신러닝은 여러 산업 분야에 다양하게 활용 가능
- 최근 딥러닝이 물체의 인식 등에 획기적으로 성공함
- 미국에서는 머신러닝 기술로 빅데이터를 분석하는 ‘데이터과학자(datascientist)’의 수요가 급증
- 자율주행 자동차, 문자인식 등과 같이 알고리즘 개발이 어려운 문제 해결에 활용되고 있음

### 머신러닝의 개인비서(personal assistant)
- 머신러닝은 스마트폰의 개인 비서에 활용됨
- 음성인식, 언어 습관, 행동 패턴 등을 학습
- 머신러닝 기법을 이용한 지능적인 역할 담당
- 삼성의 Bixby, 애플의 Siri, 구글의 Assistant 등

### 머신러닝의 SNS에의 활용
- 머신러닝은 SNS에도 상당히 중요한 역할
- 여러 번 검색해본 책, 영화 등의 습관을 학습
- 적절한 시각에 알려주거나 광고를 보내기도 함
- 페이스북에서는 출신학교나 친구들의 관계를 적용
- 머신러닝이 새로운 친구 제안

### 머신러닝의 동영상에의 활용
- 유튜브(YouTube)에 ‘내 관련 재생 목록’으로 응용됨
- 즐겨 찾던 동영상 리스트가 추천 리스트로 올라옴

### 머신러닝의 기상 예측 등에의 활용
- 데이터와 통계적 도구를 결합하여 결과를 예측
- 결과물은 기상 예측 등에 유용하게 활용됨
- 그 외 사기 탐지, 작업 자동화 등에도 활용

### 머신러닝에서의 학습 방법
- 학습의 형태에 따라 3가지 학습 방법
- 지도 학습, 비지도 학습, 강화 학습으로 구분
- 지도 학습
  - 분류, 회귀
- 비지도 학습
  - 클러스터링, 차원 축소
- 강화 학습
- 지도 학습(supervised learning)
  - 입력과 미리 알려진 출력을 연관시키는 관계를 학습
  - 주어진 입력과 출력 쌍 사이의 대응 관계를 학습
  - 자동차 번호판이 오염된 경우 인식하지 못할 수도 있음
  - 그러나 오염된 번호판 사례들을 학습시켜 인식률을 높임
- 비지도 학습(unsupervised learning)
  - 출력값을 알려주지 않고 스스로 모델을 구축하여 학습
  - 비지도 학습은 입력만 있고 출력 즉 레이블(label)이 없음
  - 규칙성을 스스로 찾아내는 것이 학습의 주요 목표
  - 결과는 지도 학습의 입력으로 사용 가능
  - 전문가에 의해 해석되어 다른 용도로 활용됨
  - 데이터 마이닝(data mining) 기법은 비지도 학습의 예
- 강화 학습(reinforcement learning)
  - 주어진 입력에 대응하는 행동에 대해 보상(reward)
  - 이러한 보상을 이용하여 학습하는 방법
  - 주어진 입력에 대한 출력, 즉 정답 행동이 주어지지 않음
  - 주요 응용 분야로는 로봇, 게임, 내비게이션 등

- 지도학습
  - 주어진 입력과 정해진 출력 간의 관계를 학습
  - 각 데이터에 레이블(label) 또는 태그(tag) 표시 붙임
  - 데이터에 ‘P’(pass) 또는 ‘F’(fail)라는 레이블 활용
  - 예를 들어 ‘이들은 사과’라는 레이블로 학습한 후, 새로운 사과 하나를 제시하면 그것을 ‘사과’라고 예측하는 방법
- 지도학습의 장단점
  - 장점
    - 이전의 경험으로부터 데이터 출력을 생성
    - 경험을 사용하여 성능 기준을 최적화
    - 다양한 유형의 문제 해결에 도움이 됨
  - 단점
    - 출력에 반드시 레이블이 있는 데이터들을 사용해야 함
    - 일반적으로 많은 시간이 걸림
    - 빅데이터의 경우 엄청난 시간이 걸릴 수도 있음
- 지도학습에서의 분류와 회귀
- 지도 학습은 분류와 회귀로 나누어짐
- 분류(classification)
  - 유사한 특성을 가진 데이터들끼리 묶어서 나누는 것
  - 2개로 분류하는 이항 분류, 그 이상의 다항 분류
  - 이항 분류는 합격/불합격, 스팸 메일/정상 메일 등 분류 방법
  - 0에서 9까지의 아라비아 숫자 인식은 다항 분류
  - 일상생활에서 수많은 패턴들을 분류
  - 일반 버스/마을 버스/광역 버스 등의 구별
  - 많은 남자와 여자 사진을 레이블을 붙여놓고 학습
  - 학습 후 새로운 사진에 대해 남자/여자 분류
  - 사진으로 남자와 여자의 구별
  - 개와 고양이의 구분
  - 스팸 메일과 정상 메일 구분
  - 0에서 9까지의 숫자의 구분
  - 알파벳과 한글 문자 등의 구분
  - 편지봉투의 손으로 쓴 주소 판별
  - 카드 부정 사용 감지
  - 의료 영상에서 종양의 존재 여부 판단
- 회귀(regression)
  - 회귀란 변수들 사이의 관계를 결정하는 통계적 측정
  - 하나의 독립 변수를 사용하는 직선 형태의 ‘선형 회귀’
  - 선형 회귀는 각 점에서 회귀 직선까지의 y축 방향의 거리 제곱의 총합을 최소로 해서 얻어지는 직선
  - 직선 y＝a＋bx를 x에 대한 y의 회귀 직선이라 함
- 회귀 분석(regression analysis)
  - 변수 사이의 회귀에 대해 검정이나 추정을 하는 것
  - 회귀 분석은 학습 데이터를 사용하여 출력값 예측
  - 산출물은 항상 확률론적 의미를 내포
- 회귀와 회귀 분석의 예측에의 활용
  - 날씨에 대한 예측
  - 월별 판매액을 보고 다음 달 판매액 예측
  - 금융, 투자, 비즈니스적 가격 판단
  - 금값이나 원유 가격 예측
  - 주택 가격의 예측
  - 장단기 주가 예측
  - 원유 가격 추정 등
- 분류와 회귀의 차이점
  - 분류는 일정한 기준에 따라 명백하게 구분 짓는 것
  - 회귀는 오차 제곱의 합을 최소화하는 직선을 긋는 작업 
  - 명확히 직선으로 구별되는 것이 아님
- 분류와 회귀의 차이 구분
  - 분류의 출력은 남자/여자 등과 같은 선택식 출력
  - “내일 날씨는 더울 것이다.”와 같은 이분법적 선택
  - 회귀의 출력은 연속값으로 나타냄
  - “내일 기온?”에 대해 “18.3도로 추정된다.” 등의 형태
- 분류의 방법
  - 몇 가지 유형의 주요 분류 방법
  - Naive Bayes 분류기
  - 의사결정 트리
  - SVM
  - K-Nearest Neighbor(K-NN) 등  

- Naive Bayes 분류기
  - 나이브 베이즈 분류기는 머신러닝의 한 분야
  - 자료의 분류를 베이즈 정리를 활용하여 판단
  - 나이브 베이즈 분류기는 조건부 확률 모델
  - 모든 특성값은 서로 독립이라고 가정
- 나이브 베이즈 분류의 장점
  - 구축하기 쉽고, 대규모 데이터 세트에 유용함
  - 지도 학습 환경에서 효율적으로 훈련될 수 있음
  - 복잡한 실제 상황에서 비교적 잘 작동
  - 주가의 상승이나 하락이 예상되는 종목들을 분류
  - 문서의 내용에 따라 문서 분류 가능
  - 이메일 내용에 따라 스팸/정상 메일로 분류
- 의사결정 트리(Decision Tree)
  - 관측값과 목표값을 연결하는 예측 모델
  - 최대 2가지의 판단을 하는 이진 트리 사용
  - ‘스무고개’ 문답처럼 선택 방법으로 진행
  - 주택이나 자동차 구입비용 등의 추정에 활용
  - 타이타닉호 탑승객의 생존 여부를 나타내는 결정 트리
- SVM(Support Vector Machine : SVM)
  - 1990년에 개발, 통계 학습 이론의 결과 기반
  - 데이터를 2개의 영역으로 분류하는 이진 분류기
  - 새로운 데이터가 어느 영역에 속하는지를 판단
  - 가장 큰 폭을 가진 하나의 경계선을 찾는 알고리즘
  - 영역의 여백(margin, gap)이 최대가 되는 중심선 찾기
- SVM 분류의 활용
  - SVM은 패턴인식과 자료 분석을 위한 지도 학습 모델임
  - 분류, 회귀 분석, 멀티미디어 정보 검색 등에 사용
  - 두 영역 사이의 여백을 최대로 하는 직선으로 분류
  - SVM으로 개와 고양이의 특성을 분류에 활용하는 예
- K-Nearest Neighbor(K-NN)
  - 1950년대에 개발된 지도 학습 모델의 분류 기법
  - 간단한 분류 기법, ‘최근접 이웃 분류’라고도 불림
  - 가장 가까운 것들과의 거리 계산으로 클래스를 분류
  - 새로운 입력 데이터와 가장 가까운 k개의 이웃 데이터 선택
  - 이웃 데이터들의 클래스 중 다수결로 데이터의 클래스 결정
  - 다수결에서 결과가 나오기 위해 k는 반드시 홀수여야 함
- K-NN의 장단점과 활용 분야
  - 장점은 매우 간단하며 빠르고 효과적인 알고리즘
    - 어떤 데이터라도 유사성 측정 가능
  - 단점으로는 적절한 k를 선택해야 한다는 점
    - 새로운 데이터에 대해 일일이 거리를 계산한 후 분류
- K-NN의 활용 분야
  - 영화나 음악 추천에 대한 개인별 선호 예측
  - 수표에 적힌 광학 숫자와 글자인식
  - 얼굴인식과 같은 컴퓨터 비전
  - 유방암 등 질병의 진단과 유전자 데이터 인식
  - 재정적인 위험성의 파악과 관리, 주식 시장 예측
- K-NN의 꽃잎 분류에의 적용 예
  - 꽃잎의 크기와 밝기에 따른 K-NN 분류
  - 오른쪽 위에 새로운 꽃잎이 입력으로 들어왔을 때
    - 빨간 화살표의 3가지를 비교한 후 분류하는 것을 보여줌
- 클러스터(cluster)와 클러스터링(clustering)
  - 클러스터는 유사한 여러 개의 클래스로 나누어진 데이터
  - 클러스터링은 유사한 특성을 가진 그룹들로 묶는 작업
  - 같은 클러스터의 것은 다른 클러스터의 것보다 더 유사
  - 이와 같은 유사한 것들끼리의 집합이 바로 클러스터
- 클러스터의 분류 예
  - 원래 데이터를 3개의 클러스터로 분류해 놓은 예
  - 빨간색, 파란색, 녹색
- 분류와 클러스터링의 차이점
  - 분류는 지도 학습 영역, 클러스터링은 비지도 학습 영역
  - 분류는 데이터를 기준에 따라 직선으로 분류하는 것
  - 클러스터링은 유사성에 따라 몇 개의 클러스터들로 묶는 것
  - 급여, 나이, 위험도 상관관계의 예에서의 차이점의 예
- 비지도 학습
  - 주어진 입력에 대응하는 출력 정보 없이 학습
  - 데이터 분류에 대한 정보가 전혀 없이 패턴을 찾거나 데이터를 분류하려고 할 때 사용하는 학습 방법
  - 데이터에 레이블을 전혀 사용하지 않음
  - 관계를 스스로 학습한 후, 과일들을 각 그룹으로 알아서 묶기
- 비지도 학습의 주요 응용 분야
  - 비슷한 성향의 고객을 그룹으로 묶기
  - 블로그에서 주제별로 구분하기
  - 유사한 꽃이나 동물들끼리 묶기
  - 네트워크상에서의 비정상적인 접근의 탐지
- 비지도 학습을 통한 클러스터링과 추천 시스템
  - 머신러닝에서의 주요 비지도 학습 방법
    - K-means 클러스터링
    - 가우스 혼합 모델
    - 계층적 클러스터링
    - 추천 시스템 등
- K-means 클러스터링
  - 비지도 학습 알고리즘 중 대표적인 클러스터링 방법
  - 우리말로 ‘K-평균 군집화’라고 함
  - 간단하면서도 많이 쓰이는 클러스터링 방법 중 하나
  - 유사한 특성을 가진 k개의 데이터 그룹으로 묶는 방법
  - 예로 주어진 데이터 집합에서 3개와 4개의 클러스터들
- 클러스터와 클러스터 중심점(centroid)
  - 주어진 데이터 집합에 대해 k개의 클러스터 중심점 찾기
  - 각 클러스터에는 클러스터 중심이 있음
  - 각 점은 다른 중심점보다 지정된 클러스터 중심점에 더 가까움
  - 4개의 클러스터로 구성된 2가지 예
  - 별표는 각 클러스터의 중심점을 나타냄
- K-means 클러스터링 알고리즘 작동의 예
  - K-means 클러스터링 알고리즘을 작동시킨 예
    - 왼쪽은 원래의 데이터
    - 오른쪽은 k = 2인 K-means 알고리즘을 작동시킨 결과
    - 빨갛고 녹색인 사각형은 각 클러스터의 중심점
- K-means 클러스터링의 장단점
  - 장점은 알고리즘이 비교적 간단하고, 수행 속도가 빠르다는 점
    - 주어진 데이터에 대한 사전 정보 없이 클러스터링을 함
    - 데이터를 분류하는 머신러닝과 데이터 마이닝의 도구
  - 단점은 클러스터링의 개수 k와 최초로 지정하는 중심점들에 따라 결과가 다소 달라질 수 있는 점
- K-means 클러스터링의 활용 분야
  - 통계 : 주어진 데이터의 분류나 성향 분석
  - 전자상거래 : 고객의 구매 이력으로 고객 분류
  - 건강 관리 : 질병과 치료를 위한 패턴 탐지
  - 패턴 : 유사한 이미지를 그룹화
  - 재무 : 신용카드 사기 탐지
  - 회사 : 매출 등을 토대로     회사의 등급 분류
  - 기술 : 네트워크 침입과 악의적 활동 탐지
  - 기상 예보 : 폭풍 예측
- 추천 시스템(Recommender System)
  - 추천을 위해 연관 데이터 정의에 도움 주는 클러스터링 방법
  - 사용자의 ‘선호도’를 예측하는 정보 필터링의 일종
  - 네이버나 구글 등에서 상업적으로 활용 중
  - 현재 검색해본 책이나 동영상 등의 추천
  - 또 인기 있는 식당, 연구 관련 기사, 금융 서비스 등 추천
  - 교보문고에서 책을 검색하면 그 사람이 이전에 검색했던 도서나 관련 도서를 알려줌
  - 사용자의 검색 경험 정보 파악, 적절한 광고 내보내기
  - 그 외 비지도 학습 방법에는 가우스 혼합 모델, 계층적 클러스터링, PCA/T-SNE 등이 있음
- 지도 학습과 비지도 학습의 특징 비교
<table>
    <tr>
        <th>기반</th><th>지도학습</th><th>비지도학습</th>
    <tr>
        <td>입력 데이터</td><td>입력과 출력(값 또는 레이블)이 지정된 데이터를 사용하여 학습함</td><td>출력값이나 레이블이 전혀 없는 데이터를 사용하여 학습함</td>
    </tr>
    <tr>
        <td>주요 기능</td><td>분류, 회귀</td><td>클러스터링, 추천시스템</td>
    </tr>
    <tr>
        <td>계산의 복잡성</td><td>비교적 간단함</td><td>상당히 복잡함</td>
    </tr>
    <tr>
        <td>정확성</td><td>매우 정확함</td><td>다소 덜 정확함</td>
    </tr>
</table>

### 강화학습
- 강화 학습이란?
  - 강화 학습은 시행착오를 통해 보상하는 행동 학습
  - 최적의 값을 추구하기 위해 당근과 채찍을 사용
  - 로봇이 미로에서 옳은 방향으로 진입하면 +2점, 막힌 길로 들어가면 -3점 등
  - 입출력이 쌍으로 된 훈련 집합으로 제시되지 않는다는 점에서 일반적인 지도 학습과는 다름
- 강화 학습의 응용 분야
  - 보상(reward)이 주어지는 문제 해결에 매우 효과적
  - 통신망, 로봇 제어, 엘리베이터 제어, 그리고 체스와 바둑 같은 게임에
주로 응용됨
  - 알파고도 강화 학습을 통해 실력 향상
  - 최근 게임에서는 거의 필수적으로 강화 학습이 사용됨
### 베이지안 네트워크와 은닉 마르코프 모델
- 베이지안 네트워크(Bayesian network)
  - ‘빌리프 네트워크(Belief network)’라고도 불림
  - 집합을 조건부 독립으로 표현하는 확률의 그래픽 모델
  - 추론과 학습을 수행하기 위한 효과적인 알고리즘이 존재
  - 예를 들어, 질환과 증상 사이의 확률 관계를 나타낼 수 있음
  - 증상이 주어지면 다양한 질병의 존재 확률 계산 가능
- 은닉 마르코프 모델(Hidden Markov Model, HMM)
  - HMM은 마르코프(Markov) 모델의 일종
  - 은닉된 상태와 관찰 가능한 결과로 이루어진 확률형 모델
  - 동적 베이지안 네트워크로 간단히 나타낼 수 있음
  - 대량의 데이터를 통계적으로 분석하여 추론에 응용
  - 음성인식, 자연어 처리 등에 활용