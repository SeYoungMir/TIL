
## Servlet JSP vs JSON 연동하기(4) - 공공데이터 포털사이트 JSON 연동2

### data.js
- 6/29 데이터에서 확장
```java
$(document).ready(function(){
    
    $.ajax({
        //ajax 옵션 설정
        url:"공공데이터 포털 요청 주소-상세설명-서비스 url-미리보기에서 제작후 링크 가져오기",

        type:"GET"
        dataType:"json",

        //요청이 성공시 할 일 처리
        success:function(){
            console.log(data.items.item)
            console.log(data.items.item,typeof data)
         
            data = JSON.stringify(data)
            console.log(typeof data)

            data = JSON.parse(data)
            console.log(typeof data)

            //할 일 처리
            let api_data="";
            $.each(data.items.item,function(key,value){

                api_data += "<tr>"
                api_data += "<td>"+ key +"</td>"
                api_data += "<td>"+ value.sido_sgg.nm +"</td>"
                
                api_data += "<td>"+ value.spot_nm +"</td>"
                api_data += "<td>"+ value.sl_dnv_cnt +"</td>"
                api_data += "<td>"+ value.se_dnv_cnt +"</td>"
                api_data += "<td>"+ value.dth_dnv_cnt +"</td>"
                api_data += "</tr>"

            });
            //페이지 단에 붙이기
            $('#member_table').append(api_data);
        }

    });
});

```


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
                        <th>No</th>
                        <th>관할 경찰서</th>
                        
                        <th>다발지역 위치</th>
                        <th>경상자수</th>
                        <th>중상자수</th>
                        <th>사망자수</th>
                    </tr>
                <tbody></tbody>
            </table>
        </div>
    </body>
</html>
```