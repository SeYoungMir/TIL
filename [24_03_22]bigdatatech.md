# 6. 스크레이핑 개발(응용)
## 5. Scrapy를 사용해서 스크레이핑
### 2. 특정 아이템 수만 추출하고 싶을 때 - 이어서
- 코드를 추가해 다음처럼 기존 .py 파일을 수정
- ```python
   """http://quotes.toscrape.com/크롤러
   메인 페이지만 크롤링해서 격언 수집
   """
   import scrapy
   from scrapy.spiders import CrawlSpider

   from my_project.items import Quote

   class QuotesSpider(CrawlSpider):
        """Quote 아이템을 수집하는 크롤러"""
        name= 'quotes'
        allowed_domains=['quotes.toscrape.com']
        start_urls=['http://quotes.toscrape.com/']

        def parse(self,response):
            """크롤링한 페이지에서 Item을 스크레이핑"""
            for i, quote_html in enumerate(response.css('div.quote')):
                # 테스트로 3개 추출
                if i > 2 : 
                    raise scrapy.exceptions.CloseSpider(reason='abort')
                item = Quote()
                item['author'] = quote_html.css('small.author::text').extract_first()
                item['text']=quote_html.css('span.text::text').extract_first()
                item['tags']=quote_html.css('div.tags a.tag::text').extract()
                yield item
   ```
### 3. 수집한 아이템을 JSON으로 변환하고 파일로 저장
1. 수집한 아이템을 JSON으로 변환
   - 명령 라인 옵션에 -o quotes.json이라고 붙여서 실행
   - `$ scrapy crawl quotes -o quotes.json`
2. 로그 확인
   - 로그를 보면 다음과 같은 부분이 있음
   - `[scrapy.extensions.feedexport] INFO: Stored json feed (3 items) in : quotes.json`
   - scrapy crawl 명령어에 -o 옵션을 설정하고 파일의 이름을 .json, .xml, .csv, .jsonl등의 확장자로 지어주면 알아서 해당 형식으로 출력
3. 파일 확인을 위한 jq 명령어
   - 명령어를 실행한 디렉터리 아래에 quotes.json 파일이 있음. 이 파일을 쉽게 살펴볼 수 있게 json 유틸리티인 jq를 brew install 명령어로 설치
   - `$ brew install jq`
4. 파일 확인
   - JSON, XML, CSV로 각각 확인
   - 같은 파일 이름을 지정해서 크롤링 명령어를 다시 실행 시 파일에 내용이 추가됨. 문제가 있어서 처음부터 다시 해야할 시 파일을 제거한 후 실행
   - XML을 보기 쉽게 해 주는 도구로 xmllint가 있음. 이는 macOS에 표준으로 설치됨
   - CSV은 각 값의 레이블을 나타내는 헤더 줄이 출력, 구분 문자를 값으로 포함할 때에는 자동으로 큰따옴표로 감싸짐
   - JSONL은 JSON을 한 줄씩 아이템을 가지는 형식, 파이썬 표준 직렬화 형식인 Pickle도 지원
   - JSONL은 -o quotes.jl 또는 -o quotes.jsonlines로, Pickle은 -o quotes.pickle로 출력 가능
   - 파이썬 내부에서 사용할 수 있는 파이너리 형식인 'Marshal'도 지원, 필요한 경우는 거의 없음.