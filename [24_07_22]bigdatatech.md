# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 5. N그램 사용 - 이어서
5. whoosh_searcher.py
   - from whoosh_lib 부분에서는 whoosh_lib.py에 정의한 get_pr_create_index함수를 읽어들임. ix= 부분에서 읽어들인 get_or_Create_index 함수를 호출, 인덱스 핸들러를 추출.
   - keyword= 부분에서는 내장 함수 input을 사용, 터미널에 입력 프롬프트를 출력. 사용자가 프롬프트에 키워드를 입력 시 keyword 변수에 저장
   - with ix.searcher 부분에서는 인덱스 핸들러의 searcher() 메소드를 호출, 검색 처리를 하는 searcher 객체를 생성
   - query 부분에서는 입력된 키워드를 기반으로 검색 쿼리 객체를 생성. QueryParser 함수를 사용해서 body 필드를 대상으로 검색 쿼리를 생성.
   - results 부분에서는 searcher 객체의 search() 메서드의 매개 변수로 query 부분에서 만든 쿼리 객체를 전달. 이렇게 하면 검색 처리가 이뤄짐. 검색 결과는 변수 results에 저장. query 부분에서 검색 결과가 찾아지지 않을 때는 if not 부분으로 넘어감. 터미널에 메시지를 출력한 뒤 프로그램을 곧바로 종료
   - for i,r in 부분에서는 찾은 검색 결과를 반복문으로 하나하나 꺼내고, URL 출력.다음 명령어로 whoosh_searcher.py를 실행, 검색 결과를 출력. 검색 키워드로는 'test'를 사용.
   - ```cmd
     (venv_tumblr_search) $ python whoosh_searcher.py
     ```
   - 팔로우한 사용자와 인덱싱을 실행했을 때 대시보드에 있던 글에 따라서 결과가 다르게 나올 수 있음. (팔로우한 사용자가 너무 없으면 아예 검색되지 않을 수도 있음.)대시보드를 확인, 인덱싱을 실행했을 때 글에 포함되어 있던 단어로 검색 추천
