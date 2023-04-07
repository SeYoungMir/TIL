## 특성 공학: 특성 추출(Feature Extraction) 방법론
## 특성 추출법 개요
- 특성공학
  - 특성 공간 방법론
    - 특성 선택(feature selection):가지고 있는 특성 중 더 유용한 특성을 선택
    - 특성 추출(feature extraction):가지고 있는 특성을 결합하여 더 유용한 특성을 생성
  - 주요 특성 추출법
    - PCA(Principal Component Analysis)
    - SVD(Singular Value Decomposition)
    - LDA(Linear Discriminant Analysis)
    - NMF(Non-negative Matrix Factorization)
### 주성분 분석(PCA)
- 주성분 분석이란
  - 서로 연관되어 있는 변수들($x_1,...,x_k$)이 관찰되었을 때, 이 변수들이 전체적으로 가지고 있는 정보들을 최대한 확보하는 적은 수의 새로운 변수(주성분,PC)를 생성하는 방법
- 주성분 분석의 목적
  - 자료에서 변동이 큰 축을 탐색함
  - 변수들에 담긴 정보의 손실을 최소화하면서 차원을 축소함
  - 서로 상관이 없거나 독립적인 변수인 주성분을 통해 데이터의 해석을 용이하게 함
- 주성분 분석 아이디어
  - $k$개의 특성변수 $x_1,...,x_k$의 주성분이 $y_1,...,y_k$라면 이들은 $x_1,...,x_k$의 선형결합식으로 아래와 같이 표현됨<br>$y_1=l_{11}x_1+l_{21}x_2+\cdots +l_{k1}x_k$<br>
 $y_2=l_{12}x_1+l_{22}x_2+\cdots +l_{k2}x_k$<br> $\cdots$ <br>
 $y_k=l_{1k}x_1+l_{2k}x_2+\cdots +l_{1k}x_k$
- 주성분 분석에 관한 기하학적 의미
  - 주성분 축은 원래 변수들의 좌표축이 직교 회전 변환된 것으로 해석할 수 있음
    - 첫번째 주성분 축은 데이터의 변동이 가장 커지는 축임
    - 두번째 주성분 축은 첫번째 주성분 축과 직교하며 첫번째 주성분 축 다음으로 데이터의 변동이 큰 축을 나타냄
    - 각 관찰치별 주성분 점수는 대응하는 원 자료 값들의 주성분 좌표축에서의 좌표값에 해당함
    - 자료들의 공분산 행렬이 대각행렬이 되도록 회전한 것으로 해석할 수 있음
### 특성값 분해(SVD)
- 특성값 분해 이론
  - 특이값 분해: 임의의 $n\times d$행렬 $A$는 $A=U\Sigma V^T$로 분해 가능함
    - $U$와 $V$는 직교행렬: $U^TU=I_{n\times n},VV^T=I_{d\times d}$
    - $U$의 각 열을 $A$의 왼쪽 특성벡터, $V$의 각 열을 $A$의 오른쪽 특성벡터라고 함
    - $\Sigma$는 $n\times d$의 대각행렬: 대각 원소를 $A$의 특성값이라고 함
  - 특이값 분해와 차원 축소
    - $U$의 각 열을 $u_i,i=1,...,n$
    - $V^T$의 각 행을 $v_i^t,i=1,...,d$
    - $\Sigma$의 0이 아닌 대각원소를 $\lambda_i,i=1,...,r(\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_r)$ 이라고 할 때,<br>$A=U\Sigma V^T = \sqrt{\lambda_1}u_1v_1^T+\sqrt{\lambda_2}u_2v_2^T+\cdots + \sqrt{\lambda_m}u_mv_m^t+\cdots \sqrt{\lambda_r}u_rv_r^T$
    - 정보가 많은 순서대로 $m$개만 이용하여 근사하는 경우 $m$계수 근사라고 함
  - 주성분 분석(PCA)와 특성값 분해의 관계
    - $A$의 오른쪽 특성벡터는 $A$의 공분산행렬의 고유벡터와 동일함
    - 자료 행렬에 대한 특성값 분해로 주성분을 도출 가능