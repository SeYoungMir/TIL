## 데이터가 얼마나 퍼져 있는지 : 변이 통계량
- 데이터들이 얼마나 흩어져 있는가를 나타내는 것(산포도)
- 하나의 수치로 데이터가 흩어진 정도를 계산 
- 대표값과 더불어 데이터를 비교하는 경우에 유용하게 사용 
- 예. 평균이 같은 A와 B반의 성적 : 두 집단이 동일한 집단?

  - 어느 대학에서 같은 과목을 두 교수가 가르친다고 하자.두 교수 모두 평균 C학점을 학생들에게 준다면 그 과목을 배우려는 학생들은 어떤 교수를 선택해도 마찬가지라고 생각할 것이다.
  - 그러나 한 교수는 대부분의 학생들이 평범하다고 생각하여 C만 주고 다른 교수는 학생들이 반은 우수하고 반은 공부를 안 한다고 생각하여 A를 주거나 D-만 준다.
  - 그러므로 이러한 흩어짐의 정보 없이 학생들이 평균 성적 C라는 사실만 가지고 교수를 선택한다면 학점 때문에 어려움에 처할 수도 있게 된다.

#### 범위(range)

- 데이터의 최대값과 최소값의 차이
- 데이터가 퍼져 있는 정도를 나타내는 가장 간단한 방법
- 범위가 클수록 산포가 크다고 말할 수 있지만
- 중앙값과 마찬가지로 극단적인 값에 영향을 받음
- 데이터 중 2개의 정보(최대값, 최소값)만을 이용하므로 `적절한 척도로 사용하기 어려움`

**범위(R)=최댓값 - 최솟값**


#### 중간 범위 /중앙값과는 다르다.

- 최대값과 최소값의 평균

#### 사분위간 범위 (interquartile range: IQR)

- 데이터를 크기순서로 나열한 다음, 개수로 4등분할 때 첫 번째 사분위수(Q1:1사분위수, 25%지점)와 세 번째 사분위수(Q3:3사분위수, 75%지점)의 차이


#### 사분위수 편차(quartile deviation) ->이미지, 영상에서 음파를 분리한 파형 편차를 구할 때 사용된다.

- 범위의 문제점을 보완한 척도
- 사분위간 범위의 값을 2로 나눈 값으로 사분위 범위의 평균값 

### 분산(variaince)

- 산포도의 척도로 가장 널리 사용되는 방법 
- 데이터가 퍼져 있는 정도의 기준으로 평균을 사용
- 계산방법
    - 각 데이터와 평균과의 차이를 제곱하여 합한 값의 평균
        - 모두 양수로 만들기 위함, 양수 음수가 함께 있으면 상쇄가 발생
    - 데이터가 모집단 전체일 경우에는 데이터의 개수(n)로 나누어 줌
    - 표본일 경우 (n-1)로 나누어 줌
    - 표본의 경우 n으로 나누어 주는 것보다 (n-1)로 나누어 주는 것이 더 좋은 척도가 되기 때문인데 표본의 크기가 큰 경우에는 별 차이가 없음
    - 분산 계산 : var() 함수 사용

```python
## ddof인수 :  (자유도-모수집단냐 표본이냐)는 값을 1로 두고 사용한다고 생각하면 편함
## 특별한 경우 제외하고는 모두 sample 데이터이므로 분모를 n-1로 둠
## 즉 , ddof는 1로 둔다
x = [1, 2, 3, 4, 5]
np.var(x, ddof=1) # 분모 = n-1
np.array(x).var() # 분모 = n
pd.Series(x).var(ddof=0) # 분모 = n

# 값의 스케일에 크게 영향을 받음으로
# 변수를 스케일링 한 후 분산, 표준편차를 구하는게 일반적임
```

### 표준편차(standard deviation)


- 계산된 분산의 제곱근으로 계산
- 평균을 중심으로 일정한 거리에 포함된 데이터의 비율이 얼마인가를 계산
- 모든 데이터를 고려한 척도


- 특징
    - 모든 데이터가 동일한 값을 갖는다면 분산과 표준편차는 0으로 계산
    - 모든 데이터에 동일한 값을 더해 주거나 빼도 변하지 않음
    - 모든 데이터에 동일한 값(C)을 곱하면 분산은 $분산×C^2$으로 표준편차는 $표준편차×C$ 만큼 커짐 

#### 표준편차 계산 : std() 함수 사용

- 분산에서제곱의 영향을없앤 지표
- 분산과 표준편차가 크면 클수록 산포가 크다

```python
x = [1, 2, 3, 4, 5]
np.std(x, ddof=1)
np.std(x, ddof=0)
np.array(x).std(ddof=1)
```
#### 변동계수(CV: Coefficient of Variable)

- 표본 표준편차를 표본평균으로 나눈 값 또는 그 값에 100을 곱한 값
- 상대표준편차
- **서로 다른 평균과 표준편차를 갖는 여러 데이터의 흩어진 정도를 비교**할 때 사용
- 변동계수 값이 크다는 것은 데이터의 흩어진 정도가 상대적으로 크다는 의미

- 표본 변동계수 $𝐶𝑉=\frac{S}{\overline{x}}$,  모변동계수  $𝐶𝑉= \frac{𝜎}{𝜇}$

#### 변동계수의 필요성
- 변수 스케일링 한 후 표준편차를 구함(데이터가 모두 양수인 경우 변동계수 사용)

```python
x1 = np.array([1, 2, 3, 4, 5])
x2 = x1 * 10
np.std(x1, ddof=1)
np.std(x2, ddof=1)
```