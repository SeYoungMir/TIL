## JSON 데이터를 다루기위한 JS 기본 사용법2

### 1. 데이터
```js
const person = [
    {"name":"홍길동","age":20,"nationality":"한국"},
    
    {"name":이순신","age":30,"nationality":"미국"},
    
    {"name":"강감찬","age":40,"nationality":"영국"},

    {"name":"을지문덕","age":50,"nationality":"프랑스"}
];

console.log(typeof person);
 //object
console.log(typeof person[0]);
//string
```
### 2. 수정
```js
console.log('------------------역따옴표')
person[0].name="홍길자";
person[0].age=22;
console.log(`홍길동의 이름이 ${person[0].name}로 수정되었고,나이는 ${person[0].age}로 수정되었습니다`)

```
### 3. 반복
```js
console.log('-----------------for .. in');
for(let i in person) { 
    console.log(i)
}
//index인 0,1,2,3 출력
for(let k in person[0]) { 
    console.log(k)
/// key 값인 name, age, nationality 출력

}

```

