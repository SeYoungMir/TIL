# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 4. 통지 기능 추가
#### 4. 슬랙(Slack)에 통지 보내기
4. 스크립트 작성
   - slack_example.py를 다음처럼 작성.
   - ```python
     import requests

     WEBHOOK_URL ='https://hooks.slack.com/services/.............~~~'

     def notify_to_slack(text):
        data = {"text":text}
        r = requests.post(WEBHOOK_URL,json=data)
        r.raise_for_status()

     if __name__=='__main__':
        notify_to_slack("@me Slack으로 텍스트 전송")
     ```
   - 슬랙의 Incoming Webhooks 전용 URL과 requests 라이브러리를 조합, 슬랙에 메시지를 보내는 코드
   - WEBHOOK_URL 부분은 슬랙의 Incoming Webhook 전용 URL을 지정.
   - def 부분은 슬랙에 메시지를 보내는 notify_to_slack을 정의. 매개 변수로 문자열을 지정하면 해당 문자열을 보내는 형태
   - data 부분은 메시지데이터 data를 딕셔너리 자료형으로 생성, 슬랙에 보낼 메시지를 text키에 지정.
   - r 부분은 requests.post 메서드로 위에서 지정한 Incoming Webhooks 전용 URL에 위에서 만든 메시지 데이터를 POST로 전송. Incoming Webhooks에 POST로 데이터를 보낼 때는 JSON 문자열을 지정해야하므로 키워드 매개 변수 json 지정.
   - r.raise_for_status 부분은 Incoming Webhooks URL에 POST로 전송한 요청의 응답에 문제가 있을 때 예외를 발생시키게 함.
5. 슬랙에 메시지 보내기
   - 다음 명령어로 슬랙에 메시지 전달
   - ```cmd
     $ python -m slack_example
     ```
   - 슬랙을 열어서 메시지 확인.