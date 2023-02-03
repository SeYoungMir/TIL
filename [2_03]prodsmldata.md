## 데이터 전처리: 데이터 변환, 데이터 결합
### Keywords
- 로그 변환
- 제곱근 변환
- 박스 콕스
- 이너 조인
- 레프트 조인
- 라이트 조인
- 풀아우터 조인
#### 데이터 변환
- 자료 변환을 통해 자료의 해석을 쉽고 풍부하게 하기 위한 과정
- 데이터 변환 목적
  - 분포의 대칭화
  - 산포를 비슷하게 하기 위하여
  - 변수 간 관계를 단순하게 하기 위하여.
    - x와 y의 관계가 비선형일때 선형으로 바꾸어 단순화
- 변환 유형 1: 제곱근 변환 vs 제곱 변환
  - 제곱근의 경우 왼쪽으로 치우쳐짐
  - 제곱의 경우 오른쪽으로 치우쳐짐
- 변환 유형 2: 로그 변환 vs 지수 변환
  - 로그 변환의 경우 왼쪽으로 치우쳐짐
  - 지수 변환의 경우 오른쪽으로 치우쳐짐
- 일반화한 변환
  - 박스 콕스 변환(Box-Cox Transform)
  - p 제곱을 해준다.
  - $y= {1 \over p}((x+1)^p-1),p={1\over2},{1\over4},{1\over8},\cdots$:제곱근 유형의 변환을 일반화.
  - $y= ln(x+1),p=0$
  - $y= (1+ { x \over p})^p-1 ,p=2,4,8,\cdots$:제곱 유형의 변환을 일반화.
    - p를 무한대로 보내면 $exp(x+y)$
  - (0,0)에서 시작
  - $x=0, y'=1$
### 데이터 결합
#### 데이터 결합


<style>
    .multi{column-count:2;
         column-gap:10px;}
</style>
<div class="multi">
<p><table>
    <tr><th>X1</th><th>X2</th></tr>
    <tr><td>A</td><td>1</td></tr>
    <tr><td>B</td><td>2</td></tr>
    <tr><td>C</td><td>3</td></tr>
</table>
</p>

<p>
<table>
    <tr><th>X1</th><th>X3</th></tr>
    <tr><td>A</td><td>T</td></tr>
    <tr><td>B</td><td>F</td></tr>
    <tr><td>D</td><td>T</td></tr>
</table>
</p></div>

  - X1: 키(Key)변수
- 이너조인 (inner join)
  - 두 테이블에 키(key)가 공통으로 존재하는 레코드(record)만 결합
  - (A,1,T),(B,2,F)
- 풀아우터 조인(full outer join)
  - 두 테이블 중 어느 한 쪽이라도 존재하는 키에 대한 레코드를 모두 결합
  - (A,1,T),(B,2,F),(C,3,NA),(D,NA,T)
- 레프트 조인(left join)
  - 왼쪽 테이블에 존재하는 키에 대한 레코드를 결합
  - (A,1,T),(B,2,F),(C,3,NA)
- 라이트 조인(right join)
  - A,1,T),(B,2,F),(D,NA,T)
  