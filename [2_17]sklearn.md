## 사이킷런 소개
### 사이킷런
- 파이썬 기반의 다른 머신러닝 패키지도 사이킷런 스타일의 API를 지향할
정도로 쉽고 가장 파이썬스러운 API를 제공
- 머신러닝을 위한 매우 다양한 알고리즘과 개발을 위한 편리한 프레임워
크와 API를 제공
- 오랜기간 실전 환경에서 검증됐으며, 매우 많은 환경에서 사용되는 성숙
한 라이브러리
- 주로 Numpy와 Scipy기반 위에서 구축된 라이브러리

-[사이킷런 페이지](https://scikit-learn.org/stable/)

### 사이킷런을 이용한 붓꽃 데이터 분류
- 사이킷런을 통해 첫 번째로 만들어볼 머신러닝 모델은 붓꽃 데이터 세트
로 붓꽃의 품종을 분류(Classification)하는 것
- 붓꽃 데이터 세트는 꽃잎의 길이와 너비, 꽃받침의 길이와 너비 피처
(Feature)을 기반으로 꽃의 품종을 예측하기 위한 것
  - Sepal length
  - Sepal width
  - Petal length
  - Petal width
-  붓꽃 데이터 피처와 붓꽃 품종 레이블(Label)
   - Petal과 Sepal 데이터는 피처(Feature)
   - 레이블(Label)은 품종 (Iris setosa,Iris versicolor, Iris virginica )
### 머신러닝을 위한 용어 정리
- 피처(Feature)? 속성?
  - 피처는 데이터 세트의 일반 속성임
  - 머신러닝은 2차원 이상의 다차원 데이터에서도 많이 사용되므로 타겟값을 제외한 나머
지 속성을 모두 피처로 지칭
- 레이블, 클래스, 타겟(값), 결정(값)
  - 타겟값 또는 결정값은 지도 학습 시 데이터의 학습을 위해 주어지는 정답 데이터
  - 지도 학습 중 분류의 경우에는 이 결정값을 레이블 또는 클래스로 지칭
### 지도학습 -분류
#### 분류(Classification)
- 대표적인 지도학습(Supervised Learning) 방법의 하나
- 지도학습은 학습을 위한 다양한 피처와 분류 결정값인 레이블(Label) 데
이터로 모델을 학습한 뒤, 별도의 테스트 세트에서 미지의 레이블을 예측
- 즉 지도학습은 명확한 정답이 주어진 데이터를 먼저 학습한 뒤 미지의 정
답을 예측하는 방식
- 이 때 학습을 위해 주어진 데이터 세트를 학습데이터 세트, 머신러닝 모델
의 예측 성능을 평가하기 위해 별도로 주어진 데이터 세트를 테스트 데이
트 세트
- 붓꽃 데이터를 학습 데이터와 테스트 데이터로 분류
  - 둘의 차이는 학습은 꽃 종류가 있지만 테스트는 꽃 종류가 없음
#### 분류 예측 프로세스
```python
import sklearn
import pandas
```
```python
train_test_split()

```

<table>
    <tr>
        <th> 데이터세트 분리 </th><td>데이터를 학습 데이터와 테스트 데이터로 분리 </td>
    </tr>
    <tr>
        <th> 모델 학습 </th><td>학습 데이터를 기반으로 ML 알고리즘을 적용해 모델을 학습 </td>
    </tr>
    <tr>
        <th> 예측 수행 </th><td>학습된 ML 모델을 이용해 테스트 데이터 분류를 예측 </td>
    </tr>
    <tr>
        <th> 평가 </th><td>예측된 결과값과 테스트 데이터의 실제 결과값을 비교해 ML 성능을 평가 </td>
    </tr>
</table>

- 분류 예측 프로세스
  - 학습 데이터로 모델 학습
  - 학습 모델을 통해 테스트 데이터의 레이블 값 예측
  - 예측된 레이블 값과 실제 레이블 예측 정확도 평가

### 사이킷런 기반 프레임워크
- Estimator와 fit(), predict()
<table>
    <tr><th>평가</th><th>종류</th><th>구현 클래스</th>
    </tr>
    <tr>
        <td rowspan=2>Estimator <br> 학습: fit()<br>예측 : predict()</td><td>Classifier(분류)</td><td>DecisionTreeClassifier<br>
        RandomForestClassifier<br>
        GradientBoostingClassifier<br>
        GaussianNB<br>
        SVC</td>
    </tr>
    <tr>
        <td>Regressor(회귀)</td><td>LinearRegression<br>
        Ridge<br>
        Lasso<br>
        RandomForestRegressor<br>
        GrandientBoostingRegressor</td>
    </tr>
</table>

### 사이킷런의 주요 모듈
<table>
    <tr>
        <th>분류</th>
        <th>모듈명</th>
        <th>설명</th>
    </tr>
    <tr>
        <td>예제 데이터</td>
        <td>sklearn.datasets </td>
        <td>사이킷런에 내장되어 예제로 제공하는 데이터 세트</td>
    </tr>
    <tr>
        <td rowspan= 3>피처 처리
</td>
        <td>sklearn.preprocessing</td>
        <td>데이터 전처리에 필요한 다양한 가공 기능 제공
(인코딩, 정규화, 스케일링 등)</td>
    </tr>
    <tr>
        <td>sklearn.feature_selection</td>
        <td>알고리즘에 큰 영향을 미치는 피처를 우선순위대로
설렉션 작업을 수행하는 다양한 기능 제공
</td>
    </tr>
    <tr>
        <td>sklearn.feature_extraction<br>
sklearn.feature_extraction.text
(텍스트데이터)<br>
sklearn.feature_extraction.image
(이미지 데이터)
</td>
        <td>텍스트 데이터나 이미지 데이터의 벡터화된 피처를
추출하는데 사용함.<br>
(예를 들어 텍스트 데이터에서 Count Vectiorizer나
Tf-Idf Vectiorizer 등을 생성하는 기능 제공.)</td>
    </tr>
    <tr>
        <td>피처 처리 & 
차원 축소</td>
        <td>sklearn.decomposition</td>
        <td>차원 축소와 관련한 알고리즘을 지원하는 모듈.
(PCA,NMF, Truncated SVD</td>
    </tr>
    <tr>
        <td>터 분리, 검증
& 파라미터 튜닝
</td>
        <td>sklearn.model_selection</td>
        <td>교차 검증을 위한 train/test 데이터 분리, 그리드 서치
(GridSearch)로 최적 파라미터 추출 등의 API 제공</td>
    </tr>
    <tr>
        <td>평가 </td>
        <td>sklearn.metrics</td>
        <td>분류,회귀,클러스터링,페어와이즈(Pairwise)에 대한 다양한 성
능 측정 방법 제공
(Accuracy, Precision, Recall, ROC-AUC, RMSE등)</td>
    </tr>
    <tr>
        <td rowspan=7>ML 알고리즘</td>
        <td>sklearn.ensemble</td>
        <td>앙상블 알고리즘 제공.
(랜덤포레스트, 에이다부스트, 그래디언트 부스팅 등)</td>
    </tr>
    <tr>
        <td>sklearn.linear_model
</td>
        <td>주로 선형회귀, 릿지(Ridge), 라쏘(Lasso) 및 로지스틱 회귀 등
회귀 관련 알고리즘을 지원.
또한 SGD(Stochastic Gradient Descent) 관련 알고리즘도 제공</td>
    </tr>
    <tr>
        <td>sklearn.naive_bayes </td>
        <td>나이브 베이즈 알고리즘 제공. 가우시안 NB, 다항분포 NB 등</td>
    </tr>
    <tr>
        <td>sklearn.neighbors</td>
        <td>최근접 이웃 알고리즘 제공, K-NN 등</td>
    </tr>
    <tr>
        <td>sklearn.svm</td>
        <td>서포트 벡터 머신 알고리즘 제공
</td>
    </tr>
    <tr>
        <td>sklearn.tree</td>
        <td>의사 결정 트리 알고리즘 제공</td>
    </tr>
    <tr>
        <td>sklearn.cluster</td>
        <td>비지도 클러스터링 알고리즘 제공 (K-평균, 계층형,DBSCAN 등)</td>
    </tr>
    <tr>
        <td>유틸리티</td>
        <td>sklearn.pipline</td>
        <td>피처 처리 등의 변환과 ML알고리즘 학습, 예측 등을 함께 묶어서 실행할 수 있는 유틸리티 제공
</td>
    </tr>
</table>

### 사이킷런 내장 예제 데이터 셋
- 분류 및 회귀용
  
<table>
    <tr>
        <th>API명</th><th>설명</th>
    </tr>
    <tr>
        <td>datasets.load_boston()</td>
        <td>회귀 용도, 미국 보스턴의 집 피처들과 가격에대한 데이터 세트</td>
    </tr>
    <tr>
        <td>datasets.load_breast_cancer() </td>
        <td>분류 용도. 위스콘신 유방암 피처들과 악성/음성레이블 데이터 세트</td>
    </tr>
    <tr>
        <td>datasets.load_diabetes() </td>
        <td>회귀 용도. 당뇨 데이터 세트</td>
    </tr>
    <tr>
        <td>datasets.load_digits()</td>
        <td>분류 용도. 0~9까지 숫자의 이미지 픽셀 데이터세트
</td>
    </tr>
    <tr>
        <td>datasets.load_iris()</td>
        <td>분류 용도. 붓꽃 데이터 피처를 가진 데이터 세트</td>
    </tr>
</table>

### 내장 예제 데이터 셋 구성
- feature_names
- data
- target
- target names

#### 붓꽃 데이터 세트
- 꽃잎의 길이와 너비, 꽃받침의 길이와 너비 feature을 기반으로 폼의 품종을 예측하기 위한 것
- 지도학습 중 분류
- 독립변수(x): 꽃잎의 길이, 너비, 꽃받침의 길이, 너비
- 종속변수(y): 품종( Setosa, Vesicolor,  Virginica)
  
#### 붓꽃 데이터 분류 예측 프로세스
1. 데이터 세트 분리: 데이터를 training data와 test data로 분리
2. 모델 학습: training data를 기반으로 ML 알고리즘을 적용하여 모델을학습
3. 예측 수행: 학습된 ML 모델을 이용해 test data의 분류를 예측
4. 평가: 이렇게 예측된 결과값과 test data의 실제 결괏값을 비교해 ML 모델 성능을 평가


### Model Selection 소개
#### 학습 데이터와 테스트 데이터
- 학습 데이터 세트
  - 머신러닝 알고리즘의 학습을 위해 사용
  - 데이터의 속성들과 결정값(레이블) 값 모두를 가지고 있음
  - 학습 데이터를 기반으로 머신러닝 알고리즘이 데이터 속성과 결정값의 패턴을 인지하고 학습
- 테스트 데이터 세트
  - 테스트 데이터 세트에서 학습된 머신러닝 알고리즘을 테스트
  - 테스트 데이터는 속성 데이터만 머신러닝 알고리즘에 제공하며, 머신러닝 알고리즘은 제공된 데이터를 기반으로 결정값을 예측
  - 테스트 데이터는 학습 데이터와 별도의 데이터 세트로 제공되어야 함

#### 학습 데이터와 테스트 데이터 분리
- train_test_split()
- sklearn.model_selection의 train_test_split()함수
```python
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, 
iris_data.target, test_size=0.3, random_state=121)
```
- test_size : 전체 데이터에서 테스트 데이터 세트 크기를 얼마로 샘플링 할 것인가를 결정. 디
폴트는 0.25, 즉 25%
- train_size : 전체 데이터에서 학습용 데이터 세트 크기를 얼마로 샘플링 할 것인가를 결정
- shuffle : 데이터를 분리하기 전에 데이터를 미리 섞을지를 결정. 디폴트는 True. 데이터를 분
산시켜서 더 효율적인 학습 및 테스트 데이터 세트를 만드는 데 사용
- random_state : 호출할 때 마다 동일한 학습/테스트용 데이터 세트를 생성하기 위해 주어지
는 난수 값

#### 교차 검증(Cross Validation)

- 학습 데이터를 다시 분할하여 학습
데이터와 학습된 모델의 성능을 일차
평가하는 검증 데이터로 나눔
- 학습 데이터 세트
  - 분할
    - 학습 데이터세트
    - 검증 데이터세트
- 모든 학습/검증 과정이 완료된 후 최
종적으로 성능을 평가하기 위한 데이
터 세트
  - 테스트 데이터 세트

##### K 폴드(k-Fold) 교차 검증
- K=5일 경우 총 5개의 폴드 세트에 5번의 학습과 검증
- 평가 반복 수행, 교차 검증 최종평가 =평균(평가(1,2,3,4,5))
- 일반 K폴드
- Stratified K 폴드
  - 불균형한(imbalanced) 분포도를 가진 레이블(결정 클래스) 데이터 집합을 위한 K 폴드 방식
  - 학습데이터와 검증 데이터 세트가 가지는 레이블 분포도가 유사하도록 검증 데이터 추출

#### 교차 검증을 보다 간편하게
- Cross_val_score()
- Kfold 클래스를 이용한 교차 검증 방법
  1. 폴드 세트 설정
  2. For 루프에서 반복적으로 학습/검증 데이터 추출 및 학습과 예측 수행
  3. 폴드 세트별로 예측 성능을 평균하여 최종성능 평가
- cross_val_score() 함수로 폴드 세트 추출, 학습/예측, 평가를 한번에 수행
```python
cross_val_score(estimator, X, y=None, scoring=None, 
cv=None, n_jobs=1, vervose=0, fit_params=None, 
pre_dispatch=‘2*n_jobs’)
```
#### 교차 검증과 최적 하이퍼 파라미터 튜닝
- GridSearchCV
- 사이킷런은 GridSearchCV를 이용해 Classifier나 Regressor와 같은 알고리즘에 사용되는 하이퍼 파라미터를 순차적으로 입력하면서 편리하게 최적의 파라미터를 도출할 수 있는 방안을 제공
```python
Grid_parameters = {‘max_depth’:[1,2,3],
‘min_samples_split’:[2,3]}
```
- CV 세트가 3이라면

|파라미터 순차 적용 횟수 |CV 세트 수|학습/검증 총 수행 횟수|
|---|---|---|
|6  |3 |18|

##### 과적합(overfitting)
- 실제 예측의 경우, 예측 성능은 감소