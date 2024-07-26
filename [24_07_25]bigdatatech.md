
# 부록 - 유용한 라이브러리
## 1. 프로세스 관리 도구 Supervisor
### 1. Supervisor
2. Supervisor로 실행할 프로세스 설정
   - Celery 전용 워커 프로그램 설정 샘플이 다음 URL에 있음. 이를 참고.
   - celery/extra/supervisord/celery.conf[[URL](https://github.com/celery/celery/blob/master/extra/supervisord/celeryd.conf)]
   -  위 설정 파일에 있는 샘플 코드를 참고, 코드 A-1를 작성, /usr/local/etc/superviosr.d/crawler_with_celery_sample.ini 라는 이름으로 저장.
      -  디렉터리 이동
         -  macOS의 파인더에서 [command]+[shift]+[G] 키를 누르면 입력 화면, 여기에 경로 입력 시 이동할 수 있음.
   - ```ini
     [program:celery]
     directory=/Users/username/python/crawler_with_celery_sample
     command=/Users/username/python/crawler_with_celery_sample/venv_crawler_with_celery_sample/bin
     /celery -A crawler_with_celery_sampel booker -Q download -c 2 -l warning -n download@%%h

     autostart=true
     autorestart=true
     startsecs=10
     numprocs=1
     stopwaitsecs = 600
     stopasgroup=false
     killasgroup=false
     user= username
     stdout_logfile=/Users/username/python/crawler_with_celery_sample/booker_download_stdout.log
     stderr_logfile=//Users/username/python/crawler_with_celery_sample/booker_download_stderr.log
     environment=PATH="/Users/username/python/crawler_with_celery_sample/venv_crawlerwith_celery_sample/bin:/usr/local/bin:%(ENV_PATH)s"
     ```
   