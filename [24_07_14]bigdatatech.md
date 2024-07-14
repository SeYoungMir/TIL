# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 1. 텀블러(Tumblr)란?
5. 샘플 코드 사용 - 이어서
   - Dashboard 부분의 위에 있는 입력 양식에서 'Type'을 'text'로 하면 대시보드에 올라오는 텍스트 타입의 포스트를 API로 추출할 수 있는 코드가 나옴.
   - 샘플 코드 페이지에 있는 코드를 다음 코드처럼 수정, dashboard_crawler.py라는 이름으로 현재 ㄷ렉터리에 저장.
   - ```python
     """Tumblr 대시보드를 크롤링"""
     import json
     import pytumblr

     # OAuth 인증을 사용한 API 클라이언트 객체를 생성
     client = pytumblr.TumblrRestClient(
        # 이하 부분은 샘플 코드 부분을 복사해서 사용
        """이하 내용
        """
     )
     def get_dashboard_posts():
        """대시 보드의 글 추출"""
        return client.dashboard(type='text')
     if __name__ == '__main__':
        dashboard_posts = get_dashboard_posts()
        print(json.dumps(dashboard_posts,ensure_ascii=False))
     ```
6. 코드 실행.
   - 위 코드를 실행 시 JSON  형식으로 응답 받을 수 있음. jq 명령어로 파이프해서 가공한 다음 출력
   - ```cmd
     (venv_tumblr_search)$ python dashboard_crawler.py | jq .
     ```
   - 다음 텀블러 API 문서를 참고하면 post_url 필드에 업로드한 글의 URL, body 필드에 글 본문이 들어있다는 것을 알 수 있음.
     - 텀블러 API 문서[[URL](https://www.tumblr.com/docs/en/api/v2#m-posts-responses)]
   - 지금까지 API를 사용해서 텀블러 대시보드에 올라오는 글을 추출. 이어서 글 검색 엔진과 조합해서 활용.