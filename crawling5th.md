### HTML 소스코드를 분석하고 처리하기
#### 줄 바꿈으로 가독성 높이기
- HTML 소스 코드를 파일('br_example_constitution.html')로 저장
```python
%%writefile C:/Myexam/br_example_constitution.html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>줄 바꿈 테스트 예제</title>
  </head>
  <body>
  <p id="title"><b>대한민국헌법</b></p>
  <p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>
  <p id="content">제2조 <br/>①대한민국의 국민이 되는 요건은 법률로 정한다.<br/>②국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다.</p>
  </body>
</html>
```
- HTML 파일('br_example_constitution.html')을 읽어서 변수
html_source에 할당한 후 요소에서 텍스트를 추출하고 출력
```python
from bs4 import BeautifulSoup

f= open('C:/Myexam/br_example_constitution.html',encoding='utf-8')
b
html_source = f.read()
f.close()
soup = BeautifulSoup(html_source,'lxml')
title= soup.find('p',{"id":"title"})
contents = soup.find_all('p',{"id":"content"})

print(title.get_text())
for content in contents:
    print(content.get_text())
```


- 추출된 HTML 코드에서 줄 바꿈 태그를 파이썬의 개행 문자(\n)로 바꿈
- Beautiful Soup의 'replace_with(새로운 문자열)'를 이용
- 기존의 태그나 문자열을 새로운 태그나 문자열로 바꿈
- find_result = BeautifulSoup.find ('태그')
- find_result.replace_with('새 태그나 문자열')

- 추출된 HTML 코드에서 줄 바꿈 태그를 파이썬의 개행 문자(\n)로 바
꿈
- Beautiful Soup의 'replace_with(새로운 문자열)'를 이용해
- 기존의 태그나 문자열을 새로운 태그나 문자열로 바꿀
- find_result = BeautifulSoup.find ('태그')
- find_result.replace_with('새 태그나 문자열')

- HTML 코드에서 br 태그를 파이썬의 개행문자로 바꾸고 싶으면
```python
html1=  '<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.</p>'

soup1= BeautifulSoup(html1,'lxml')

print('==> 태그 p로 찾은 요소')
content1= soup1.find('p',{"id":"content"})
print (content1)

br_content = content1.find("br")
print('==> 결과에서 태그 br로 찾은 요소:',br_content)

br_content.replace_with("\n")
print('==> 태그 br을 개행문자로 바꾼 결과')
print(content1)
```
#### 추출된 요소 전체에 적용

- HTML 코드에서 br 태그를 파이썬의 개행문자로 바꾸고 싶으면
```python
soup2 = BeautifulSoup(html1,"lxml")
content2 = soup2.find('p',{"id":"content"})
br_contents = content2.find_all("br")
for br_content in br_contents:
    br_content.replace_with("\n")
print(content2)
```
-  함수 사용

```python
def replace_newline(soup_html):
    br_to_newlines= soup_html.find_all("br")
    for br_to_newline in br_to_newlines:
        br_to_newline.replace_with("\n")
    return soup_html
```
- Beautiful Soup로 파싱된 HTML 소스에서 br 태그를 개행문자(\n)로
변경
- 함수를 이용한 결과에서 요소의 내용만 추출하기 위해 get_text()를 적용

```python
soup2 = BeautifulSoup(html1,"lxml")
content2 = soup.find('p',{"id":"content"})
content3 = replace_newline(content2)
print(content3.get_text())
```
- HTML 소스코드를 할당한 변수 html_source에 위의 파이씬 코드를 적용

- 줄을 바꾸어 문단을 구분하는 p 태그를 표기하기 위해
- 'content1.get_text()'를 print()로 출력할 때 개행문자{\n)를 추가
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_source,'lxml')

title= soup.find('p',{"id":"title"})
contents = soup.find_all('p',{"id":"content"})

print(title.get_text(),"\n")

for content in contents:
    content1 = replace_newline(content)
    
    print(content1.get_text(),'\n')
```
#### 웹 스크레이핑 시 주의 사항
- 웹 페이지의 소스코드에서 데이터를 얻기 위한 규칙을 발견
- 파이썬 코드를 이용해 웹 스크레이핑을 할 경우 해당 웹 사이트에 너무 빈
번하게 접근 금지
- 사이트는 언제든지 예고 없이 변경될 수 있음
- 인터넷 상에 공개된 데이터라고 하더라도 저작권(copyright)이 있는 경우
가 있음

### 웹 페이지에서 이미지 가져오기
#### 하나의 이미지 내려받기
- requests 라이브러리를 이용해 이미지 파일을 위한응답 객체 가져오기
```python
import requests
url= 'https://www.python.org/static/img/python-logo.png'
html_image = requests.get(url)
html_image
```
- 저장 디렉토리 
- 파일명 필요

|읽기|쓰기|
|---|---|
|read()|write()|
|read_csv()|write_csv()|
|read_excel()|write_excel()|
|load()|save()|

- 이미지 주소에서 이미지 파일명만 추출해 이용
- 이미지 파일의 전체 경로에서 파일 이름만 추출한 것
```python
import os
image_file_name = os.path.basename(url)
image_file_name
```
- os.makedirs(folder)
- os.path.exists(folder)

```python
folder = 'C:/Myexam/download'

if not os.path.exists(folder):
    os.makedirs(folder)
```
- 생성된 폴더와 추출한 이미지 파일명을 합치기 위해서 0S모듈의 메서드를 이용
- os.path.join(path1[,path2[,...]])
- 파일을 저장 하려는폴더가 folder이고 파일 이름이 file
- 'os.path.join(folder, file)'로 파일의 전체 경로를 생성
- 생성한 이미지 파일을 위한 폴더와 추출한 이미지 파일을 통합하는 코드
```python
image_path = os.path.join(folder,image_file_name)
image_path
```
- 이미지 파일을 저장하기 전에 우선 open('file_name','mode')을 이용해 파일을 오픈
- file_name에는 앞에서 지정한 경로 이름을 넣고
- mode에는 쓰기 모드와 바이너리 파일 모드를 지정
- 저장하려는 파일이 텍스트 파일이 아니고 이미지 파일이므로 바이너리 파일 모드로 지정
```python
imageFile = open(image_path,'wb')
```
- requests 라이브러리의 iter_content(chunk_size)를 이용해 전체 이미지를 chunk_size [bytes] 만큼 나눠서 내림
-  전체 파일의 마지막까지 나눠서 내려 받은 데이터를 차례대로 파일 쓰기를 하면 최종적으로 완전한 하나의 이미지 파일을 내려 받을 수 있음

```python
#이미지 데이터를 1000000 바이트씩 나눠서 내려받고 파일에 순차적으로 저장
chunk_size =1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()
```
- 지정된 폴더의 파일 목록을 보여주는 'os.listdir(folder)'를 수행
```python
os.listdir(folder)
```
- 이미지 주소를 알 경우 이미지 파일을 컴퓨터로 내려 받는 방법
```python
import requests
import os
url = 'https://www.python.org/static/img/python-logo.png'
html_image = requests.get(url)
image_file_name =  os.path.basename(url)

folder ='C:/Myexam/download'

if not os.path.exists(folder):
    os.makedirs(folder)

image_path = os.path.join(folder, image_file_name)

imageFile = open(image_path, 'wb')
#이미지 데이터를 1000000 바이트씩 나눠서 내려받고 파일에 순차적으로 저장
chunk_size =1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()
```
#### 여러 이미지 내려받기
- select('a img')를 수행하면 해당 이미지의 요소가 추출

```python
import requests
from bs4 import BeautifulSoup

URL= 'https://www.reshot.com/free-vector-illustrations/animal/'
html_reshot_image = requests.get(URL).text
soup_reshot_image = BeautifulSoup(html_reshot_image,"lxml")
reshot_image_elements = soup_reshot_image.select('a img')
reshot_image_elements[0:4]
```
- 출력 결과를 보면 img 태그가 포함된 이미지가 있는 요소가 추출
- 리스트 reshot_image_elements의 제일 첫 번째 요소는 reshot의 로고 이미지
- 동물 이미지만 가져오기 위해서는 reshot_image_elements[1:]을 이용
- BeautifulSoup에서 get('속성')은 '속성'에 들어간 '속성값'을 반환
- 추출된 요소에서 src 의 속성값인 이미지 주소를 구하려면 get('src')을 수행
```python
reshot_image_url = reshot_image_elements[1].get('src')
reshot_image_url
```

- 이미지의 주소를 알고 있을 때 이미지를 내려 받는 방법

```python
html_image = requests.get(reshot_image_url)

folder = "C:/Myexam/download"

# os.path.basename(URL)는 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리하는 방법
imageFile = open(os.path.join(folder, os.path.basename(reshot_image_url)),'wb')

#이미지 데이터를 1000000 바이트씩 나눠서 내려받고 파일에 순차적으로 저장
chunk_size =1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()
```
- 함수로 만들고 반복문으로 지정한 개수만큼 이미지를 내려받는 코드를 작성

```python
import requests
from bs4 import BeautifulSoup
import os

#URL(주소)에서 이미지 주소 추출
def get_image_url(url):
    html_image_url = requests.get(url).text
    soup_image_url = BeautifulSoup(html_image_url,'lxml')
    image_elements = soup_image_url.select('img')
    if(image_elements !=None):
        image_urls=[]
        for image_element in image_elements:
            image_urls.append(image_element.get('src'))
        return image_urls
    else:
        return None

def download_image(img_folder,img_url):
    if (img_url != None):
        html_image = requests.get(img_url)
        #os.path.basename(URL)는 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리
        imageFile = open(os.path.join(img_folder,os.path.basename(img_url)),'wb')
        
        chunk_size =1000000 #이미지 데이터를 1000000 바이트씩 나눠서 내려받고 파일에 순차적으로 저장
        for chunk in html_image.iter_content(chunk_size):
            imageFile.write(chunk)
            imageFile.close()
        print("이미지 파일명:'{0}',내려받기 완료!".format(os.path.basename(img_url)))
    else:
        print("내려받을 이미지가 없습니다.")
#웹사이트의 주소 지정
reshot_url = 'https://www.reshot.com/free-vector-illustrations/animal/'

figure_folder = "C:/Myexam/download" #이미지를 내려받을 폴더 지정

reshot_image_urls =get_image_url(reshot_url) #이미지 파일의 주소 가져오기

num_of_download_image = 7 #내려받을 이미지 개수 지정
#num_of_download_image=len(reshot_image_urls)

for k in range(num_of_download_image):
        download_image(figure_folder,reshot_image_urls[k])
print("="*30)
print("선택한 모든 이미지 내려받기 완료!")

```

- len(reshot_image_urls)로 이미지가 몇 개인지 확인

```python
num_of_download_image=len(reshot_image_urls)
num_of_download_image
```

## 정리
- webbrowser 라이브러리를 이용해 원하는웹 사이트를 웹 브라우저
로 열어서 접속하는 방법
- HTML 코드를 분석하고 requests 라이브러리를 이용해 HTML 소스를 가져오는 방법
- HTML 소스를 Beautiful Soup 라이브러리를 이용해 파싱하고 원하는 결과를 추출하는 방법
- 웹 사이트에 있는 이미지 파일을 내려 받는 방법
