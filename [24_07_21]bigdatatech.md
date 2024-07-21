# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 5. N그램 사용 - 이어서
4. 인덱스를 기반으로 검색
   - 인덱싱 명령어 실행이 완료되었다면 터미널에서 키워드를 입력해서 검색할 수 있는 프로그램을 제작.
   - 다음 코드를 whoosh_searcher.py라는 이름으로 저장.
   - ```python
     import sys
     
     from whoosh_lib import get_or_create_index
     from whoosh.qparser import QueryParser

     if __name__=='__main__':
        # 인덱스 읽어 들이기
        ix= get_or_create_index()

        # 키워드 입력 프롬프트를 출력해서, 키워드 입력받기
        keyword=input("검색 키워드를 입력:")

        # body 필드를 대상으로 문자열 검색
        with ix.searcher() as searcher:
            # 키워드를 사용해서 검색 쿼리 객체 생성
            query = QueryParser("body",ix.schema).parse(keyword)
            # 검색 실행
            results= searcher.search(query)
            if not results:
                print('검색 결과가 없습니다.')
                sys.exit(0)
            print('검색 결과를 출력.')
            for i, r in enumerate(results):
                print("{}:post_url: {}".format(i+1,r['post_url']))
    ```