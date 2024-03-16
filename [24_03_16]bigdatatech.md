# 6. 스크레이핑 개발(응용)
## 5. Scrapy를 사용해서 스크레이핑
### 1. 다양한 스크레이핑 - 이어서
2. Scrapy 설치
   - pip install 명령어로 scrapy 설치
   - `$ pip install scrapy`
3. 프로젝트 만들기
   - Scrapy는 '프로젝트'라는 단위로 스크레이핑 애플리케이션을 작성. 다음 명령어로 프로젝트를 만듦
   - `$ scrapy startproject my_project`
   - `$ cd my_project`
   - 실행하면 다음과 같은 형태로 디렉터리와 파일 생성
     - my_project
       - my_project
         - `__init__.py`
         - items.py
         - middlewares.py
         - pipelines.py
         - settings.py
         - spiders
           - `__init__.py`
       - scrapy.cfg
4. Item 정의
   - 다음 공식 문서의 튜토리얼에서 설명하는 예제 작성 순서와는 약간 다르지만 Item 정의부터 시작
     - Scrapy Tutorial(공식 문서 튜토리얼)[(URL)](https://doc.scrapy.org/en/latest/intro/tutorial.html)
   - 'Quotes to Scrape'라는 격언 소개 사이드를 대상으로 연습
     - Quotes to Scrape[(URL)](http://quotes.toscrape.com/)
   - 사이트에는 유명인의 격언들이 카드 형태로 들어있음. 각각의 카드는 다음과 같은 요소로 구성
     - 저자 이름(Author)
     - 격언 텍스트(Text)
     - 태그(Tags)
   - 프로젝트 이름과 같은 서브 디렉터리 'my_project' 아래에 items.py가 있음. items.py를 열면 기본적인 형태 작성.이를 참고해 하단 코드 작성.
   ```python
   """격언 스크레이핑 프로그램"""
   import scrapy

   Class Quote(scrapy.Item):
    """격언 아이템"""
        author = scrapy.Field()
        text = scrapy.Field()
        tags = scrapy.Field()
   ```
     - 수집하고 싶은 값을 name=scrapy.Field() 형태로 작성
