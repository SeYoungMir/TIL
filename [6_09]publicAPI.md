## JSON 객체 vs JSON 배열
- JSON을 많이 쓰는 이유? $\rarr$ 데이터를 전달하고, 교환하고, 저정할 때 $\rarr$ 가볍고, 텍스트기반, JS기반

1. JSON 객체 
   $\rarr$ 중괄호 {} 사용.

   - JSON에서 객체(Object)란?
     - key : value의 한 쌍으로 이루어진 정렬되지 않은 속성(property)들의 집합
     - 콤마(,)로 구분하여 여러 개의 속성을 가질 수 있다.
     - 문자열은 반드시 큰따옴표("")로 묶어준다.
     - 예시 
```
{
    "name":"홍길동","age":20,
    "nationality":"대한민국",
    "hobby":"영화보기"
}
```
2. 객체 안의 객체 $\rarr$ 계층적 구조
```
{
    "group1":{

        "name":"홍길동",    "age":20,
        "nationality":"대한민국",
        "hobby":"영화보기",
        "company":{
            "cname":"XX 원자력 발전소",
            "cphone":"02-1234-5678",
           "caddress":"경기도 용인시 용인동 용인 신도로 1234"
        }
    }
}
```
3. JSON 배열 $\rarr$ 대괄호 [] 사용
   - 역시 콤마(,)를 사용하여 여러 JSON 객체를 추가 및 구분할 수 있다
   - 배열 이름이 person이고, 3개의 JSON 객체를 이 배열의 요소로 가지는 JSON 배열
```
"person":[
    {"name":"홍길동","age":20,"nationality":"한국"}
    
    {"name":이순신","age":30,"nationality":"미국"}
    
    {"name":"강감찬","age":40,"nationality":"영국"}
]
```
