# 6. 스크레이핑 개발(응용)
## 2. XML로 변환
### 4. 데이터를 분할해서 제공하기
- 웹 사이트에서 데이터베이스의 내용을 XML로 출력하여 사용자에게 제공할 때, 매번 모든 데이터를 XML로 변환하는 것이 좋지 않음
- 출판사별로 요청, 도서를 카테고리별로 구분해서 되도록 하나의 요청에 대해 데이터의 일부만 제공하는 것이 좋음
- 임의의 XML을 외부로부터 읽고 파싱할 때는 공식 문서에서도 추천하는 'defusedxml'을 사용하는 것이 좋음
## 3. JSON으로 변환
### 1. JSON 사용하기
- JSON은 자바스크립트의 객체를 작성할 때 사용하는 형식
- XML처럼 트리 구조를 가짐
```json
[
    {
        "id":71051687,
        "title": "파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발",
        "publisher" : {
            "id":1,
            "name":"위키북스"
        },
        "language":{
            "id":1,
            "name":"한국어"
        }
    },
    //데이터 생략
]
```
- XML과 다르게 모두 '키(Key)와 '값(Value)'으로 표현되며, 요소에 별도의 속성값을 부여할 수 없음.
- 속성값은 하나의 객체처럼 작성함.
- JSON도 XML처럼 트리의 모든 내용을 읽어 들이기 전까지는 데이터에 접근할 수 없습니다. JSON은 작성 방법이 굉장히 간단하고, 프로그램이 표준으로 가진 자료 구조로 변환하기 쉬워서 쉽게 사용할 수 있음
- XML 변환 코드를 기반으로 데이터베이스의 내용을 JSON으로 변환
```python
"""DB의 내용을 다양한 형식으로 출력하기"""
import json
##변환함수 이전은 같음
def create_json():
    """JSON 만들기"""
    books = []
    publisher = Publisher.all()
    publisher.load('books','books.language') # Eager Loading
    for publisher in publisher:
        for book in publisher.books:
            d={}
            d['id']=book.id
            d['title']=book.title
            d['publisher']={'id':publisher.id,'name':publisher.name}
            d['language']={'id':language.id,'name':language.name}
            books.append(d)
    return json.dumps(books, ensure_ascii=False, indent=2)

#main 실행 블록
if __name__=='__main___':
    json_str=create_json()
    print(json_str)
```