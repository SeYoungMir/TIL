# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 5. 단위 테스트 생성.
2. 테스트 대상 코드와 테스트 코드 준비
   1. 테스트 대상 코드 생성.
      - 테스트 대상 코드 scraper.py를 생성. 다음처럼 입력. 이는 오류를 반환하는 코드
      - ```python
        from bs4 import BeautifulSoup

        class ScraperException(Exception):
            """스크레이핑 예외"""

        def scrape_title(html):
            """<title> 태그의 내용 반환."""
            soup = BeautifulSoup(html,"htm.parser")
            title_elm = soup.find('title')
            if title_elm is None:
                raise ScraperException('title 태그 존재하지 않음.')
            title = title_elm.text
            if not title:
                raise ScraperException('title 태그에 내용이 없음.')
            return title_elm.text
        ```
        - 매개 함수 html을 BeautifulSoup 함수로 파싱. `<title>`요소를 추출. 다음 해당 내용을 문자열로 반환하는 함수.
        - class 부분에서는 스크레이핑 처리에서 발생시킬 사용자 정의 예외 클래스 ScraperException를 정의
        - soup 부분에서는 매개 변수 html의 내용을 BeautifulSoup로 파싱, find 태그로 `<title>` 태그 요소를 추출
        - if 문에서 find 메서드로 `<title>`태그가 찾아지지 않아서 결과가 None일 때, 사용자 정의 예외 ScraperException을 발생시키게 함.