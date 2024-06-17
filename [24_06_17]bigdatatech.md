# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 4. 통지 기능 추가
#### 2. 메일로 통지 보내기
4. 설정 내용 반영하기
   - 다음 명령어로 postfix에 반영
   - ```cmd
     $ sudo postmap /etc/postfix/sasl_password
     ```
5. 통합 설정하기
   - 다음 명령어를 실행해서 편집기를 열고 postfix 통합 설정을 진행.
   - ```cmd
     $ sudo vim /et/postfix/main.cf
     ```
   - main.cf 뒷부분에 다음 코드 작성. [G]키를 누르면 가장 끝부분으로 이동 가능. [i]키로 편집 모드 진입 가능, 편집이 종료되면 [ESC] 키로 편집 모드를 빠져나온 다음 :wq를 입력해 저장하고 종료
   - ```cf
     readme_directory = /usr/share/doc/postfix
     inet_protocols = all
     message_size_limit = 10485760
     mailbox_size_limit = 0
     biff = no
     mynetbooks = 127.0.0.0/8, [::1]/128
     smtpd_client_restrictions = permit_my_nettbooks permit_sasl_authenticated permit
     recipient_delimiter = +
     tls_random_source = dev:/dev/urandom
     smtpd_tls_ciphers = medium
     inet_interfaces = loopback-only

     # Gmail SMTP relay
     relayhost = [smtp.gmail.com]:587

     # Enable SASL authentication in the Postfix SMTP client.
     smtpd_sasl_auth_enable = yes
     smtp_sasl_auth_enable = yes
     smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
     smtp_sasl_security_options =
     smtp_sasl_mechanism_filter = AUTH LOGIN

     # Enable Transport Layer Security (TLS), i.e. SSL.
     smtp_use_tls = yes
     smtp_tls_security_level = encrypt
     ```
    - main_cf를 수정하고 다음 명령어를 사용해서 문법 확인
    - ```cmd
      $ sudo postfix check
      ```
    - 'postfix fatal:'로 시작하는 문자열이 출력되었다면 오류가 있다는 의미, 이러한 경우 잘못 작성한 부분이 없는지 확인. 오류가 없다면 다음 명령어로 main.cv 내용을 postfix에 반영
    - ```cmd
      $ sudo postfix reload
      ```