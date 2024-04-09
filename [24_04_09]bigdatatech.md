# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 3. 네임스페이스를 사용한 RSS 확장 - 이어서
4. 표준 XML 모듈을 사용해서 RSS 생성- 이어서
   - XML 요소 객체 생성 후 `<channel>` 요소 바로 아래의 `<item>` 요소를 나타내는 elm_item 를 ET.SubElement로 생성. 현재 만드는 피드에서 <item> 요소는 출판사의 도서 정보를 나타내는 요소
   - `<item>`바로 아래의 `<title>` 요소를 나타내는 elm_item_title을 ET.SubElement로 만들어 요소의 내용을 elm_item_title.text 속성 지정
   - `<item>` 바로 아래의 `<link>`요소를 나타내는 elm_item_link를 ET.SubElement로 생성
   - `<item>` 바로 아래의 `<description>`요소를 나타내는 elm_item_description을 ET.SubElement로 생성. 긴 문자열을 만들때는 여러 문자열로 분할, 괄호로 감싸 결합하는 방법 사용 시 편리함.
   - 위 코드로부터 다음과 같은 XML 생성.
   - ```XML
     <title>파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발</title>
     <link>http://example.com</link>
     <description>&lt;a href=&quot;http://example.com&quot;&gt;이스케이프 처리 확인 전용 링크&lt;/a&gt;설명을 입력했다고 가정</description>
     ```
   - 이후 코드는 사용자 정의 네임 스페이스가 가지는 <book:publisher> 생성, 마찬가지로 ET.SubElement 메서드 사용, elm_item_publisher 객체 생성. 첫 번째 매개 변수로 부모 요소(elm_item)지정, 두 번째 매개 변수로 사용자 정의 네임 스페이스를 가지는 요소 이름 "book:publisher" 지정. 키워드 매개 변수 id 지정, 요소에 출판사 ID를 속성으로 설정. 이 요소는 출판사 정보를 나타내는 요소.
    - 위와 같은 처리로 book:publisher XML 속성 생성
    - 위 까지의 과정으로 <rss>요소 모두 생성. 이어서 ET.tostring 메서드로 이를 XML 문자열로 변환, 두 번째 매개 변수로 문자 코드 지정. 일반적으로 XML은 UTF-8 사용
    - 위에서 변환한 XML 문자열은 줄바꿈, 들여쓰기 적용되지 않으며 XML 문서에 필요한 XML 선언`<?xml version="1.0"?>`이 없으므로 XML 문자열을 가공, XML 선언을 붙일 수 있게 minidom.parseString 메서드로 파싱, xml.dom.minidom.Document 클래스의 객체인 dom 추출. dom.toprettyxml 메서드를 사용하여 XML 선언이 붙은 가공된 XML 문자열을 획득 가능. 키워드 매개 변수 indent에 띄어쓰기 2개 지정 시 각 XML 요소의 들여쓰기가 띄어쓰기 2개로 들어감
5. 명령어 실행
   - `$ python rss_with_et.py` 명령어로 해당 파이썬 파일 실행. XML 파일 생성.
   - 실행 결과의 `<description>` 부분 살펴보면 명령어를 실행한 경과에는 HTML 태그가 이스케이프 처리되어 있음. 이는 ET.tostring 메서드가 XML의 사양에 따라 XML 태그와 혼동될 수 있는 기호를 자동으로 이스케이프 처리하기 때문.
   - CDATA 섹션으로 이를 처리하면 복잡하므로 마크업 문자로 이스케이프를 다루는 것을 추천.
