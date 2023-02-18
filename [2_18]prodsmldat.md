## 머신러닝의 기본 개념 및 방법론의 분류
### 머신러닝의 기초
#### 머신러닝 기본 개념
- 머신러닝
  - 컴퓨터 시스템에 명시적으로 프로그래밍하지 않더라도 데이터를 스스로 학습하여 문제를 해결할 수 있게 하는 기술을 의미
  - 사람이 인지하기 어려운 복잡한 규칙과 패턴을 파악하여 의미있는 결과를 얻을 수 있음
  - ex)금융 사기 진단 프로그램
    - 새로운 사례가 나올때마다 프로그램을 수정해야함
    - 이 경우 새로운 패턴을 학습하게 하면 스스로 판단 가능
    - 비용이나 시간의 측면에서 훨씬 더 효과적으로 프로그램 관리
- 머신러닝의 발전
  - 머신러닝의 활용 증가
    - 머신러닝 알고리즘의 발전
    - 컴퓨팅 성능의 발전
    - 대용량 데이터의 축적 및 관리기술 발전
#### 머신러닝 방법론의 분류
- 지도 학습(Supervised Learning)
  - 라벨이 있는 훈련용 데이터에서, 여러 특성변수를 이용하여 목표변수인 라벨(label)을 예측하도록 모델을 학습함
  - 라벨의 데이터 타입에 따라 라벨이 연속형이면 회귀(regression)알고리즘, 라벨이 범주형이면 분류(classification)알고리즘으로 구분함
  - 대표 알고리즘
    - Linear Regression,K-nearest Neighbors,Logistic Regression,Softmax Regression, Decision Tree,SVM,Random Forest, Boosting,Neural Network, Deep Learning
  - 분류(classification)vs회귀(regression)
    - 색상으로 or 선을 기준으로 분류 (분류)
    - x와 y의 관계를 함수로 그어 표시(회귀)
- 비지도학습(Unsupervised Learning)
  - 라벨이 없는 훈련용 데이터에서 특징 변수들간의 관계나 유사성을 기반으로 의미있는 패턴을 추출
  - 자율학습이라고도 함
  - 군집화(Clustering),차원축소(dimension reduction),추천 시스템(recommendation)등에 활용됨.
  - 대표 알고리즘
    - k -means Clustering, Hieracrchical Clustering, PCA,t-SNE,Apriori,Auto-Encoders.
  - 군집화(clustering)
    - 비슷한 것끼리 그룹화.
    - 서로 얼마나 거리가 가까운지, 유사한지를 이용해 label을 만들어내는 과정.
  - 차원축소(dimension reduction)
    - 특성변수들만 모아서 차원축소
    - 특성변수들이 많을때, 가장 잘 표현하는 특성변수를 선택.