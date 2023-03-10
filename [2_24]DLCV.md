### 컴퓨터 비전
- 현대는 양호한 프로그래밍 환경
  - 예전에는 알고리즘을 바닥부터 구현
  - 현대는 함수 호출로 영상 처리하는 시대. 대표적 컴퓨터 비전 라이브러리는 OpenCV
  - 파이썬 언어와 OpenCV 라이브러리로 컴퓨터 비전 시대를 시작
- 인텔이 만들어 공개한 OpenCV
  - $바퀴를 다시 발명_{reinventing the wheel}$하는 쓸데없는 노력을 방지할 목적
  - 인텔 칩의 성능을 평가할 목적
#### 개요와 간략한 역사
- 개요
  - 클래스와 함수는 C와 C++로 개발. 전체 코드는 180만 라인 이상
  - 인터페이스 언어는 C, C++, 자바, 자바스크립트, 파이썬
  - OS 플랫폼은 윈도우, 리눅스, macOS, 안드로이드, iOS
  - 교차 플랫폼 지원
  - 교육과 상업 목적 모두 무료
- 간략 역사

OpenCV의 역사
<table>
    <tr>
        <th>연도</th>
        <th>사건</th>
    </tr>
    <tr>
        <td>1998</td>
        <td>인텔 직원인 개리 브라드스키(Gary Bradski)가 아이디어 제안</td>
    </tr>
    <tr>
        <td>1999</td>
        <td>오픈 소스로 공개하기로 결정하고 이름을 OpenCV로 정함</td>
    </tr>
    <tr>
        <td>2000</td>
        <td>CVPR 컨퍼런스에서 알파 버전 발표</td>
    </tr>
    <tr>
        <td>2001-2005</td>
        <td>5개의 베타 버전 발표</td>
    </tr>
    <tr>
        <td>2005</td>
        <td>스탠퍼드 대학교의 자율 주행차인 스탠리의 개발 팀에 합류해 그랜드 챌린지 우승<br>OpenCV Korea 출범 (https://cafe.naver.com/opencv)</td>
    </tr>
</table>


#### 공식 사이트
- OpenCV를 지원하는 사이트
  - 공식 홈페이지(https://opencv.org)
  - 매뉴얼 사이트: 프로그래밍할 때 가장 많은 도움(https://docs.opencv.org)
  - 깃허브
  - 대한민국 OpenCV 사이트(https://cafe.naver.com/opencv)

#### OpenCV 매뉴얼 활용하기
- OpenCV-Python 튜토리얼을 잘 살필 것
- 함수 선언을 잘 살필 것
#### 객체지향 잘 활용하기
- 파이썬은 객체지향 언어
- 객체지향은 컴퓨터 비전 프로그래밍에 매우 유리
#### 객체 다루기
- 객체지향 특성과 강점
  - 객체는 능동적: 자신이 소유한 멤버 함수를 능동적으로 호출
  - 필요한 만큼 얼마든지 찍어낼 수 있음
#### 객체 확인하기 - type과 dir 내장 함수
- 객체의 클래스를 알려주는 type과 사용 가능한 멤버 함수를 알려주는 dir
- 함수가 하는 일을 알아내려면 help
#### 영상을 읽고 표시하기
- 처음 해보는 OpenCV 프로그래밍

#### OpenCV에서 영상은 numpy.ndarray 클래스 형의 객체
- numpy는 다차원 배열을 위한 사실상 표준 모듈
  - 이런 이유로 OpenCV는 영상을 numpy.ndarray로 표현
  - OpenCV가 다루는 영상은 numpy가 제공하는 다양한 기능(함수)을 사용할 수 있음
- 영상의 표현
  - 화소의 위치 (r,c) 또는 (y,x)
  - 화솟값 조사
```python
print(img[0,0,0],img[0,0,1],img[0,0,2]) # (0,0) 화소 조사
print(img[0,0,0],img[0,0,1],img[0,0,2]) # (0,1) 화소 조사
```
#### 영상 형태 변환하고 크기 축소하기
- 컬러 변환
  - cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
    - BGR 컬러 영상을 명암 영상으로 변환
- 크기 축소
  - cv.resize(gray,dsize(0,0),fx=0.5,fy=0.5) 
    - 반으로 축소
- cvtColor 함수가 컬러 영상을 명암 영상으로 바꾸는 방법
  - $I=round(0.299\times R+0.587 \times G + 0.114 \times B) \space \space \space (2.1)$
  - (참조: https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html)

#### 웹 캠에서 비디오 읽기
- 웹 캠에서 비디오 읽기
- 비디오에서 영상 수집하기(numpy의 hstack 함수 사용)
- 자료구조
  - 프레임별로 모아서 모으면 영상.
#### 그래픽 기능과 사용자 인터페이스 만들기
-  OpenCV의 그래픽 기능
   - 영상에 글씨나 도형을 넣는데 유용(Gui features in OpenCV 참조)
  - line, rectangle, polylines, circle, ellipse, putText 함수
- 영상에 도형을 그리고 글씨 쓰기
  - opencv_6.py
- 함수 선언에 대한 이해
- 마우스를 통한 상호작용(콜백 함수에 대한 이해 필요)
  - opencv_7.py
- 마우스 드래그로 도형 크기 조절하기
  - opencv_8.py
- 페인팅 기능
  - opencv_9.py

### Preview
- 컴퓨터 비전의 오랜 난제와 딥러닝의 혁신
  - 의미 분할 문제
  - 영상 설명하기 문제
- [의미 분할](https://huggingface.co/facebook/detr-resnet-50-panoptic)
- [영상 설명](https://huggingface.co/spaces/akhaliq/CLIP_prefix_captioning)
#### 방법론의 대전환
- 규칙 기반 방법론과 딥러닝 방법론
- 규칙 기반은 사람이 영상을 보고 규칙을 도출하고 프로그래밍
  - 분명한 한계. 예) 스케일 공간에서 가우시안보다 좋은 필터는 없을까? 데이터에 따라 최적 필터를 설계해야 하지 않을까?
- 딥러닝은 데이터 기반 학습을 통해 문제 해결
  - 예) 최적 필터를 학습으로 알아냄
  - 양질의 데이터가 매우 중요
- 둘 다 이해하고 다룰 수 있을 때 컴퓨터 비전 전문성 완성

- 딥러닝으로 대전환함으로써 혁신을 이룸
  - 신경망은 기계학습의 일종
  - 딥러닝은 층을 깊게 쌓은 깊은 신경망을 이용
- 컴퓨터 비전 방법론
  - 규칙 기반 방법론
  - 기계 학습 방법론
    - 비신경망 모델
      - 결정 트리
      - 랜덤 포레스트
      - SVM
    - 신경망 모델
      - 얕은 신경망
      - 깊은 신경망(딥러닝)
#### 머신러닝 기초
- 1단계: 데이터 수집
    - 모델의 입력은 특징 벡터feature vector, 출력은 참값GT; ground truth (또는 레이블label이라 부름)
    - 특징 벡터: **x**$=(x_1,x_2,\cdots,x_d)$
    - 데이터셋: $D={(\bold{x}^1,y^1),(\bold{x}^2,y^2),\cdots,(\bold{x}^n,y^n)}$
  - 회귀regression와 분류classification 문제
    - 회귀는 레이블이 연속 값(온도, 판매량 등): 회귀 문제
    - 분류는 레이블이 이산 값(숫자 부류, 물체 부류, 성별 등)
  
  - 검출, 분할, 추적 등의 다양한 문제
  - 데이터 수집은 많은 비용 소요
  - 다행히 공개 데이터 많음
예: aihub 사이트(https://www.aihub.or.kr/)

- 2단계 : 모델 선택 (model selection)
  - 선형 모델과 비선형 모델
  - 예) 2차 함수를 모델로 사용하면 가중치(매개변수)가 3개로 확대
    - $y=u_2 x^2+u_1 x+ u_0$
    - 가중치(매개변수) 집합 $\bold{w}=(u_0,u_1,u_2)$
  - 딥러닝은 가중치가 수만~수조개
- 3단계: $학습_{learning}$
  - 훈련 집합에 있는 샘플을 최소 오류로 맞히는 최적의 가중치 값을 알아내는 작업
  - 단순한 경우, 방정식 풀어 해결하는 $분석적 방법_{analytical method}$ 사용
  - 기계학습은 오류를 조금씩 줄이는 과정을 반복하는 $수치적 방법_{numerical method 사용}$
  - 모델이 범하는 오류를 측정하는 $손실 함수_{loss function}$ 필요
  - $평균제곱오차_{MSE: mean\space squared \space error}$는 가장 널리 쓰이는 손실 함수
    - 참값과 예측 값의 차이를 제곱하고 평균을 계산
  $평균제곱오차: J(\bold{W}) = {1 \over n}\Sigma_{i=1,n}(f(\bold{x}^i)-y^i)^2$
  - 손실 함수가 최소가 되는 점을 알아내는 최적화 알고리즘을 옵티마이저optimizer 라 부름
    - 파란색 모델이 최적에 더 가까움
- 4단계: 예측prediction(또는 추론inference라고 부름)
  - 학습을 마친 모델에 (학습에 사용하지 않았던) 새로운 특징 벡터를 입력하고 출력을 구하는 과정
  - 예측을 통해 모델의 성능을 측정
  - 일반화 능력 중요
    - 훈련 집합과 테스트 집합으로 나누고 테스트 집합으로 성능 측정
    - 또는 성능에 대한 신뢰를 높이려고 k-겹 교차 검증k-fold cross validation 사용

#### 딥러닝 소프트웨어 맛보기
- 머신러닝 라이브러리
  - sklearn은 딥러닝 이전의 고전적 기계학습 모델 지원(mlp, svm, decision tree, random forest 등)
  - $텐서플로_{TensorFlow}$와 $파이토치_{PyTorch}$는 딥러닝 지원
- 텐서플로 소개
  - 2015년 최초 공개
  - 숄레는 텐서플로 위에서 동작하는 케라스를 개발하여 공개
  - 2019년에 버전2를 공개: 버전2에서는 tensorflow 객체가 numpy와 호환되고 케라스와 한 몸이 됨(텐서플로 설치하면 케라스 따라 설치됨)
- 데이터와 텐서
  - 텐서플로가 제공하는 데이터셋 확인
    - MNIST 필기 숫자 데이터셋
    - CIFAR-10 자연영상 데이터셋
  - 딥러닝에서는 다차원 배열을 텐서라 부름
    - 001 딥러닝 비전.pdf 48p 참고
      - MNIST의 경우 
        - 훈련 집합에 28*28 영상이 6만개
        - 테스트 집합에 28*28 영상이 10000개
      - CIFAR-10
        - 훈련 집합에 32*32*3 영상이 5만개
        - 테스트 집합에 32*32*3 영상이 10000개
      - 데이터 셋의 텐서 구조 상 MNIST가 하나의 3차원 덩어리라면 CIFAR-10은 여러개의 3차원 덩어리로 이루어짐
- 퍼셉트론
  - 퍼셉트론
    - 1958년에 등장한 원시적인 모델
    - 딥러닝 이론의 토대이고 핵심 부품으로 사용되므로 딥러닝을 이해하는데 지름길
  - 구조와 연산
    - 임계치에 따라 가산점 혹은 감산점을 계산, 이를 가중치만큼 곱하여 출력
- 깊은 다층 퍼셉트론
  - 퍼셉트론은 선형 분류기
    - 선형 분리 가능한 데이터만 높은 성능
    - 현실에서는 대부분 비선형(선형 분리 불가능) 데이터
    - 루멜하트는 다층 퍼셉트론으로 비선형 분류 문제 해결
- 다층 퍼셉트론
  - 다층 퍼셉트론의 구조
    - 입력층과 은닉층을 연결하는 가중치 행렬
    - 은닉층과 출력층을 연결하는 가중치 행렬
    - 은닉층과 출력층은 완전 연결
  - 가중치
    - 은닉층의$j$번째 노드와 입력층의 $i$번째 노드를 연결하는 에지 가중치를 $u_{ji}^1$로 표기
    - 출력층의 $k$번째 노드와 은닉층의 $j$번째 노드를 연결하는 에지 가중치를 $u_{kj}^2$로 표기
  - 데이터에 따라 신경망 구조가 결정됨
    - 특징 벡터의 차원이 $d$이고 부류의 개수가 $c$이면 입력층의 노드 개수는 $d+1$이고 출력층의 노드 개수는$c$
      - 예)MNIST의 경우, 입력층은 785개(28*28+1),출력층은 10개의 노드를 가짐
    - 은닉층의 노드 개수 $p$는 하이퍼 매개변수(사용자가 지정해야 함)
- 신경망 출력을 부류 정보로 해석
  - 이 단계를 예측prediction 또는 추론inference이라 부름
    - 최종부류 : $: \hat{k} = \bold{argmax} o_k$
    - 출력층은 보통 softmax 활성 함수 사용
- 활성함수의 종류
  - step
  - logistic sigmoid
  - hyperbolic tangent
  - ReLU
  - leaky ReLU
  - softplus
  - Swish

#### 하이퍼 매개변수 다루기
- 하이퍼 매개변수
  - 신경망의 구조 또는 학습과 관련하여 사용자가 설정해야 하는 매개변수
  - 아주 많은 하이퍼 매개변수가 있음
    - 예) 층 수, 노드 수, 활성 함수, 옵티마이저, 학습률, 미니배치 크기, 세대 수, 손실 함수 … 
- 예) Dense 층과 Adam 옵티마이저의 API

- 하이퍼 매개변수 설정에 만능은 없음. 몇 가지 유용한 요령
  - 텐서플로가 제공하는 기본값 사용
  - 신뢰할 수 있는 논문이나 웹 사이트가 제공하는 권고 사항 따름
  - 중요한 하이퍼 매개변수 1~3개에 대해 성능 실험을 통해 스스로 설정
