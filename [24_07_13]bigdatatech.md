# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 1. 텀블러(Tumblr)란?
4. 텀블러 API 애플리케이션 등록 - 이어서
   - 반드시 입력해야하는 부분은 다음과 같음.
   - <table>
        <tr>
            <th>항목</th>
            <th>입력 예</th>
        </tr>
        <tr>
            <td>앱이름</td>
            <td>dashboard_crawler</td>
        </tr>
        <tr>
            <td>앱 웹사이트</td>
            <td>https://localhost:5000/app</td>
        </tr>
        <tr>
            <td>앱 설명</td>
            <td>대시보드를 크롤링</td>
        </tr>
        <tr>
            <td>기본 콜백 URL</td>
            <td>http://localhost:5000/callback_page</td>
        </tr>
        <tr>
            <td>혹시 로봇이신가요?</td>
            <td>체크</td>
        </tr>
     </table>
    - 위와 같이 입력했다면[등록]버튼 클릭. [등록]버튼 클릭 후에는 다음 [Explore API]라는 문자열 링크가 있는 화면으로 이동, 링크 클릭.
    - 계정 정보 허용 요청 화면 나오면 [수락] 클릭. 수락 버튼을 클릭 시 Ruby, PHP,자바스크립트,자바,파이썬,오브젝티브C에서 API를 사용하는 샘플 코드 나옴.
5. 샘플 코드 사용
   - [PYTHON] 클릭 후 오른쪽 사이드 메뉴에서 [Dashboard]를 클릭, 샘플 코드에는 실제 API 요청에 사용할 수 있는 토큰이 나옴.이를 그대로 사용하면 됨. 샘플 코드는  pytumblr라는 API를 사용하고 있음을 확인 가능.
     - pytumblr[[URL](https://github.com/tumblr/pytumblr)]
     - 공식적으로 제공하는 pytumblr는 파이썬3을 지원하지 않으므로 다음명령어를 사용해서 파이썬 3을 지원하는 버전 설치
     - ```cmd
       (venv_tumblr_search) $ pip install https://github.com/dianakhuang/pytumblr/archive/diana/python-3-support.zip
       ```