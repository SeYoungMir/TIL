# 8. 크롤러 유지보수와 운용
## 3. 관리 화면 사용
### 3. 장고 어드민 사용하기
6. 데이터베이스 테이블 만들기
   - 다음 명령어로 장고 어드민의 관리 사이트에 로그인 할 때 사용할 사용자 정보와 접근 권한 등을 저장할 데이터베이스 테이블을 생성.
   - ```cmd
     <venv_django>$ python manage.py migrate
     ```
   - 데이터베이스를 생성할 때의 모델
     - 데이터베이스를 만들 때 models.py에 정의한 class 내부의 class Meta에 managed= True로 지정된 모델이 있으면 자동으로 정의와 대응되는 테이블이 데이터베이스 내부에 생성되므로 주의.
7. 관리 사이트의 슈퍼 사용자 생성.
   - 다음과 같이 관리 사이트의 슈퍼 사용자를 생성.
     - 슈퍼 사용자란?
       - 장고 어드민 관리 사이트의 최상위 권한을 가진 사용자를 슈퍼 사용자라고 부름. 장고 어드민을 사용하려면 최소한 한 명의 사용자 정보가 필요, 이 때 최초 사용자가 슈퍼 사용자가 됨. 추가로 장고 어드민을 여러 명이 사용한다면 슈퍼 사용자로 로그인한 다음에 새로운 사용자를 생성.
     - ```cmd
       (venv_django)$ python manage.py create superuser

       Username (leave blank to use '슈퍼사용자명'): 
       Email address:
       Password:
       Password (again) :
       Superuser created successfully
       ```
    - 슈퍼 사용자는 원하는 이름과 비밀번호로 생성.