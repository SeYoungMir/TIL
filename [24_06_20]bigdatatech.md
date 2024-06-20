# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 4. 통지 기능 추가
#### 4. 슬랙(Slack)에 통지 보내기
1. 팀 만들기 - 이어서
   - 화면 아래에 있는 'Post to Channel'에서 통지에 사용할 채널(채팅방)을 선택.
   - 채널을 선택했다면 [Add Incoming WebHooks integration] 버튼을 클릭
   - 변경을 완료했다면 [Save Settings]버튼 클릭. 
   - 이동되는 화면에서 Webhook URL을 확인 가능. 이를 메모한 뒤 [Save Settings]버튼을 다시 한번 확인.
2. 테스트
   - 메모한 Webhook URL을 사용. 다음처럼 curl 명령어를 실행하면 글 업로드
   - ```cmd
     $ curl -X POST -H 'Content-type: application/json' --data '{"text":"Slack으로 텍스트 전송.\n모바일 애플리케이션을 설치해두면 편리하게 알림을 확인할 수 있음."}'\ (webhook URL 입력)
     ```
3. 특정 사용자 멘션
   - 특정 사용자를 멘션하고 싶을 때에는 '@사용자'형태를 넣어줌. 데이터에 "link_names":1 이라고도 지정.
   - ```cmd
     $ curl -X POST -H 'Content-type: application/json' --data '{"text":"@사용자 Slack으로 텍스트 전송.\n모바일 애플리케이션을 설치해두면 편리하게 알림을 확인할 수 있음."}'\ (webhook URL 입력)
     ```
     - 멘션(mention)이란 @ 기호를 붙여 댓글을 다는 것을 의미
   - '@사용자'를 '@here'로 변경 시 현재 슬랙을 사용하는 모든 채널 참가자에게 메시지 전송. '@channel'을 사용하면 슬랙을 켜고있지 않은 채널 참가자에게도 메시지 전송
3. requests 설치
   - 파이썬을 사용해서 메시지 전송. 일단 pip install 명령어로 requests 설치
   - ```cmd
     $ pip install requests
     ```