# 8. 크롤러 유지보수와 운용
## 2. 다중 실행 방지하기
### 1. 동일 처리 다중 실행 대책
- 주기적으로 사람이 직접 실행하는 프로그램은 상관 없지만, cron 등을 사용해서 정기적으로 프로그램을 자동으로 실행할 때는 '동일 처리 다주 실행'에 주의해야 함.
- 예를 들어 1시간에 한 번 실행되는 크롤링 처리를 cron으로 설정하였을 때, 처음 프로그램을 만들고 운용 시작 시에는 1시간 내로 종료되던 처리가 시간이 지나면서 상대 사이트의 페이지 수가 증가하는 등의 이유로 1시간 안에 끝나지 않는 문제 발생할 수 있음. 이 경우 같은 프로그램이 중복해서 실행될 수 있음.
- 같은 프로그램이 중복해서 실행되면 크롤러의 설계에 따라서 CPU와 메모리를  많이 소비하는 경우 존재. CPU와 메모리를 많이 사용하는 설계로는 과부하가 걸려 시스템 전체에 문제가 생길수도 있음. 
- 따라서 다음처럼 다중 처리 방지하는 것이 좋음.
- ```shell
  #!/bin/bash
  function main_commmand(){
    echo '명령어 실행 중.';
    sleep 30;
  }

  # 프로세스 ID를 출력할 파일 이름
  PIDFILE=/tmp/lock_example.pid

  # 프로세스 ID를 출력할 파일이 존재 시
  if [ -f $PIDFILE ]; then
    # 프로세스 ID를 변수 PID에 저장
    PID=$(cat $PIDFILE);
  
  # ps 명령어를 사용해서 변수 PID의 프로세스 ID를 가진 프로세스가 존재하는지 확인.
  ps -p $PID > /dev/null 2>&1;

  # 위 명령어의 실행 결과가 0이라면 프로세스 존재.
  if [ $? -eq 0 ]; then
    echo "이미 실행중. PID: $PID";
    exit 1;
  # 그렇지 않은 경우 프로세스 ID를 출력한 파일은 존재, 프로세스가 존재하지 않음
    else
        echo "$PIDFILE 는 존재, 프로세스 실행중이지 않음.";
        echo "상태를 확인해서 문자가 있다면 $PIDFILE 제거, 다시 실행.";
        exit 1;
    fi
  fi

  # 프로세스 ID를 파일 이름 PIDFILE에 출력
  echo $$ > $PIDFILE;
  echo "명령어 실행. 프로세스 ID: $(cat $PIDFILE)";

  # 다음 main_command를 실제로 실행하고 싶은 명령어로 변경
  main_command;
  # 명령어 실행 종료 시 프로세스 ID 출력 파일도 함께 제거
  rm $PIDFILE;
  ```
  - 위에서는 다중 실행을 제어할 명령어를 함수로 정의. 예제에서는 echo 명령어와 sleep 명령어 작성. 파이썬으로 만든 크롤러 프로그램을 주기적으로 실행하고 싶을때는 다음과 같이 작성.
  - ```shell
    function main_command() {
        python /User/foldername/python/crawler.py
        sleep 5;
    }
    ```
  - 위 코드에서는 셸 스크립트 실행 시  프로세스 ID를 적어둘 파일의 이름(경로)를 변수 PIDFILE에 저장.