## 1. 기본문법 활용하기 - 이어서
### 4. 데이터 타입
1. C언어 기준 기본 프로그래밍
    ```C
    1 #include <stdio.h>
    2 void main()
    3 {
    4     //...
    5 }
    ```

   1. 선행처리 지시자
   2. 프로그램 시작 함수
   3. 프로그램의 시작
   4. 알고리즘 실행 문장
   5. 프로그램의 종료
2. 데이터 타입
   - 변수가 저장할 데이터가 정수인지, 실수인지, 아니면 또 다른 어떤 데이터인지를 지정하는 것
     - 표준 자료형
       - 정수형 
         - short
         - int
         - long
       - 실수형
         - float
         - double
         - long double
       - 문자형
         - char
3. 변수의 선언
    ```C
    int num1; // 변수 선언
    int num2; // 변수 선언
    int num1,num2; //여러개 변수 선언
    ```
4. 변수 / 상수
   1. 변수(variable) : 저장된 값의 변경이 가능한 공간
   2. 상수(constant) : 저장된 값의 변경이 불가능한 공간 (데이터 선언때 초기화)
5. 데이터
   1. 정수형 데이터
      - int
   2. 실수형 데이터
      - float,double
   3. 문자형 데이터
      - char
6. 자료형의 종류
   1. 정수형
      - 정수 값을 표현하는 자료형
      - 소수 값이 없는 음수, 0, 양수를 가짐
    <table>
        <tr>
            <th colspan=3>구분</th>
            <th>설명</th>
            <th>바이트 수</th>
            <th>범위</th>
        </tr>
        <tr>
            <td rowspan=6>정수형</td>
            <td rowspan=3>부호 있음</td>
            <td>short</td>
            <td>short형 정수</td>
            <td>2</td>
            <td>-32768~32767</td>
        </tr>
        <tr>
            <td>int</td>
            <td>정수</td>
            <td>4</td>
            <td>-2147483648~2147483647</td>
        </tr>
        <tr>
            <td>long</td>
            <td>long형 정수</td>
            <td>4</td>
            <td>-2147483648~2147483647</td>
        </tr>
        <tr>
            <td rowspan=3>부호 없음</td>
            <td>unsigned short</td>
            <td>부호 없는 short형 정수</td>
            <td>2</td>
            <td>0~65535</td>
        </tr>
        <tr>
            <td>unsigned int</td>
            <td>부호 없는 정수</td>
            <td>4</td>
            <td>0~4294967295</td>
        </tr>
        <tr>
            <td>unsigned long</td>
            <td>부호 없는 long형 정수</td>
            <td>4</td>
            <td>0~4294967295</td>
        </tr>
    </table>

   2. 문자형
      - ASCII 코드 표 기반의 하나의 문자를 저장하는 자료형
      - 문자의 크기 8bit - 문자형에 정수 값을 표현할 수 있음.(-128~127 크기)
      - unsigned 수정자를 포함할 수 있음
        <table>
            <tr>
                <th colspan=3>구분</th>
                <th>설명</th>
                <th>바이트 수</th>
                <th>범위</th>
            </tr>
            <tr>
                <td rowspan=2>문자형</td>
                <td>부호 있음</td>
                <td>char</td>
                <td>문자 및 정수</td>
                <td>-128~127</td>
            </tr>
            <tr>
                <td>부호 없음</td>
                <td>unsigned char</td>
                <td>문자 및 부호 없는 정수</td>
                <td>1</td>
                <td>0~255</td>
            </tr>
        </table>
   3. 실수형
      - 소수점이 존재하는 수치 표현
      - float형 : 32bit를 이용한 실수 표현
      - double형 : 64bit를 통한 실수 표현
      - 보다 큰 수를 표현을 위해 수정자 long이 사용 가능함
        <table>
            <tr>
                <th colspan=2>구분</th>
                <th>설명</th>
                <th>바이트 수</th>
                <th>범위</th>
            </tr>
            <tr>
                <td rowspan=2>부동 소수점형</td>
                <td>float</td>
                <td>단일 정밀도 부동 소수점</td>
                <td>4</td>
                <td>1.2E-38~3.4E38</td>
            </tr>
            <tr>
                <td>double</td>
                <td>두 배 정밀도 부동소수점</td>
                <td>8</td>
                <td>2.2E-308~1.8E308</td>
            </tr>
        </table>
    4. 그 외의 타입
        <table>
            <tr>
                <th colspan=2>구분</th>
                <th>설명</th>
                <th>바이트 수</th>
                <th>범위</th>
            </tr>
            <tr>
                <td>열거형</td>
                <td>enum</td>
                <td>사용자 정의 열거형</td>
                <td>4</td>
                <td>0~4294967295</td>
            </tr>
            <tr>
                <td>배열형</td>
                <td>[]</td>
                <td>변수의 배열형</td>
                <td>n</td>
                <td></td>
            </tr>
            <tr>
                <td>포인터형</td>
                <td>*</td>
                <td>메모리 주소 저장</td>
                <td>4</td>
                <td></td>
            </tr>
            <tr>
                <td>구조체형</td>
                <td>struct</td>
                <td>변수의 집합</td>
                <td>n</td>
                <td></td>
            </tr>
            <tr>
                <td>공영체형</td>
                <td>union</td>
                <td>변수의 공용</td>
                <td>1~8</td>
                <td>가장 큰 변수의 값</td>
            </tr>
        </table>