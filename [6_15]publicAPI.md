## JSON 데이터를 웹페이지로 출력하기(1)
- Parsing $\rarr$ 다른 형식으로 저장된 데이터를 목적에 맞는 형태의 형식으로 변환하는 것
- JSON Parsing $\rarr$ JSON형식의 텍스트 문자열을 목적에 맞게 객체로 변환
```js
//데이터
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
        ],
    "picture":"images/joe.jpg",
    "description":"어쩌고저쩌고 ~",
    "comments":[{
        "id":"독자1",
        "text":"뭐라뭐라~"
    },
    {
        "id":"독자2",
        "text":"뭐라고라~"
    },
    {
        "id":"독자3",
        "text":"고라뭐라~"
    }],
    "comwinner":["독자1","독자2"]
    "add1":false,
    "add2":True,
}
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
        <button id="btn">클릭하세요! &nbsp; OO도서 이벤트의 댓글 참가자와 당첨자를 볼 수 있습니다</button>

        <br><br>
        <div id="bookList">
            <ul>
                <li>독자1-어쩌고</li>
                <li>독자2-저쩌고</li>
                <li>독자3-그쩌고</li>
            </ul>
            </div>
        <br><br>
        <div id="bookListWinner" style="font-weight:bold:color:red">독자1,독자2,독자3</div>

    </body>
</html>
```
* DOM 관련 공부를 하는 것이 좋음
* 