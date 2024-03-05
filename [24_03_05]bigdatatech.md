# 5. 크롤러 설계/개발(응용)
## 5. 병렬 처리
### 3. 작업 큐(여러 개의 머신을 사용, 병렬 처리) - 이어서
10. 워커를 데몬으로 만들기
    - 워커의 실행
      - 워커는 데몬으로 만들 수 있으며, 데몬으로 만들어야 서브 프로세스도 잘 처리할 수 있음. 다음과 같이 실행
      ```
      $ celery -A crawler_with_celery_sample multi start download -Q download -c 2 -l info --logfile=worker-download.log --pidfile=worker-download.pid
      $ celery -A crawler_with_celery_sample multi start media -Q media -c 2 -l info --logfile=worker-media.log --pidfile=worker-media.pid
      
      ```
    - 데몬이란, 리눅스에서 메모리 위에 항상 존재하면서 다양한 서비스를 제공하는 프로세스를 의미
    - 다시 크롤링을 실행하면 콘솔 화면에 별다른 로그가 출력되지 않음.
    - 조금 기다리면 실행 디렉터리에 워커의 로그 파일이 생성되는 모습 확인 가능
    ```
    $ ls worker-*.log
    ```
    - 애플리케이션 코드를 변경하면 워커를 다시 실행해야함. 다음 명령어를 사용
    ```
    $ celery -A crawler_with_celery_sample multi restart download -Q download -c 2 -l info --logfile=worker-download.log --pidfile=worker-download.pid
    $ celery -A crawler_with_celery_sample multi restart media -Q media -c 2 -l info --logfile=worker-media.log --pidfile=worker-media.pid
    ```
    - 워커를 종료할 때는 프로세스 ID를 지정, kill 명령어를 실행.
    ```
    $ kill 'cat worker-download.pid'
    # kill 'cat worker-media.pid'
    ```
    - 매번 워커를 이렇게 실행하고 종료하는 것은 귀찮기때문에 프로세스 제어 도구인 Supervisor 등을 사용해서 데몬으로 실행하는 것이 좋음.
11. Flower를 사용해 큐의 상태 확인
    - 로그를 tail -f 등으로 감시하면 태스크의 실행 상황을 알 수 있음. 하지만 큐의 상태까지는 알 수 없음.
    - Celery 애플리케이션은 웹 GUI 모니터링 도구인 Flower를 사용해서 큐의 상태를 볼 수 있게 해놓음. pip install 명령어를 사용 flower를 설치
    ```
    $ pip install flower
    ```
    - Flower를 설치했다면 Celery 애플리케이션의 서브 명령어로 Flower 사용 가능
    - 워커를 실행할 때처럼 Celery 애플리케이션을 지정해 실행, 기본값으로 5555번 포트에서 실행
    ```
    $ celery -A crawler_with_celery_sample flower &
    ```
    - 브라우저에서 http://localhost:5555 에 접근하면 대시보드 화면이 열리며 워커 목록이 나옴
    - 메뉴에서 [Tasks]를 클릭 시 태스크 목록 화면이 나오며, 태스크의 실행 상태가 출력
    - 태스크의 ID(UUID)에 링크가 설정되어 있다는 것을 확인 가능
    - 태스크 ID(UUID)를 클릭하면 태스크 상세 화면이 나옴
    - 태스크 상세 화면에서는 태스크가 오류를 일으켜서 정상적으로 종료하지 못했을 때 트레이스백도 출력, 디버깅할 때 유용하게 사용 가능.