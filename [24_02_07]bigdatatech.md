# 3. 크롤러 및 스크레이핑 개발 환경 준비와 파이썬 기본
## 3. 파이썬 기초
### 6. 제어 구문
1. 조건 분기 : if 조건문
   - if 조건문으로 조건 분기
   - 다른 언어와 다른 특징적인 부분은 {}로 스코프를 나타내는 게 아니라 들여쓰기로 스코프를 나타냄
   - 파이썬에서는 들여쓰기가 코드를 쉽게 볼 수 있도록 하는 기능 뿐만 아니라 스코프를 나타내는 중요한 역할을 함
   - 간단한 if 조건문
   ```python
   if <조건식>:
      <처리>
   ```
   - 여러 조건을 가진 if 조건문
   ```python
   if <조건식 1>:
        <처리 1>
   elif <조건식 2>:
        <처리 2>
   else :
        <처리 3>
   ```
   - 조건식은 다음 표를 참고할 수 있음
   <table>
        <tr>
            <th>식</th>
            <th>설명</th>
        </tr>
        <tr>
            <td>a==b</td>
            <td>a와 b가 같을 때 True</td>
        </td>
        <tr>
            <td>a!=b</td>
            <td>a와 b가 다를 때 True</td>
        </tr>
        <tr>
            <td>a<b</td>
            <td>a가 b보다 작을때 True</td>
        </tr>
        <tr>
            <td>a<=b</td>
            <td>a가 b보다 작거나 같을때 True</td>
        </tr>
        <tr>
            <td>a>b</td>
            <td>a가 b보다 클 때 True</td>
        </tr>
        <tr>
            <td>a>=b</td>
            <td>a가 b보다 크거나 같을때 True</td>
        </tr>
        <tr>
            <td>a and b</td>
            <td>a 와 b가 모두 True일 때 True</td>
        </tr>
        <tr>
            <td>a or b</td>
            <td>a 와 b 중의 하나가 True일 때 True</td>
        </tr>
        <tr>
            <td>not a</td>
            <td>a 가 False일 때 True</td>
        </tr>
        <tr>
            <td>a is b</td>
            <td>a와 b가 같은 객체일 때 True</td>
        </tr>
        <tr>
            <td>a is not b</td>
            <td>a와 b가 다른 객체일 때 True</td>
        </tr>
   </table>
   - 파이썬은 조건식 문자열 "", 빈 리스트 [], 빈 튜플()를 입력하면 이를 거짓으로 보게 됨
2. 반복 제어 : for, while 반복문
   - 처리를 반복할 때 사용하는 구문으로 for 반복문과 while 반복문이 있음.
   - 두 가지 반복문 모두 중간에 반복을 중지하는 break 구문과 다음 반복으로 넘어가는 continue 구문을 사용 가능
   - for 반복문
   ```python
   for <변수> in <리스트,튜플,문자열 등>:
        <처리>
   else:
        <최종적으로 할 처리>
   ```
   - while 반복문
   ```python
   while <조건식>:
        <처리>
   else:
        <최종적으로 할 처리>
   ```
   - 자료 구조 리스트를 for 반복문으로 반복하려면 다음과 같음
   ```python
   for x in [1,2,3]:
        print(x)
   ```
   - 단순하게 지정한 횟수만큼 반복하고 싶다면 range 함수 사용
   ```python
   for x in range(5):
    print(x) # 0부터 4까지 차례대로 출력
   ```