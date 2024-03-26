# 6. 스크레이핑 개발(응용)
## 6. 링크를 따라 돌며 크롤링
### 1. 링크를 따라 돌며 크롤링하려면
- 처음 QuotesSpider 예에서는 최상위 페이지만 크롤링. 이를 변경해서 링크를 따라 돌며 크롤링하게 함.
1. Spider 변경하기
   - 다음처럼 Spider를 변경. 동작은 확인하면서 상대방의 서버에 부담을 주지 않을 수 있게 Settings.py의 DEPTH_LIMIT을 1로 추가
   ```python
   """http://quotes.toscrape.com/크롤러
   
   하나 아래 계층까지 크롤링해서 페이지마다 격언을 1개씩 수집
   """
   import scrapy
   from scrapy.linkextractors import LinkExtractor
   from scrapy.spiders import CrawlSpider,Rule

   from my_project.items import Quote

   class QuotesSpider(CrawlSpider):
        """Quote 아이템을 수집하는 크롤러"""
        name= 'quotes'
        allowed_domains=['quotes.toscrape.com']
        start_urls=['http://quotes.toscrape.com/']
        
        rules = (
            Rule(
                LinkExtractor(allow=r'.*'),
                callback='parse_start_url',
                follow=True,
            )
        )
        def parse_start_url(self,response):
            """start_urls 아래의 다음 페이지도 스크레이핑"""
            return self.parse_item(response)

        def parse_item(self,response):
            """크롤링한 페이지에서 Item을 스크레이핑"""
            items= []
            for i,quote_html in enumerate(response.css('div.quote')):
                if i>1:
                    return items
                item = Quote()
                item['author'] = quote_html.css('small.author::text').extract_first()
                item['text']=quote_html.css('span.text::text').extract_first()
                item['tags']=quote_html.css('div.tags a.tag::text').extract()
                items.append(item)
   ```
   
   - rules에는 어떤 링크를 따라 돌 것인가를 다음과 같이 지정
     - LinkExtractor는 스크레이핑 대상으로 요청할 링크를 정규 표현식으로 지정
     - callback에는 추출한 결과를 처리할 함수 이름을 지정
     - follow에는 추출한 결과에서 또 어떤 링크를 따라 돌지를 지정
   - LinkExtractor에서 지정한 조건을 기반으로 변수 starts_urls에 설정한 페이지부터 크롤링을 시작하며 HTML을 추출하게 됨
   - 추출한 HTML은 Rule(callvack=...)에 지정한 함수에 전달. 현재 예제에서는 callback에 parse_start_url 메서드를 지정
   - parse_start_url은 CrawlSpider의 메서드. 이를 오버라이드 해서 parse_item 메서드를 호출 시 최상위 페이지의 처리를 진행
   - Scrapy는 start_urls를 사용해서 지정한 URL을 '계층적인 크롤링 대상 링크가 있는 인덱스 페이지'로 생각. 따라서 Rule(callback=...)에 Item 처리 전용 메서드를 지정했다고 해도 메인(최상위 페이지)는 스크레이핑되지 않음.