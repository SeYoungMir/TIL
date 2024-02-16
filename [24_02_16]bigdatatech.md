# 4. 스크레이핑 기본
## 2. 웹 페이지 스크레이핑
### 4. HTML 소스 분석 - 이어서
2. lxml로 스크레이핑하기
   - CSS 선택자를 사용한 스크레이핑
     - 인터넷 서점으로 이동하는 링크의 소스 코드
    ```html 
    <ul id="book-stores" class="unstyled">
        <li>
            <a href = '<인터넷서점1>'>
                <img src="<인터넷서점1 이미지>">
            </a>
        </li>
        <li>
            <a href = '<인터넷서점2>'>
                <img src="<인터넷서점2 이미지>">
            </a>
        </li>
        <li>
            <a href = '<인터넷서점3>'>
                <img src="<인터넷서점3 이미지>">
            </a>
        </li>
    </ul>
    ```
    - CSS 선택자로 요소를 추출할 때는 HtmlElement 클래스의 cssselect 메서드 사용
    ```python
    >>> linkAs = root.cssselect('#book-stores>li>a')
    >>> for linkA in linkAs:
            print(linkA.arrtib["href"])
    ```
## 3. RSS 스크레이핑
### 1. 라이브러리 설치
1. feedparser
   - RSS를 파싱할 때는 feeparser를 사용
   - Feedparser는 RSS 1.0 , RSS 2.0, Atom등의 여러 사양에 모두 대응해서 같은 형식으로 사용할 수 있게 해줌
   - 굉장히 편리하게 스크레이핑 가능, pip install 명령어 사용해 설치
    ```linux
    $ pip install feedparser
    ```
2. XML 분석하기
   - RSS는 알라딘 서점의 일부를 사용
   - URL에 접근하면 RSS 사양의 응답을 받을 수 있음.
   - feedparser는 굉장히 쉽게 사용할 수 있는 라이브러리로, parse 메서드에 URL을 지정해서 호출하기만 하면 RSS 피드를 읽어들인 뒤 알아서 파싱해줌
    ```python
    >>> import feedparser
    >>> rss = feedparser.parse("<RSS 링크>")
    >>> print(rss)
    ``` 
   - parse 메서드는 FeedParserDict 클래스의 객체 (인스턴스)를 반환
   - 이 객체는 딕셔너리처럼 다루어짐.
   - 피드 정보는 feed 키에 들어있음.