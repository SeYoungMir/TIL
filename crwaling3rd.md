## 크롤링과 스크레이핑
### 크콜러와 크롤링
- 크롤러는 자동으로 웹 페이지에 있는 정보를 수집하는 프로그램
- 크롤러는 사람이 브라우저로 웹 페이지를 조회하고 정보를 수집하는 것과 비교할 수 없는 대규모의 정보를 단시간에 수집
- 크롤러로 정보를 수집하는 일을 '크롤링'

### 스크레이핑
- 스크레이핑은 수집한 정보를 분석해서 필요한 정보를 추출하는 것

### 크롤링과 스크레이핑
- 크롤링+스크레이필 <웹 크롤링>
- 웹 페이지의 정보는 
  '수집 - 분석 - 추출 - 가공 - 저장 - 출력'이라는 일련의 흐름
  '뷰티플 샵'모듈 사용
### 크롤링과 스크레이핑 할 때의 주의 사항
- 웹 사이트에 접근할 때의 주의 사항
- 웹 사이트의 이용 규약을 확인하고 지킨다
- robots.txt와 robots 메타 태그의 접근 제한 사항을 지킨다.
- 제한이 없더라도 상대 서버에 부하가 가지 않을 정도의 속도로 접근한다.- rel="nofollow"가 설정되어 있으면 크롤러로 접근하지 않는다.
-  크롤링을 거부하는 조치가 있으면 즉시 크롤링을 멈추고 이미 추출한 정보를 모두 삭제한다.

- 수집한 데이터를 다룰 때의 주의 사항
-  수집한 데이터는 자작권을 지켜서 사용해야 함
-  수집한 데이터는 저작권에 문제가 있으면 개인적인 용도로만 사용한
-  수집한 데이터를 기반으로 검색 서비스를 제공하는 경우, 웹 사이트와 API 등의 사용 규약을 확인하고 문제가 없을 때만 제공함
-  이용 규약이 따로 없을 때도 상대방에서 확인한 뒤 데이터를 공개

## 크롤러 설계 기본
### 목적과 대상을 명확하게 보기
- 개발 전에 목적을 명확하게 함
  - 개발 전에 목적을 명확하게 ㅁ함
  - 대상을 충분하게 분석하는 것
### URL 확인하기
- 사이트 맵을 트리구조(페이지)로 제공하는 사이트
  - 사이트 맵을 보면 어떤 정보가 어떤 UL 아래 있는지 쉽게 확인
- 사이트 맵을 XML로 제공하는 사이트
  - http://www.usa.gov/sitemap.xml)
- 사이트 맵을 확인 할 수 없을때
  -  카테고리 목록 페이지로 이동하는 링크가 없는지,사이트 내부에서 하나하나 찾아봄
### 목적 데이터를 따로 제공하는지 확인하기
- 사이트에 따라서는 불특정 다수의 크롤러가 접근해서 부하를 발생시키는 것을 막기 위해 공식 아카이브 데이터를 제공하기도 함
  - https://ko.wikipedia.org/wiki/위키백과:데이터베이스_다운로드
- 아카이브 데이터 덤프를 제공해주지 않는 경우라도 웹 API와 피드를 제공해준다면 이를 활용
  
### 웹 API
- 웹 API는 특정 URL에 정해진 매개 변수를 넣어 접근하면 XML 또는 JSON등의 구조화 된 데이터를 제공해주는 기능
  -  https://developers.naver.com/docs/common/openapiguide/apilist.md
  - https://developers.kakao.com/

## 크롤러가 가지는 설계할 때의 주의 사항
### 설계가 필요한 부분
- '출력 결과로 무엇이 필요한가' 가 바로 '목적'
  - 스프레드 시트의 특정 위치에 숫자를 반영
  - 다른 시스템과 연동할 수 있게 API를 제공
  - 자신의 사이트에서 읽어 들일 수 있게 피드를 만듦
- 출력 결과와 관련된 명확한 상세가 있어야 함
- 크롤러의 각 처리 공정
  - 수집 크롤러-> 데이터 요청
  - 분석 텍스트 데이터 -> 구조화 데이터
  - 추출 구조화 데이터 추출
  - 가공 가공가능한 데이터로 가공
  - 저장 위에서 얻은 데이터를 DB에 저장
### 네트워크 요청
- 간격 설정하기
  - 적어도 1초에 한번 정도만 요청할 수 있게 하는 것을 권장(sleep())
- 타임 아웃
  - 요청한 사이트로부터 응답이 오지 않는 경우에 타임아웃 설정
  - 3초동안 응답이 없으면 멈춤
- 재시도
  - 큰 문제가 없는데도 오류를 응답하는 경우
  - 재시도할 때는 어느 정보의 횟수 제한(1~3회 정도)이 있어야함
  - 재시도 간격도 고려
### 파싱(분석)
- 문자 코드
  - 대부분 UTP-8로 작성되어 있지만 HTML 소스 코드는 다양한 문자코드로 작성된 경우가 많음(EUC-KR 등)
- HTML/XML 파싱
  - 웹 페이지 중에는 태그가 잘못 구성되어 있거나 속성 값에 큰 따옴표가 쳐져 있지 않은 경우도 많음
- JSON 디코드
  - 대부분의 웹 API는 JSON 형식으로 데이터를 응답
### 스크레이핑과 정규 표현식
- URL 정규화
  - 링크를 추출할 때 링크가 상대 경로인 경우
- 테스트
  - 스크레이핑 라이브러리를 사용하거나 정규 표현식을 사용하더라도 한 번에 원하는 데이터를 추출하는 경우가 적음
  - 테스트 코드를 사용하면 수집 처리와 스크레이핑 처리를 분리하기 쉬움
  - 
### 운영 시 주의점
- 장애/복구
  - Back up / Restore
- 보안
  - 서비스 분산 공격 (DDoS)
  - 데이터 유출(암호화 등의 대처법)
  - 
### 데이터 저장소의 구조와 선택
- 데이터 저장소
  - 파일(csv, excel...)
  - 문서 데이터베이스
  - 관계형 데이터베이스(RDBMS)
  - 객체 데이터베이스
  - 키-값 데이터 베이스 
  - 괄호 제외는 모두 NOSQL

### 배치를 만들 때의 주의점
- 공정분리하기
- 중간 데이터 저장해두기
- 실행 시간 알아 두기
- 중지 조건을 명확하게 하기
- 함수의 매개 변수를 간단하게 하기
- 날짜를 다룰 때의 주의 사항
- 특히 주의해야 하는 경우
  - 날짜 형식 
    - ex) 2023.1.17/2023/1/17/2023-1-17/Jan 17,2023 
    - 날짜 형식 통일
  - 한글
    - ~ 한다./ ~ 있다.  의 경우 ㅏ.가 |로 인식 |의 경우 end로 인식, 종료하는 문제.

#### 자동화 CD/CI , DEVOPS(develop + operate)
- 개발 -> 빌드 -> 테스트 -> 배포
- 배치 or 파이프라인(자동화)

#### 최근 추세의 용어
- 자동화
- 관리의 관리(오케스트레이션)

### 설계 (https://wikibook.co.kr/list/)
- 소스 확인하기

- 저장 방법
- 파일 저장 형식
  - CSV(Comma-Separated Values)
  - TSV(Tab-Separated Values)
  - JSON(JavaScript Object Notation)

## 파이썬을 사용하는 이유
### 파이썬 언어의 특징
- 파이썬이 크롤링과 스크레이핑에 적합한 이유
  - 코드의 가독성이 높음
  - 문법이 단순하고 명쾌함
  - 컴파일이 필요하지 않은 스크립트 언어
  - 풍부한 라이브러리
- 시행착오를 많이 반복하는 크롤링과 스크레이핑에 적합함


## 크롤링과 스크레이핑
### 웹 브라우저 실행
#### 웹 브라우저 실행시키기(webbrowser)
- webbrowser는 자신의 시스템에서 사용하는 기본 웹브라우저가 자동으로 실행되게 하는 모듈
- 웹 브라우저를 자동으로 실행시키고 해당 URL인 www.naver.com으로 감
```python
import webbrowser
webbrowser.open("http://www.naver.com")
```
- webbrower의 open함수는 웹브라우저가 실행된 상태이면 해당 주소로 이동
- 웹브라우저가 실행되지 않은 상태이면 새로이 웹브라우저가 실행되어 해당
주소로 이동
- Open_new 함수는 이미 웹브라우저가 실행된 상태에서 새로운 창으로 해당
주소가 열리도록 함
```python
import webbrowser
webbrowser.open_new("http://google.co.kr"
```
### 웹 페이지 추출하기
#### urllib으로 웹 페이지 추출하기
- 페이지를 추출할 때는 표준 라이브러리 urilib.request 모듈을 사용
- urllib.request에 포함돼 있는 urlopen() 함수에 URL을 지정하면 웹 페이지를
추출
```python
from urllib.request import urlopen
# urlopen()함수는 HTTPResponse 자료형의 객체를 반환합니다.
f = urlopen('http://hanbit.co.kr')
type(f)
f.read() # read() 메서드로 HTTP 응답 본문(bytes 자료형)을 추출합니다
f.status # 상태 코드를 추출합니다.
f.getheader('Content-Type') # HTTP 헤더의 값을 추출합니다
```
#### meta 태그에서 인코딩 방식 추출하기
- HTML 내부의 meta 태그 또는 응답 본문의 바이트열도 확인해서 최종적 인
인코 딩 방식을 결정하고 화면에 출력

```python
import re
import sys
from urllib.request import urlopen
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
bytes_content = f.read() 
scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
encoding = match.group(1)
else:
encoding = 'utf-8'
print('encoding:', encoding, file=sys.stderr)
text = bytes_content.decode(encoding)
print(text)
```
#### 정규 표현식으로 스크레이핑하기
- 표준 라이브러리의 re 모듈을 사용

```python
import re
from html import unescape
# 이전 절에서 다운로드한 파일을 열고 html이라는 변수에 저장합니다.
with open('dp.html') as f:
html = f.read()
# re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
# 도서의 URL을 추출합니다.
url = re.search(r'<a href="(.*?)">', partial_html).group(1)
url = 'http://www.hanbit.co.kr' + url
# 태그를 제거해서 도서의 제목을 추출합니다.
title = re.sub(r'<.*?>', '', partial_html)
title = unescape(title)
print('url:', url)
print('title:', title)
print('---')
```
#### XML(RSS) 스크레이핑
- 블로그 또는 뉴스 사이트 등의 웹사이트는 변경 정보 등을 RSS라는 이름의
XML 형식으로 제공
- RSS는 XML을 기반으로 만들어졌으므로 HTML보다 간단하게 파싱
- rss라는 이름의 요소를 루트로 하는 트리 구조를 가지고 있음
- 내부에는 피드를 나타내는 channel 요소가 있음
- channel 요소의 앞부분에는 피드의 메타 정보를 나타내는 title 요소와 link 
요소 등이 있음
### 데이터 저장하기
#### CSV 형식으로 저장하기

- CSV(Common Seperated Values)는 하나의 레코드를 한 줄에 나타내고, 각
줄의 값을 쉼표로 구분하 는 텍스트 형식
- 행과 열로 구성되는 2차원 데이터를 저장할 때 사용
- CSV 형식을 만드 는 가장 쉬운 방법은 str.join() 메서드를 사용
- csv.writer를 사용하면 간단하게 CSV 형식으로 출력
- 한 줄을 줄력할 때 는 writerow()메서드를 사용하며 , 매개변수로 list 또는
tuple과 같은 반복 가능한 객체

#### JSON 형식으로 저장하기
-JSON(JavaScript Object Notation)은 자바스크립트에서 객체를 표현하는 방
법을 사용하는 텍스트형식
- JSON을 사용하면 list 또는 dict를 조합 한 복잡한 데이터 구조를 쉽게 다룸
- 파이썬은 JSON 형식을 쉽게 다룰 수 있게 json 모듈을 제공
- json.dumps()함수 를 사용하면 list와 dict 등의 객체를 JSON 형식 문자열로
변환

#### 데이터베이스 (SQLite3) 에 저장하기
- SQLite3는 파일기반의 간단한 관계형 데이터베이스
- 구문을 사용해 데이터를 읽고 쓸 수 있음
- SQLite는 가볍게 사용할 수 있는 관계형 데이터베이스지만 파일을 쓰는 데
시간이 꽤 걸린다는 것이 단점
- 적은 데이터를 다룰 때는 문제 없지만 크롤링한 대량의 데이터를 계속해
서 올리면 SQLite를 사용할 경우 파일을 쓰는 부분이 병목지점으로 작용
- 어떤 프로그램 이 파일을 열고 내용을 쓰고 있을 때는 다른 프로그램에서
해당 파일을 사용할 수 없으므로 동시 처리도 불가능
- 주로 핸드폰에 사용

### 파이썬으로 스크레이핑하는 흐름
#### 파이썬으로 스크레이핑하는 흐름
- fetch(url)
  - 매개변수로 url을 받고 지정한 URL의 웹 페이지를 추출
- scrape(html)
  - 매개변수로 html을 받고 정규 표현식을 사용해 HTML에서 도서 정보를 추출
- save(db_path, books)
  - 매개변수로 books라는 도서 목록을 받고, SQLite 데이터베이스에 저장

### urllib 사용법 및 기본 스크래핑
#### urllib.request 기초 사용법

- 네이버 이미지 다운로드 대상
- 구글 HTML 정보 다운로드 대상
- Header 정보 확인
- 다운로드 정보 파일 저장

```python
import urllib.request as req
#파일 URL
img_url= "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"

html_url ="http://google.com"

#다운받을 경로
save_path1 = "C:/Myexam/test1.jpg"
save_path2 = "C:/Myexam/index.html"

try:
    file1, header1 = req.urlretrieve(img_url,save_path1)
    file2, header2 = req.urlretrieve(html_url,save_path2)
except Exception as e:
    print("Download failed.")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)
    # 다운로드 파일 정보
    print("Filename1 {}".format(file1))
    print("Filename2 {}".format(file2))
    print()
    # 성공
    print("Download Succeed")
```

#### urllib.request 예외 처리
- 기존 소스 코드 변경
- 예외 처리 추가
- 기타 리팩토링

```python
import urllib.request as req
from urllib.error import URLError,HTTPError
# 다운로드 경로 및 파일명
path_list=["C:/Myexam/test1.jpg","C:/Myexam/index.html"]
#다운로드 리소스 URL
target_url =["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg","http://google.com"]

for i, url in enumerate(target_url):
    #예외 처리
    try:
        #웹 수신 정보 읽기 #jupyter 도움말 = shift +tab
        response = req.urlopen(url)
        
        #수신 내용
        contents = response.read()
        
        print('-'*30)
        #상태 정보 중간 출력
        print('Header Info-{}:{}'.format(i,response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('-'*30)
        
        #파일 쓰기
        with open (path_list[i],'wb') as c:
            c.write(contents)
            
        # HTTP 에러 발생 시
    except HTTPError as e:
        print("Download failed.")
        print('HTTPError Code :',e.code)
        
        #URL 에러 발생 시
    except URLError as e:
        print("Download failed.")
        print('URLError Code :',e.reason)
        
        #성공
    else:
        print()
        print("Download Succeed")
    
```


### lxml.html 사용
#### 네이버 뉴스 스탠드 스크랩핑(1)
- 네이버 메인 뉴스 정보 스크랩핑
- 신문사 정보 리스트 출력
- CSS 선택자 활용
```python
from typing import get_args
import requests
from lxml.html import fromstring, tostring

def main():
    """
    네이버 지식인 스크랩핑 메인 함수
    """
    
    #세션 사용
    session= requests.Session()
    
    #스크랩핑 대상 URL(GET,POST)
    response = session.get("https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
    
    #신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)
    
    #딕셔너리 확인
    # print(urls)
    
    #결과 출력
    for name,url in urls.items():
        #url 출력
        print(name,url)
        #파일 쓰기
        #생략
def scrape_news_list_page(response):
    # url 리스트 선언
    urls = {}
    
    #태그 정보 문자열 저장
    #print(response.content)
    root=fromstring(response.content)
    #print(root)
    
    for a in root.xpath('//ul[@class="basic1"]/li/dl/dt/a[@class="_nclicks:kin.txt _searchListTitleAnchor"]'):
        # a 구조 확인
        # print(a)
        
        # a 문자열 출력
        # pirnt(tostring(a,pretty_print=True))
        
        name, url = extract_conents(a)
        #딕셔너리 삽입
        urls[name] = url
    return urls

def extract_conents(doc):
    #링크 주소
    link = doc.get("href")
    name = doc.text_content()
    return name, link

#스크랩핑 시작
if __name__== '__main__':
    main()
```

#### 네이버 뉴스 스탠드 스크랩핑(2)
- 네이버 메인 뉴스 정보 스크랩핑
- 신문사 정보 딕셔너리 출력
- Session 사용
- Xpath 활용

```python
import requests
import lxml.html

response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)

for a in root.cssselect('.view_box a'):
    url = a.get('href')
    print(url)
```