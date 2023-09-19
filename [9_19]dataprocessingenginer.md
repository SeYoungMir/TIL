## 2. 명령문 및 함수
- 프로그래밍 언어의 연산자와 명령문을 사용하여 애플리케이션에 필요한 기능을 정의하고 사용할 수 있음
### 1. 연산자
1. 산술 연산자
   1. 컴퓨터의 명령어 집합 가운데 가장 기본적이며 중요한 명령으로서 산술 명령이 있음
   2. 산술 명령은 사칙 연산임
   3. 덧셈(+), 뺄셈(-), 곱셈($\times$),나눗셈(/),제곱 또는 지수(**) 등의 기호를 가리킴
    <table>
        <tr>
            <th>연산자</th>
            <th>기능</th>
            <th>예시</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>+</td>
            <td>더하기</td>
            <td>c=a+b</td>
            <td>a에 b를 더해 c에 대입</td>
        </tr>
        <tr>
            <td>-</td>
            <td>빼기</td>
            <td>c=a-b</td>
            <td>a에서 b를 빼서 c에 대입</td>
        </tr>
        <tr>
            <td>*</td>
            <td>곱하기</td>
            <td>c=a*b</td>
            <td>a에 b를 곱해 c에 대입</td>
        </tr>
        <tr>
            <td>/</td>
            <td>나누기</td>
            <td>c=a/b</td>
            <td>a에서 b를 나눠 c에 대입</td>
        </tr>
        <tr>
            <td>%</td>
            <td>나머지</td>
            <td>c=a%b</td>
            <td>a에서 b를 나눈 값의 나머지를 c에 대입</td>
        </tr>
    </table>
   2. 비트 연산자(&,|,^,~)
      1. bit는 0 혹은 1의 값을 가지는 문자형 혹은 정수형 변수 값
      2. bit 연산자는 문자형 혹은 정수형에만 적용
      <table>
        <tr>
            <th>연산자</th>
            <th>기능</th>
            <th>예시</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>&</td>
            <td>bitwise AND</td>
            <td>10 & 20</td>
            <td>10과 20을 AND 연산</td>
        </tr>
        <tr>
            <td>|</td>
            <td>bitwise OR</td>
            <td>10|20</td>
            <td>10과 20을 OR 연산</td>
        </tr>
        <tr>
            <td>^</td>
            <td>bitwise XOR</td>
            <td>10^3</td>
            <td>10과 20을 XOR 연산</td>
        </tr>
        <tr>
            <td>~</td>
            <td>complement</td>
            <td>~1</td>
            <td>1(참)이면 0(거짓)<br>0(거짓)이면 1(참)</td>
        </tr>
    </table>
   3. 관계 연산자(relational operator)(<,<=,==,!=)
      1. 각 관계식은 참(true) 혹은 거짓(false)로 판별됨
      2. 참(True : 1), 거짓(False : 0)
      <table>
        <tr>
            <th>연산자</th>
            <th>기능</th>
            <th>예시</th>
            <th>내용</th>
        </tr>
        <tr>
            <td><</td>
            <td>크다, 작다</td>
            <td>a<b</td>
            <td>a는 b보다 작다</td>
        </tr>
        <tr>
            <td>>=</td>
            <td>크거나 같다</td>
            <td>a>=b</td>
            <td>a는 b보다 크거나 같다</td>
        </tr>
        <tr>
            <td>==</td>
            <td>같다</td>
            <td>a==b</td>
            <td>a는 b와 같다</td>
        </tr>
        <tr>
            <td>!=</td>
            <td>다르다</td>
            <td>a!=b</td>
            <td>a는 b와 같지 않다</td>
        </tr>
    </table>
   4. 연산자 우선순위(relational operator)
      - 우선 순위가 같을 때는 왼쪽부터 연산을 수행함
      - 위에서 아래로 내려오면서 연산자의 우선 순위가 낮아짐
    <table>
        <tr>
            <td>!,++,:</td>
            <td rowspan=6>순위 높음<br><br><br><br><br>순위 낮음</td>
        </tr>
        <tr>
            <td>*,/</td>
        </tr>
        <tr>
            <td><,>,==,!=</td>
        </tr>
        <tr>
            <td>&&</td>
        </tr>
        <tr>
            <td>||</td>
        </tr>
        <tr>
            <td>=</td>
        </tr>
    </table>