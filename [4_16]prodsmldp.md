## 규제가 있는 선형 회귀 모델(Ridge,Lasso,Elastic net)
### Keywords
- 릿지 회귀
- 라쏘 회귀
- 엘라스틱 넷
- 선형회귀모델의 규제
- L1 규제
- L2 규제
### 규제가 있는 선형 회귀모델
- 파라미터가 너무 커지지 않도록 규제하는 추정법
- 중요하지 않은 변수, 중복된 변수의 영향력 규제
- 릿지, 라쏘, 엘라스틱 넷 등 모델의 과적합 방지
### 규제가 있는 선형 회귀모델
- 선형회귀모델의 규제
  - 모형의 과대적합을 막기 위한 규제방법(regularization)으로 선형회귀모형에서는 보통 모델의 가중치를 제한하는 방법을 사용함
  - 선형 회귀 모델의 비용함수<br>$J(\beta)={1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2$
  - 규제가 있는 경우 비용함수<br>$J(\beta)={1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2+\lambda\cdot penalty(\beta_1,...,\beta_k)$
  - 가중치를 제한하는 방법에 따른 규제 선형 회귀 모델의 종류
    - 릿지회귀(Ridge Regression)
    - 라쏘회귀(Lasso Regression)
    - 엘라스틱 넷(Elastic Net)
  - $L_p Norm = (\Sigma_{j=1}^k|\beta_j|^p)^{1\over p}$
    - p=2 릿지, p=1 라쏘, 엘라스틱은 중간
### 릿지 회귀
- 릿지 회귀(Ridge Regression)와 L2규제
  - 릿지회귀의 비용함수
    - 비용함수 $J(\beta)$에 규제항 $\lambda\cdot \Sigma_{j=1}^k\beta^2_i$이 추가된 선형회귀모형<br>$J(\beta)={1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2+\lambda\cdot\Sigma_{j=1}^k\beta^2_i$
    - $\lambda$(규제정도를 결정하는 하이퍼 파라미터
      - $\lambda$가 크면 규제 많음, 회귀계수 추정치가 작아짐
      - $\lambda$가 0이면 일반선형회귀모델과 동일한 결과
      - 적절한 $\lambda$는 교차검증(cross-validation)등으로 최적화
      - 릿지회귀의 훈련
        - 비용함수$J(\beta)$를 최소로 하는 회귀계수$\hat\beta^R= \hat\beta^R_0,\hat\beta^R_1,...,\hat\beta^R_k)$를 찾는 문제.<br>$\hat\beta^R=argmin_\beta J(\beta)$
      - Alternative Formulation
        - 어떤 임의의 $\lambda$에 대해 이에 대응하는 하나의 $t$가 존재하여, 아래 식으로 동일한 해$\hat\beta^R$를 얻게 됨
        - $\hat\beta^R=argmin_\beta {{1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2}subject to \Sigma_{j=1}^k\beta_j^2 \leq t$
### 라쏘회귀(Lasso Regression)와 L1규제
- 라쏘회귀의 비용함수
  - 비용함수 $J(\beta)$에 규제항 $\lambda\cdot \Sigma_{j=1}^k|\beta_j|$이 추가된 선형회귀모형<br>$J(\beta)={1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2+\lambda\cdot\Sigma_{j=1}^k|\beta_j|$
  - $\lambda$:규제정도를 결정하는 하이퍼 파라미터,교차검증(cross-validation)등으로 최적화
  -  비용함수$J(\beta)$를 최소로 하는 회귀계수$\hat\beta^L= \hat\beta^L_0,\hat\beta^L_1,...,\hat\beta^L_k)$를 찾는 문제.<br>$\hat\beta^L=argmin_\beta J(\beta)$
-  Alternative Formulation
     - 어떤 임의의 $\lambda$에 대해 이에 대응하는 하나의 $t$가 존재하여, 아래 식으로 동일한 해$\hat\beta^R$를 얻게 됨
      - $\hat\beta^L=argmin_\beta {{1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2}subject to \Sigma_{j=1}^k|\beta_j| \leq t$
### 릿지회귀와 라쏘회귀의 특징
- 릿지회귀와 라쏘회귀의 특징
  - 두 방식 모두 추정치는 일반 선형회귀모형과는 달리 편의가 발생하지만, 분산은 더 작아지게 됨 $\rarr \lambda$에 따라 일반화 오차가 더 작아질 수 있음
  - 라쏘 회귀의 경우 제약범위가 각진 형태 $\rarr$파라미터의 일부가 0이 되는 경향이 있음(sparse model)
  - 릿지 회귀의 경우 제약범위가 원의 형태$\rarr$파라미터가 0이 되지 않고 전반적으로 줄어드는 경향이 있음.
### 엘라스틱 넷
- 엘라스틱 넷(Elastic Net)
  - L1과 L2 규제를 혼합한 방식
  - 엘라스틱 넷의 비용함수<br> $J(\beta)={1\over n}\Sigma_{i=1}^n(y_i-\beta_0-\beta_1x_{1i}-\beta_2x_{2i}-\cdots-\beta_kx_{ki})^2+\lambda_1\cdot\Sigma_{j=1}^k\beta_j^2+\lambda_2\cdot\Sigma_{j=1}^k|\beta_j|$
  - 릿지회귀와 라쏘회귀의 장점을 모두 가짐
  - 이론적으로는 둘보다 좋지만 실제로는 둘 중 하나만 쓰는게 더 좋음.
