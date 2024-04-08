# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 3. 네임스페이스를 사용한 RSS 확장 - 이어서
4. 표준 XML 모듈을 사용해서 RSS 생성- 이어서
   - XML 객체 생성후, `<rss>`요소 바로 아래의 `<channel>`요소에 대등하는 XML 요소 객체 elm_channel을 ET.SubElement 메서드로 생성
   - ET.SubElement 메서드는 첫 번째 매개 변수로 ET.Element 메서드를 사용, 생성ㄷ한 객체를 지정, 해당 요소 바로 아래에 서브 요소를 생성.
   - 서브 요소 이름은 두 번째 매개 변수를 사용, channel로 지정, `<channel> `요소는 피드의 정보를 나타내는 요소.
   - 위와 같은 처리로 다음과 같은 XML 생성
   - ```xml
     <channel>
     </channel>
     ```
   - `<title>, <link>,<description>`이 있으며, 이러한 요소를 한 번에 생성하기 위한 준비.
   - 딕셔너리 자료형의 변수 channel_sources에 필수 요소의 요소 이름, 요소의 내용(태그로 감싼 내용)을 지정, 이는 다음과 같은 XML 요소들을 만들기 위함.
   - ```xml
     <title>파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발</title>
     <link>http://example.com</link>
     <description>설명 입력 가정</description>
     ```
   - 다음 코드는 그 뒤의 코드에서 생성할 XML 요소 객체들을 저장하기 위한 리스트 자료형의 변수 children_of_channel을 생성
   - 위에서 준비한 `<channel>`요소 내부에 넣을 내용을 가진 딕셔너리 자료형의 변수인 channel_sources에 items 메서드를 적용, 키와 값을 추출하고 반복 처리.
   - 요소 이름과 요소의 내용이 각각 반복문을 반복할때 반복 변수인 tag와 text에 들어감.
   - ET.Element 메서드에 요소 이름(tag)을 전달, XML 요소 객체인 child_elm_of_channel 생성. 요소의 내용은 child_elm_of_channel.text에 지정
   - 생성한 child_elm_of_channel을 children_of_channel 리스트 변수에 append 메서드로 추가.
   - 다음은 생성한 `<channel>` 요소와 대응되는 XML 요소 객체의 서브요소를 elm_channel.extend 메서드를 사용해 일괄 추가,내부적으로는 ET.SubElement로 여러개의 서브 요소 생성 처리 실행.
   - 이 처리로 `<channel>`아래의 요소 객체 생성.
   - 위 까지의 작업으로 피드 정보를 가진 XML 요소 객체 생성.
- 