## 모평균 비교에 관한 가설검정(Two way ANOVA)
### Keywords
- 요인설계
- 이원배치 분산분석(Two way ANOVA)
- 상호작용 효과
### 이원배치 분산분석(Two way ANOVA)
- One way ANOVA
  - 하나의 factor가 주어졌을 때, 그룹이 k개로 구분되면 평균차이가 있는가?
- Two way ANOVA
  - factor가  두 개인 ANOVA
  - 각각의 factor 별로 미치는 효과
  - 두개의 factor에 대한 상호작용 효과
### 요인 설계 및 이원배치 분산분석 개요
- 요인설계(Factorial Design)
  - 반응변수에 영향을 미치는 요인의 수가 여러개인 경우, 요인 설계(factorial design)을 적용해야 함
- 이원배치 분산분석(Two way ANOVA)
  - 가장 단순한 요인설계 분석법으로, 요인이 2개, 각 요인 별 처리 수준이 2개 이상인 경우.
    - 주 효과: 각 요인 별 처리수준 간의 모평균 차이에 관한 분석
    - 상호작용 효과: 두 요인 간 상호작용에 관한 분석
  - 완전 확률화 과정: 실험대상은 각 요인의 처리수준별 조합(셀)에 무작위로 배치됨
  - 가정: 정규, 등분산,독립
  - 이원배치 분산분석 자료구조(각 셀 별 반복수 n이 동일한 경우)

<table>
    <tr rowspan=2, colspan=2><th colspan=3>요인B</th><th rowspan=2>평균</th>
    </tr>
    <tr><th>처리1</th><th>...</th><th>처리b</th>
    </tr>
    <tr><th rowspan=4>요인A</th><td>처리1</td><td>y111,...,y11n</td><td>...</td><td>y1b1,...,y1bn</td><td>ybar1..</td></tr>
    <tr><td>처리2</td><td>y211,...,y21n</td><td>...</td><td>y2b1,...,y2bn</td><td>ybar2..</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td>
    <tr><td>처리a</td><td>ya11,...,ya1n</td><td>...</td><td>yab1,...,yabn</td><td>ybar a..</td></tr>
    <tr><th>평균</th><td>bar y .1.</td><td>...</td><td>bar y.b.</td><td>bar y ...</td>
</table>

- 제곱합의 분해
$SST = SSA + SSB + SSAB+ SSE$
<br>
총 변동성 = 요인 A 처리변동+ 요인 B 처리변동+ 요인 A,B의 상호작용변동 + 오차변동
<br>
$(abn-1) = (a-1)+(b-1)+(a-1)(b-1)+ab(n-1)$
<br>
$MSA = {{SSA} \over {a-1}}$
$MSB = {{SSB} \over {b-1}}$
$MSAB = {{SSAB} \over {(a-1)(b-1)}}$
$MSE = {{SSE} \over ab(n-1)}$
<br>
factor a의 효과가 있으면 MSE보다 MSA가 큼
factor b의 효과가 있으면 MSE보다 MSB가 큼
factor a,b의 상호작용효과가 있으면 MSE보다 MSAB가 큼

- 이원배치 분산분석의 가설 검정 절차
  - 가설
  1. 요인A의 처리 효과에 관한 가설
     - $H_0$요인 A의 처리 그룹간 평균의 차이가 없음, 처리효과없음
     - $H_1$요인 A의 처리 그룹간 평균의 차이가 존재, 처리효과있음
  2. 요인B의 처리 효과에 관한 가설
     - $H_0$요인 B의 처리 그룹간 평균의 차이가 없음, 처리효과없음
     - $H_1$요인 B의 처리 그룹간 평균의 차이가 존재, 처리효과있음
  3. 요인A와 요인B의 상호작용 효과에 관한 가설
     - $H_0$요인 A와 요인B의 상호작용 효과가 없음
     - $H_1$요인 A와 요인B의 상호작용 효과가 존재.
  - 검정통계량의 표본분포
    1. 요인 A의 처리효과
       - 요인 A에 관한 $H_0$이 사실인 경우,
       - $F_1= {{MSA}\over{MSE}}={{SSA/(a-1)}\over{{SSE}/ab(n-1)}} \sim F[(a-1),(ab(n-1))]$를 따름
    2. 요인 B의 처리효과
       - 요인 B에 관한 $H_0$이 사실인 경우,
       - $F_2= {{MSB}\over{MSE}}={{SSB/(b-1)}\over{{SSE}/ab(n-1)}} \sim F[(b-1),(ab(n-1))]$를 따름
  3. 요인 A와 요인 B의 상호작용효과
       - 요인 A와 요인 B의 상호작용에 관한 $H_0$이 사실인 경우,
       - $F_3= {{MSAB}\over{MSE}}={{SSAB/(a-1)(b-1)}\over{{SSE}/ab(n-1)}} \sim F[(a-1)(b-1),(ab(n-1))]$를 따름
  - 유의확률(p-value)의 계산
    - 귀무가설($H_0$)이 사실일 때, 검정통계량의 분포에서, $f_0$(=표본 자료로부터 계산된 검정통계량의 값)보다 더 큰 값이 나올 확률
 - 유의수준 (significance level) 100 $\alpha\%$검정법
  - 자료로부터 계산된 유의확률(p-value)이 주어진 유의수준$\alpha$보다 작은 경우에 귀무가설 $H_0$를 기각함
  - p-value$\leq \alpha$면 $H_0$을 기각
  분산분석표

|<br>|제곱합|자유도|평균제곱|F값|
|---|---|---|---|---|
|요인 A|$SSA$|$a-1$|$MSA(={SSA\over a-1})$|${MSA \over MSE}$|
|요인 B|$SSB$|$b-1$|$MSB(={SSB\over b-1})$|${MSB \over MSE}$|
|요인 A와 요인 B의 상호작용|$SSAB$|$(a-1)(b-1)$|$MSAB(={SSAB\over (a-1)(b-1)})$|${MSAB \over MSE}$|
|잔차|$SSE$|$ab(n-1)$|$MSE(={SSE\over(ab(n-1))})$|<br>|
|합계|$SST$|$N(=abn)-1$|<br>|<br>|