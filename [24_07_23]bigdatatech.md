# 부록 - 유용한 라이브러리
## 1. 프로세스 관리 도구 Supervisor
### 1. Supervisor
- supervisor는 파이썬으로 만들어진 프로세스 관리 도구. 프로세스 데몬 실행, 정지, 재실행 등을 간단하게 할 수 있게 해줌
- Supervisor 자체도 데몬으로 실행, 여러 프로세스 관리 제공.
- Supervisor는 책의 번역시점(2019.04)에 파이썬 3.x 를 지원하지 않으므로 pip install 이 아닌 brew install 명령어로 설치
- ```cmd
  $ brew install supervisor
  ```
- brew install 명령어로 설치된 Supervisor는 기본값으로 '/user/local/etc/supervisor.d/*.ini'설정을 관리 대상으로 읽어들이게 되어 있음. 설정은 ini 파일 형식으로 작성
- 다음 명령어로 디렉터리생성
- ```cmd
  $ mkdir -p /usr/local/etc/supervisor.d
  ```
- Supervisor를 실행할 때는 다음 명령어 사용
- ```cmd
  $ supervisord -c /usr/local/etc/supervisord.ini
  ```
  