# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 4. feedgen을 사용해서 RSS 생성 - 이어서
5. 피드 생성 프로그램 작성 - 이어서
   - 코드에서, import 부분은 rss_with_feedgen/feedgen_ext.py를 사용, book 이라는 사용자 정의 네임 스페이스를 추가하기 위한 BookEntryExtension과 BookFeedExtension을 임포트
   - def 부분에서 피드 데이터 저장 전용 객체인 fg를 FeedGenerator 함수로 생성. 피드에 포함되는 데이터는 모두 이 객체를 기반으로 구축
   - 위의 임포트한 클래스 사용, 피드 객체의 register_extension 메서드로 사용자 정의 네임 스페이스 book 등록
   - `<channel>` 요소 바로 아래에 포함되는 `<title>`요소, `<link>`요소,`<description>`요소의 값을 각각 fg.title,fg.link,fg.description 메서드로 추가
   - fg.add_entry 메서드로 `<item>`요소에 대응되는 XML 요소 객체인 fe 생성. `<item>`요소 바로 아래에 포함할 도서 정보로 `<title>`요소, `<link>`요소,`<description>`요소의 값을 각각 fe.title, fe.link, fe.description 메서드로 추가
   - 사용자 정의 네임 스페이스 book을 가지는 요소 publisher를 fe.book.publisher 메서드로 추가. 이는 위에서 사용자 정의 요소를 추가했기 때문에 가능
   - fg.rss_str 메서드로 만든 피드 데이터를 RSS 형식의 문자열로 변환. pretty=True를 지정하지 않으면 XML 요소가 용량을 최소화해서 한 줄로 출력
6. 실행하고 출력 결과 확인
   - 다음 명령어로 프로그램 실행
   - ```cmd
     $ python -m rss_with_feedgen
     ```
   - 결과에서 네임 스페이스로 xmlns:atom="http://www.w3.org/2005/Atom"와 xmlns:content="http://purl.org/rss/1.0/modules/content/"가 들어있는 모습을 볼  수 있음. 이는 feedgen의 기본 동작임. 사용하지 않는 네임 스페이스가 들어 있어도 큰 문제 없음.
   - 파이썬의 대표적인 웹 프레임워크인 장고(Django)에도 RSS 출력 기능이 있음.
     - Django documentation:The syndication feed framework[[URL](https://docs.djangoproject.com/en/2.1/ref/contrib/syndication)]
   - RSS 출력만을 위해서 장고를 설치하는 것은 과함. 피드 출력만 필요할 땐 feed와 xml.etree.ElementTree(또는 lxml)를 사용하느 것을 추천.