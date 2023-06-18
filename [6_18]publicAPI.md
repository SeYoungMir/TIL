## JSON 데이터를 웹페이지로 출력하기(4)

### 6/17 데이터에서 시작
```js
//데이터
window.onload = () => {

    document.getElementByID('btn').addEventListener('click',function()){
       console.log('test..');
       // ----------
       let json = 
        {   
            "book":[{
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
            }]
        }
        json = json["book"];
        console.log(json.length); // 1 출력
        console.log(json);
        console.log(json.isbn); //undefined
        console.log(json[0].isbn) //isbn 출력
        console.log(json[0].editor) // editor 출력
        console.log(json[0].category) // category 출력
        console.log(json[0].comments) //comments 출력
        console.log(json[0].comments[0]) //첫번째 comments 출력
        console.log(json[0].comments[json[0].comments.length-1]) //마지막번째 요소 출력
        console.log('-------------');
        for(let i=0; i <json.length;i++) {
            console.log(json[i].comments);
            console.log(json[i].comwinner);
        }
        console.log('-------------');
        // ul 태그 노드 생성
        let ul = document.createElement('ul');
        let bookList=document.getElementById("bookList");
        bookList.appendChild(ul);

         for(let i=0; i <json.length;i++){
            for (let j=0;j<json[i].comments.length;j++){

                // 댓글 참가자 출력
                let bookComments=json[i].comments[j]
                console.log(bookComments.id+":"+bookComments.text);
                //############
                //ul 태그 노드 생성 (여기서 진행 시 반복되어 표시됨)
                //let ul = document.createElement('ul');
                // li 태그 노드 생성
                let li=document.createElement('li');
                //aTagNode.href="#";

                //텍스트 노드 생성
            
                let txtNode=document.createTestNode(bookComments.id+":"+bookComments.text);
                li.appendChild(txtNode);
                ul.appendChild(li);
                //리스트에 붙이기
                
                bookList.appendChild(ul);
                //################
            }
            // 당첨자 출력
            console.log(json[i].comwinner.join(",")); //type = string
            document.getElementById('bookListWinner').innerHTML=json[i].comwinner.join(",");
            }
         }
        // -----------
}
;
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
            
            </div>
        <br><br>
        <div id="bookListWinner" style="font-weight:bold:color:red"></div>

    </body>
</html>
```