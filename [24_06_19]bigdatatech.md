# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 4. 통지 기능 추가
#### 4. 슬랙(Slack)에 통지 보내기
- 채팅 서비스를 사용하는 것도 유용한 통지 수단. 여기서는 슬랙(Slack) 사용
  - 슬랙(Slack)[[URL](https://slack.com)]
- 외부에서 슬랙에 글을 올리기 위한 API로 Incoming WebHooks와 Web API가 있음. Web API는 파일 첨부 등도 가능, 여기서는 간단하게 사용할 수 있는 Incoming WebHooks를 사용
- 다음 사이트 참고하면서 진행
  - App features:Incoming WebHooks[[URL](https://api.slack.com/incoming-webhooks)]
1. 팀 만들기
  - 슬랙은 팀이라는 단위로 채팅 그룹 관리. 가입된 팀이 없다면 https://slack.com/get-started에서 'Create a new workspace'클릭 후 다음 팀 생성.
  - 팀 생성 후 [URL] https://my.slack.com/services/new/incoming-webhook/ 에 들어감. 로그인 요구 시 로그인. 여러 개의 팀에 소속되어 있다면 통지에 사용할 팀 선택
  - 슬랙 채널 새로 만들기
    - [URL] https://<생성 workspace 이름>.slack.com에 들어가서 로그인, 로그인 시 왼쪽 네비게이션 메뉴에서 Channels 오른쪽에 [+](플러스 아이콘)이 보임. 이를 클릭해서 새로운 채널 생성 가능.
    - 'Name에 채널 이름(ex:pythoncrawler)을 입력, [Create Channel] 버튼을 클릭 시 채널 생성.