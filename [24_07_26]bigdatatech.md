# 부록 - 유용한 라이브러리
## 1. 프로세스 관리 도구 Supervisor
### 1. Supervisor
2. Supervisor로 실행할 프로세스 설정 - 이어서
   - 각 항목은 다음과 같음.
     - directory:Supervisor로 프로세스 실행할 위치 지정
     - command:Supervisor로 실행할 프로그램의 완전한 경로 지정
     - autostart:Supervisor 서비스 프로세스(데몬)이 실행될 때 함께 자동으로 실행할 지 지정
     - startsecs: 이 값으로 지정한 초(Seconds)보다 프로세스가 빨리 종료되면 실행 실패로 간주.
     - numprocs : command에 지정한 프로세스를 몇 개 실행할지 지정. command 뒤에 지정한 실행 옵션 -c 2 를 통해 내부적으로 자식 프로세스가 2개 실행, 여기서는 1로지정
     - stopwaitsecs: 프로세스 종료 명령어를 실행 시 여기에 지정한 초가 경과해도 프로세스가 종료되지 않으면 강제 종료
     - killasgroup: true로 설정 시 프로세스 종료할 때 command에서 지정한 프로세스의 자식 프로세스들도 함께 종료
     - user: 프로세스를 실행할 사용자 지정
     - stdout_logfile: command로 지정하 프로세스가 표준 출력에 출력할 내용을 여기에서 지정한 파일에 출력.
     - stderr_logfile: command로 지정한 프로세스가 표준 오류에 출력할 내용을 여기서 지정한 파일에 출력
     - environment: %(ENV_PATH)s는 기존의 환경 변수 PATH의 참조 의미. Supervisor설정 파일에서는 $(ENV_<환경변수이름>)s의 형태로 환경 변수 참조 가능.