## JSON 데이터를 출력시키는 BS 테이블 클래스 연습하기(2)

- 6/30의 파일에서 이어서

### bootstrap_table_example.html
```html
<!DOCTYPE.html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Bootstrap Table Example</title>
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
        <link rel "stylesheet" href="http://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js"></script>
        <!--
            3.table-bordered
            4.table-striped
            5.table-dark,table-light  
            6.thead에만 다크 적용도 가능 : class=thead-dark. 물론 이 반대로 하는 것도 가능  
            6-1.원하는 것만 정렬을 바꿀때, 반복문 내에서 처리를 바꿔서 정렬을 변환시킬 수 있음
            7.colspan 사용도 가능
            8.table-hover: 마우스를 가져다 대면 색이 변함
            9.table-sm:small로써 컴팩트하고 피트하게 맞춰줌.폰트사이즈도 고려
            10.tr,td:class="table-info","table-danger","table-success","table-warning"
            11.tr,td:class="bg-info","bg-danger","bg-success"
            12.<caption>List of members</caption> 테이블에 대한 설명 추가, table 안에, 보통은 thead 전에
            13.text-center:글자 가운데 정렬, thead에만 적용하면 thead만 가운데정렬
        -->
    </head>
    <body>
        <div class="container">
        <h3 style="text-align:center;padding-top:50px">Bootstrap Table Example
            <small class="text-muted"></small>with faded Secondary text</small>
        </h4>

        <h1 class="display-4">Bootstrap Table Example</h1>
        <br>

        <table class="table table-bordered table-striped table-dark text-right table-sm table-hover"> 
            <caption>Free member list of members</caption>
            <thead class="thead-light text-left">
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
            <tbody class="text-center">
                <tr>
                    <td>1</td>
                    <td>홍길동</td>
                    <td>22</td>
                    <td class= "text-left">서울시 서초구 양재동~</td>
                    <td>Male</td>
                    <td>Programmer</td>
                    <td>영화보기</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>이순신</td>
                    <td>33</td>
                    <td class= "text-left">부산광역시 해운대구 ~</td>
                    <td>Female</td>
                    <td>Designer</td>
                    <td>음악감상</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>강감찬</td>
                    <td>44</td>
                    <td class= "text-left">인천시 서구 서구동~</td>
                    <td>Male</td>
                    <td>Manager</td>
                    <td>우표수집</td>
                </tr>
                <tr class="bg-info">
                    <td colspan=6>최종 합계</td>
                    <td>100명</td>
                </tr>
                <tr class="bg-warning">
                </tr>
                <tr class="bg-success">
                </tr>
            </tbody>
             
        </table>
        </div>
    </body>
</html>
```