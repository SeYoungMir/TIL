# 8. 크롤러 유지보수와 운용
## 1. 정기적인 실행과 주기적인 실행
### 3. 특정 디렉터리를 기준으로 실행할 때
- PATH에는 /usr/bin:/bin만 설정. 특정 디렉터리를 기준으로 실행해야 할 때는 디렉터리를 이동한 다음에 프로그램을 실행해야하므로 주의.
- 예를 들어 직접 만든 프로그램이 /home/username/crawer/src/commands/crawl.py에 있고, 이 프로그램 내부에서 /home/username/crawler/src/commands/settings.py를 상대 경로로 읽는다면 다음과 같이 설정.(6시간마다 크롤러를 실행할 때)
- ```crontab
  0 *.6 * * * cd /home/username/crawler/src/commands && python -m crawl
  ```
1. 로컬 메일로 내용 전송하기
   - 명령어의 실행 결과를 표준 문자열로 출력하면 cron은 이를 로컬 메일로 전송하게 되어 있음
   - crontab -e로 다음과 같이 설정해보자
   - ```crontab
     * * * * * echo 'test' && date
     ```
   - 1분 정도 기다린 다음 터밀널에서 [Enter] 키를 누르면 다음과 같은 내용이 출력
   - ```cmd
     You have mail in /var/mail/username
     ```
2. 로컬 메일로 내용 확인
   - 로컬로 전송된 메일은 mail 명령어로 확인 가능
   - ```cmd
     $ mail
     ```
3. 특정 메일 확인
   - 메일 번호를 입력하면 해당하는 번호의 메일 내용을 확인 가능
   - 예를 들어서 [1] + [Enter] 키를 입력 시 메일 내용 확인 가능. mail 프로세스는 [q]키를 눌러서 종료.