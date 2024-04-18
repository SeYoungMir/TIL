# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 2. 플라스크를 사용한 웹 API 만들기 - 이어서
4. 샘플 수정하기
   - 동작을 확인할 수 있게 http://flask.pocoo.org/의 메인 페이지에 있는 샘플 동작을 확인
   - 'hello.py'라는 이름으로 다음 코드를 저장
   - ```python
     from flask import Flask
     app = Flask(__name__) # 플라스크 인스턴스 생성
     # / 에 접근할 때 호출
     @app.route("/")
     def hello(): # 아무 이름으로 함수 생성
        return "Hello World!"
     ``` 
5. 샘플을 실행해서 브라우저에서 결과 확인
   - 다음 명령어로 코드 실행
   - ```cmd
     $ FLASK_APP=hello.py flask.run
     ```
   - 플라스크 설치 시 flask run이라는 명령어를 사용할 수 있게 됨. 이 명령어는 환경 변수 FLASK_APP에 지정된프로그램 실행
   - 브라우저를 사용해서 http://127.0.0.1:5000/에 접근, 'Hello World!'라는 문자 출력 시 정상적으로 실행. 확인했다면 CTRL + C키를 사용, 실행 상태 벗어남