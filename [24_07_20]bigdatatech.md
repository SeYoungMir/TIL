# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 5. N그램 사용 - 이어서
3. 텀블러 API에서 추출한 글 데이터를 Whoosh로 인덱싱 - 이어서
   - from dashboard 부분은 dashboard_crawler.py에서 텀블러 API로 대시보드의 글을 추출하느 get_dashboard_posts함수를 읽어 들임.
   - from whoosh_lib 부분은 whoosh_lib.py에서 인덱스 핸들러를 만드는 get_or_create_index 함수를 읽어 들임
   - writer =  부분에서는 인덱스 핸들러의 writer 메서드를 호출, 인덱스 작성에 사용할 writer 객체를 생성.
   - dashboard_posts 부분에서는 위에서 읽어 들인 get_dashboard_posts 함수를 실행. 텀블러 API의 글을 읽어 들임. 추출한 데이터는 dashboard_posts 변수에 저장.
   - for post 부분의 dashboard_posts 변수는 딕셔너리 자료형, posts 키 내부에 리스트로 글이 저장되어 있음. 이를 반복문으로 잉요해 반복하면서 post 변수에 꺼냄
   - writer.update_document부분에서는 위에서 생성한 writer 객체의 update_document 메서드로 인덱스출력을 준비. update_document 메서드는 스키마에 유일 키가 있는 경우 ID가 중복된 데이터라면 덮어쓰고, 중복되지 않았다면 새로 생성.
   - body 부분에서는 글을 나타내는 post['body']를 스키마의 body 필드에 할당. 이 떄 HTML 태그를 w3lib 라이브러리의 w3lib.html.remove_tags메서드를 사용해서 제거
   - writer.commit() 부부에서는 writer 객체의 commit 메서드를 사용해 지금까지 만든 인덱스 데이터를 파일에 반영. 이 코드를 실행하지 않으면 파일로 인덱스가 출력되지 않으므로 주의.
   - 다음 명령어로 whoosh_indexer.py를 실행 시 텀블러 API에서 대시보드를 읽어들이고, 인덱싱(색인 생성)함
     - ```cmd
       (venv_tumblr_search) $ python whoosh_indexer.py
       ```