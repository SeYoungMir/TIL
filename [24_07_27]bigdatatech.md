# 부록 - 유용한 라이브러리
## 1. 프로세스 관리 도구 Supervisor
### 1. Supervisor
2. Supervisor로 실행할 프로세스 설정 - 이어서
   - 파일을 만들었다면 다음 명령어로 설정 반영
   - ```bash
     (venv_crawler_with_celery_sample) $ supervisorctl -c /usr/local/etc/supervisord.ini reload
     ```
   - supervisorctl을 사용, reload 옵션의 설정 반영 후, 설정 파일의 autostart = true로 설정하면 자동으로 프로세스 실행
   - 10초정도 기다리고, 다음 명령어를 사용해서 Celery 워커의 실행 상태 확인
   - ```bash
     (venv_crawler_with_celery_sample)$ supercisorctl -c /usr/local/etc/supervisord.ini status
     ```
   - Supervisor의 모든 프로세스를 종료할 땐 다음 명령어 실행
   - ```bash
     (venv_crawler_with_celery_sample)$ supervisorctl -c /usr/local/etc/supervisord.ini stop all
     ```
   - Supervisor 데몬 자체를 종료할 때는 다음과 같은 명령어 사용
   - ```bash
     $ supervisorctl -c /usr/local/etc/supervisord.ini shutdown
     ```
   - supervisorctl과 관련된 명령어는 다음 공식 문서 참고
     - Running supervisorctl[[URL](http://supervisord.org/running.html#running-supervisorctl)]
   - 추가로 설정 항목과 관련된 자세한 내용은 다음 공식 문서 참고
     - Configuration File[[URL](http://supervisord.org/configuration.html)]