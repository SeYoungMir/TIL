## JSON 데이터 객체와 문자열로 변환하기
- JSON.parse()
- JSON.stringify()

### JSON.parse(jsonText)$\rarr$ JSON 형식의 텍스트 $\rarr$ 객체로 변환
```js
let jsonText='{'name':"홍길동","age":20,"nationality":"대한민국"}';

console.log("변환 전 -->"+typeof jsonText); //string

const jsonObj = JSON.parse(jsonText);
console.log("변환 후 -->"+typeof jsonObj); //object

console.log(jsonText.name);// 이 경우 object가 아니기 때문에 제대로 출력되지 않음

let jsonText={'name':"홍길동","age":20,"nationality":"대한민국"};
console.log("변환 전 -->"+typeof jsonText); //object

console.log('-------------------')
console.log(jsonObj.name);//홍길동
console.log(jsonObj.age);//20
console.log(jsonObj.nationality);//대한민국

console.log(jsonObj.name + "" + jsonObj.age+ "" + jsonObj.nationality);
console.log('이름과 나이는 ${jsonObj.name}(${jsonObj.age})이며, 국적은 ${jsonObj.nationality} 이다.');
```
### JSON.stringify(dataObj) $\rarr$ 데이터 객체를 $\rarr$ JSON 형식의 텍스트로 변환

```js

console.log('-------------------')
const jsonStr= JSON.stringify(jsonObj);


console.log(jsonStr); //{'name':"홍길동","age":20,"nationality":"대한민국"}
console.log(typeof jsonStr); //string

```
