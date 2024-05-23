# 8. 크롤러 유지보수와 운용
## 1. 정기적인 실행과 주기적인 실행
### 4. 주기적으로 실행
- cron은 특정 시점에 명령어를 실행할 수 있게 해 줌. 하지만 어떠한 상황 이후 30분마다 프로그램을 실행하는 것처럼 주기적으로 반복해야 할 때는 cron이 적합하지 않을 경우가 많음. 이러할 때는 UNIX 계열에서 사용할 수 있는 watch 유틸리티가 굉장히 편리함
1. watch 실행
   - brew install 명령어로 watch를 설치
   - ```cmd
     $ brew install watch
     ```
2. echo_date.sh 만들기
   - 다음 코드의 내용을 입력, echo_date.sh생성.
   - tee 명령어는 표준 출력과 ~/echo_date.log 파일 모두에 내용을 출력할 때 사용하는 명령어
   - ```shell
     echo_date() { 
        echo "command run at -> $(date + \"%Y-%m-%d\ %H:%M:%S\")";
        sleep 5;
     }
     echo_date | tee -a ~/echo_date.log
     ```
3. 실행 주기를 지정해서 로그의 내용 확인
   - 다음 명령어 실행, 30초정도 대기. -n 옵션에 이어서 숫자를 지정하면 실행 주기를 초 단위로 지정한 것이 됨. 다음 명령어는 2초마다 명령어 실행 코드
   - ```cmd
     $ watch -n2 bash echo_date.sh
     ```
   - 이어서 [Ctrl] +[C] 로 종료, ~/echo_date.log의 내용 확인
   - ```cmd
     $ cat ~/echo_date.log
     ```
   - 2초마다 echo_date 함수 실행, echo_date 함수의 실행은 내부에서 sleep으로 5초동안 정지하게 설정한 결과, 7초마다 로그 출력.