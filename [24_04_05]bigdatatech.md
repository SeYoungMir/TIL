# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 3. 네임스페이스를 사용한 RSS 확장
- 지금까지 설명한 요소는 RSS가 기본적으로 가진 요소.
-  요소를 잘 살펴보면 대부분 요소가 '기사'를 목적으로 만들어진 듯한 느낌이 있음.
-  다른 분야의 RSS를 만들고 싶은 사람이라면 다른 요소를 포함하게 만들고 싶어할 수 있음.
-  RSS는 이러한 요소를 확장할 수 있는 기능을 제공
- 마음대로 태그를 추가하면 안됨. 예를 들어 item 요소에 없던 RSS 요소를 추가할 수 없음.
- RSS에 독자적인 사용자 요소를 추가하고 싶다면 XML 네임 스페이스를 추가한 후에 사용
- 네임 스페이스(namespace) 선언은 다음과 같이 RSS 요소에 함.
  - `<rss version="2.0" xmlns:book="http://my-service.com/smlns//book">`
  - XML 네임스페이스
    - 관련된 내용은 다음 사이트 참고
      - Namespaces in XML 1.0(Third Edition)[[URL]](https://www.w3.org/TR/REC-xml-names/)
- xmlns 뒤에 콜론으로 구분, 사용자 정의 네임 스페이스인 book을 추가. 네임스페이스의 정의가 작성된 페이지의 URL을 입력.(위 rss 요소 링크를 적당히 변경)
- 네임스페이스의 정의를 작성하기 위해서는 XML과 관련된 높은 수준의 이해 필요.
- 사실 XML 사양에서 네임 스페이스의 URL(URI)은 네임스페이스를 유일하게 식별하기 위해서 사용하며, 실제로 해당 URL(URI)를 참조할 수 있는지 등은 따로 확인하지 않음
- RSS에는 author라는 요소가 있으므로 출판사 이름은 이 요소를 사용하면 될 수도 있음. 하지만'요소가 계ㅖ층 구조를 이루게 한다', '계층 구조를 이룬 요소는 id를 가질 수 있다'등의 사양이 없으므로 출판사 id는 사용자 정의 요소로 추가.
- 샘플은 다음과 같음.
  - ```xml
    <?xml version="1.0"?>
    <rss version="2.0" xmlns:book="http://my-service.com/xmlns/book">
        <channel>
            <title>위키북스의 도서 목록</title>
            <link>http://example.com</link>
            <description>설명을 입력했다고 가정</description>
            <item>
                <title>파이썬을 이용한 머신러닝, 딥러닝 실전 앱개발</title>
                <link>http://example.com</link>
                <description>설명</description>
                <author>위키북스</author>
                <book:author_id>2</book:author_id>
            </item>
        </channel>
    </rss>
    ```
    - 출판사 이름도 사용자 정의 요소로 만들고, id를 속성으로 붙여도 됨.