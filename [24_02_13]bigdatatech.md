# 4. 스크레이핑 기본
## 2. 웹 페이지 스크레이핑\
### 2.  웹에 있는 리소스 추출
2. Requests의 응답
   - 웹 API에 Requests 모듈로 요청 전송, Requests 모듈의 사용 방법 탐색
   - 추출이 정상적으로 완료되었는지 나타내는 상태 코드를 확인하는 방법
     - GET 등의 메서드 반환 값은 Response 클래스, Response 클래스의 멤버 변수 status_code에 접근 시 상태 코드 확인 가능
    ```python
    >>> import requests
    >>> r = requests.get(<목표 API 주소>)
    >>> r.status_code
    ```
  - 응답 본문(Body)는 두 가지 방법으로 추출 가능. byte 자료형일때는 멤버 변수 content에, str 자료형일때는 멤버 변수 texttest에 접근
    ```python
    >>> r.text
    ```
3. JSON 파싱하기
   - Response 클래스에는 json이라는 편리한 메서드 존재, body가 JSON 형식이라면 이를 파싱(분석)해서 딕셔너리 자료형으로 만들어주는 메서드
   - 예를 들면 네이버 검색어 순위 데이터는 다음과 같은 방식으로 추출
    ```python
    >>> json = r.json()
    >>> for rank in json["data"][]["data"]:
            print(rank["rank"],"",rank["keyword"])
    ```
### 3. XPath와 CSS 선택자
- XPath는 XML Path Language의 줄임말
- 표준화 단체 W3C에 의해 개발된 마크업 언어인 XML로 작성된 문서의 특정 부분을 선택할 때 사용하는 언어
- 2014년에 버전 3.0이 권고되었으며, 공식 문서는 XML Path Language(XPath)3.0에서 확인 가능
  - XML Path Language(XPath)3.0 [http://www.w3.org/TR/xpath-30/]
1. XPath로 요소 지정하기
   - 예시 HTML 소스 코드
    ```HTML
    <html>
        <body>
            <h1>도서</h1>
            <div class = "book">
                <p class="title">책 제목 예시</p>
                <a href="<책 상대주소>">
            </div>
        </body>
    </html>
    ```
   - 위 HTML 소스에서 h1 요소의 위치는 XPath로 다음과같음
    `/html/body/h1`
    - 이러한 위치 지정을 '로케이션 패스'라고 하고, 디렉터리 경로처럼 'html 요소' > 'body 요소' > 'h1 요소'를 찾아가는 것처럼 표현
    - 위의 경로는 절대 경로, XPath의 상대 경로 표기도 있음.
    - 앞에 슬래시가 없다면 상대 경로 의미. 현재 위히가 h1 태그일 때 하나 위의 계층을 body이고 이는 다음과 같이 표현.
    `../`
    - 앞이 //로 시작하는 경우 전체 요소를 대상으로 함. //div라고 입력하면 HTML 소스 내부의 모든 div 지정