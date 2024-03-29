## 다중 회귀 분석(Multiple Linear Regression)
### Keywords
- 다중선형회귀모형
- 범주형 독립변수
- 더미변수
### 다중회귀분석
- 독립변수가 두 개 이상인 경우, 여러 개의 독립변수를 이용하면 종속변수의 변화를 더 잘 설명할 수 있음
- 기본적인 모형 식 정의
- 모수를 추정하는 방법
- 회귀모형은 범주형 독립변수 포함 가능($\rarr$더미변수 이용)
### 다중 선형 회귀 모형
- 다중선형 회귀모형으로의 확장
  - 다중선형회귀모형
    - 독립변수가 두 개 이상인 선형회귀모형.
    - 여러 개의 독립 변수를 이용하면 종속변수의 변화를 더 잘 설명할 수 있을 것임.
    - 자료($(x_{1i},x_{2i},...,x_{ki}),Y_i$), $i=1,\cdots,n$에 다음의 관계식이 성립한다고 가정함<br>$Y_i=\alpha+\beta_1 x_{1i} + \beta_2 x_{2i}+\cdots+\beta_k x_{ki}+\epsilon_i$, $i=1,2,...,n$
  - 오차항인 $\epsilon_1,\epsilon_2,\cdots,\epsilon_n$은 서로 독립인 확률변수로 $\epsilon_i \sim N[0,\sigma^2]$:정규,등분산,독립 
  - 회귀계수$\alpha,\beta_1,...,\beta_k$와$\sigma^2$은 미지의 모수로, 상수임.
    - $\beta_j$의 해석ㅣ$x_j$를 제외한 나머지 모든 예측 변수들을 상수로 고정시킨 상태에서 $x_j$의 한 단위 증가에 따른 $E[Y]$의 증분을 의미$(j=1,...,k)$
- 회귀계수 $\alpha,\beta_1,...,\beta_k$의 추정
  - 수직거리 제곱합<br>$SS(\alpha,\beta_1,...,\beta_k)=\Sigma_{i=1}^n(y_i-\alpha-\alpha-\beta_1x_{1i}-\cdots-\beta_kx_{ki})^2$이 최소가 되도록 $\alpha,\beta_1,...,\beta_k$를 추정
  - 최소제곱 추정량 $\hat\alpha,\hat\beta_1,...,\hat\beta_k$
  - 다중선형회귀모형 추정 결과
    - 결정계수 $R^2$ <br> $R^2={SSR\over SST}=1-{SSE\over SST}$
- 범주형 독립변수가 포함된 회귀모형
  - 범주형 독립변수를 회귀모형에 포함하기 위해서는 더미변수(dummy variable)기법을 사용
  - 더미변수는 0 또는 1의 값을 갖는 변수로 다음과 같이 정의됨.
    - 더미변수의 개수 = 범주의 개수 -1
