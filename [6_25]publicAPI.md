## Servlet/JSP vs JSON 연동하기(1)



### Eclipse 설정하기
  - New
    - Dynamic Web Project
      - WebContent 안에 Json- data.json 생성
### Data 형성
```java
[
    {
        "index":"1",
        "name":"name1",
        ...
        "homepage":"~~~.com"
    }
]
```
### html 파일 
- WebContent 밑에 생성

### JSP
- Create Servelet
  - Java Resoureces 밑에 생성
  - url mapping
    - /data.do
    - src - data.api.json
      - ApiServelet.java
### ApiServelet.java
- response.sendRedirect("dataList.jsp");
### dataList.jsp
  - `<script src="./js/data.js"></script>`
  - WebContent 밑에 js폴더 - data.js 파일 생성
