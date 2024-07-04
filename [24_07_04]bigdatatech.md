# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 1. 자바스크립트로 렌더링 되는 페이지를 스크레이핑하기
### 2. 파이썬 가상 환경과 venv
1. 자바스크립트로 렌더링되는 페이지 스크레이핑 - 코드 2
   - 셀레니움을 사용한 다음 코드를 작성, get_cinema_titles.py라는 이름으로 저장.
   - ```python
     """ 크롬 헤드리스 드라이버로 자바스크립트를 사용하는 페이지 스크레이핑하기"""
     import logging
     import time
     
     from selenium import webdriver
     from selenium.webdriver.chrom.options import Options

     # 로거 설정
     logger = logging.getLogger(__name__)
     formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d %(message)s'
     )
     handler = logging.StreamHandler()
     handler.setFormatter(formatter)
     logger.setLevel(logging.DEBUG)
     logger.addHandler(handler)

     # 크롬드라이버 실행 옵션 설정
     chrome_options = Options()
     chrome_options.add_argument("--headless")
     chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
     chrome_driver_path = ('/Users/hasat/python/chromedriver')

     if __name__ == '__main__":
        try:
            # 크롬을 헤드리스 모드로 실행
            driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
            # 스크레이핑 대상 URL 지정
            target_url = "http://0.0.0.0:8000/vue_sample.html"

            # 헤드리스 모드 크롬으로 스크레이핑 대상 페이지 열기
            driver.get(target_url)

            # 내부적으로 Ajax를 사용해서 처리하는 경우
            # 화면을 모두 읽어 들일때까지 어느 정도 대기해야 함.
            time.sleep(2)

            # 영화 제목 요소를 CSS 선택자로 지정해서 추출
            title_elms = driver.find_elements_by_css_seletor(".cinema_title")

            # 추출된 요소 출력
            for i, t in enumerate(title_elms):
                print(i+1, t.text)
        except Exception as e:
            # 예외 발생 시 스택 트레이스 출력
            logger.exception(e)

        finally:
            # 예외 발생해서 프로그램 종료 시
            # 크롬 프로세스가 남는 것을 피할수 있게 finally 구문 내부에서 종료
            driver.close()
     ```
     - 가상 환경에서 get_cinema_titles.py를 실행
     - ```cmd
       (venv_selenium)$ python get_cinema_titles.py
       ```
     - 127.0.0.1로 시작하는 줄은 파이썬의 HTTP 서버에서 HTTP 요청을 받았을 때 출력되는 로그. 실제 스크레이핑 결과는 두 번째 줄부터.