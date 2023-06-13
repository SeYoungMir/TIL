## 중첩된 JSON 데이터 다루기 - 반복문을 이용한 카테고리 출력


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
### 2. 출력
```js
//[6_12]에 이은 내용
//개별 액세스
let val = "";
val=book.category[0];
document.getElementById("aaa").innerText = val;

// 반복문을 이용한 엑세스
//for 
for (let i =0;i<book.category.length;i++){
    val += book.category[i]+"<br>";
    //val += '해당 도서가 속한 카테고리는 ' book.category[i]+"<br>...";
    //val += '${book.category[i]}<br>';
}
documnet.getElementById("aaa").innerHTNL = val;
//for .. in
for (let i in book.category){ val += book.category[i]+"<br>";

}
documnet.getElementById("aaa").innerHTNL = val;

//for ..of
for (let value of book.category){
    val += value+"<br>";
}
documnet.getElementById("aaa").innerHTNL = val;
```