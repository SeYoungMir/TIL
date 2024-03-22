# 6. 스크레이핑 개발(응용)
## 1. 크롤링한 데이터를 구조화 데이터로 변환
### 1. 수집한 데이터를 구조화
- 크롤러로 수집한 데이터는 구조화되어 있지 않은 경우 많음
- 처음부터 XML 또는 JSON으로 구조화되어 있는 데이터를 크롤러로 추출할 수 있는 경우라도 그것이 우리가 원하는 최종적인 형태일 수 없음. 데이터는 자신이 사용할 최종적인 형태로 변환하는 과정 필요
- 간단한 예로 도서 정보를 구저ㅗ화하는 경우, 특정 출판사의 새로운 책을 수집하는 목적 ,크롤러 제작- 수집은 매일 진행, 새로운 책이 있을 경우 데이터 추가 가정
1. 웹페이지 분석
   - Yes24에서 데이터 수집 가정, 국내도서 신간 페이지를 매일 수집 시 새 책들을 쉽게 수집 가능
     - Yes24의 IT 모바일 신간 페이지[(URL)](http://www.yes24.com/24/Category/NewProductList/001001003?subGb=04)
   - 웹페이지 양쪽에 광고, 광고들은 페이지 새로 고침 혹은 시간의 변화에 따라 변경. 따라서 페이지 소스 코드의 변화만으로는 광고가 바뀐 것인지, 실제 컨텐츠가 변경된 것인지 알 수 없음
   - 변화 감지는 목록의 도서 데이터 추출, 가장 최신 도서가 바뀌었을 때 새로 추가된 신간을 감지, 이전에 수집했던 최신 도서 위치까지만 데이터 수집
   - 데이터 수집 예시는 다음과 같음
    <table>
        <tr>
            <th>출판사</th>
            <th>책 이름</th>
        </tr>
        <tr>
            <td>한빛미디어</td>
            <td>HTML 5 웹 프로그래밍 입문</td>
        </tr>
        <tr>
            <td>한빛미디어</td>
            <td>Hello Coding 파이썬</td>
        </tr>
        <tr>
            <td>위키북스</td>
            <td>파이썬을 이용한 머신러닝,딥러닝 실전 앱 개발</td>
        </tr>
        <tr>
            <td>Addison-Wesley</td>
            <td>The Art of Computer Programming</td>
        </tr>
    </table>
### 2. 구조화된 데이터 저장
- 구조화한 데이터를 저장할 때는 MySQL 또는 PostgreSQL과 같은 관계형 데이터 베이스에 저장하는 것이 일반적, 또한 관계형 데이터베이스에 저장한 데이터는 이후에 다른 구조화데이터 형식으로 활용하는 경우 많음
  - MySQL은 오라클이 개발/지원하는 오픈소스 관계형 데이터베이스, 웹 개발에서 널리 사용되고 있음. 유료 버전과 무료 버전이 있으며, 무료 버전 사용 시 MySQL Community Edition 사용이 좋음
  - PostgreSQL은 매우 많은 기능이 았으며, 최근 들어서 성능이 굉장히 발전하고 있고, 국내에서도 많이 사용되고 있는 오픈소스 관계형 데이터베이스, 웹 개발에서 많이 사용되며, 무료로 사용 가능.
- 데이터베이스에 저장하면 굉장히 빠른 속도와 다양한 방법으로 데이터 검색 가능
1. 데이터베이스 테이블 예
   - 국내 IT 모바일 도서 정보를 수집 시 특별한 경우가 아니라면 데이터의 양이 10만개를 넘지 않기 때문에 단순하게 저장, 단순하게 추출해서 사용해도 문제 없음
   - 공부를 위해 데이터베이스에 저장한 다음 다양하게 활용할 수 있는 형태로 설계 - 언어와 출판사,isbn과 이름으로 테이블 구성
### 3. 수집한 데이터 사용
   - 수집한 도서 데이터를 활용하는 경우, 다른 프로그램 또는 서버와 연동하는 경우. 다음과 같은 형식 사용
     - XML
     - CSV
     - JSON
   - 위와 같은 형식 생각하며 데이터를 구조화해두면 더욱 더 원활하게 데이터 흐름 설계 가능. 각각의 형식으로 변환한 예를 살펴보기로 함.