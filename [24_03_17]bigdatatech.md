# 6. 스크레이핑 개발(응용)
## 5. Scrapy를 사용해서 스크레이핑
### 1. 다양한 스크레이핑 - 이어서
5. Spider 생성
   - Spider 생성은 하단 Spider 생성 전용 명령어를 사용. 멸령어를 사용하지 않고도 만들 수 있지만, 명령어를 사용하면 기본적인 형태의 코드가 작성된 파일이 생성되므로 이를 참고하여 코드를 작성할 수 있게 됨. 따라서 명령어를 사용해서 만드는 방법을 추천
   - `$ scrapy genspider -t crawl quotes quotes.toscrape.com`
   - -t는 템플릿을 지정하는 옵션, Scrapy는 웹 사이트 크롤링 전용(crawl), XML 피드 크롤링 전용(xmlfeed), CSV 피드 크롤링 전용(csvfeed) 등의 Spider 템플릿을 제공
   - 현재 예제는 웹 사이트 크롤링하는 것이므로 crawl 템플릿을 지정. quotes는 Spider 파일 이름
   - 마지막으로 크롤링 대상 도메인을 지정. 위의 명령어를 실행 시 ,my_project/my_project/spider/quotes.py가 생성
   - 이를 참고해 하단 코드 작성
   ```python
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
            for quote_html in response.css('div.quote'):
                item = Quote()
                item['author'] = quote_html.css('small.author::text').extract_first()
                item['text']=quote_html.css('span.text::text').extract_first()
                item['tags']=quote_html.css('div.tags a.tag::text').extract()
                yield item
   ```
   - 위의 코드의 name,allowed_domains,start_urls는 다음과 같은 것을 설정
     - name을 사용해서 크롤러를 실행할 때에 지정할 크롤러 이름을 설정
     - allowed_domains를 사용해서 크롤링 대상 콘텐츠의 도메인을 제한
     - start_urls를 사용해서 크롤링 시작 지점이 되는 인덱스 페이지의 URL을 설정함
  - parse 메서드는 CrawlSpider 클래스에 이미 선언된 메서드를 오버라이드를 하고 잇음.
  - 변수 start_urls에 설정한 인덱스 페이지부터 크롤링을 시작, 인덱스 페이지의 HTML 소스는 parse 메서드의 두 번째 매개 변수인 response에 scrapy.http.response.html.HtmlResponse 클래스 객체 형태로 전달됨.
  - 이 응답 객체는 response.body와 response.text 형태로 내부의 내용을 참조할 수 있음
  - 응답 객체에 저장된 HTML 소스를 스크레이핑하는 메서드도 제공됨. 예제에서는 css라는 스크레이핑 전용 메서드를 사용해서 스크레이핑을 진행하고 있음.
  - http://quotes.toscrape.com/에서 추출한 데이터를 item['author'], item['text'],item['tags']에 저장. css 메서드를 보면 알겠지만, CSS 선택자를 사용해 요소를 선택하는 메서드. xpath메서드도 제공, 이를 사용하면 XPath로 지정할 수 있음.
  - 아무거나 사용해도 상관없기는 하지만 xpath 메서드 사용 시 몇 가지 주의 필요. css 메서드를 사용할 때는 response.css('div.quote')처럼 하나의 객체를 대상으로 스크레이핑
  - 하지만 xpath 메서드는 선택한 객체를 스크레이핑하는 것이 아니라 XPath로 지정한 부모의 DOM 계층에서 스크레이핑이 일어남. 실제로 사용하다보면 이로 인해 예상하지 못한 결과가 나오는 경우도 있어, 특별한 이유가 없다면 css 메서드를 사용하는 것이 좋음.
  - 스크레이핑 전용 메서드로 추출한 결과는 scrapy.selector.unified.SelectorList 클래스의 객체로 반환. 이 객체에 추가로 xpath 메서드와 css 메서드를 적용할 수도 있음.
  - extract 메서드는 스크레이핑 조건에 맞는 객체들을 반환하는 메서드. extract_first 메서드는 스크레이핑 조건에 맞는 처음 객체만 반환하는 메서드
  - 마지막을 보면 yield item 이라고 되어 있는데. yield 는 return과 비슷한 동작을 하지만, 반환한 다음 함수의 실행을 종료하지 않고 잠시 중단함. 그리고 이후에 다시 함수가 호출되면 이전에 잠시 중단했던 상황부터 실행을 재개함. 파이썬에서는 yield를 포함한 함수를 "제너레이터(generator)"라고 부름.
  - 예를 들어. parse 메서드의 내용을 List로 append 하는 방식으로 사용해 return으로 작성하면 같은 결과가 나오지만 yield를 사용하면 더 간단하게 작성 가능