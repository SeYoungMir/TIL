## 모평균 비교에 관한 가설검정(F-test of equality of variances)
### Keywords
- 등분산 F검정(F-test of equality of variances)
- Bartlett 검정
- Levene 검정
### 두 모집단의 모분산 비교
- 두 모집단의 모분산($\sigma_1^2/\sigma_2^2$)차이
  - 독립인 두 표본
  - $\theta =\sigma_1^2/\sigma_2^2$에 관한 추론 $\rarr$ 추정량($\hat\theta =\sigma_1^2/\sigma_2^2$)의 표본분포룰 이용
  - $X = ({\sigma_1^2\over \sigma_2^2})\cdot({S_1^2\over S_2^2})\sim F[n_1-1,n_2-1]$
### 모분산 비교 F 검정
- 모평균 비교에 관한 가설검정(F-test of equality of variances)
- 가설유형
    - 관심 모수가 $\sigma_1^2/\sigma_2^2$이고 검정하고자 하는 모수의 경계값은 1가 되므로,
- <table>
    <tr><th colspan=2>단측(한쪽 꼬리)검정</th><th rowspan=2>양측(양측 꼬리) 검정</th>
    </tr>
    <tr>
        <th>왼 꼬리 검정</th><th>오른 꼬리 검정</th>
    </tr>
</table>
<td>

|$H_0:\sigma_1^2/\sigma_2^2=1$<br>$H_1:\sigma_1^2/\sigma_2^2 <1$|$H_0:\sigma_1^2/\sigma_2^2=1$ <br>$H_1:\sigma_1^2/\sigma_2^2>1$|$H_0:\sigma_1^2/\sigma_2^2=1$<br>$H_1:\sigma_1^2/\sigma_2^2\neq 1$|
|---|---|---|
  - 검정통계량
    - 두 모집단이 모두 정규분포인 경우 다음의 검정통계량$X$는 귀무가설$H_0:\sigma_1^2/\sigma_2^2=1$이 사실일 때,<br> $X =1 \cdot({S_1^2\over S_2^2})\sim F[n_1-1,n_2-1]$ 를 만족함
  - 유의확률(p-value)의 계산
    - 귀무가설 $H_0$가 사실일 때, 검정통계량 $X$의 분포 $X =({S_1^2\over S_2^2})\sim F[n_1-1,n_2-1]$에서, $x_0$(=표본 자료로부터 계산된 검정통계량의 값) 보다 대립가설 방향으로 더 극단적인 값이 나올 확률
  - 유의수준 (significance level) 100 $\alpha\%$검정법
    - 자료로부터 계산된 유의확률(p-value)이 주어진 유의수준$\alpha$보다 작은 경우에 귀무가설 $H_0$를 기각함
    - p-value$\leq \alpha$면 $H_0$을 기각