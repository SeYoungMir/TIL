# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 5. 단위 테스트 생성.
2. 테스트 대상 코드와 테스트 코드 준비
   2. 테스트 코드 생성. - 이어서
      - from 부분에서 scraper.py에 정의한 '사용자 정의 예외 ScraperException'과 '`<title>`태그를 스크레이핑 하는 scrape_title 함수'를 임포트.
      - def 함수 내에서 `<title>` 태그를 포함하는 HTML을 변수 html에 저장, scraper_title 함수의 매개 변수로 전달. 그리고 반환된 값이 '제목'과 같은지 테스트, 테스트 할 때는 assert 구문을 사용.
      - 그 아래에서는 `<title>`태그를 포함하지 않는 HTML을 변수html_without_title에 저장. with 구문을 사용, with pytest.raises(ScraperException)라고 작성시 with 구문 블럭 내부에서 ScraperException 예외가 발생하는지 테스트 가능. 이 때 발생한 예외는 as 구문에 지정한 변수 e에 저장. scrape_title 메서드의 매개 변수에 `<title>`태그를 포함하지 않는 HTML이 전달되면 예외가 발생, pytest.raises에서 해당 예외가 사용자 정의 예외 ScraperException인지 테스트하게 됨. assert 구문에서는 이 때 발생한 사용자 정의 예외 메시지가 'title 태그가 미존재'인지 테스트
      - 그 아래에서는 `<title>`태그를 포함하고 있지만, 해당 내용이 비어 있는HTML을 변수 html_empty_title에 저장. 위 코드와 마찬가지로 with 구문 사용, 사용자 정의 예외 ScraperException이 발생하는지 테스트
      - scrape_title 메서드의 매개 변수에 `<title>`태그의 내용이 없는 HTML이 전달, 예외 발생. pytest.raises 메서드로 해당 예외가 사용자 정의 예외 ScarperException인지 테스트. 이 때 assert 구문에서는 발생한 사용자 정의 예외의 메시지가 'title 태그에 내용 미존재'인지 테스트.