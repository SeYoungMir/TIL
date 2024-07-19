# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 5. N그램 사용 - 이어서
2. Whoosh의 인덱스 저장 전용 디렉터리 생성 - 이어서
   - 글을 인덱스로 만들 수 있게 '인덱스 개체'를 Whoosh에 등록해서 사용
   - schema = 부분에서는 인덱스 객체의 스키마(구조)를 정의. 예제에서는 글의 URL을 저장할 post_url과 글 본문을 저장할 body라는 스키마 보유.
   - 인덱스 객체를 유일하게 특정할 수 있게 ID 필드를 사용. 이는 post_url 부분에서 하고 있음. unique= True로 지정 시 해당 필드의 값이 중복되지 않음. stored=True로 지정시 글 URL을 인덱스 객체에 함께 저장.
   - body= 부분에서 글을 N그램으로 인덱스하게 지정. stored=True를 지정해서 분할되지 않은 원본 글도 인덱스 객체에 저장.
   - def get_or_create_index() 부분에서는 인덱스 데이터를 저장할 디렉터리 준비. 디렉터리가 없으면 디렉터리를 생성, 인덱스 저장 전용 파일을 index.create_in 메서드로 생성해서 반환. 만약 디렉터리가 있다면 해당 파일을 index.open_dir 메서드로 열고 반환.
3. 텀블러 API에서 추출한 글 데이터를 Whoosh로 인덱싱
   - 인덱싱이란 인덱스를 만드는 것을 의미. 다음 코드를 입력, whoosh_indexer.py라는 파일 이름으로 저장
   - ```python
     import os
     import sys
     import time
     import w3lib.html
     from dashboard_crawler import get_dashboard_posts
     from whoosh_lib import get_or_create_index

     if __name__ == '__main__':
        # 인덱스 핸들러 읽어 들이기
        ix = get_or_create_index()

        # 인덱스 쓰기 전용 writer 객체 만들기
        writer = ix.writer()

        # 대시보드의 글 추출
        dashboard_posts = get_dashboard_posts()

        # 데이터 인덱싱
        for post in dashboard_posts['posts]:
            writer.update_document(
                post_url=post['post_url'],
                # 인덱스 대상 문장에서 HTML 태그 제거
                body=w3lib.html.remove_tags(post['body']),
            )
        # 인덱스 반영
        writer.commit()
     ```