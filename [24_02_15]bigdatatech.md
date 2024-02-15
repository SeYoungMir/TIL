# 4. 스크레이핑 기본
## 2. 웹 페이지 스크레이핑
### 3. XPath와 CSS 선택자
2. CSS 선택자로 요소 지정하기
   - CSS 선택자는 웹 페이ㄷ지 또는 웹 애플리케이션을 개발해 본 사람이라면 굉장히 친숙
   - 전과 같은 HTML 소스 코드에서 h1 태그를 선택하면 CSS 선택자로는 다음과 같이 지정
    ```CSS
    html > body > h1
    ```
    - 클래스 이름을 지정할 때는 . 뒤에 클래스 이름, id 이름을 지정할 때는 # 뒤에 id 이름을 지정함
    ```CSS
    .<클래스 이름>
    #<id 이름>
    ```
### 4. HTML 소스 분석
   - XPath와 CSS 선택자 사용, 웹 페이지 HTML 소스 분석
   - 임의의 페이지의 도서 정보 페이지 분석
1.  추출하고 싶은 요소의 XPath와 CSS 선택자 추출
    - 1장에서 스크레이핑 했을 때와 마찬가지로 크롬 개발자 도구 사용
    - 크롬 개발자 도구에는 선택한 요소의 XPath 또는 CSS 선택자를 추출하는 기능 있음
    - 크롬에서 추출할 페이지의 주소로 이동, 도서 제목 부분을 마우스 오른쪽으로 클릭, 컨텍스트 메뉴에서 [검사]선택 시 개발자 도구 실행, 해당 위치 선택
    - 개발자 도구 먼저 실행, 소스 코드 내부에서 해당 위치를 찾아서 선택해도 됨
    - 스크레이핑을 테스트 하는 경우처럼 해당 페이지 HTML 구조를 제대로 이해하지 못했을 때는 [검사]를 사용하는 방법이 간편
    - 요소 선택한 상태에서 마우스 오른쪽 버튼 클릭 - 컨텍스트 메뉴 오픈 > [copy] 선택, 서브메뉴로 [copy selector]와 [copy XPath]
    - 각 메뉴 클릭하면 클립보드에 해당 선택자 내용 복사
2. lxml로 스크레이핑하기
   - lxml은 굉장히 유연하게 xml/html을 조작할 수 있게 해주는 라이브러리
   - 필요한 모듈 임포트, lxml은 매우 많은 서브 모듈 가지고 있으며, HTML 소스 파싱할 때는 lxml.html 사용
   ```python
   >>> import requests
   >>> import lxml.html
   ```
   - 일단 Requests를 사용 ,HTML 소스 코드를 가져옴
   - URL 지정, get 메서드를 호출
   - 반환값은 Response 클래스, 멤버 변수 text로 HTML 소스 코드를 추출 가능, 이를 변수에 저장
   ```python
   >>> r = requests.get("<링크>")
   >>> html = r.text
   ```
   - 추출한 HTML 소스 코드를 lxml을 사용, HtmlElement 클래스의 객체로 변환, 그 다음 매개 변수에 HTML 소스 코드를 지정, fromstring 메서드 호출
   ```python
   >>> root = lxml.html.fromstring(html)
   ```
   - HtmlElement의 xpath 메서드에 XPath를 지정, 요소 추출.
   - 이전에 크롬 개발자 도구를 사용해서 확인한 XPath 지정.
   - 결과는 리스트로 반환
   ```python
   >>> titleElement = root.xpath('<추출한 XPath 주소>')
   ```
   - 추출한 요소(li 태그)의 텍스트가 도서 제목, HtmlElement 클래스의 멤버 변수로 텍스트 추출
   ```python
   >>> titleElement[0].text
   ```
   - 텍스트 이외에도 태그 이름, 태그의 속성 등도 추출 가능
   ```python
   >>> titleElement[0].tag
   >>> titleElement[0].attrib
   ```