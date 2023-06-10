## JSON 데이터를 다루기위한 JS 기본 사용법1

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

### 2. 출력
```js
console.log('-----------------');
console.log(person[0].name+""+person[0].age+""+person[0].nationality);

```
### 3. 반복
```js
console.log('-----------------전개 연산자');
const str1 ="korea';
console.log(...person); 
console.log(...str1);
// 전개 연산자
console.log([...str1]); 
// __proto__ -> Array
console.log({...str1});
// __proto__ -> Object
console.log([...person])
console.log({...person})

console.log([...person].length) //4 출력
console.log([...person][0].name) // 홍길동 출력
console.log([...person][3].name) //을지문덕 출력
console.log([...person][3].age) // 50 출력
console.log({...person})
console.log({...person}[1].name) // 이순신 출력
```

### 4. 반복 가능한 객체 $\rarr$ for .. of,... (전개 연산자)
```js
console.log('-----------------for .. of');
for(let ele of person) { 
    console.log(ele)
    //person -->iterable, 즉 반복 가능한 객체가 오면 됨

}