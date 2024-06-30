# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 1. 자바스크립트로 렌더링 되는 페이지를 스크레이핑하기
### 1. 자바스크립트로 렌더링되는 페이지를 스크레이핑하려면?
2. 셀레니움과 크롬 드라이버 설정
   - 파이썬에서 크롬 헤드리스 모들르 사용하려면 브라우저 자동 조작 도구인 셀레니움(Selenuim)과 크롬 드라이버(ChromeDriver)설정해야 함
     - 셀레니움[[URL](http://www.seleniumhq.org)]
     - 크롬드라이버[[URL](https://developer.chrome.com/docs/chromedriver?hl=ko)]
    - 크롬 드라이버는 다음 공식 사이트에서 내려받을 수 있음. 작성 기준으로 최신버전은 114.0.5735.90.
      - [[URL](https://developer.chrome.com/docs/chromedriver/downloads?hl=ko#chromedriver_1140573590)]
      - macOS에서는 chromdriver_mac64.zip을 다운로드.(64비트 리눅스에서는 chromdriver_linux64.zip을 다운로드)
    - 현재 디렉터리 바로 아래에 python이라는 이름으로 디렉터리 생성, 내려받은 zip 파일의 압축 해제. 셀레니움은 파이썬 바인딩이 있어서 pip install로 설치 가능. 일단 venv로 가상 환경 생성, 셀레니움 설치. (venv_selenium)은 가상환경이 활성화되엇음을 나타내는 프롬프트
    - ```cmd
      $ python -m venv venv_selenium
      $ source venv_selenium/bin/activate
      (venv_selenium) $ pip install selenium
      ```
       - 파이썬 바인딩
         - 언어 바인딩이란 '라이브러리' 또는 'OS 서비스 API'를 특정 프로그래밍 언어 전용으로 제공하는 것을 의미. 셀레니움은 C#과 자바 등의 다양한 프로그래밍 언어를 모두 지원. 어떤 도구에 '파이썬 바인딩이 있다'라는 것은 '파이썬에서 해당 도구를 사용할 수 있는 라이브러리가 제공된다'는 의미.
         - 셀레니움의 파이썬 바인딩과 관련된 내용은 다음 사이트에 자세하게 나와 있음.
           - Selenium with Python [[URL](http://selenium-python.readthedocs.io)]