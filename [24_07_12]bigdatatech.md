# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 1. 텀블러(Tumblr)란?
- 매일매일 인터넷의 다양한 콘텐츠가 인용되어 게시, 작성자를 팔로우하면 '대시보드;라는 메인 화면에서 그들이 올리는 글을 볼 수 있음.
  - 텀블러(Tumblr)[[URL](https://www.tumblr.com)]
- 텀블러는 굉장히 재미있는 콘텐츠가 많이 올라오는 자유도가 굉장히 높은 서비스, 검색할 때 약간 힘든 점이 있음.
- '예전에 봤던 글을 찾고 싶을 때' 다른 내용들까지 검색되어 이전에 봤던 글을 찾기가 쉽지 않음.
- 따라서 이번 절에서는 내 타임라인에 올라온 글들을 크롤링해서 수집, 수집한 내용 안에서 검색하는 프로그램 생성. 이를 활용하면 '예전에 봤던 글을 찾고자 할 때' 쉽게 찾아볼 수 있음.
1.  텀블러 계정 생성.
    - 텀블러 API를 사용하려면 사용자 계정을 등록해야 함. 따라서 계정이 없다면 계정을 만들어야 함. 계정은 텀블러 메인 페이지에서 생성 가능.
    - 계정을 만들었다면 적당한 사용자 몇 명을 팔로우, 팔로우 해야 이후에 글을 크롤링할 수 있음.
2. venv 가상 환경 만들기
   - 작업을 시작하기 전에 venv로 가상 환경 생성.
   - ```cmd
     $ python -m venv venv_tumblr_search
     $ source venv_tumblr_search/bin/activate
     ```
3. 웹 API 사용
   - 텀블러는 공식적으로 웹 API(WebAPI)제공. 애플리케이션을 등록해서 요청 토큰을 받으면 API를 사용할 수 잇음.
     - 텀블러 API 문서 페이지[[URL](https://www.tumblr.com/docs/en/api/v2)]
4. 텀블러 API 애플리케이션 등록
   - 텀블러 API 애플리케이션 등록 페이지에 들어감. 다음 페이지에서 [+ 앱 등록]버튼을 클릭.
   - 애플리케이션 등록 페이지[[URL](https://www.tumblr.com/oauth/apps)]
   - 앱 등록 버튼을 누르면 애플리케이션 등록 화면으로 이동.