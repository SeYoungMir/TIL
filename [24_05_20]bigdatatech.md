# 8. 크롤러 유지보수와 운용
## 1. 정기적인 실행과 주기적인 실행
### 2. cron 환경 변수
- cron 은 crontab 명령어로 환경 변수를 설정할 수 있음. 예를 들어 PATH에 실행 명령어의 경로를 지정할 수도 있음. 직접 만든 프로그램에서 PATH가 제대로 동작하지 않는다면 이를 따로 설정해 줘야 함.
- cron은 사용자별로 환경 변수를 구분 따라서 .bashrc, .bah_profile 등에 설정한 환경 변수를 받을 수 없으므로 필요한 경로를 설정해 줘야 함.
1. 경로 확인
   - 경로 확인. which env를 사용, env 명령어의 경로 확인
   - ```cmd
     $ which env
     > /usr/bin/env
     ```
2. cron을 설정하고 내용 확인.
   - 다음과 같이 cron 설정, 모든 확인이 끝난 이후에는 설정 제거.
   - ```crontab
     * * * * * /usr/bin/env > ~/cron_env.log
     ```
   - 1분정도의 대기 후 다음 명령어 실행.
   - ```cmd
     $ cat ~/cron_env.log
     ```
   - 실행하면 다음과 같은 내용 확인.
   - ```cmd
     SHELL=/bin/sh
     USER=**
     PATH=/usr/bin:/bin
     PWD=/Users/**
     SHLVL=1
     HOME=/Users/**
     LOGNAME=**
     _=/usr/bin/env
     ```
3. 셸 버전 확인
   - cron은 셸로 /bin/sh 사용. macOS에서는 /bin/sh도 bash. 다음 명령어로 확인
   - ```cmd
     $ sh --version
     ```