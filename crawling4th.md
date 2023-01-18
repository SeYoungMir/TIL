## GET 방식/ POST 방식
- GET방식은 무엇을 얻느냐를 알 수 있으며 속도가 비교적 빠름, 파라미터 제한
- POST 방식은 무엇을 가져오는지 알 수 없으며 속도가 비교적 느림, 파라미터 비교적 제한 없음

### Get 방식 데이터 통신
#### urlopen 함수의 다양한 함수

- 사이트 요청 정보 확인
- encar(엔카)사이트 정보 수신
- Get 파라미터 요청
- 수신 데이터 디코딩(Decoding)
- 요청 URL 정보 분석

```python
import urllib.request
from urllib.parse import urlparse

#기본 요청 1(encar)
url = "http://www.encar.com/"
mem = urllib.request.urlopen(url)

#여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(1).decode('utf-8'))) #바이트 수
print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test')))

#기본 요청2 (ipify)
API = "https://api.ipify.org"

# Get 방식 Parameter
values = {
    'format': 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

# 요청 URL 생성
url = API + "?" +params
print("요청 url = {}".format(url))

# 수신 데이터 읽기
data = urllib.request.urlopen(url).read()

#수신 데이터 디코딩
text = data.decode("utf-8")
print('response: {}'.format(text))
```
#### RSS 데이터 스크랩핑

- 행정안전부 사이트 RSS 데이터 수신
- RSS란?
  - Really Simple Syndication, Rich Site Summary의 약자
  - 블로그처럼 컨텐츠 업데이트가 자주 일어나는 웹사이트에서, 업데이트된 정보를 쉽게 구독자들에게 제공하기 위해 XML을 기초로 만들어진 데이터 형식.
- 반복문을 활용한 연속 요청
- 요청 URL 정보 분석
- 수신 XML 데이터 확인
```python
import urllib.request
import urllib.parse

# 행정 안전부: https://www.mois.gokr
# 행정 안전부 RSS API URL
API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
params = []

for num in [1001,1012,1013,1014]:
    params.append(dict(ctxCd=num))

#연속해서 4회 요청
for c in params:
    #파라미터 출력
    #print(c)
    #URL 인코딩
    param = urllib.parse.urlencode(c)
    #URL 완성
    url= API + "?" + param
    #URL 출력
    print("url=",url)
    #요청
    res_data = urllib.request.urlopen(url).read()
    #수신 후 디코딩
    contents = res_data.decode("utf-8")
    #출력
    print(contents)

    #다음 주식 정보 가져오기
    #!pip install fake-useragent

    import json
import urllib.request as req
from fake_useragent import UserAgent

# Fake Header 정보(가상으로 User-Agent 생성)
ua = UserAgent()

#헤더 선언
headers={
    'User-Agent':ua.ie,
    'referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

#요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

#응답 데이터 확인(Json Data)
#print('res',res)

# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)['data']

#중간 확인
print('중간 확인:',rank_json,'\n')
for elm in rank_json:
   #print(type(elm)) #Type 확인
    print('순위: {}, 금액:{}, 회사명:{}'.format(elm['rank'],elm['tradePrice'],elm['name']))
```
### requsts 사용 스크랩핑
#### Session 및 Cookie 사용
- Requests 요청 정보 Payload
- 세션 활용성화 및 비활성화
- 쿠키 정보 전송
- User-Agent 정보 전송
- 수신 상태 코드 확인

#### JSON 수신 데이터 처리
- Httpbin 사이트를 이용한 JSON
- 수신 데이터 처리
- 수신데이터 -> JSON 변환 출력
- Response 다양한 정보 출력

#### Rest API
- 개발자 도구 송수신 분석
- Rest API 란?
- POST, PUT
- DELETE
- Requests

### BeautifulSoup 사용 스크랩핑
#### Beautiful Soup 사용법
- Beautiful Soup Selector
- HTML 태그 선택자 이해
- FIND, FIND_ALL
- SELECT, SELECT_ONE
- 다양한 DOM 접근 방법

#### 네이버 이미지 다운로드
- Beautiful Soup 이미지 다운로드
- Naver 이미지 검색 송수신 분석
- Select, Find_all
- 이미지 변환 및 저장
- 예외 처리

#### 로그인 처리
- Session 사용 로그인, 데이터 수집
- 대상 사이트 로그인 과정 분석
- 로그인 후 페이지 이동
- 필요 데이터 추출

### Selenium 사용
#### Selenium – 웹 자동화
- Selenium 설명 및 기본 설정
- Driver 설치
- 웹 자동화의 이해
- Selenium 기초
- 다음 사이트 기반
## 웹 스크레이핑을 위한 기본 지식
### 웹 페이지의 HTML 소스 가지고 오기
- 구글 웹 페이지(https://www.google.co.kr")의 소스 코드
```python
import requests

r= requests.get("https://www.google.co.kr")
r
#응답 객체를 잘 가져왔는지 확인
#HTML 파일 전체 중 일부분 출력
r.text[0:100]

```
## HTML 소스코드를 분석하고 처리하기
### 데이터 찾고 추출하기
- HTML 코드를 분석해 원하는 데이터를 추출하는 방법
- HTML 코드를 분석하기 위해서는 HTML 코드 구문을 이해하고 요소별로
HTML 코드를 분류
- Beautiful Soup 라이브러리를 이용해 HTML 소스를 파싱하고 태그나 속
성을 통해 원하는 데이터를 추출
  - 태그(요소, 속성)
    - find(), findall()
  - 선택자
    - select()
  - 단일 개체일때는 .get_text()
  - 여러 개체일때는 for문 + .get_text()

```python
from bs4 import BeautifulSoup

#테스트용 html 코드
html = """<html><body><div><span>\
       <a href=http://www.naver.com>naver</a>\
       <a href=http://www.google.com>google</a>\
       <a href=http://www.daum.net>daum</a>\
       </span></div></body></html>"""
```
- BeautifulSoup를 이용해 HTML 소스를 파싱
```python
soup =BeautifulSoup(html,'lxml')
soup
```
- 파싱 결과를 좀 더 보기 편하게 HTML 구조의 형태로 확인
```python
print(soup.prettify())
```
- 파싱한 결과에서 BeautifulSoup.find('태그')를 수행
- HTML 소스코드에서 해당 '태그'가 있는 첫 번째 요소를 찾아서 반환

```python
soup.find('a')
```

- get_text()는 HTML 소스코드의 요소에서 태그와 속성을 제거하고 텍스트 문자열만 반환
- get_text()는 원하는 HTML 요소를 가져온 후에 마지막 단계에서 요소의 텍스트 부분만 추출할 때 이용
```python
soup.find('a').get_text()
```

- HTML 코드 안의 모듬 a 태그를 찾아서 a 태그로 시작하는 모든 요소를 다 반환
- BeautifulSoup.find_all('태그')를 이용
```python
soup.find_all('a')
```
- 태그 이름의 모든 요소를 반환하는 find_all()의 결과는 리스트 형태로 반환

- get_text()는 리스트에 적용할 수 없으므로 for문을 이용해 항목별로 get_text()를 적용
```python
site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())
```

- HTML 파일을 작성한 후에 html2 변수에 할당
```python
from bs4 import BeautifulSoup

#테스트용 HTML 코드
html2="""
<html>
 <head>
   <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id ="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>
  
  <p id="book_title">감옥으로부터의 사색</p>
  <p id ="author">신영복</p>
 </body>
</html>
 """

soup2 = BeautifulSoup(html2,'lxml')

```
- Beautiful Soup의 다양한 기능을 활용해 HTML 소스로부터 필요한 데이터를 추출
- HTML 소스에서 title 태그의 요소는 'BeautifulSoup.title'을 이용해 가져올 수 있음
```python
soup2.title
```
- HTML 소스의 body 태그의 요소는 'BeautifulSoup.body'를 이용해 가져올 수 있음
```python
soup2.body
```
- body 태그 요소 내에 h1태그의 요소는'BeautifulSoup.body.h1'로 가져올 수 있음
```python
soup2.body.h1
soup2.body.p
```
- 이 때 요소는 맨 처음 요소만 나옴.

- find_all()을 이용
- 변수 html2에 있는 HTML 소스코드에서 p 태그가 들어 간 요소를 모두 가져올 수 있음
```python
soup2.find_all('p')
```
- p 태그 중 책 제목과 작가를 분리해서 가져오려면 find()나 find_all()을 이용
- '태그' 뿐만 아니라 태그 내의 '속성'도 함께 지정
- BeautifulSoup.find_all('태그',‘속성')
- BeautifulSoup.find('태그',‘속성')
- html2의 HTML 코드의 p 태그 요소 중 id가 book_title 인 속성을 갖는 첫 번째 요소만 반환
```python
soup2.find('p',{"id":"book_title"})
soup2.find_all('p',{"id":"author"})
```

- 책 제목과 작가를 포함한 요소를 각각 추출한 후에 텍스트만 뽑는 코드
```python
from bs4 import BeautifulSoup
soup2 = BeautifulSoup(html2,'lxml')

book_titles = soup2.find_all('p',{"id":"book_title"})
authors = soup2.find_all('p',{"id":"author"})
for book_title,author in zip(book_titles,authors):
    print(book_title.get_text()+'/'+author.get_text())
```

- CSS 선택자(selector)를 이용
- CSS 선택자는 CSS에서 원하는 요소를 선택 하는 것으로서 파이썬뿐만 아니라 다른 프로그래밍 언어에서도 HTML 소스를 처리할 때 많이 이용
- Beautiful Soup도 'BeautifulSoup.select('태그 및 속성')를 통해 CSS 선택자를 지원
- 'BeautifulSoup.select()'의 인자로 '태그 및 속성'을 단계적으로 입력하면 원하는 요소를 찾을 수 있음
- html2 변수에 할당된 HTML 소스에서 body 태그 요소 내에 h1 태그 요소를 가지고 오기
```python
soup2.select('body h1')
```
- body 태그 요소 중에 p 태그를 포함한 요소를 모두 갖고 오기
- 변수 html2의 HTML 소스에서 p 태그는 body 태그 요소 내에서만 있음
```python
soup2.select('body p')
```

- 태그 안의 속성과 속성값을 이용해 요소를 세밀하게 구분해 추출
- 태그 안의 속성이 class인 경우 '태그.class_속성값'으로 입력
- 속성이 id인 경우에는 '태그#id_속성값'으로 입력해 추출
- 그 안에 있는 속성이 id이므로 'p#id_속성값'으로 원하는 요소를 추출

```python
soup2.select('p#book_title')
soup2.select('p#author')
```
##### html 파일 생성 
```python
%%writefile C:/Myexam/HTML_example_my_site.html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>사이트 모음</title>
    </head>
    <body>
        <p id="title"><b>자주 가는 사이트 모음</b></p>
        <p id="contents">이 곳은 자주 가는 사이트를 모아 둔 곳입니다</p>
        <a href="http://www.naver.com" class="portal" id = "naver">네이버</a>
        <a href="http://www.google.com" class="search" id = "google">구글</a>
        <a href="http://www.daum.net" class="portal" id = "daum">다음</a>
        <a href="http://www.nl.go.kr" class="government" id = "nl">국립중앙도서관</a>
    </body>
</html>

```
- BeautifulSoup.select('태그 몇 속성')'에서 태그 안의 속성이 class인 경우
- '태그.class_속성값'으로 원하는 요소를 추출
- HTML 소스 파일은 이미 저장돼 있으므로 텍스트 파일을 읽어와서 변수 html3에 할당

```python
f = open('C:/Myexam/HTML_example_my_site.html',encoding='utf-8')
#with as 구문을 사용 시 f.close는 생략 가능
html3 = f.read()
f.close()

soup3 = BeautifulSoup(html3,"lxml")
```
- 읽어온 HTML 소스에서 태그가 a인 요소를 모두 가져오기
```python
soup3.select('a')
```
- HTML 소스에서 태그가 a이면서 class 속성값이 "portal"인 요소만 가져오기

```python
soup3.select('a.portal')
```
### 웹브라우저의 요소 검사
- soup3.select('html body a’)
- soup3.select('body a')
- soup3.select('html a')
- soup3.select('a')

- HTML 소스에서 태그 a를 포함하는 요소 중 class 속성이 "portal"인 요소만 선택

```python
soup3.select('a.portal')
```
-  태그를 포함하는 요소 중 id 속성이 "naver" 인 요소를 선택

```python
soup3.select('a#naver')
```
- '네이버'만 추출
```python
site_names = soup3.select('a#naver')
for site_name in site_names:
    print(site_name.get_text())
```


