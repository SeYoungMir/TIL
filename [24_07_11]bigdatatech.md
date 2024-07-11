# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 2. 공개 데이터 사용
### 1. 공개 데이터란?
3. 공개 데이터 활용 - 코드 설명
   - service_key 부분에서는 엔드 포인트와 요청 매개 변수를 변수에 저장. serviceKey 부분 까지는 단순한 문자열로, 이오ㅢ의 매개 변수는 딕셔너리 자료형으로 선언
   - default_options 부분에서는 위에서 정의한 정보를 기반으로 요청 URL 생성. urllib.parse.urlencode 함수를 사용하면 딕셔너리 자료형으로 선언한 요청 매개 변수를 'numOfRows=1&pageNo=1&dateTerm=Daily&ver=1.3'형태로 변환 가능.
   - r.requests.get 부분에서는 resquests 모듈을 사용해 데이터 요청
   - soup 부분에서는 Beautiful Soup 모듈을 사용, XML을 파싱, 스크레이핑. 최종적으로 지역(region),PM10 수치(pm_10),PM 25 수치(pm_25)를 딕셔녀리로 만들어서 반환
   - if `__name__` 부분에서는 강서ㅜ와 강남구의 미세 먼지 수치를 수집해서 테스트. 실행하면 강서구와 강남구의 미세먼지 수치를 출력. 실행할 때 Beautiful Soup가 없다는 오류 발생 시 pip install beautifulsoup4 명령어를 실행, BeautifulSoup을 설치.
   - 공공 데이터 포털을 사용하는 기본적인 방법 탐색. 미세 먼지 이외에도 공공 데이터 포털에서는 수많은 데이터 제공. 통계 정보를수집하기 위한 용도, 서비스를 만들기 위한 용도, 머신러닝에 활용하기 위한 용도 등으로 다양하게 활용 가능.