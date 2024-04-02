# 6. 스크레이핑 개발(응용)
## 10. 크롬 개발자 도구 사용
### 1. 크롬(Chrome)
- 스크레이핑 개발을 할 때에는 대상 요소를 어떤 선택자와 XPath로 추출할 수 있는지 여러 번 시행착오를 반복
- 상대 사이트의 HTML 소스가 있어도 소스를 하나하나 확인하면서 시행착오를 반복하는 것은 힘듦
- 크롬 브라우저에는 개발자 도구라는 개발 보조 도구 있음. 이를 사용 시 효율적으로 스크레이핑에 사용할 선택자와 XPath 등을 찾을 수 있음
- 크롬 브라우저에서 Quotes to Scrape 사이트 접근
  - Quotes to Scrape[[URL]](http://quotes.toscrape.com/)
- 다음과 같은 방법으로 크롬 개발자 도구 실행
  - 크롬 메뉴 > 보기 > 개발자 정보 > 개발자 도구
  - 브라우저 위의 더보기 클릭 > 도구 더보기 > 개발자 도구
- 개발자 도구 실행 시 화면 아래에 개발자 도구 출력
- 확인하고 싶은 대상 요소 위에 마우스 올리고 마우스 오른쪽 버튼 클릭 > 검사 클릭
- 또는 개발자 도구 왼쪽 위의 인스펙터 클릭, 인스펙터를 클릭한 다음 페이지 내부의 'by Albert Einstein'라는 문자 위에 커서를 위치시키고 클릭 시 요소 선택 가능
- 지정했다면 http://quotes.toscrape.com/ 페이지 위에서 사람 이름 확인
- 다음과 같은 DOM 계층 출력
  - `html body div.container div.row div.col-md-8 div.quote span small.author`
- CSS 선택자를 가장 최상위부터 지정할 필요는 없음, 구분할 수 있는 정도의 계층부터만 지정.
- 개발자 도구의 Element 탭을 Console 탭으로 변경, CSS 선택자 결과 확인
  - 다음과 같은 코드를 콘솔에 입력
    - `$$('span small.author')`
- CSS 선택자로 추출한 결과는 $$ 메서드로 확인 가능.
- 첫 번째 요소 내부의 텍스트 확인
  - `$$('span small.author')[0].innerText`
  - 의도한 대로 추출됨. CSS 선택자의 동작은 브라우저에서도 할 수 있음.
- XPath도 확인, XPath는 $x 메서드 사용
  - `$x('//div[@class="quote"][1]/span/small[@class="author"]/text()'[0])`
- XPath는 여러 개의 요소가 있을 때 인덱스를 1부터 세므로 주의.
- 개발자 도구로 쿨키 확인 레퍼러 확인 등이 가능. Chrome DevTools 확인