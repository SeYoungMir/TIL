# 5. 크롤러 설계/개발(응용)
## 2. print 함수로 로그 출력
### 2. 로그 출력과 관련된 다양한 개선 필요 이유
1. with 구문으로 close 메서드 누수 막기
   - 파이썬에는 파일 객체의 close 메서드 누수를 막을 수 있는 기능이 있음. with 구문이 바로 그것으로,예제로 하단과 같은 구문에서 close 메서드 누수를 막을 수 있음
   - with 구문을 사용하면 with 구문을 빠져나올 때 close 메서드가 자동 호출, 예외 발생 시도 close 메서드 호출.
   - 이전 코드 부분에서
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
        with open('crawler_info.log','a') as f_info_log, 
        open('crawler_error.log','a') as f_error_log:
            # 추출 내용 저장 딕셔너리
            page_contents = {}
    ```
  - 위와 같이 수정 시, close 메서드 누수 관련 불안 제거
  - 다른 처리에서 같은 로그 파일에 내용 출력 시는 로그 파일 이름 입력 시 실수하지 않도록 주의
  - 만약 더 많은 로그 종류를 추가하고 싶다면 매개 변수가 점점 증가, 복잡해질 수 있음
  - 이런 경우에 logging 모듈을 사용, 관리 할 수 있음
## 3. logging 모듈로 로그 출력, 관리
### 1. logging 모듈 사용
   - 이전의 다양한 문제를 해결하기 위해 파이썬이 기본적으로 제공하는 로그 출력 전용 라이브러리인 logging 모듈을 사용 가능
   - 세부적인 설명을 이용해 로그를 굉장히 유연하게 출력하고 관리할 수 있게 해줌.