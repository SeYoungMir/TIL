# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 4. feedgen을 사용해서 RSS 생성
4. 네임스페이스 전용 클래스 생성.
   - 네임 스페이스 전용 클래스 생성. 파일이름은 feedgen_ext.py
   - ```python
     """feedgen 확장 네임 스페이스(book: http://my_service.com/xmlns/book)."""
     from lxml import etree
     from feedgen.ext.base import BaseExtension

     class BookBaseExtension(BaseExtension):
        """book 확장 네임 스페이스"""
        # 사용자 정의 네임 스페이스의 URL
        BOOK_NS = "http://my_service.com/xmlns/book"

        def __init__(self):
            """사용자 정의 요소 이름 앞에는 __ 삽입"""
            # 변수는 딕셔너리 자료형으로
            self.__publisher= {}
        def extend_ns(self):
            """확장 네임 스페이스"""
            return {'book':self.BOOK_NS}
        
        def _extend_xml(self,elm):
            """요소 추가"""
            if self.__publisher:
                publisher = etree.SubElement(
                    elm,#부모요소
                    '{%s}publisher' % self.BOOK_NS #{<네임스페이스의 URL>} 요소 이름
                    attrib={'id':self.__publisher.get('id')}
                )
                publisher.text = self.__publisher.get('name')# 요소의 내용 적용
            return elm

        def publisher(self,name_and_id_idct=None):
            """self.__publisher"""
            if name_and_id_dict is not None:
                name = name_and_id_dict.get('name')
                id_ = name_and_id_dict.get('id')
            if name and id:
                self.__publihser = [{'name':name,'id':id_}]
            elif not name and not id_: #name이 없는 경우는 요소를 만들지 않음
                self.__publisher = {}
            else:  
                raise ValueError('name과 id를 함께 지정')
        return self.__publisher

        class BookFeedExtension(BookBaseExtension):
            """channel 요소에 적용"""
            def extend_rss(self,rss_feed)"
            """요소 추가때 호출"""
                channel = rss_feed[0]
                self._extend_xml(channel)
        class BookEntryExtension(BookBaseExtension):
            """item 요소에 적용"""
            def extend_rss(self,entry):
                """요소 추가때 호출"""
                self._extend_xml(entry)
        ```