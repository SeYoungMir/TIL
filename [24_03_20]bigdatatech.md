# 6. 스크레이핑 개발(응용)
## 5. Scrapy를 사용해서 스크레이핑
### 1. 다양한 스크레이핑 - 이어서
9. 로그 확인(3)
   - 출력에서 http://quotes.toscrape.com의 최상위 페이지를 크롤링해서 스크레이핑.
   - 페이지를 스크레이필해서 Item을 만드는 메서드(parse 메서드)에서 return 또는 yield 내용이 로그에 출력
   - Spider 처리가 끝나면 Closing spider 출력
   - Dumping Scrapy stats에는 크롤링 결과의 여러 통계 정보가 출력
   - 'downloader/request_count': 2 와 같은 로그처럼 요청된 페이지 수는 2개, 로그 출력으로 Crawled가 2개 있었음을 알 수 있으며, 이는 출력된 수와 일하는 값.
   - 최상위 페이지가 실제로 크롤링 되었다는 걸 알 수 있고, 이 항목들이 의미하는 것은 다음과 같음.
     - downloader/response_status_count/200:1 
       - 정상적으로 내려받은 페이지가 1개
     -  downloader/response_status_count/404:1 
        -  콘텐츠를 찾지 못해 내려받지 못한 페이지가 1개, 예제에서는 robots.txt를 제대로 찾지 못함
     - finish_reason
       - finished라고 출력되면 정상적으로 완료
     - finish_time
       - 크롤링 종료 시각
     - item_scraped_count
       - 수집한 아이템의 수를 표시
     - start_time
       - 크롤링 시작 시간, finish_time과 비교 시 2초동안 크롤링
### 2. 특정 아이템 수만 추출하고 싶을 때
 - 목적에 따라서 아이템을 3개만 추출하고 싶을 때 parse 메서드 내부에서 크롤링과 스크레이핑을 중지하고 싶은 부분에 다음과 같은 코드 입력 시 Spider가 중간에 처리를 중지하게 됨
   - `raise scrapy.exceptions.CloseSpider(reason='메시지')`
- reason에는 이해하기 쉬운 메시지를 넣는 것을 추천