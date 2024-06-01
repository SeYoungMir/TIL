# 8. 크롤러 유지보수와 운용
## 2. 다중 실행 방지하기
### 1. 동일 처리 다중 실행 대책- 이어서
- 이렇게 값이 저장된 변수는 $PIDFILE처럼 달러 기호를 붙여 참조할 수 있음. 이 파일을 프로세스를 중간에 종료할 때 사용하는 pkill 명령어의 매개 변수에 지정할 프로세스 ID를 저장해두기 위한 용도로 사용
- 참고로 pkill 명령어로 프로세스를 강제로 종료할 때는 다음과 같은 명령어를 사용.
- ```cmd
  $ pkill -TERM -P 'cat /tmp/lcok_example.pid'
  ```
- 이 명령어는 /tmp/lock_example.pid에 작성된 프로세스 ID를 cat 명령어로 출력하고, 추출한 프로세스 iD를 pkill 명령어로 종료시킴.
- TERM은 SIGTERM 시그널을 종료에 사용한다는 의미. -P 는 부모 프로세스ID 지정을 나타냄.
- 일반적인 kill 명령어를 사용하지 않고, pkill 명령어를 사용해서 부모 프로세스의 ID를 지정한 이유는 단순하게 프로세스 ID만을 지정해서 종료시키면 종료된 프로세스의 내부에서 다른 프로세스(자식 프로세스를 나타냄. 참고로 이 때 자식 프로세스를 실행한 프로세스를 부모 프로세스라고 부름)를 실행한 경우, 자식 프로세스가 종료되지 않고 남기 때문.
- [-f <파일명>]으로 파일의 존재를 확인 가능.
- []은 괄호 내부의 조건을 평가(evaluation, 코드를 실행하고 결과 확인)한다는 의미. -f는 파일의 존재를 확인하는 조건 연산자.
- $(cat $PIDFILE)의 cat 명령어는 파일의 내용을 출력하는 명령어.
- $() 기법으로 cat $PIDFILE의 명령어의 실행 결과를 전개, 변수 PID에 저장.
- ps 명령어는 실행중인 프로세스를 확인하는 명령어. -p 옵션으로 프로세스ID를 지정해서 프로세스의 존재를 확인할 수 있음. 예제에서는 명령어 실행 후의 '종료 상태(다음의 if문)'만 필요하므로 실행 결과를 /dev/null로 리다이렉트해서 제거하게 함.
- /dev/null은 유닉스 계열 시스템에서 불필요한 출력을 제거하기 위해 사용하는 특수한 파일임. 현재 코드에서는 ps 명령어의 실행에서 오류가 발생하더라도 화면에 아무것도 출력할 필요가 없으므로 이곳에 출력.
- 만약 표준 출력과 표준 오류 제어와 관련된 자세한 내용을 알고싶다면 다음 문서 참고.
  - Bash Reference Manual 3 Redirections[[URL](https://www.gnu.org/software/bash/manual/bash.html#Redirections)]