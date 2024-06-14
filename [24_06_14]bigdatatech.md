# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
8. 스크립트 수정
   - 장고 어드민으로 publisher 테이블을 다룰 수 있게 book_db/book/admin.py를 다음처럼 수정
   - ```python
     from django.contrib import admin
     
     from book.models import Publisher

     admin.site.register(Publisher)
     ```
   - admin.site.register 메서드로 publisher 테이블의 전용 데이터베이스 테이블 모델인 Publisher를 등록하면 장고 어드민에서 publihser 테이블을 관리할 수 있음
   - python manage.py runserver로 개발 전용 서버를 실행, 브라우저에서 http://127.0.0.1:8000/admin/으로 접근
