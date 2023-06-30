## JSON 데이터를 출력시키는 BS 테이블 클래스 연습하기(1)

- Bootstrap은 CSS보다 단순하고 간편하게 결과를 출력 가능함
- 디자인적으로 할 때는 Bootstrap만으로도 가능함


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
            1.컨테이너 없이 테이블만 작성하면 너비가 100% 꽉 참.
            2.테이블 외곽에 div 쓰고 class=table 적용하면 양쪽에 적절한 마진이 생김
            
        -->
    </head>
    <body>
        <div class="container">
        <h3 style="text-align:center;padding-top:50px">Bootstrap Table Example
            <small class="text-muted"></small>with faded Secondary text</small>
        </h4>

        <h1 class="display-4">Bootstrap Table Example</h1>
        <br>

        <table class="table">
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
                <tr>
                    <td>1</td>
                    <td>홍길동</td>
                    <td>22</td>
                    <td>서울시 서초구 양재동~</td>
                    <td>Male</td>
                    <td>Programmer</td>
                    <td>영화보기</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>이순신</td>
                    <td>33</td>
                    <td>부산광역시 해운대구 ~</td>
                    <td>Female</td>
                    <td>Designer</td>
                    <td>음악감상</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>강감찬</td>
                    <td>44</td>
                    <td>인천시 서구 서구동~</td>
                    <td>Male</td>
                    <td>Manager</td>
                    <td>우표수집</td>
                </tr>
            </tbody>
        </table>
        </div>
    </body>
</html>
```