# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 1. 자바스크립트로 렌더링 되는 페이지를 스크레이핑하기
### 2. 파이썬 가상 환경과 venv
2. get_cinema_titles.py에 대해
   - get_cinema_titles.py의 코드 설명
   - chrome_options 부분은 크롬을 헤드리스 모드로 실행할 때의 옵션 지정. 크롬을 헤드리스 모드로 실행하려면 --headless 옵션을 반드시 지정.
   - chrome_oprtions.binary_location에 크롬 애플리케이션 자체의 경로 지정.
   - chrome_driver_path 부분에서는 크롬을 조작하기 위한 크롬 ㄷ드라이버 겨로 지정. 예제는 내려받은 크롬 드라이버를 /Users/hasat/python/chromdriver에 넣었을때의 예시
   - if문 안의 driver 부분은 webdriver.Chrome 메서드를 이용, 크롬을 헤드리스 모드로 호출, 매개 변수로 크롬드라이버의 경로와 실행 옵션 전달
   - driver.get 메서드 부분은 이를 사용해서 URL을 오픈, 브라우저의 주소창에 URL을 입력해서 페이지를 열 때와 같은 처리가 내부적으로 일어남.
   - time.sleep 옵션은 내부적으로 Ajax 요청이 있을 때를 대비, 2초동안 잠시 처리 중단. 현재 예제에서는 필요 없지만, 이후에 내용이 많은 페이지를 크롤링하는 경우를 대비해서 삽입. 대상 사이트에 따라서 더 오래 대기해야 할 수 도 있음.
   - title_elms 부분에서는 driver.find_elements_by_css_selector 메서드 사용, 위에서 읽어들인 페이지에서 영화 제목을 스크레이핑.영화 제목이 `<span>`태그 안에 class="cinema_title" 형태로 들어있으므로 .cinema_title이라고 지정.
   - for 문에서는 위에서 스크레이핑한 영화 제목을 터미널에 출력. 스크레이핑한 각 요소의.text 속성을 사용하면 내부의 텍스트 추출 가능
   - driver.close 부분은 프로그램의 후처리 진행. 프로그램 실행 중에 예외가 발생해서 프로그램 강제 종료로 헤드리스 모드로 실행한 크롬의 종료가 되지 않으면 프로세스에 남게 됨. 이를 막기 위해 driver.close 메서드로 종료시키는 처리 finally 구문 내부에 추가
### 3. 크롬 헤드리스 모드의 명령 라인 실행
   - 크롬 헤드리스 모드는 파있너과 연동하지 않아도 스크린샷을 찍는 등의 처리 가능. 굉장히 편리한 기능이므로 간단하게 살펴봄
   - 예를 들어 pyython.org의 스크린샷은 다음처럼 코드를 작성하여 촬영.
   - ```cmd
     $ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --screenshor http://www.python.org/
     ```
   - 이외의 명령 라인 실행과 관련된 옵션은 다음 페이지 참고
     - Getting Started with Headless Chrome[[URL](https://develpoers.google.com/web/updates/2017/04/headless-chrome)]