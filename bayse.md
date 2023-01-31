## 확률과 확률분포
### 표본공간의 분할과 전확률 공식
#### 표본공간의 분할
- B<sub>1</sub>,..B<sub>k</sub>가 다음 조건을 만족하면 표본 공간 s의 분할이라고 함.
- 서로 다른 *i,j*에 대해 *B<sub>j</sub>* $\cap$ *B<sub>j</sub>* $\varnothing$:상호배반
- *B<su>j</sub>* $\cup$ B<sub>2</sub>*$\cup$  ... $\cup$ *B<sub>k</sub>* = *S*

#### 전확률 공식
사건 *B<sub>1</sub>,B<sub>2</sub>..B<sub>k</sub>* 는 상호 배반이며 *B<su>j</sub>* $\cup$ B<sub>2</sub>*$\cup$  ... $\cup$ *B<sub>k</sub>* = *S* 라고 함
- 이 때 *S*에서 정의되는 임의의 사건 *A*에 대하여 다음이 성립
- *P(A) = P(A$\cap$ B<sub>1</sub>)+...+P(A$\cap$ B<sub>k</sub>)*
 = *P(B<sub>1</sub>)P(A|B<sub>1</sub>)+P(B<sub>k</sub>)P(A|B<sub>k</sub>)*
  
#### 베이즈 정리
  - 데이터라는 조건이 주어졌을 때의 조건부 확률을 구하는 공식
  - $P(결과|원인)$  -> $P(원인|결과)$을 구하는 방법
 - 사건 *B<sub>1</sub>,B<sub>2</sub>..B<sub>k</sub>* 는 상호 배반이며 *B<su>j</sub>* $\cup$ B<sub>2</sub>*$\cup$  ... $\cup$ *B<sub>k</sub>* = *S* 라고 함
 - 이 때 사건 A가 일어났다는 조건 하에 사건 B<sub>i<sub>가 일어날 확률은 다음과 같음
- $P(B_i|A) =  {P(A \cap B_i)\over P(A)}$ = $P(B_i)P(A|B_i)\over P(b_1)P(A|B_1)+\cdots+P(B_k)P(A|B_k)$
 - $B_1,B_2,...,B_k$으로 분할된 사건의 각 확률을 알고 각 $B_i$를 전제로 했을 때의 사건 $A$가 발생할 조건부 확률을 알 때 사건 $A$를 전제로 한 각 $B_i$의 조건부 확률을 구하기 위한 정리