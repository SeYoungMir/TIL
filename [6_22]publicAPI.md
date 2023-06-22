## JSON 데이터 웹페이지 테이블로 출력하기 with getJSON(1)

### 사용하는 도구
- 부트스트랩(Bootstrap)
- 제이쿼리(JQuery)

### Chrome 설정
- Chrome 
  - 속성
    - 대상 뒷부분에 --disable-web-security --user-data-dir="c:\chrome"
  - 파일 로컬 경로를 주소에 넣어 실행
### JSON 파일 - 데이터
```js
{
    {
        "id":1,
        "name":"홍길동".
        "age":20,
        "address":"서울시 서초구 양재동 OO물산 307-12 양재로 111",
        "gender":"Male",
        "job":"Programmer",
        "hobby":"영화보기"
    }
    {
        "id":2,
        "name":"이순신".
        "age":30,
        "address":"서울시 서초구 양재동 OO물산 307-12 양재로 111",
        "gender":"Male",
        "job":"Programmer",
        "hobby":"영화보기"
    }
    {
        "id":3,
        "name":"강감찬".
        "age":27,
        "address":"서울시 서초구 양재동 OO물산 307-12 양재로 111",
        "gender":"Male",
        "job":"Programmer",
        "hobby":"음악감상"
    {
        "id":4,
        "name":"을지문덕".
        "age":20,
        "address":"서울시 서초구 양재동 OO물산 307-12 양재로 111",
        "gender":"Male",
        "job":"Programmer",
        "hobby":"영화보기"
    }
    {
        "id":5,
        "name":"김유신".
        "age":20,
        "address":"서울시 서초구 양재동 OO물산 307-12 양재로 111",
        "gender":"Male",
        "job":"WebDesigner",
        "hobby":"영화보기"
    }
    
}
}
```
### HTML 파일
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Exam 001</title>
        <script src="http://code.jquery.com/jquery-latest.min,js"></script>
        <!--script src= "https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></!script 버전 유지시-->
        <link rel="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/csss/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class = "container">
            <div class = "table-responsive">
                <h4>JSON data to WebPage table with getJSON method</h4>
                <br>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Address</th>
                            <th>Gender</th>
                            <th>Job</th>
                            <th>Hobby</th>
                        </tr> 
                    </thead>
                    <tbody>
                    </tbody>
                </table>

            </div>
        </div>
        <script src="./exam_001.js"></script>
    </body>
</html>
```
### JSON 파일 - 코드
```js
```