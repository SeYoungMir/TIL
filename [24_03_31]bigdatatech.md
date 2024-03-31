# 6. 스크레이핑 개발(응용)
## 8. 디버그하기
### 1. 시행착오를 반복하며 스크레이핑
- 스크레이핑 처리에 다음과 같은 CSS 선택자 사용
  - `item['author'] = quote_html.css('small.author::text').extract_first()`
  - 이러한 선택자를 찾을 때 발생하는 실수를 매번 scrapy crwal 명령어를 실행하며 여러 번 확인한다면 상대방의 서버에 부담이 될 수 있음.
  - 이러한 경우를 위해 scrapy에는 URL을 지정해서 response 객체를 만들고, CSS 선택자를 테스트해보며 스크레이핑 결과를 확인할 수 있는 디버그 기능 존재
1. shell 명령어를 실행해서 출력 확인
   - 다음과 같이 shell 명령어 실행
   - `$ scrapy shell`
   - 터미널에 출력. 이는 Scrapy의 기능을 부분적으로 실행할 수 있게 해 주는 인터랙티브 셸. 로그에 출력된 메서드와 객체 사용 가능
2. fetch(url)실행
   - 예를 들어 fetch(url) 실행 시 response 변수에 페이지의 결과가 들어감
   ```python
   >>> fetch('http://quotes.toscrape.com/')
   ```
   - 다음과 같이 작성해 CSS 선택자를 테스트
   ```python
   >>> response.css('div.quote small.author::text').extract()
   ```
   - 다음과 같이 긴 코드 작성, 실행 가능
   ```python
   >>> from my_project.items.import Quote
   >>> items = []
   >>> for quote_html in response.css('div.quote'):
        item = Quote()
        item['author'] = quote_html.css('small.author::text').extract_first()
        item['text'] = quote_html.css('span.text::text').extract_first()
        item['tags'] = quote_html.css('div.tags a.tag::text').extract()
        items.append(item)
   >>> items
   ```
   - 추가로 링크를 따라 돌며 실행했을 때 로그 출력.
   - 실제로 확인은 다음과 같이
   - `>>> len(response.xpath('//a/@href').extract())`
   - 이로써 크롤링 한 페이지의 최상위 페이지에는 55개 링크가 포함. start_urls에 지정한 최상위 페이지와 robots.txt를 포함했기 때문에 57개
   - 스크레이핑할 때 어떤 CSS 선택자와 XPath를 지정해야할지 잘 모르겠을 때에는 Spider를 본격적으로 만들기 전에 scrapy shell을 사용, 먼저 결과를 확인해보는 것이 좋음.