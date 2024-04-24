# 7. 크롤러로 수집한 데이터 사용
## 2. 플라스크(Flask)로 웹 API 만들기
### 4. 플라스크 플러그인:Flask-RESTful 사용
2. 플라스크 애플리케이션 생성- 코드
    - ```python
      """film 테이블 전용 RESTful API"""
      from flask import Flask, abort
      from flask_restful import Api,Resource, reqparse

      # db.py를 기반으로 Film 모델 전용 클래스 읽어 들이기
      from db import Film
      app= Flask(__name__)

      # RESTful API 전용 인터페이스 생성
      api=Api(app)

      # 단일 아이템을 출력하는 클래스
      class FilmItem(Resource):
        """Film 아이템"""
        def get(self,film_id):
            """GET 실행 때의 액션"""
            try:
                #film 테이블에서 film_id를 검색해서 데이터베이스에서 추출
                film = Film.get(Film.film_id==film_id)
            except Film.DoesNotExist:
                # 없는 경우 404 응답
                abort(404,description="Film not found")
            
            #딕셔너리 자료형으로 반환하면 자동으로 JSON 변환
            return film.to_dict()
      # 여러 개의 아이템을 출력하는 클래스
      class FilmList(Resource):
        """Film 목록"""
        # 한 페이지 당 아이템 수
        ITEMS_PER_PAGE = 5
        
        def __init__(self,*args,**kwargs):
            """GET 요청 때의 요청 매개 변수 파싱"""
            self.parser=reqparse.RequestParser()
            # 이렇게 하면 ?page=2 등으로 추가적인 정보를 전달 받을 수 있음
            self.parser.add_argument('page',type=int,default=1)
            super().__init__(*args,**kwargs)
        def get(self):
            """GET 실행 때의 액션"""
            # GET 요청 때의 요청 매개 변수 추출
            args = self.parser.parse_args()

            #film 테이블에서 page 요청매개 변수에 따라 페이징해서 아이템 5개씩 추출
            films=Film.select().order_By(Film.film_id).paginate(args['page'],self.ITEMS_PER_PAGE) #페이징 처리

            # 딕셔너리 자료형으로 반환 시 자동으로 JSON 변환
            return [film.to_dict() for film in films]
      # 어떤 URL 형식으로 접근할 때 어떤 것을 실행할 지 지정
      api.add_resource(FilmItem,'/film/<int:film_id>')
      api.add_resource(FilmList,'/films')
      
      if __name__=='__main__':
        # 웹 서버 실행
        app.run(debug=True)
      ```