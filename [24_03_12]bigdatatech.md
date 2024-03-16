# 6. 스크레이핑 개발(응용)
## 1. XML로 변환
### 3. Orator 사용
2. XML 만들기
   - XML을 구축할 때는 표준으로 제공되는 xml 모듈을 사용
   ```python
   """DB의 내용을 다양한 형식으로 출력하기"""
   import xml.etree.ElementTree as ET
   from xml.dom import minidom
   import logging

   from orator import DatabaseManager , Model
   from orator.orm import belongs_to,has_many

   # Orator가 어떤 SQL을 실행하는지 로그로 출력해서 확인하기
   logger = logging.getLogger('orator.connection.queries')
   logger.setLevel(logging,DEBUG)

   formatter = logging.Formatter('It took %(elapsed_time)sms to execute the query %(query)s'
   )
   handler = logger.StreamHandler()
   handler.setFormatter(formatter)

   logger.addHandler(handler)

   # MySQL 접속 설정
   config = { 
    'mysql':{
        'driver' :'mysql',
        'host' : 'localhost',
        'database' : 'book_db',
        'user' : 'root',
        'password' : '',
        'prefix' : '',
        'log_queries': True,
    }
   }
   
   db = DatabaseManager(config)
   Model.set_connection_resolver(db)

   # 각 테이블과 객체의 관계성 정의
   # 클래스 이름이 소문자 또는 스네이크 케이스로 변경되어 테이블의 이름과 대응됨

   class Language(Model):
        """언어의 종류"""
        pass
   class Book(Model):
        """도서"""
        # books 테이블의 language_id에 해당하는 데이터 가져오기
        @belongs_to
        def language(self):
            """책의 언어"""
            return Language
        # publishers 테이블의 publisher_id에 해당하는 데이터 가져오기
        @belongs_to
        def publisher(self):
            """책의 출판사"""
            return Publisher
    class Publisher(Model):
        """출판사"""
        # 하나의 출판사에는 여러 도서가 들어갈 수 있음
        @has_many
        def books(self):
            """출판사의 도서들"""
            return Book
    # 변환함수
    def create_xml():
        """XML 만들기"""
        elm_root = ET.Element("catalog")
        publishers = Publisher.all()
        publishers.load('books','books.language') # Eager Loading
        for publisher in publishers:
            for book in publisher.books:
                elm_book = ET.SubElement(elm_root,"book",id=str(book.id))
                ET.SubElement(elm_books,"publisher",id=str(publisher.id)).text=publisher.name
                ET.SubElement(elm_book,"title").text=book.title
                ET.SubElement(elm_book,"language",id=str(book.language.id)).text=book.language.name
        with minidom.parseString(ET.tostring(elm_root,'utf-8')) as dom:
            return dom.toprettyxml(indent="  ")

   # main 실행 블록
   if __name__ == '__main__':
        xml_str=create_xml()
        print(xml_str)
   ```
   - `publisher.load('books','books.language')` 부분에서
   Eager Loading(즉시 로딩) 이라고 부르는 '관련된 데이터를 먼저 읽어두는 처리'
   이 부분이 없으면 반복문에서 publisher.books나 book.language.name이 호출될 때마다 해당 출판사와 관련된 데이터베이스 쿼리 발행

   - 현재 소개하는 샘플은 데이터의 개수가 적으므로 큰 영향이 없지만, Eager Loading이 없는 경우 데이터베이스 내부에 등록된 데이터가 많으면 많을수록 성능이 굉장히 떨어지게 됨.
   - 이러한 문제를 일반적으로 'N+1' 문제라고 부르며, 데이터베이스에 쿼리를 발행할 때 굉장히 주의해야하는 고전적인 예
   - ORM 사용할 때 내부에서 어떤 쿼리가 실행되는지 주의해야함
   - Orator가 내부적으로 발행하는 SQL을 출력하기 위해 logging.getLoggger 메서드의 매개 변수에 Orator 쿼리 로거 이름(orator.connection.queries)을 전달하는 부분에서 logger.setLevel 메서드를 사용. Orator 쿼리 로거의 로그 레벨을 DEBUG(logging.DEBUG)로 정의.
   - 이 경우 book_db_xml_exporter.py를 실행할 때 Orator 가 내부적으로 발행하는 SQL 출력.
   - DEBUG 레벨을 INFO 레벨로 설정하면 디버그 로그 따로 출력되지 않음.
   - 데이터가 예제는 아주 작지만, 수천 수만명의 데이터 출력 시에는 출력 방법과 성능을 고려해야함.