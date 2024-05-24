# 8. 크롤러 유지보수와 운용
## 1. 정기적인 실행과 주기적인 실행
### 5. 백그라운드에서 실행 지속
- 터미널을 종료하더라도 백그라운드에서 실행을 지속할 수 있음.
1. 스크립트 수정
   - echo_date.sh를 다음처럼 echo_date_2.sh으로 수정
   - ```shell
     function echo_date() { 
        echo "command run at -> $(date + \"%Y-%m-%d\ %H:%M:%S\")";
     }
     (
     while true
     do
        echo_date >> ~/echo_date.log;
        sleep 300;
     done
     ) &
     disown
     echo $! > ~/echo_date.pid
     ```
   - while true 문 내부에서 echo_date 함수를 실행한 다음 5분동안 슬립을 반복하게 함. 그리고 &로 백그라운드 잡으로 설정, disown으로 현재 잡 테이블에서 제외하게 함. 마지막으로 이후에 스크립트를 kill 명령어로 종료할 수 있도록 직전에 실행한 프로세스(while true ...)의 프로세스 id를 ~/echo_date.pid로 출력
2. 스크립트 실행
   - 다음 명령어로 스크립트 실행
   - ```cmd
     $ bash echo_date_2.sh
     ```
   - 곧바로 터미널로 복귀. 로그를 보면 sleep에 지정한 300초마다 echo_date 함수의 결과가 출력.
3. 프로세스 ID 확인
   - 다음과 같이 프로세스 ID를 확인 가능.
   - ```cmd
     $ cat ~/echo_date.pid
     ```
   - ps 명령어로도 프로세스 ID 확인 가능.
   - ```cmd
     $ ps auxw |grep echo_date_2.sh
     ```
   - bash echo_date_2.sh의 실행 프로세스 ID와 일치하는 걸 확인 가능.
4. 스크립트 종료
   - 스크립트를 종료할 때는 kill 명령어 사용. 다음 명령어는 SIGHUP 시그널을 보내 종료.
   - ```cmd
     $ kill -SIGHUP 'cat ~/echo_date.pid'
     ```
   - 스크립트 종료를 확인하기 위해 ps 명령어 사용
   - ```cmd
     $ ps auxw |grep echo_date_2.sh
     ```