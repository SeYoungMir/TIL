## 모평균 비교에 관한 가설검정(independent two sample t test)
### keywords
- 독립 이표본 t 검정(two sample t test)
- 모평균 비교
### 모평균 비교에 관한 추론
- 두 모집단의 모평균($\mu_1 -\mu_2$)차이
  - 독립인 두 표본
  - 등분산 가정:$\sigma_1^2=\sigma_2^2=\sigma^2$
  - 정규 모집단
  - $\theta = \mu_1 -\mu_2$에 관한 추론 $\rarr$추정량$(\hat\theta = \bar X_1 - \bar X_2)$의 표본분포를 이용.

- 추정량$(\hat\theta = \bar X_1 - \bar X_2)$의 표본분포
  - 두 모집단이 정규분포이고, 모분산 $\sigma^2$이 알려지지 않았지만 동일한 것으로 가정, 두 표본은 독립.
  - $\bar X_1 - \bar X_2\sim N[\mu_1 -\mu_2,\sigma^2(1/n_1+1/n_2)]$
  - $Z={{\bar X_1 - \bar X_2-(\mu_1 -\mu_2)}\over{\sqrt{\sigma^2(1/n_1+1/n_2)}}}\sim N[0,1]$
- 추정량$(\hat\theta = \bar X - \bar Y)$의 표본분포
  - $Z={{\bar X_1 - \bar X_2-(\mu_1 -\mu_2)}\over{\sqrt{S_p^2(1/n_1+1/n_2)}}}\sim t[n_1+n_2-2] \rarr$여기서 $S_p^2$는 합동분산추정량임
  - $S_p^2={{(n_1-1)S^2_1+(n_2-1)S^2_2} \over {n_1+n_2-2}}$

- 모평균 비교에 관한 독립 이표본 t-검정(independent two sample t test)
  - 가설 유형
    - 관심 모수가 $\mu_1 -\mu_2$이고 검정하고자 하는 모수의 경계값은 0가 되므로
 <table>
    <tr><th colspan=2>단측(한쪽 꼬리)검정</th><th rowspan=2>양측(양측 꼬리) 검정</th>
    </tr>
    <tr>
        <th>왼 꼬리 검정</th><th>오른 꼬리 검정</th>
    </tr>
</table>
<td>

|$H_0:\mu_1 - \mu_2=0$<br>$H_1:\mu_1 -\mu_2<0$|$H_0:\mu_1 -\mu_2=0$ <br>$H_1:\mu_1-\mu_2>0$|$H_0:\mu_1 -\mu_2=0$<br>$H_1:\mu_1\neq \mu_2$|
|---|---|---|
- 검정통계량
  - 검정통계량 $T$는 귀무가설$H_0:\mu_1 - \mu_2=0$이 사실일 때, 
  - $T={{\bar X_1 - \bar X_2}\over{\sqrt{S_p^2(1/n_1+1/n_2)}}}\sim t[n_1+n_2-2]$를 만족함
- 유의확률(p-value)의 계산
  - 귀무가설$H_0:\mu_1 - \mu_2=0$이 사실일 때,
  - 검정통계량 $T$의 분포 $T={{\bar X_1 - \bar X_2}\over{\sqrt{S_p^2(1/n_1+1/n_2)}}}\sim t[n_1+n_2-2]$에서, $t_0$(=표본 자료로부터 계산된 검정통계량의 값)보다 대립가설 방향으로 더 극단적인 값이 나올 확률
- 유의수준 (significance level) 100 $\alpha\%$검정법
  - 자료로부터 계산된 유의확률(p-value)이 주어진 유의수준$\alpha$보다 작은 경우에 귀무가설 $H_0$를 기각함
  - p-value$\leq \alpha$면 $H_0$을 기각