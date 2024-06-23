# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 5. 단위 테스트 생성.
1. 단위테스트란?
   - 단위 테스트는 '유닛 테스트(Unit Test)'라고도 부르며, 프로그램을 구성하는 함수 또는 메서드가 제대로 동작하는지 검증
   - 크롤러를 개발할 때는 웹에서 데이터를 읽어 들이고, 파싱하고, 요소를 추출하고, 가공하는 처리를 각각 만들고 이를 조합하는 것이 일반적. 이러한 각 부분을 조금씩 변경할 때마다 프로그램이 제대로 작동하는지 직접 프로그램을 실행해서 눈으로 확인하기는 귀찮음.
   - 이러할 때에 각 부분별로 테스트하고, 결과를 확인하는 코드를 만든다면 굉장히 편리
2. 테스트 대상 코드와 테스트 코드 준비
   - HTML에서 `<title>`태그의 내용을 스크레이핑하는 scrape_title 함수를 생성, 테스트 코드를 만든 다음 단위 테스트에 대해서 알아봄.
   - 테스트 프레임워크로 pytest를 사용. unittest라는 파이썬 표준 프레임워크가 있지만, pytest를 사용하면 훨씬 더 간단하게 코드를 작성할 수 있음.
     - pytest[[URL](https://github.com/pytest-dev/pytest)]
     - unittest[[URL](https://docs.python.org/3/library/unittest.html)]
   - 스크레이핑에는 BeautifulSoup 사용
   - pytest와 BeautifulSoup을 pip install 명령어로 설치.
     - ```cmd
       $ pip install beautifulsoup4 pytest
       ```