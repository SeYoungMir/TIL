# 5. 크롤러 설계/개발(응용)
## 2. print 함수로 로그 출력
### 1. 로그를 화면 또는 파일에 출력
- 크롤러를 만들 때 크롤링 진행 상태 출력 또는 디버그 하기위해 조건 분기에 사용되는 변수의 내용 확인하고 싶을때
- 최종적으로는 데이터 저장소에 데이터를 저장, 크롤링 과정에서 눈으로 상황 확인하고 싶을 때. 동작하는 상황을 중간중간에 출력, 확인하는 과정에 사용
- 프로그램의 동작 상태 또는 이력이 출력된 텍스트를 '로그(log)'라고 함
1. print 함수와 출력 형식
   - 일반적으로 프로그램을 디버그할 때 기본적이고 널리 사용되는 방법
   - 이를 print 디버그라고 부름
   - 단순 변수 출력시는 print(value)를 사용, 이후 항목 추가를 위해 레이블 붙여 사용하면 편리
   - `print("lable:" +value)`
2. 요청에 걸린 시간 출력
   - 요청한 URL,HTTP 상태, 문자 코드, 요청에 걸린 시간 출력
   - HTTP 요청에는 파이썬 대표적인 HTTP 라이브러리 requests 사용
    ```python
    import time
    import requests

    PAGE_URL_LIST=[
        'http://example.com/1.page',
        'http://example.com/2.page',
        'http://example.com/3.page',
    ]
    for page_url in PAGE_URL_LIST:
        res = requests.get(page_url,timeout=30)
        print(
            "페이지 URL:" + page_url+","+\
            "HTTP 상태: " + str(res.status_code)+","+\
            "처리 시간(초): " + str(res.elapsed.tatal_seconds())
        )
        time.sleep(1)
    ```
    - 파이썬은 동적으로 자료형 지정하는 언어, 변수가 자료형 가짐
    - 다른 자료형끼리 연상하기 위해 기본적으로 자료형 변환 필요
    - requests 모듈의 응답 객체(변수 res)에서 추출한 HTTP 상태 코드(변수 res.status_code)는 int 자료형. 문자열과 숫자를 결합하기 위해 int 자료형을 str 자료형으로 변환한 다음 결합
    - print 함수 사용 시 계속 처리하기 복잡하므로 문자열 자료형의 format 메서드 사용하는 경우 더 많음
    ```python
     print(
            "페이지 URL:{} ,HTTP 상태: {} ,처리 시간(초): {} ".format(
                page_url,
                res.status_code,
                res.elapsed.total_seconds()
            )
    ```
    