# Django 웹 프레임워크
## 일반적인 특징
### 일반적인 특징
- 일반적인 MVC 패턴
- 개발 시 일반적으로 언급되는 MVC(Model-View-Controller) 패턴이란
데이터 Model, 사용자 인터페이스View, 데이터를 처리하는 로직
Controller을 구분해서 한 요소가 다른 요소들에 영향을 주지 않도록 설
계하는 방식
- MVC 패턴 기반 MVT
  - 장고는 MVC Model-View-Controller를 기반으로 한 프레임워크
  - 장고에서는 View를 Template, Controller를 View라고 함
- 객체 관계 매핑
  - 장고의 객체 관계 매핑 ORM, Object-Relational Mapping은 데이터베이스 시스템과 데이터 모델 클래스를 연결시키는 다리와 같은 역할
- 자동으로 구성되는 관리자 화면
  - 장고는 웹 서버의 콘텐츠, 즉 데이터베이스에 대한 관리 기능을 위하여 프로젝트를 시작하는 시점 에 기본 기능으로 관리자 화면을 제공
- 유연한 URL 설계
  - 웹 프로그래밍에서 URL 디자인은 필수인데, 장고에서는 유연하면서도 강력한 기능을 제공. 장고에서는 우아한 Elegant URL 방식을 채택하여 URL을 직관적이고 쉽게 표현
- 자체 탬플릿 시스템
  -  장고는 내부적으로 확장이 가능하고 디자인이 쉬운 강력한 템플릿 시스템을 갖고 있음. 이를 통해 화면 디자인과 로직에 대한 코딩을 분리하여 독립적으로 개발 진행
- 캐시 시스템
  - 동적인 페이지를 만들기 위해서 데이터베이스 쿼리를 수행하고 템플릿을 해석하며, 관련 로직을 실행해서 페이지를 생성하는 일은 서버에 엄청난 부하를 주는 작업
- 다국어 지원
  - 다국어 장고는 동일한 소스코드를 다른 나라에서도 사용할 수 있도록 텍스트의 번역, 날짜/시간/숫자의 포맷, 타임존의 지정 등과 같은 다국어 환경을 제공
- 소스 변경사항 자동 반영
  - 장고에서는 *.py 파일의 변경 여부를 감시하고 있다가 변경이 되면 실행 파일에 변경내역을 바로 반영

## 장고 프로그램 설치
### 윈도우에서 장고 설치
- 파이썬 3.x 버전을 설치하면 pip 프로그램도 같이 설치.
- pip(Python Install Package) 프로그램은 파이썬의 오픈소스 저장소인 PyPI(Python Package Index)에 있는 SW 패키지를 설치하고 관리해주는 명령
- (base) C:\MyTest>pip install Django

### 장고 프로그램 설치 확인
- 장고는 파이썬 환경에서 동작하는 패키지이므로, 장고가 정상적으로 설치
되었는지 확인하기 위해서 아래와 같이 명령을 입력
- (base) C:\MyTest>python -m django --version
  
## 장고에서의 애플리케이션 개발 방식
### 장고에서의 애플리케이션 개발 방식

- 웹 사이트의 전체 프로그램 또는 모듈화된 단위 프로그램을 애플리케이션 즉, 프로그램으로 코딩할 대상을 애플리케이션이라고 부름
- 사이트에 대한 전체 프로그램을 프로젝트(Project)라고 함
- 모듈화된 단위 프로그램을 애플리케이션(Application)이라 부름
### MVC 패턴 기반 MVT
- 일반적인 MVC 패턴
- 개발 시 일반적으로 언급되는 MVC(Model-View-Controller) 패턴이란
데이터 Model, 사용자 인터페이스View, 데이터를 처리하는 로직Controller을 구분해서 한 요소가 다른 요소들에 영향을 주지 않도록 설계하는 방식

- 장고의 MVT 패턴
- View를 Template, Controller는 View라고 표현
- MVC 대신에 MVT(Model-View-Template)패턴이라고 함
-  모델(Model)은 데이터베이스에 저장되는 데이터를 의미
- 템플릿(Template)은 사용자에게 보여지는 UI부분
- 뷰(View)는 실질적으로 프로그램 로직이 동작하여 데이터를 가져오고 적절하게 처리한 결과를 템플릿에 전달하는 역할을 수행
- 웹 클라이언트 -Request (URL conf)>View -(Model C.R.U.D)>Model <-(ORM)-> DB
- 웹 클라이언트 <-response- View -TemplateRendering>Template

- 클라이언트로부터 요청을 받으면 URL.conf를 이용하여 URL을 분석
- URL 분석 결과를 통해 해 당 URL에 대한 처리를 담당할 뷰를 결정
- 뷰는 자신의 로직을 실행하면서. 만일 데이터베이스 처리가 필요하면 모델을 통해 처리
하고 그 결과를 반환
- 뷰는 자신의 로직 처리가 끝나면 템플릿을 사용하여 클라이언트에 전송할 HTML 파일
을 생성
- 뷰는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답

### Model – 데이터베이스 정의(models.py)
- 모델이란 사용될 데이터에 대한 정의를 담고 있는 장고의 클래스
- 장고는 ORM 기법을 사용하여 애플리케이션에서 사용할 데이터베이스를
`클래스로 매핑해서 코딩`할 수 있음
- 장고는 테이블 및 컬럼을 자동으로 생성하기 위해 필요한 많은 규칙

### URL.conf – URL 정의 (urls.py)

- 파이썬의 URL 정의 방식은 전통적인 자바나 PHP 계열의 URL보다 직관
적이고 이해하기가 쉬움. 
- 이런 방식을 우아한(Elegant URL)이라고 부르는 것.
- URL을 정의하기 위해서는 urls.py 파일에 URL과 처리 함수(뷰 View라고
부름)를 매핑하는 파이썬 코드를 작성하면 됨

### 웹 클라이언트가 웹 서버에 페이지 요청 시
- 웹 클라이언트가 웹 서버에 페이지 요청 시
- 장고에서 URL을 분석하는 순서
  - Setting.py파일의 ROOT_URLCONF 항목을 읽어 최상위 URLconf(urls.py )의 위치 파악
  - URLconf를 로딩하여 urlpatterns 변수에 지정되어 있는 URL리스트를 검사
  - 위에서부터 순서대로 URL 리스트의 내용을 검사하면서 URL 패턴이 매치되면 검사를 종료
  - 매치된 URL의 뷰를 호출 - 여기서 뷰는 함수 또는 클래스의 메소드
  - 호출 시 HttpRequest 객체와 매칭할 때 추출된 단어들을 뷰에 인자로 넘겨줌
  - URL 리스트 끝까지 검사했는데도 매칭에 실패하면 에러를 처리하는 뷰를 호출

### URL 패턴을 정의
- URL 패턴의 일부 문자열을 추출하기 위한 것이며` <type:name>`형식으로 사용
- 장고에서는 Path Converter
  - str : /(슬래시)를 제외한 모든 문자열과 매치. 타입이 지정되지 않았다면 디폴트로 str 타입을 사용
  - Int : 0 또는 양의 정수와 매치 매치된 정수는 파이썬의 int 타입으로 변환
  - slug : slug 형식의 문자열(ASCII, 숫자, 하이픈, 밑줄로만 구성됨)과 매치
  - uuid : UUID 형식의 문자열과 매치. 매치된 문자열은 파이썬의 UUID 타입으로 변환
  - path :/(슬래시 )를 포함한 모든 문자열과 매치 이는 URL 패턴의 일부가 아니라 전체를 추출하고자할 때 많이 사용
- 정규표현식에 사용되는 문자들

<table>
  <tr>
    <th>표현</th><th>의미</th>
  </tr>
  <tr>
    <td>.(Dot)</td><td>모든 문자 하나(any single character)</td>
  </tr>
  <tr>
    <td>^(Caret)</td><td>문자열의 시작</td>
  </tr>
  <tr>
    <td>$</td><td>문자열의 끝</td>
  </tr>
  <tr>
    <td>[]</td><td>[]괄호에 있는 문자 하나, 예를 들어 [akz]라면 a또는 k 또는 z</td>
  </tr>
  <tr>
    <td>[^]</td><td>[]괄호에 있는 문자 이외의 문자 하나, 만일 [^ab]라면 a와 b를 제외한 문자 하나</td>
  </tr>
  <tr>
    <td>*</td><td>0번 이상 반복, {0,}과 동일</td>
  </tr>
  <tr>
    <td>+</td><td>1번 이상 반복, {1,}과 동일</td>
  </tr>
  <tr>
    <td>?</td><td>0번 또는 1번 반복, {0,1}과 동일</td>
  </tr>
  <tr>
    <td>{n}</td><td>n번 반복</td>
  </tr>
  <tr>
    <td>{m,n}</td><td>최소 m번에서 최대 n번까지 반복</td>
  </tr>
  <tr>
    <td>|</td><td>예를 들어 A|B라면, A 또는 B</td>
  </tr>
  <tr>
    <td>[a-z]</td><td>a에서 z까지의 임의의 문자, 즉 영문 소문자 한 개</td>
  </tr>
 <tr>
    <td>\w</td><td>영문,숫자 또는 밑줄(_)한 개, [0-9a-zA-z_]와 동일</td>
 <tr>
    <td>\d</td><td>숫자 한 개, [0-9]와 동일</td>
  </tr>
</table>

### View – 로직 정의 (view.py)

- 뷰는 웹 요청을 받아서 데이터베이스 접속 등 해당 애플리케이션의 로직
에 맞는 처리를 하고, 그 결과 데이터를 HTML로 변환하기 위하여 템플릿
처리를 한 후에, 최종 HTML로 된 응답 데이터를 웹 클라이언트로 반환하
는 역할

### Template – 화면 UI 정의 (*.html)
- 개발자가 응답에 사용할 *.html 파일을 작성하면, 장고는 이를 해석해서 최종
HTML 텍스트 응답을 생성하고, 이를 클라이언트에게 보내줌
- 클라이언트(보통 웹 브라우저)는 응답으로 받은 HTML 텍스트를 해석해 서
우리가 보는 웹 브라우저 화면에 UI를 보여주는 것
- 템플릿 파일은 *.html 확장자를 가지며, 장고의 템플릿 시스템 문법에 맞게
작성
- 장고에서 템플릿 파일을 찾을 때는 TEMPLATES 및 INSTALLED_APPS에서 지
정된 앱의 디렉토리를 검색.
- 이 항목들은 프로젝트 설정 파일인 settings.py 파일에 정의되어 있음
### MVT 코딩 순서
- 모델, 뷰, 템플릿 셋 중에서 무엇을 먼저 코딩해야 하는지에 대해 정해진
순서는 없음.
- MVT 방식에 따르면 화면 설계는 뷰와 템플릿 코딩으로 연결되고, 테이
블 설계는 모델 코딩에 반영. 
- 그렇기 때문에 독립적으로 개발할 수 있는 모델을 먼저 코딩하고, 뷰와 템
플릿은 서로 영향을 미치므로 모델 이후에 같이 코딩하는 것이 일반적


- `프로젝트 뼈대 만들기` : 프로젝트 및 앱 개발에 필요한 디렉토리와 파일
생성
- `모델 코딩하기` : 테이블 관련 사항`(DB)`을 개발(models.py`(class)`, admin.py`(class)` 파일)
- `URLconf 코딩하기` : URL 및 뷰 매핑 관계를 정의(urls.py`(path)` 파일)
  - project의 urls.py
  - application의 urls.py
  - 두 개 모두 코딩해야함
- `템플릿 코딩하기` : 화면 UI 개발(templates/ 디렉토리 하위의 *.html 파일들)
- `뷰 코딩하기` : 애플리케이션 로직 개발(views.py`(def)` 파일)

## 애플리케이션 설계
### 애플리케이션 설계
- index.html : 최근에 실시하고 있는 질문의 리스트를 보여줌.
- detail.html : 하나의 질문에 대해 투표할 수 있도록 답변 항목을 폼으로
보여줌
- results.html : 질문에 따른 투표 결과를 보여줌

- Question 테이블 설계
<table>
  <tr>
    <th>컬럼명</th><th>타입</th><th>제약조건</th><th>설명</th>
  </tr>
  <tr>
    <td>id</td><td>integer</td><td>NotNull,PK,AutoIncrement</td><td>Primary Key</td>
  </tr>
  <tr>
    <td>question_text</td><td>varchar(200)</td><td>NotNull</td><td>질문 문장</td>
  </tr>
  <tr>
    <td>pub_date</td><td>datetime</td><td>NotNull</td><td>질문 생성 시각</td>
  </tr>
</table>

- Choice 테이블 설계
<table>
  <tr>
    <th>컬럼명</th><th>타입</th><th>제약조건</th><th>설명</th>
  </tr>
  <tr>
    <td>id</td><td>integer</td><td>NotNull,PK,AutoIncrement</td><td>Primary Key</td>
  </tr>
  <tr>
    <td>choice_text</td><td>varchar(200)</td><td>NotNull</td><td>답변 항목 문구</td>
  </tr>
  <tr>
    <td>votes</td><td>integer</td><td>NotNull</td><td>투표 카운트</td>
  </tr>
  <tr>
    <td>question</td><td>integer</td><td>NotNull,FK(Question_id),Index</td><td>ForeignKey</td>
  </tr>
</table>
