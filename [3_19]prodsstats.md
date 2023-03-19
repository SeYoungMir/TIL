## 모평균에 관한 가설검정(One Sample t test)
### Keywords
- 일표본 t 검정(One Sample t test)
- 모평균에 관한 검정
### 모평균에 관한 추론
- 모평균에 관한 추론
  - 모평균이 정규분포를 따를때 분산이 알려지지 않을때.
  - $X \sim N[\mu,\sigma^2]$ 모평균 $\mu$
  - $X_1,...,X_n$ $\mu$ 에 관한 추론
    - 추정량 $\bar X$의 표본분포가 필요함
  - 표본평균: $\bar X = {{\Sigma^n_{i=1}x_i}\over {n}}$
- 모집단이 정규인 경우의 표본평균의 표폰분포
  - 모집단이 정규분포이고 모분산 $\sigma^2$이 알려진 경우
    - $Z = {{\bar X - \mu}\over{\sigma/\sqrt{n}}} \sim N[0,1]$
    - $\bar X \sim N[\mu,{\sigma^2 \over n}]$
  - 모집단이 정규분포이고 모분산 $\sigma^2$이 알려지지 않은 경우
    - $T = {{\bar X - \mu}\over{S/\sqrt{n}}} \sim t[n-1]$
    - 단 $S$는 표본표준편차로 $S = \sqrt{{\Sigma^{n}_{i=1}(x_i-\bar x)^2}\over {n-1}}$로 계산됨.
  ### 모평균에 관한 t-검정
  - 모평균에 관한 가설검정(One Sample t test)
    - 가설 유형
    - 관심 모수가 $\mu$이고 검정하고자 하는 모수의 경계값이 $\mu_0$라고 할 때,

<table>
    <tr><th colspan=2>단측(한쪽 꼬리)검정</th><th rowspan=2>양측(양측 꼬리) 검정</th>
    </tr>
    <tr>
        <th>왼 꼬리 검정</th><th>오른 꼬리 검정</th>
    </tr>
</table>
<td>

|$H_0:\mu = \mu_0$<br>$H_0:\mu <\mu_0$|$H_0:\mu = \mu_0$ <br>$H_0:\mu >\mu_0$|$H_0:\mu =\mu_0$<br>$H_0:\mu\neq \mu_0$|
|---|---|---|
- 검정 통계량
  - 모집단이 정규분포이고 모분산 $\sigma^2$이 알려지지 않은 경우, 
   - $T =  {{\bar X - \mu}\over{S/\sqrt{n}}} \sim t[n-1]$
   - 검정 통계량 $T$는  $H_0:\mu = \mu_0$이 사실일 때,
     -  $T =  {{\bar X - \mu_0}\over{S/\sqrt{n}}} \sim t[n-1]$를 만족함
-  유의 확률(p-value)의 계산 및 유의수준 (significance level) 100 $(1-\alpha)\%$검정법
   -  귀무가설 $H_0$가 사실인 경우의 검정 통계량$T$의 분포 $T =  {{\bar X - \mu}\over{S/\sqrt{n}}} \sim t[n-1]$에서, $t_0$(=표본 자료로부터 계산된 검정 통계량의 값)보다 대립 가설 방향으로 더 극단적인 값이 나올 확률
   -  자료로부터 계산된 유의확률 (p-value)이 주어진 유의수준 $\alpha$보다 작은 경우에 귀무가설$H_0$를 기각함
    - 유의확률(p-value)$\leq$ 유의수준$\alpha$ 면, 귀무가설$H_0$를 기각
