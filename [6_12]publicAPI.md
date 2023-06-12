## 중첩된 JSON 데이터 다루기
- 한 권의 도서 정보를 갖고 있는 JSON 데이터에서 해당 도서가 속해있는 카테고리 출력
### 1. 데이터
```js
{
    "isbn":"123-456-789",
    "author":{
        "name":"홍길동",
        "email":"hong@hongkildong.com",
     }
     "editor":{
        "name":"이순신",
        "email":"lee@leesoonsin.com"
     }
     "title":"대한민국의~",
     "category":[
        "Non-Fiction","IT","Politics"
        ]
}
```
```js 
//데이터 출력부
console.log(book["author"].name); // 홍길동 출력
console.log(book["editor"].name); // 이순신 출력
console.log(book["isbn"]); //isbn 출력
console.log(book.isbn); //isbn 출력 (결과는 동일)
console.log(book.title); // 타이틀 출력
console.log(book["title"]);
// 타이틀 출력(결과 동일)
console.log(book.category);
// 카테고리 출력
console.log(book["category"]);
// 카테고리 출력(결과 동일)

// 콘솔에는 출력되지만 웹페이지엔 출력되지 않음

//개별 액세스
let val = "";
val=book.category[0];
document.getElementById("aaa").innerText = val; 
// "aaa" div 태그에 해당 val 값 대입
// >실행 안됨, 왜? script src 부분을 body 부분으로 옮겨야 실행 가능
// >위쪽에서도 가능하게 하려면 js 파일 쪽에서 
window.onload=()=>{

}
// 안에 위의 코드를 넣어야 실행이 됨
```


```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>공공 데이터 API</title>
        <script src="./json/json_004.js"></script>

    </head>
    <body>
        <div id="aaa"></div>
    </body>
</html>
```