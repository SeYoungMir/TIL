# 5. 크롤러 설계/개발(응용)
## 2. print 함수로 로그 출력
### 2. 로그 출력과 관련된 다양한 개선 필요 이유
- print 함수를 사용하면 로그를 굉장히 간단하게 출력할 수 있지만 개발이 안정되고, 프로그램이 실제 운영 환경으로 이동한 경우에는 개발을 위해 출력했던 로그는 더 이상 필요 없음.
- 그러나 로그가 계속 출력된다면 이는 노이즈
- 예를 들어 조건 분기에서 사용되는 변수를 항상 출력했을 때, 로그가 쌓이면 이후에 다른 문제가 발생했을 때 많은 출력 중에서 진짜 오류 출력을 찾는데 오래 걸리게 됨. 또한 어떤 로그가 오류인지, 개발 전용 로그인지도 구분해야함. 레이블로 태그 등을 붙이기에는 귀찮으며, 이를 깜빡하면 버그가 되어서 실제 오류를 놓칠 수도 있음
- 상황의 중요성에 따라서 자동으로 레이블이 붙으면 굉장히 편리해짐
- 콘솔 화면 출력과 함께 파일에도 출력하기 위해서는 tee 명령어를 사용 가능
```python
$ python crawler.py | tee -a crawler.log
```
- 단순한 로그만 있어도 될 때는 tee 명령어도 사용 가능, 디버그 전용 로그와 오류 로그를 서로 다른 파일에 출력하고 싶다면 코드 구현 필요
```python
import json
import time
import requests

# 대상 URL 리스트
PAGE_URL_LIST=[
        'http://example.com/1.page',
        'http://example.com/2.page',
        'http://example.com/3.page',
]
def fetch_pages():
    """내용 추출"""
    # 처리 기록 전용 로그 파일 append 모드로 오픈
    f_info_log = open('crawler_info.log','a')
    # 오류 기록 전용 로그 파일 append 모드로 오픈
    f_error_log = open('crawler_error.log','a')
    # 추출 내용 저장 딕셔너리
    page_contents = {}

    # 터미널에 처리 시작 출력, 로그 파일 메시지 출력
    msg= "크롤링 시작\n"
    print(msg)
    f_info_log.write(msg)

    for page_url in PAGE_URL_LIST:
        r = requests.get(page_url,timeout=30)
        try:
            r.raise_for_status() # 응답에 문제가 있으면 예외 발생
        except requests.exceptions.RequestException as e:
            # requests와 관련된 예외 발생 시 터미널과 오류 로그에 오류 출력
            msg = "[ERROR] {exception}\n".format(exception=e)
            print(msg)
            f_error_log.write(msg)
            continue # 예외 발생 시 반복 중지가 아니라 건너뜀

        # 정상적으로 내용 추출 시 딕셔너리에 내용 저장
        page_contents[page_url] = r.text
        time.sleep(1)

        f_info_log.close()
        f_error_log.close()

        return page_contents
if __ name__ == '__main__':
    page_contents = fetch_pages()
    f_page_contents = open('page_contents.json','w')
    json.dump(page_contents,f_page_contents,ensure_ascii=False)
    f_page_contents.close()
```
- 상태 출력위한 crawler_info.log와 오류 출력 위한 crawler_error.log라는 로그 파일을 open 메서드로 열고, 최종적으로 close 메서드로 종료. 규모가 커졌을 때 파일을 제대로 닫지 않으면 파일을 열고 쓸 때 충돌 발생 가능
- 위 상태로 출력 시 page_url이 불완전한 URL이라면 requests.get 메서드에서 예외 발생.
- try구문으로 requests.get 메서드로 감싸여있지 않으므로 예외 처리 불가로 프로그램 종료.