# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 4. 플라스크 플러그인:Flask-RESTful 사용
- 플라스크는 플러그인을 이용해 기능 확장 가능
- 플러그인을 추가해서 여러 가지 기능을 추가하고 활용할 수 있음. 다음 사이트에 플라스크에 다양한 플러그인들을 확인 가능
  - Awesome Flask[[URL](https://github.com/humiaozuzu/awesome-flask)]
- 이 중에서 Flask-RESTful 사용,Flask-RESTful은 RESTful 설계 사상을 기반으로 웹 API를 쉽게 만들 수 있게 해 주는 플러그인
1. Flask-RESTful 설치
   - pip install 명령어를 사용, Flask-RESTful을 설치
   - ```cmd
     $ pip install flask-restful
     ```
2. 플라스크 애플리케이션 생성
   - 다음 기입할 코드로 플라스크 애플리케이션 생성. 파일 이름은 flask_film_api.py