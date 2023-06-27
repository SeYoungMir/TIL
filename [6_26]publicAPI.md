## Servlet JSP vs JSON 연동하기(2) - 실습

- WebContent
  - json
    - data.json
### data.json
```java
[
    {
        "id":1
        "name":"홍길동",
        "tel":"010-1111-1111",
        "homepage":"http://www.1111.com"

    }
    {
        "id":2
        "name":"이순신",
        "tel":"010-1111-1111",
        "homepage":"http://www.1111.com"

    }
    {
        "id":3
        "name":"을지문덕",
        "tel":"010-1111-1111",
        "homepage":"http://www.1111.com"

    }
    {
        "id":4
        "name":"강감찬",
        "tel":"010-1111-1111",
        "homepage":"http://www.1111.com"

    }
    {
        "id":5
        "name":"김유신",
        "tel":"010-1111-1111",
        "homepage":"http://www.1111.com"

    }

]
```
### index.html
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Servelet/JSP+JSON 연동</title>
        

    </head>
    <body>

        <a href="data.do? command=list">JSON 데이터 리스트 보기</a>
    </body>
</html>
```

### src 만들기
- src
  - data.api.json
    - NEW 
      - create Servelet
        - Class name API Servlet
        - urlmapping data.do

- doGet 아래에
  - request.setCharacterEncoding("UTF-8");
  - response.setContentType("text/html; charset=UTF-8");
  - String command = request.getParameter("command");

    if(command.equals("list")){
        response.sendRedirect("dataList.jsp")
    }

### dataList.jsp
- New jsp 생성
```java
<%@page language="java" contentType="text/html;charset=UTF-8"pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>dataList</title>
        <script src="http://code.jquery.com/jquery-lastest.min.js"></script>
        <script src="./js/data.js"></script>>

    </head>
    <body>

        <h1>JSON 데이터 리스트</h1>
        <table>
            <thead></thead>
            <tbody></tbody>
        </table>
    </body>
</html>
```
### data.js
- WebContent 
  - js
    - data.js 생성