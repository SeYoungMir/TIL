# 5. 크롤러 설계/개발(응용)
## 4. 로그 출력 라이브러리로 로그 관리
### 1. 서드 파티 로그 출력 라이브러리 사용
- 모던 웹 프레임워크를 사용한 경험이 있다면 logger.error('some message') 와 같이 입력하면 [ERROR] <시간> some message 처럼 출력되는 걸 볼 수 있음
- logging 라이브러리를 사용하면 굉장히 유연하고 강력한 로그 출력이 가능하지만 조금 복잡함
- 서드파티 로그 출력 전용 라이브러리를 사용, Eliot을 사용해 로그 출력 시도.
1. Eliot 설치
   - pip install 명령어 사용, 로그 출력 전용 라이브러리 Eliot 설치 `$ pip install eliot`
2. Eliot 사용
   - 설치 후 Eliot 사용 코드 작성. 다음과 같이 작성
    ```python
    import json
    import sys

    from eliot import Message, start_action,to_file,write_traceback
    import requests

    # 로그 출력을 표준 출력으로 설정 (터미널 출력)
    to_file(sys.stdout)

    # 크롤링 대상 URL 리스트
    PAGE_URL_LIST = [
        'https://eliot.readthedocs.io/en/1.0.0',
        'https://eliot.readthedocs.io/en/1.0.0/generating/index.html',
        'https://example.com/notfound.html',
    ]
    
    def fetch_pages():
        """페이지 내용 출력"""
        # 어떤 처리의 로그인지는 action_type로 지정
        with start_action(action_type="download",url=page_url):
            try:
                r = requests.get(page_url, timeout=30)
                r.raise_for_status()
            except requests.exceptions.RequestExceptions as e:
                write_traceback() #예외 발생 시 트레이스백 출력
                continue
            page_contents[page_url] = r. text
        return page_contents
    if __name__ = '__main__':
        page_contents = fetch_pages()
        with open('page_contents.json','w') as f_page_contents:
            json.dump(page_contents,f_page_contents,ensure_ascii = False)
    # 단순하게 로그 메시지만 출력시
    Message.log(message_type="info',msg="데이터 저장함")
    ```
3. 명령어 실행해서 출력
   - 코드를 모두 작성했다면 이하 명령어 입력, 실행. 파이프하고 있는 eliot-prettyprint명령어는 eliot 라이브러리가 출력하는 로그 형식 가공 명령어
   - `$ python sample_eliot.py|eliot-prettyprint`
   - start_action 메서드를 조합한 with 블록마다 지정한 변수와 상황 출력