## Servlet JSP vs JSON 연동하기(3) - 실습

- 6/26 데이터를 이어서


### data.js
- WebContent 
  - js
    - data.js 생성

```java
$(document).ready(function(){
    const json = './json/data.json';

    $.getJSON(json,function(data){
        
        // 할 일 처리
        let member_data="";
        $.each(data,function(key,value){
            member_data +="<tr>";
            member_data +="<td>"+value.id+"</td>";
            member_data +="<td>"+value.name+"</td>>";
            member_data +="<td>"+value.tel+"</td>>";
            member_data +="<td>"+value.homepage+"</td>>";
            member_data +="</td>";

        });
        $('#member_table').append(member_data);
        //<table id="member_table>로 이름지어진 table에 위이 데이터 삽입
        /*
        
        $.each(data,function(key,value){
        
            console.log(value.id);
            console.log(value.name);
            console.log(value.tel);
            console.log(value.homepage); //출력 확인

            //tbody에 추가
            $('table').attr('border','10');
            $('tbody').append(
                "<tr>"+
                    "<td>"+value.id+"</td>"+
                    "<td>"+value.name+"</td>"+"<td>"+value.tel+"</td>"+"<td>"+value.homepage+"</td>"+
                "</tr>"
            );
        });
        */
    });
});
```

- chrome browser로 설정 변경, 실행
- 지원되지 않는 명령줄 플래그 (--disable--web--security) 확인 후 설정한 주소 "localhost:~~/dataList.jsp 실행 확인

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
        <link ref="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h4 style="text-align:center;padding-top:50px">JSON 데이터 리스트</h4>
            <table class="table table-striped"id="member_table">
                <thead></thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Tel</th>
                        <th>Homepage</th>
                    </tr>
                <tbody></tbody>
            </table>
        </div>
    </body>
</html>
```