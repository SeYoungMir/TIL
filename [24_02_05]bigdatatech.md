# 3. 크롤러 및 스크레이핑 개발 환경 준비와 파이썬 기본
## 3. 파이썬 기초
### 3. 숫자 자료형
1. 정수(int), 부동소수점(float), 복소수(complex)
   - 파이썬의 숫자 자료형은 크게 정수(int), 부동소수점(float), 복소수(complex)로 나눌 수 있음. 숫자 자료형을 다룰 때는 다음 두 가지 사항에 주의
     - 정수와 부동소수점을 계산하면 부동소수점
     - 정수와 정수를 나누면 부동소수점
   - // 연산자를 사용하면 나눴을 때 소수 부분을 버리고 정수 결과를 얻을 수 있음(몫)
   - 복소수를 다루는 프로그래밍 언어는 거의 없으므로 처음 본다면 익숙하지 않을 수 있음.
   - 수학에서는 허수 단위를 나타낼 때 i를 사용하는 것이 일반적, 파이썬에서는 j를 사용, (1+2j) 처럼 허수 단위를 표현
2. 숫자 연산자
   - 숫자 연산자는 다음과 같음
    <table>
        <tr>
            <th>연산자</th>
            <th>설명</th>
        </tr>
        <tr>
            <td>+</td>
            <td>덧셈</td>
        </tr>
        <tr>
            <td>-</td>
            <td>뺄셈</td>
        </tr>
        <tr>
            <td>*</td>
            <td>곱셈</td>
        </tr>
        <tr>
            <td>/</td>
            <td>나눗셈</td>
        </tr>
        <tr>
            <td>//</td>
            <td>몫</td>
        </tr>
        <tr>
            <td>**</td>
            <td>제곱</td>
        </tr>
    </table>
### 4. 문자열
- 파이썬은 문자열을 str 자료형과 bytes 자료형이라는 두 가지 자료형으로 다룸. str 자료형은 유니코드를 사용해서 문자열을 다룰 때 사용하며, bytes 자료형은 바이트열을 사용해 문자열을 다룰 때 사용.
- 기본적으로 대부분의 문자열 조작은 모두 str 자료형을 사용, 파일을 읽고 쓸 때와 네트워크의 내용을 읽고 쓸 때 bytes 자료형을사용
1. 검색하기
   - 지정한 문자열을 검색해서 몇 개 포함되어 있는지 반환해주는 count 메서드, 찾는 단어가 처음으로 나오는 인덱스(위치)를 반환하는 find 메서드가 있음.
   - 두 가지 모두 검색 시작 위치와 종료 위치를 지정할 수 있음. 시작 위치와 종료 위치를 생략하면 문자열 전체를 대상으로 검색
    ```python
    count("검색할 문자열")
    count("검색할 문자열", <시작 위치>)
    count("검색할 문자열", <시작 위치>, <종료 위치>)
    ```
    ```python
    find("검색할 문자열")
    find("검색할 문자열",<시작 위치>)
    find("검색할 문자열", <시작 위치>, <종료 위치>)
    ```
    - count 메서드와 find 메서드 사용예시
    ```python
    string="example message"
    string.count("a")
    string.find("a")
    ```
   - 이 때 인덱스는 0부터 세므로 실제 3번째에 문자가 위치하면 문자 2 반환, 문자가 존재하지 않으면 -1을 반환
2. 대문자와 소문자 변환
   - str 자료형에는 upper 메서드와 lower 메서드가 있으며 이를 사용하면 이름 그대로 대문자와 소문자로 변환 가능
    ```python
    # 예시
    >>> string = "aBc"
    >>> string.upper()
    'ABC'
    >>> string.lower()
    'abc'
    >>> print(string)
    aBc
    ```
    - upper 메서드와 lower 메서드는 자기 자신을 변환시키지 않음. 