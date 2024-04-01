# 6. 스크레이핑 개발(응용)
## 9. Scrapy로 프로그램 제작
### 1. 스크립트 작성
 - Scrapy는 프레임워크이면서 동시에 스크립트에서 사용할 수 있는 API도 제공. 다음처럼 스크립트 run_crawl.py를 프로젝트 디렉터리(my_project) 바로 아래에 생성.(my_project/my_project 아래가 아님)
 - ```python
   """scrapy의 quotes 크롤러 호출"""
   from scrapy.crawler import CrawlerProcess
   from scrapy.utils.project import get_project_settings

   def run_crawl():
        """크롤링 실행"""
        process = CrawlerProcess(get_project_settings())
        process.crawl('quotes')
        process.start()
    if __name__ == '__main__':
        run_crawl()
   ```

  - 다음과 같이 실행
  - `$ python -m run_crawl`
  - scrapy crawl 명령어를 사용했을 때와 마찬가지로 로그 출력, 이러한 형태 사용 시 웹 사이트 형태로 크롤러 관리 화면을 만들어서 웹 인터페이스에서 크롤러를 실행해볼 수도 있음.
  - process.crawl 메서드의 매개 변수에는 Spider에 대한 설정도 지정할 수 있으므로 start_urls를 데이터베이스로부터 읽어 들이는 것도 가능
  - 예를 들어 먼저 DB.get_crawl_urls라는 메서드를 정의, 데이터베이스에서 크롤링 대상 URL을 을답 받는다면 다음처럼 구현
  - ```python
    crawl_urls = DB.get_crawl_urls()
    process.crawl('quotes',start_urls=crawl_urls)
    ```
  - Scrapy를 외부에서 호출하는 형태로 활용 시 다양하게 활용 가능.
1. 프레임워크를 사용할 때의 주의 사항
   - 프레임워크는 굉장히 편리하지만, 내부에서 무엇을 하고 있는지 모르는 상태로 사용하게 된다는 문제가 있음. 기대하지 않은 동작이나 버그를 피하려면 문서를 꼭 자세히 확인해야함.
   - 오픈소스 문서는 사람들이 모여서 만드는 것이다 보니 부분적으로 오래된 내용이 있을 수 있고, 기능의 세부적인 내용이 자세히 쓰여있지 않은 경우도 있음. '내부적으로 어떻게 동작하는 것인가','이런 기능은 없는가' 라는 의문이 생긴다면 소스 코드도 참고하는 것이 좋음.
   - 모두 살펴보는데는 시간이 너무 오래 걸리고 어려우므로 필요에 따라서 일부 코드만 살펴보기 바람. 소스 코드를 읽다보면 프레임워크의 사상에 대해서도 알 수 있으며, 때에 따라서는 자신의 목적과 맞지 않는 부분이 있다는 것도 알 수 있음. 이러한 것들을 기반으로 좋은 기술을 선택할 수도 있음.