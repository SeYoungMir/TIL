## 그래프에 의한 기술통계
### Keywords
- 바차트
- 파이차트
- 히트맵
- 스택트컬럼차트
- 히스토그램
- 박스플롯
- QQ플롯
- 산점도
### 데이터 시각화 개요
- 그래프를 이용한 자료의 정리
  - 자료의 유형에 맞는 그래프를 이용하여 한 눈에 알아볼 수 있게 자료를 시각화할 수 있음.
- 질적 자료인 경우 (명목형- 순서가 존재하지 않음, 순서형- 순서가 존재함)
  - 1개 변수: 바차트(막대그림),파이차트
  - 2개 변수: 히트맵, 스택드컬럼차트
- 양적 자료인 경우( 숫자형 - 이산형- 값들의 수를 셀 수 있을때/연속형- 값들의 수를 셀 수 없을때)
  - 1개 변수: 히스토그램, 박스플롯(상자그림),라인차트,QQ플롯
  - 2개 변수: 산점도
### 바차트와 파이차트
- 질적 변수, 1개 변수.
### 스택트 칼럼 차트
- 질적변수, 2개변수, 연관성
  - 막대를 이용해 쌓듯이
### 히트맵
- 질적변수, 2개변수, 연관성
  - 색을 이용해 표현
### 히스토그램
- 양적 변수, 1개 변수
  - 막대그림과의 차이
    - 가로축이 실선
    - 구간별로 자료의 빈도를 나눔
### 박스플롯
- 숫자형 변수, 1개 변수
- 자료를 요약하는 수를 연산
  - 사분위수 Q1,Q2,Q3 계산
  - Q3-Q1 = IQR
  - 1.5IQR/IQR/1.5IQR 지점으로 그림을 그림
  - 전체의 중앙값, Q1,Q3지점, 이상치의 존재 여부, 숫자형 변수들의 중심위치, 퍼진 변도, 이상치 여부를 비교하기에 용이
### 정규 Q-Q플롯
- 양적 변수 하나가 주어졌을때 정규분포를 따르는가
- 정규분포에 가까우면 직선 위에 찍힘
- 순서대로 경험 누적 확률을 계산 
- 이론 Quantile= 누적확률를 가지는 정규분포 자료의 Z1치를 계산
- 비선형의 구조면 정규분포가 아님.
  - 오른쪽 꼬리가 길면 표본정규분포와 비교해서 정규분포보다 높은 쪽은 위로, 낮은쪽은 아래로 내려가 오른쪽 아래가 오목한 구조
  - 왼쪽 꼬리가 길면 마찬가지로 되어 왼쪽 위로 볼록한 구조
### 산점도
- 두 자료의 연관성을 파악하기 위함
- 양적 변수, 2개 변수
- 2개 변수를 점을 찍어 표현