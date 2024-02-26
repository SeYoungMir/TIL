# 5. 크롤러 설계/개발(응용)
## 3. logging 모듈로 로그 출력, 관리
### 1. logging 모듈 사용
1. logging을 사용하는 예제 만들고 설정
   - 예제 코드
    ```python
    from logging import (
        getLogger,
        Formatter,
        FileHandler,
        StreamHandler,
        DEBUG,
        ERROR,
    )
    import requests

    # 로거 : __name__ 에는 실행 모듈 이름 logging_sample이 들어감
    logger = getLogger(__name__)

    # 출력 형식
    default_format = '[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d %(message)s'
    default_formatter = Formatter(default_format)
    funcname_formatter = Formatter(default_format + '(%(funcName)s)')
    
    # 로그 전용 핸들러 : 콘솔 출력
    log_stream_handler = StreamHandler()
    log_stream_handler.setFormatter(default_formatter)
    log_stream_handler.setLevel(DEBUG)
    
    # 로그 전용 핸들러 : 파일 출력
    log_file_handler = FileHandler(filename="crawler.log")
    log_file_handler.setFormatter(funcname_formatter)
    log_file_handler.setLevel(ERROR)

    # 로거에 핸들러와 레벨 설정
    logger.setLever(DEBUG)
    logger.addHandler(log_stream_handler)
    logger.addHandler(log_file_handler)

    def logging_example():
        logger.info('크롤링 시작')
        logger.warning('외부 사이트 링크 크롤링 제외')
        logger.error('사이트 탐색 실패')

        try:
            r = requests.get('#invalid_url',timeout=1)
        except requests.exceptions.RequestsException as e:
            logger.exception('요청 중 예외 발생: %r', e)
    if __name__ == '__main__':
        logging_example()
    ```
    - 이후 파이썬으로 위 스크립트 실행, 제대로 실행되는지 확인
    - 출력 결과를 보면 출력 레벨이 핸들러별로 상이함
    - Logging HOWTO 튜토리얼[(URL)](https://docs.python.org/3/howto/logging.html)에도 기입되어있지만, 일회용 스크립트가 아닌 이상 직접 logging 모듈의 메서드로 로그를 출력하지 않는 것이 좋음.
    - 루트 로거만 사용하면 직접 만든 모듈을 다른 프로젝트에서 임포트해 사용할 때 해당 프로젝트에서 직접 만든 모듈의 로그 출력을 제어하기 어려워짐.
    - logging 모듈을 사용해서 만든 로그 출력 전용 객체인 로거(logger)는 계층 구조를 가지며, 로거 이름별로 다른 출력 설정 지정 가능, 루트 로거는 디폴트로 존재하는 최상위 로거를 의미.
