# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 4. feedgen을 사용해서 RSS 생성
- 표준으로 제공되는 xml 모듈의 xml.etree.ElementTree를 사용해서 RSS 피드를 만들 때는 channel 요소와 item 요소를 모두 SubElement 메서드로 추가. 실수로 오탈자를 내도 무엇이 문제인지 알아채기 힘듦
- 또한 각각의 요소를 만들 때, 문자열을 대입하면서 같은 코드 여러번 반복
- 익숙해지면 큰 문제는 없지만 조금 더 쉽고 간단하게 피드를 만들 수 있는 feedgen이라는 라이브러리 소개
  - feedgen[[URL](https://github.com/lkiesow/python-feedgen)]
1. feedgen 소개
   - feedgen은 pip install 명령어로 설치
     - `$ pip install feedgen`
   - feedgen은 아이템의 부모 요소를 만드는 메서드와 각 아이템 자체를 만드는 메서드가 따로따로 있음. 주의해야 할 점은 네임스페이스 추가와 관련된 내용. feeedgen은 사용자 정의 네임스페이스를 만드는 확장 기능 제공
2. 네임스페이스 추가
   - 예제에서는 xmlns:book="http://my-service.com/xmlns/book" 이라는 네임스페이스 추가
   - feedgen은 기본적으로 dc(Dublin Core Metadata Initiative)와 아이튠즈 팟캐스트(iTunes Podcast)전용 확장 네임 스페이스 모듈 제공. 관련 내용은 다음 링크 참고
     - dc[[URL](https://github.com/lkiesow/python-feedgen/blob/master/feedgen/ext/dc.py)]
     - 팟캐스트:channel 요소[[URL](https://github.com/lkiesow/python-feedgen/blob/master/feedgen/ext/podcast.py)]
     - 팟캐스트:item 요소 [[URL](https://github.com/lkiesow/python-feedgen/blob/master/feedgen/ext/podcast_entry.py)]
3. 디렉터리 만들기
   - feedgen으로 만들 프로그램 전용 디렉터리 생성
   - ```cmd
     $ mkdir rss_with_feedgen
     $ cd rss_with_feedgen
     ```