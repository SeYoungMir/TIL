# 6. 스크레이핑 개발(응용)
## 5. Scrapy를 사용해서 스크레이핑
### 4. settings.py
- my_project/my_project/settings.py를 사용 시 '어떤 형태로 크롤링할 것인가'를 설정 가능. 추가로 몇 가지 미들웨어가 처음부터 기본적으로 활성화되어 있는데, 이러한 미들웨어의 설정은 settings.py에서 함. 
1. USER_AGENT
   - 크롤러가 상대 사이트에 접근할 때 사용할 User-Agent를 설정. 일부 사이트는 User-Agent에 따라서 다른 HTML 소스 코드를 응답하는 경우 있음(모바일, 데스크톱 전용 웹 페이지)
   - 크롬 브라우저와 같은 User-Agent 설정 시 크롬으로 접근했을 때와 같은 HTML 소스 코드를 응답. 다음은 크롬 웹 브라우저의 User-Agent
    ```
    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/    537.36 (KHTML, like Gecko)
    Chrome/60.0.3112.90 Safari/537.36
    ```
   - 크롤러를 만들 때는 일반적으로 뒤에 메일 주소 또는 웹 사이트의 URL을 적어서 누가 크롤링하는 것인지 명시하는 게 좋음. 예를 들면 다음처럼 뒤에 메일 주소 적을 수 있음.
    ```
    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/    537.36 (KHTML, like Gecko)
    Chrome/60.0.3112.90 Safari/537.36 Scrapy (example@example.com)
    ```
    