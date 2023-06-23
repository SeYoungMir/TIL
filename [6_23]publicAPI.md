### JSON 데이터 웹페이지 테이블로 출력하기 with getJSON(2)
- 6/22에 이어서
### JSON 파일 - 코드
```js
$(document).ready(function(){
    $.getJSON("exam_001.json",function(data){
        //할 일 처리
        let member_data = "";
        $.each(data,function(key,value){
            member_data += "<tr>";
            member_data += "<td>"+value.id+"</td>";
            member_data += "<td>"+value.name+"</td>";
            member_data += "<td>"+value.age+"</td>";
            member_data += "<td>"+value.address+"</td>";
            member_data += "<td>"+value.gender+"</td>";
            member_data += "<td>"+value.job+"</td>";
            member_data += "<td>"+value.hobby+"</td>";
            member_data += "</tr>";

        });
        $("#member_table").append(member_data)
    });
});
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
        <link rel="stylesheet"href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class = "container">
            <div class = "table-responsive">
                <h4 style = "text-align:center;padding-top:50px">JSON data to WebPage table with getJSON method</h4>
                <br>
                <table class ="table table-bordered" id="member-table">
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
