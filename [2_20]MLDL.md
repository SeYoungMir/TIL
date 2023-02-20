### 데이터 전처리(Preprocessing)
- 데이터 전처리
  - 데이터 클린징
  - 결손값 처리(Null/NaN 처리)
  - 데이터 인코딩(렝이블, 원-핫 인코딩)
  - 데이터 스케일링
  - 이상치 제거
  - Feature 선택, 추출 및 가공

### 데이터 인코딩
- 머신러닝 알고리즘은 문자열 데이터 속성을 입력 받지 않으며 모든 데이
터는 숫자형으로 표현되어야 함
- 문자형 카테코리형 속성은 모두 숫자값으로 변환/인코딩되어야 함
#### 레이블(Label) 인코딩
- 원본 데이터 > 상품 분류를 레이블 인코딩 한 데이터
- ex) [TV, 냉장고, 전자레인지, 컴퓨터, 선풍기, 믹서] > [0,1,4,5,3,2]
#### 원-핫(One-Hot) 인코딩
- 원-핫 인코딩은 피처 값의 유형에 따라 새로운 피처를 추가해 고유 값에
해당하는 컬럼에만 1을 표시하고 나머지 컬럼에는 0을 표시하는 방식
  - TV:0, 냉장고:1, 전자레인지:4, 컴퓨터:5, 선풍기:3, 믹서:2를 원-핫 인코딩
  - 상품 분류 별 column으로 변환
- 사이킷런 원-핫(One-Hot) 인코딩
  - 원본데이터 > 레이블 인코딩 > 원 - 핫 인코딩
  - 1)문자열을 숫자로 변환
  - LabelEncoder(),2차원값으로 변환
    - .fit()
    - .transform()을 이용, label 인코딩 수행
    - inverse_transform()으로 디코딩 가능
  - OneHotEncoder()
  - Pandas에서는 get_dummies(df)를 이용 가능

#### 피처 스케일링
- 데이터 전처리(Data Preprocessing) - Scaling
  -  범위(Scale)가 다른 변수들의 범위(Scale)를 비슷하게 맞추기 위한 목적
  - 연속형 변수가 다양한 범위(Scale)로 존재할 때 제곱 오차 계산 시 왜곡 발생
    - Ex) X1은 1에서 10 사이 스케일, X2는 1000에서 100만 사이 스케일
  - 스케일이 더 큰 변수에 맞추어서 가중치를 최적화하는 문제 발생
- Scaling in Python
  - from sklearn.preprocessing import MinMaxScaler
  - from sklearn.preprocessing import StandardScale

- 표준화는 데이터 피처 각각의 평균이 0이고 분산이 1인 가우시안 정
규 분포를 가진 값으로 변환하는 것을 의미
- 정규화는 서로 다른 피처의 크기를 통일하기 위해 크기를 변환해주는
개념
- Normalization(정규화)
  - 변수의 스케일을 0 ~ 1 사이 범위로 맞추는 것(min-max scaling)
  - 정규화는 변수의 범위가 정해진 값이 필요할 때 유용하게 사용
 - *X_Normalization*= ${X-min(X)}\over{max(X)-min(X)}$
- Standardization(표준화)
  - 변수의 평균을 0, 표준편차를 1로 만들어 표준정규분포의 특징을 갖도록 함
- 표준화는 가중치(weight) 학습을 더 쉽게 할 수 있도록 함
- *X_Standardization*= ${X-mean(X)}\over{std(X)}$


### 타이타닉 생존자 ML 예측 구현
- 데이터 전처리
  - Null 처리
  - 불필요한 속성 제거
  - 인코딩 수행
- 모델 학습 및 검증/예측/평가
  - 결정 트리,랜덤포레스트, 로지스틱 회귀 학습 비교
  - K 폴더 교차 검증
- cross_val_score()와 GridSearchCV() 수행
