# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 4. 통지 기능 추가
#### 2. 메일로 통지 보내기
6. postfix로 테스트 메일 보내기
   - postfix를 실행
   - ```cmd
     $ sudo postfix start 
     ```
   - 테스트 메일 발송
   - ```cmd
     $ mail 지메일 주소
     Subject : 테스트
     메일 확인
     ```
   - 입력 종료 후 [Ctrl]+[D]키로 전송. 이후 지메일에서 메일 왔는지 확인. 정상적으로 메일이 도착했다면 postfix 설정 완료
#### 3. 파이썬에서 메일 발송
1. 스크립트 생성
   - sendmail_example.py라는 파일 생성, 다음 코드 입력
   - ```python
     import smtplib
     from email.message import EmailMessage

     FROM = '자기 메일 주소 입력.'

     def mail(to,subject, body=None):
        msg = EmailMessage()
        msg['To'] = to
        msg['Subject'] = subject
        msg['From'] = FROM
        if body is None:
            raise ValueError("메일 내용 입력")
        else:
            msg.set_content(body)

            with smtplib.SMTP('localhost') as s:
                s.send_message(msg)
     if __name__ = '__main__':
        mail('지메일 주소 입려',"메일 제목", "메일 내용")
     ```
   - 위 코드는 파이썬을 사용해 메일을 전송하는 샘플 코드
   - FROM 부분에서는 발신자의 메일 주소를 지정
   - def mail 부분에서는 메일 전송 전용 함수 정의, 매개 변수로 to, subject, body 입력. 이는 수신자 주소, 제목, 내용의미
   - msg 부분은 EmailMessage 메서드를 이용, msg 객체 생성
   - msg['To'] 부분부터 msg['From']부분에서는 수신 주소, 제목, 발송 주소를 각각 msg['To'],msg['Subject'],msg['From']에 저장
   - if body 부분에서는 본문을 나타내는 매개 변수 body가 지정되어 있지 않으면 ValueError 예외 발생, 처리 중단
   - else 부분에서는 본문을 나타내는 매개 변수 body가 지정되어 있으므로 msg.set_content 메서드로 본문 메시지 구축 전용 객체를 msg에 할당.
   - with smtplib 부분에서는 smtplib.SMTP 메서드로 로컬 호스트의 메일 전송 에이전트 postfix에 접속, 메시지 전송용 객체 s 생성. 이때 이어지는 처리에서 예외가 발생해서 이상 종료되어도 로컬 호스트 메일 송신 에이전트에 대한 접속을 닫을 수 있게 with 구문 사용
   - s.send_message 부분에서는 해당 메서드로 메시지 구축 전용 객체 msg를 전달, 메일 전송 처리 진행
2. 스크립트 실행
   - 다음 명령어를 실행, 메일 확인
   - ```cmd
     $ python -m sendmail_example
     ```