# 6. 스크레이핑 개발(응용)
## 5. Scrapy를 사용해서 스크레이핑
### 1. 다양한 스크레이핑 - 이어서
6. 크롤러 실행
   - `$ scrapy crawl quotes`
7. 로그 확인(1)
   - 로그의 첫부분에는 Scrapy로 크롤러를 실행할 때의 설정 정보가 INFO 로그로 출력
   - INFO: Spider opened는 Spider에 작성한 처리를 시작한다고 알림
   - DEBUG:Crawled(404) <GET http://quotes.toscrape.com/robots.txt> (referer:None) 이라는 로그는 Scrapy가 크롤링 대상의 /robots.txt에 접근, 내부에 작성된 규칙에 따라 크롤링과 관련된 동작을 수행하기 위함. 404는 해당 사이트에 robots.txt가 없기 때문임.
   - robots.txt는 웹 사이트의 관리자가 구글 드의 검색 엔진이 사용하는 크롤러 봇에게 자신의 사이트에서 어떤 페이지를 크롤링해도 괜찮은지 알려주는 파일
    - 예를 들어 웹 사ㅏ이트 관리자가 사이트의 부하 문제로 격언 목록 페이지를 검색 엔진이 확인하지 않게 만들고 싶다면 다음과 같이 /robots.txt에 작성
        ```html
        User-agent: *
        Disallow: /all_quotes
        ```
   - 위처럼 작성 시 '/all_quotes'를 크롤링하지 않게 됨.
   - 그러나 robots.txt를 무시하는 봇도 존재함

8. 로그 확인(2)
   - 로그 내부에서 Overridden settings:로 출력되는 다양한 정보 중에서 ROBOTSTXT_OBEY가 True로 되어 있으면 'robots.txt의 내용에 따라서 크롤링한다'는 의미
   - Scrapy에는 middleware라는 크롤러 확장 기능이 있으며, 기본적으로 robots.txt를 분석해서 지정한 내용에 따라 크롤링을 할 수 있게 middleware를 조합. Spider에 robots.txt와 관련된 처리를 따로 넣지 않아도 자동으로 이를 분석하고 처리를 따르게 됨.
   - 로그에서 Enabled downloader middlewares: 라고 출력된 값 중에 RobotsTxtMiddleware가 들어 있는 것을 볼 수 있음.
