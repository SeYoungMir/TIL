#### 통계
- 통계
  - 집단 특성 확인
    - 모여/ 떨어져
      - 모여: 중심화 경향치
        - 평균,중앙값, 최빈값
          - 공통점
      - 떨어져: 산포도
        - 분산,표준 편차
          - 차이점
  - 시각화
    - Nomalization
    - S분포
    - kai 분포
    - R 분포
    - kai^2 분포

## 데이터
 - 변수의 종류
      - 질적 변수와 양적 변수
        - 질적 변수: 선택이 필요한 변수, 종류를 구별하기 위한 변수
        - 양적 변수: 양을 표현하는 변수
      - 척도 수준
        - 질적 변수는 명의 척도와 순서 척도
        - 양적 변수는 간격 척도와 비례 척도로 더 세분화
        - 명의 척도, 순서 척도, 간격 척도, 비례 척도 네가지를 척도 수준이라 함
        - 명의 척도
          - 단순히 분류하기 위한 변수, 학생번호나 전화번호, 성별 등
          - 목적은 '구별', 변수의 동일성 여부에 의미
            - 학생번호 4와 8 사이의 대소 관계는 의미 X
            - 합과 차를 계산해도 의미 X
        - 순서 척도
          - 순서 관계나 대소 관계에 의미가 있는 변수, 성적 순위, 설문 조사 만족도 등
          - 성적 순위에서 8등은 4등보다 순위가 낮으므로 대소 관계 의미
          - 4등과 8등의 차이가 8등과 12등의 차이가 동일하가고 볼 수는 없음
          - 4등은 8등의 2배라고 주장 불가
        - 간격 척도
          - 대소관계와 함께 그 차이에도 의미가 있는 변수, 연도나 온도
          - 60도와 30도보다 높은 온도, 대소 관계에 의미, 차이에 해당하는 수치 의미
          - 60도는 30도보다 2배 높은 온도라고 할 수 없음
        - 비례 척도
          - 대소관계, 차이, 비 모두에 의미가 있는 변수, 길이나 ㅁ게 등
          - 기리에서 50cm와 100cm의 차이가 50cm, 100cm는 50cm 의 2배 모두 의미
          - 간격 척도와 비례 척도는 비슷하므로 구별하기 어려울 때 있음
          - 척도를 구별하는 요령
            - 0이 '없음'을 나타내는지 여부 판단
            - 길이에서 0은 길이가 없음, 온도에서 0은 온도가 없음은 아님.
        - 이산형 변수와 연속성 변수
          - 이산형 변수
            - 하나하나의 값을 취하는 변수
            - 서로 인접한 숫자 사이에 값이 존재하지 않음
            - 주사위의 눈, 결석 횟수, 학생수 등
          - 연속성 변수
            - 연속적인 값을 취할 수 있는 변수
            - 어떤 두 숫자 사이에도 반드시 숫자가 존재
            - 길이, 무게, 시간
### 1차원 데이터
#### 데이터 중심의 지표
- 데이터 중심의 지표
  - 수치계산과 통계 분석에 필요한 라이브러리 임포트
  - 출력을 소수점 이하 3자리로 설정
```python
import numpy as np
import pandas as pd
#출력 소수점 이하 3자리로 제한(jupyter notebook)
%precision 3
#Dataframe의 출력을 소수점 이하 3자리로 제한
pd.set_option('precision',3)
```
  - 평균값
    - 평균값은 데이터를 모두 더한 뒤, 데이터의 개수로 나누어 구함
  - 평균과 중앙값
    - 중앙값
      - 중앙값은 데이터를 크기 순서대로 나열할 때 정확히 중앙에 위치한 값
      - 이상값에 영향을 덜 받음
  - 절사평균(Trimmed Mean)
    - 양쪽을 일부 제거하고 나머지들의 평균
    - 이상값(outlier)에 영향을 별로 받지 않음
    - 정보의 손실이 적음
    - 10%, 20% 절사평균
    - 다이빙 점수
      - 최고점과 최저점을 제외하고 나머지의 평균과, 난이도를 고려해 계산
  - 최빈값
    - 최빈값은 데이터에서 가장 많이 나타나는 값
#### 데이터의 산포도 지표
  - 분산과 표준 편차
    - 편차
      - 각 데이터가 평균으로부터 떨어져 있는 정도
      - 각 편찻값으로 비교가 어려우므로, 편차의 평균을 비교
    - 분산
      - 산포도의 지표인 편차의 평균은 항상 0
      - 단순히 더하면 서로 상쇄되어 0이 되므로 편차의 제곱을 ㅣㅇ용
      - 편차 제곱의 평균이 분산(모분산)
    - 표준편차
      - 분산의 단위는 기존 단위의 제곱
      - 원래의 데이터와 동일한 단위를 쓰는 산포도 지표가 필요
      - 분산에 제곱근을 취한 것이 표준편차
      - 원래 데이터와 동일한 단위이므로 동일 차원으로 그릴 수 잇음
    - 범위와 사분위 범위
      - 범위
        - 데이터 전체가 아니라 최댓값과 최솟값만으로 산포도 표현
      - 사분위범위
        - 상위수 %와 하위수 %에 위치하는 값의 차이
        - 데이터의 하위 25%,50%,75%에 위치하는 값은 각각 제1사분위수(Q1),제 2사분위수(Q2),제 3사분위수(Q3)
        - 사분위범위 $IQR= Q3-Q1$
        - 상자 수염 그림
          - 하한, 하한 사분위수, 사분범위, 중앙값, 상한 사분위수, 상한, 범위로 이루어짐
#### 데이터의 정규화
- 표준화
  - 상대적 결과가 다르므로 통일된 지표로 변환하는 정규화
  - 데이터에서 평균을 빼고 표준편차로 나누는 작업
  - $z_i= {x_i-\bar{x} \over S }$
  - 표준화된 데이터는 표준화 변량 또는 Z점수
  - 표준화된 데이터는 평균이 0, 표준편차가 1
- 편차값
  - 평균이 50, 표준편차가 10이 되도록 정규화한 값
  - $z_i= 50+10 \times {x_i-\bar{x} \over S }$
- 데이터의 주요 지표   
  - `pd.describe()`메소드 사용
#### 데이터의 시각화
- 도수분포표
  - 데이터의 분포 상태를 세부적으로 알고 싶을 때 사용
  - 데이터가 취하는 값을 몇 개의 구간으로 나누고, 각 구간에 몇개의 데이터가 들어가는가를 세는 방법
  - 분할된 구간과 데이터의 개수를 정리한 표가 도수 분포표
    - 계급: 시험 점수의 경우, 10점 간격으로 나눌 때 0~10점 구간 등
    - 도수: 각 계급에 속한 학생 수
    - 계급폭: 각 구간의 폭, 10점
    - 계급수: 계급의 수, 10
    - 계급값: 각 계급을 대표하는 값으로, 계급의 중앙값을 이용
    - 상대도수: 전체 데이터에 대해서 해당 계급의 데이터가 차지하는 비율
    - 누적 상대 도수: 해당 계급까지의 상대도수의 합
    - 최빈값: 최대가 되는 계급의 계급값
- 히스토그램
  - 도수분포표를 막대그래프로 나타내어 데이터의 분포상태를 더 시각적으로 파악 가능
- 상자 그림
  - 데이터의 분포와 이상값을 시각적으로 파악 가능
### 2차원 데이터
#### 두 데이터 사이의 관계를 나타내는 지표
- 데이터 준비
  - 영어점수와 수학 점수 데이터
    - 영어점수 높을 때 수학점수 높으면 양의 상관 관계
    - 영어점수 높을때 수학점수 낮으면 음의 상관관계
    - 영어점수와 수학점수가 영향을 서로 주지 않을때 무상관
- 공분산
  - 중간의 가로선과 세로선은 수학과 영어 평균 점수
  - 영어 점수와 수학점수는 양의 상관 관계
  - 직사각형의 가로 길이는 영어 점수 편차, 세로는 수학 점수 편차
  - 공분산은 면적, 음의 면적도 가능
- 상관계수
  - 공분산의 단위는 직감적으로 이해하기 어려우므로, 단위에 의존하지 않는 상관을 나타ㅐ는 지표
  - 시험 점수간의 공분산(점수 $\times$ 점수 ),키와 점수(cm $\times$ 점수)
  - 상관계수는 공분산을 각 데이터의 표준편차로 나누어 단위에 의존하지 않음
  - $r_{xy}={S_{xy}\over S_xS_y}$=${1\over n }\Sigma_{i=1}^n({x_i-\bar{x}\over S_x})({y_i-\bar{y}\over S_y})$
  - 양의 상관은 1에 가까워지고, 음의 상관은 -1에 가까워지고, 무상관은 0
  - 상관계수가 -1일때와 1일 때 데이터는 완전히 직선상에 놓임
- 산점도
- 회귀직선
  - $y=\beta_0+\beta_1x$
- 히트맵
  - 히스토그램의 2차원 버전으로 색을 이용해 표현하는 그래프
  - 영어 점수 35점부터 80점, 수학점수 55점부터 95점까지 5점 간격
  - 색이 진한 영역일수록 많은 학생이 분포
- 앤스컴
  - 앤스컴의 예
    - 동일한 지표, 다른 데이터
    - 동일한 지표를 가지고있지만 그림으로 표현하면 전혀 다른 데이터
  