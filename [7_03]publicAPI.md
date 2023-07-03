## 부트스트랩 반응형 테이블

- 7/1 html 파일에서 시작함
- 
### bootstrap_table_example2.html
```html
<!DOCTYPE.html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Bootstrap Table Example</title>
        <link rel "stylesheet" href="http://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h2>Responsive Table with Bootstrap 4</h2>

            <div class="table-responsive">
            <!--
                .table-responsive-sm< 576px
                .table-responsive-md < 768px
                .table-responsive-lg < 992px
                .table-responsive -xl < 1200px
            -->
                <table class="table table-bordered text-center">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            <th>table_head</th>
                            
                        </tr>
                    </thead>
                    <tbody>
                        <td>1</td>
                        <td>2</td>
                        <td>3</td>
                        <td>4</td>
                        <td>5</td>
                        <td>6</td>
                        <td>7</td>
                        <td>8</td>
                        <td>9</td>
                        <td>10</td>
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>
```
- 기본적으로 반응형의 경우 가로형 1200px 보다 작을때 작동함
-  