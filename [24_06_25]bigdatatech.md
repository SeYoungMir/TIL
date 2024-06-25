# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 5. 단위 테스트 생성.
2. 테스트 대상 코드와 테스트 코드 준비
   1. 테스트 대상 코드 생성. - 이어서
      - title 부분에서는 타이틀 태그 요소에서 해당 내용울 text 속성으로 참조해서 추출
      - if not title 부분에서는 위에서 추출한 `<title>`태그의 내용이 빈 문자열일 때, 사용자 정의 예외 ScraperException를 발생시키게 함.
    2. 테스트 코드 생성.
      - scraper.py에 정의한 scrape_title 함수를 테스트하기 위한 테스트 코드를 만듦. 테스트 코드 test_scraper.py를 만들고 다음처럼 입력
      - ```python
        import pytest

        from scraper import ScraperException, scrape_title

        def test_scraper_title():
            html="""<html>
            <title>제목</title>
            <body>
            <p>내용</p></body>
            </html>"""

            assert scrape_title(html) == "제목"

            html_without_title="""<html>
            <body><p>내용</p></body>
            </html>"""

            with pytest.raises(ScraperException)as e:
                scrape_title(html_without_title)
                assert 'title 태그 미존재.' == e.value
            html_empty_title = """<html>
            <title></title>
            <body><p>내용</p></body>
            </html>"""

            with pytest.raises(ScraperException) as e:
                scrape_title(html_empty_title)
                assert 'title 태그에 내용 미존재.' == e.value
        ```
        