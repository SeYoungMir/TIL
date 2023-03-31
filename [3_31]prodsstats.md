## 범주형 변수 간의 독립성 검정(Chi-squared test)
### Keywords
- 카이제곱 독립성 검정
- 분할표
- 기대 빈도
### 카이제곱 검정 개요
- 카이제곱 검정(Chi-squared test)
  - 범주형인 자료를 분석하는 데 활용
  - 범주형 자료 분석은 크게 적합도 검정(goodness of fit test),독립성 검정(test of independence)으로 나뉘어짐
<table>
    <tr><th>검정법</th><th>설명</th></tr>
    <tr><th>적합도 검정</th><td>하나의 범주형 변수에 대해 각 범주별 확률에 관한 검정</td></tr>
    <tr><th>독립성 검정</th><td>서로 다른 두 범주형 변수 간에 연관성이 있는지를 검정</td></tr>
</table>

- 카이제곱 독립성(Independence) 검정
  - 2개의 범주형 변수를 요약하는 $r\times c$의 2차원 분할표
    - 두 변수가 독립인 경우에 예상되는 각 셀 별 기대빈도 도출
    - 각 셀 별 빈도와 기대빈도의 차이의 크기를 이용하여 검정
    - 차이가 작으면 두 변수는 독립
    - 차이가 크면 두 변수는 독립이 아님.
<table>
    <tr><th rowspan=2, colspan=2><br></th><th colspan=4>변수2</th></tr>
    <tr><th>1</th><th>2</th><th><br></th><th>c</th></tr>
    <tr><th rowspan=4>변수 1</th><th>1</th><td>X_11</td><td>X_12</td><td>X_13</td><td><br></td><td>X_1c</td></tr>
    <tr><th>2</th><td>X_21</td><td>X_22</td><td>X_23</td><td><br></td><td>X_2c</td></tr>
    <tr><th><br></th><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr>
    <tr><th>r</th><td>X_r1</td><td>X_r2</td><td>X_r3</td><td><br></td><td>X_rc</td></tr>
</table>  

  - $i$행 범주와 $j$열 범주가 독립인 경우: <br>$i$행 과 $j$열의 결합 확률= $i$행의 주변확률 $\times$ $j$열의 주변 확률<br>$\hat p_{ij}={\Sigma^c_{j=1}x_{ij}\over n}\times {\Sigma^r_{i=1}x_{ij}\over n} - E[X_{ij}]=n\hat p_{ij}$
- 카이제곱 독립성 검정 절차
  - 가설
    - 귀무가설 $H_0$: 두 범주형 변수는 서로 독립이다(관계가 없다).
    - 대립가설 $H_1$: 두 범주형 변수는 독립적인 관계가 아니다(관계가 있다).
  - 검정통계량과 표본분포
    - 귀무가설($H_0$)이 사실일 경우,
    - 표본의 수가 충분히 큰 경우(모든 기대빈도 5 이상)
    - $X =\Sigma_{j=1}^c\Sigma_{i=1}^r{(X_{ij}-n\hat p_{ij})^2\over n\hat p_{ij}}\sim \chi^2[(r-1)(c-1)]$
- 유의확률(p-value)의 계산
  - 귀무가설 $H_0$가 사실일 때, 검정통계량 $X$의 표본분포 $X =\Sigma_{j=1}^c\Sigma_{i=1}^r{(X_{ij}-n\hat p_{ij})^2\over n\hat p_{ij}}\sim \chi^2[(r-1)(c-1)]$에서, $x_0$(=표본 자료로부터 계산된 검정통계량의 값)보다 대립가설 방향으로 더 극단적인 값이 나올 확률
- 유의수준 (significance level) 100 $\alpha\%$검정법
  - 자료로부터 계산된 유의확률(p-value)이 주어진 유의수준$\alpha$보다 작은 경우에 귀무가설 $H_0$를 기각함
  - p-value$\leq \alpha$면 $H_0$을 기각