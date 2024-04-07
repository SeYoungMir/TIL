# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 3. 네임스페이스를 사용한 RSS 확장 - 이어서
4. 표준 XML 모듈을 사용해서 RSS 생성
   - 파이썬이 표준으로 제공하는 XML 모듈을 사용, RSS 생성.
   - 다음 코드를 py 파일로 저장
   - ```python
     """xml.etree.ElementTree 로 RSS 생성"""
     import xml.etree.ElementTree as ET
     from xml.dom import minidom
     #사용자 정의 네임 스페이스(링크는 예시 링크)
     NAMESPACES= {'book': 'http://my-service.com/xmlns/book'}
     
     def create_rss():
        """RSS 생성"""
        for ns_name, ns_uri in NAMESPACES.items():
            ET.register_namespace(ns_name,ns_uri) # 네임스페이스 등록
        # <rss> 요소 생성
        elm_rss = ET.Element(
            "rss",
            attrib={
                'version':"2.0",
                'xmlns:book': NAMESPACES['book']
            },
        )
        # <channel> 요소 생성
        elm_channel = ET.SubElement(elm_rss,'channel')
        # channel 요소의 서브요소를 한 번에 추가
        channel_sources = {
            'title':"위키북스의 도서 목록",
            'link':"http://example.com",
            'description':"설명 입력 가정.",
        }
        children_of_channel = []
        for tag, text in channel_sources.items():
            child_elm_of_channel = ET.Element(tag)
            child_elm_of_channel.text = text
            children_of_channel.append(child_elm_of_channel)
            # 한 번에 추가
            elm_channel.extend(children_of_channel)

            #<item> 요소 추가: 하나씩 서브 요소 추가
            elm_item = ET.SubElement(elm_channel,'item')
            
            #<item><title>요소 추가
            elm_item_title = ET.SubElement(elm_item,'title')
            elm_item_title.text = "책 제목"

            #<item><link>요소 추가
            elm_item_link = ET.SubElement(elm_item,'link')
            elm_item_link.text = "http://example.com"

            #<item><description>요소 추가
            elm_item_description = ET.SubElement(elm_item,'description')
            elm_item_description.text = ('<a href="http://example.com">이스케이프 처리 확인 전용 링크</a>'"설명 입력 가정.")

            #<item><book:publisher>요소 추가
            elm_item_publisher = ET.SubElement(elm_item,'book:publisher',id="1")
            elm_item_publisher.text = "위키북스"

            #XML 문자열로 변환
            xml = ET.tostring(elm_rss,'utf-8')

            # 앞에 <?xml version="1.0"?>을 추가, 보기 좋게 가공
            with minidom.parseString(xml) as dom:
                return dom.toprettyxml(indent=" ")

        if __name__ == '__main__':
            rss_str = create_rss()
            print(rss_str)
        ```
   - 위 코드에서는 표준으로 제공되는 XML 라이브러리인 xml.etree.ElementTree를 읽어들임. 이름이 너무 길어 as 구문으로 ET라는 별칭 참조
   - 사용자 정의 네임 스페이스를 NAMESPACES라는 딕셔너리 자료형의 변수로 정의. RSS가 표준을 갖고 있지 않은 네임 스페이스인 book을 추가하기 위해 사용. {'네임스페이스 이름':'네임스페이스 URL'}로 지정. '네임스페이스 URL'은 네임스페이스 정의가 작성된 페이지의 URL 지정, 해당 URL에 아무것도 없더라도 큰 문제 없음.
   - 다만 해당 문서 내부에서 URL 중복이 발생하면 안 됨. 인터넷에 공개할 피드를 만들 때에는 피드를 호스팅하고 있는 도메인에 /xmlns/book을 붙여 적당한 URL을 만들어 넣으면 됨. 인터넷에 공개하지 않는 피드를 작성할 때에는 예제처럼 적당하게 넣어도 됨.
   - xml.etree.ElementTree 모듈에 위에서 정의한 네임스페이스 등록, 위에서 정의한 NAMESPACES는 딕셔너리 자료형의 변수, items 메서드 사용해 키와 값을 쌍으로 꺼내 반복문을 돌릴 수 있으며, 예제에서는 ns_name,ns_uri를 반복 변수로 사용, 반복 처리. ET(xml.etree.ElementTree)의 별칭이 가진 register_namespace 메서드에 네임스페이스(ns_name)과 네임스페이스의 URL(ns_uri)을 전달, 네임스페이스 등록
   - NAMESPACES 변수에 네임 스페이스는 하나 이상 추가할 수 있으므로, 반복문으로 처리
   - XML의 최상위 요소인 `<rss>` 생성 ET.Element 메서드 사용, elm_rss 생성. 키워드 매개 변수 attrib에 딕셔너리 자료형의 변수 지정, rss요소의 속성으로 RSS 버전과 사용자 정의 네임 스페이스 추가
   - 현재 많이 사용되는 RSS 버전이 RSS 2.0이므로 version 키의 값은 언제나 "2.0"으로 두면 됨. 네임 스페이스는 xmlns:<네임 스페이스>형태이므로 이를 따름.
   - 이어서 네임스페이스의 값에는 네임스페이스의 URL 지정
   - 이러한 처리로 다음과 같은 XML 개체가 만들어짐
   - ```xml
     <rss version="2.0" xmlns:book="http://my_service.com/xmlns/book">
     </rss>
     ```