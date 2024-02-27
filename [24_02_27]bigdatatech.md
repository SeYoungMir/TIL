# 5. 크롤러 설계/개발(응용)
## 3. logging 모듈로 로그 출력, 관리
### 2. 딕셔너리 형식으로 설정 작성
- 로거 설정은 명령문으로도 설정 가능하나, 파이썬의 딕셔너리 자료형을 사용한 형식으로도 설정 가능
- 위 경우 설정을 logging.dictConfig 메서드로 읽음
  * dictConfig 메서드
    - dictConfig 메서드를 사용할 때는 version: 1이라는 키와 값 필수
- settings.py라는 파일 이름으로 저장, 출력을 쉽게 볼 수 있게 colorlog 라이브러리를 사용, 로그에 색을 지정.
- pip install 명령어 사용, colorlog 라이브러리 설치
- `$ pip install colorlog`
- 이하 코드는 로그와 관련된 설정 작성 스크립트 파일
```python
"""설정 파일"""
import os

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs') #로그 파일 디렉터리

#로그 파일 디렉터리가 없다면 생성
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOGGING_CONF = {
    'version': 1, #필수 
    # logger 설정 처리가 중복되면 덮어씌우기
    'disable_existing_loggers': True,
    #출력 형식 설정
    'formatters' : {
        'default' : { #디폴트 형식
            '()' : 'colorlog.ColoredFormatter', # colorlog 라이브러리 적용
            'format' : '\t'.join([
                "%(log_color)s[%(levelname)s]", # 로그 레벨
                "asctime: %(asctime)s", # 로그 출력 날짜
                "process:%(process)d", # 로그 출력 실행 프로세스 이름
                "thread:%(thread)d", # 로그 출력 실행 프로세스 ID
                "module:%(module)s",#로그 출력 실행 프로세스 모듈 이름
                "%(pathname)s:%(lineno)d", #로그 출력을 실행한 모듈 경로와 줄 번호
                "message:%(message)s", #로그 출력 메시지
            ]),
            'datefmt':'%Y-%m-%d %H:%M:%S',#asctime으로 출력할 로그 출력 날짜 형식
            #로그 레벨에 따라 색 적용
            'log_colors':{
                'DEBUG':'bold_black',
                'INFO':'white',
                'WARNING':'yellow',
                'ERROR':'red',
                'CRITICAL':'bold_red',
            },
    },
    'simple' : { # 로그를 적게 출력하는 간단한 형태의 형식
        '()': 'colorlog.ColoredFormatter', # pip install colorlog
        'format' : ' \t'.join({
            "%(log_color)s[%(levelname)s]",
            "%(asctime)s",
            "%(message)s", #로그 레벨, 날짜, 메시지만 출력
        }),
        'datefmt':'%Y-%m-%d %H:%M:%S',#asctime으로 출력할 로그 출력 날짜 형식
            #로그 레벨에 따라 색 적용
            'log_colors':{
                'DEBUG':'bold_black',
                'INFO':'white',
                'WARNING':'yellow',
                'ERROR':'red',
                'CRITICAL':'bold_red',
            },
    },
    'query' : { #SQL 쿼리 출력 전용 형식
        '(): 'colorlog.ColoredFormatter',
        'format':'%(cyan)s[SQL] %(message)s', #쿼리만 출력
    },
},
# 로그 출력 대상에 따른 핸들러 설정
'handlers':{
    'file':{ # 파일에 로그를 출력할 핸들러 설정
        'level':'DEBUG', # logger.level이 DEBUG 이상일 때만 출력
        #로그 크기가 일정량을 넘으면 새로운 로그 파일을 생성하는 핸들러
        'class' : 'logging.handlers.RotationgFileHandler',
        #로그 파일 경로 지정
        'filename':os.path.join(LOG_DIR,'crawler.log'),
        'formatter':'default', # 디폴트 형식으로 로그 출력
        'backupCount':3, # 오래된 로그 파일은 3개만 남김
        'maxByte':1024*1024*2, #로그 크기가 2MB를 넘을 경우 새로운 로그 파일 생성
    },
    'console':{ # 터미널에 로그를 출력하는 핸들러의 로그 형식 지정
        'level' : 'DEBUG',
        'class' : 'logging.StreamHandler', # 터미널에 로그를 출력할 핸들러
        'formatter':'default',#디폴트 형식으로 로그 출력
    },
    'console_simple':{ # 터미널에 로그를 출력하는 핸들러의 간단한 로그 형식 지정
        'level' : 'DEBUG',
        'class' : 'logging.StreamHandler', 
        'formatter':'simple',#간단한 형식 지정
    },
    'query' : { # 터미널에 SQL 쿼리 로그를 출력할 핸들러
        'level' : 'DEBUG',
        'class' : 'logging.StreamHandler', 
        'formatter':'query', #SQL 쿼리 출력 전용 형식
    },
},
'root':{ # 디폴트 설정
    'handlers':['file','console_simple'], # 위에 설정한 file,console 설정으로 출력
    'level':'DEBUG',
},
# 로그 이름, 핸들러, 로그 레벨 설정
'loggers': {
    # logging,getLogger(__name__)의 __name__으로 참조되는 이름이 키로 사용
    'celery':{
        'handlers' : ['console','file'],
        'level':'WARNING', # Celery 로그는 WARNING 이상만 출력
        'propagate': False, # 로그 이벤트를 루트 로거에 전달하지 않게 지정
    },
    'my_project' : { # my_project.py 모듈에서 사용할 때의 로거
        'handlers':['console','file'],
        'level':'DEBUG',
        'propagate':False,
    },
},
}
```
- 이러한 설정을 쉽게 사용할 수 있게 로그 전용 모듈을 생성
```python
"""로그 전용 모듈"""
import logging.config

import settings

def get_my_logger(name):
    logging.config.dictConfig(settings.LOGGING_CONF)
    return logging.getLogger(name)
logger = get_my_logger(__name__)

if __name__ == '__main__':
    """my_logging 사용"""
    logger.debug('DEBUG 레벨')
    logger.info('INFO 레벨')
    logger.warning('WARNING 레벨')
    logger.error('ERROR 레벨')
    logger.critical('CRITICAL 레벨')
```

- my_logging.py를 실행, 로그 출력이 어떻게 되는지 확인
`$ python my_logging.py`
- 로그 파일도 살펴보기
`$ cat logs/crawler.log`