## CSS 개요
- css란?
  - Cascading style sheets
- 선택자 - CSS3에서 특정 HTML 태그를 선택할 때 사용
- ex) `h1 {color:red}`
- 이 때, h1이 선택자, color가 스타일 속성, red가 스타일 값.
- select h1 과 같은 방식(sql)로 이러한 값들을 뽑아올 수 있음.
### CSS 선택자 종류


|종류|형태|사용 예|
|---|---|---|
|전체 선택자|* | *|
|태그 선택자|태그|h1|
|아이디 선택자|#아이디|#id|
|클래스 선택자|.클래스|.header|
|속성 선택자| | |
|후손 선택자|선택자 선택자|header h1|
<table> CSS3 선택자 종류
  <th>종류</th><th>형태</th><th>사용 예</th>
  <tr><td>전체 선택자</td><td>*</td><td>*</td></tr>
  <tr><td>태그 선택자</td><td>태그</td><td>h1</td></tr>
  <tr><td>아이디 선택자</td><td>#아이디</td><td>#id</td></tr>
  <tr><td>클래스 선택자</td><td>.클래스</td><td>.header</td></tr>
  <tr><td rowspan=6>속성 선택자</td><td>선택자[속성 = 값]</td><td>input [type = text]</td></tr>
  <tr><td>선택자[속성 ~= 값]</td><td>div[data-role ~=row]</td></tr>
  <tr><td>선택자[속성 := 값]</td><td>div[data-role :=row]</td></tr>
  <tr><td>선택자[속성 ^= 값]</td><td>div[data-role ^=row]</td></tr>
  <tr><td>선택자[속성 $= 값]</td><td>div[data-role $=9]</td></tr>
  <tr><td>선택자[속성 *= 값]</td><td>div[data-role *=row]</td></tr>
  <tr><td>후손 선택자</td><td>선택자 선택자</td><td>header h1</td></tr>
  <tr><td>자손 선택자</td><td>선택자 > 선택자</td><td>header > h1</td></tr>
  <tr><td rowspan=2>반응 선택자</td><td>선택자:active</td><td>div:active</td></tr>
  <tr><td>선택자:hover</td><td>div:hover</td></tr>
  <tr><td rowspan=4>상태 선택자</td><td>선택자:checked</td><td>input:checked</td></tr>
  <tr><td>선택자:focus</td><td>input:focus</td></tr>
  <tr><td>선택자:enabled</td><td>input=enabled</td></tr>
  <tr><td>선택자:disabled</td><td>input=disabled</td></tr>
  <tr><td rowspan=8>구조 선택자</td><td>선택자:first-child</td><td>li:first-child</td></tr>
  <tr><td>선택자:last-child</td><td>li:last-child</td></tr>
  <tr><td>선택자:nth-child(수열)</td><td>li:nth-child(2n+1)</td></tr><tr><td>선택자:nth-last-child(수열)</td><td>li:nth-last-child(2n+1)</td></tr><tr><td>선택자:first-of-type</td><td>h1:first-of-type</td></tr><tr><td>선택자:last-of-type</td><td>h1:last-of-type</td></tr><tr><td>선택자:nth-of-type(수열)</td><td>h1:nth-of-type(2n+1)</td></tr><tr><td>선택자:nth-last-of-type</td><td>h1:nth-last-of-type(2n+1)</td></tr>
  <tr><td rowspan=2>동위 선택자</td><td>선택자+선택자</td><td>h1+div</td></tr>
  <tr><td>선택자~선택자</td><td>h1~div</td></tr>
  <tr><td rowspan=2>링크 선택자</td><td>선택자:링크</td><td>a:link</td></tr>
  <tr><td>선택자:visited</td><td>a:visited</td></tr>
  <tr><td rowspan=5>문자 선택자</td><td>선택자:first-letter</td><td>p::first-letter</td></tr>
  <tr><td>선택자:first-line</td><td>p::first-line</td></tr>
  <tr><td>선택자:after</td><td>p::after</td></tr>
  <tr><td>선택자:before</td><td>p::before</td></tr>
  <tr><td>선택자:selection</td><td>p::selection</td></tr>
   <tr><td>부정 선택자</td><td>선택자:not(선택자)</td><td>li:not(.item)</td></tr>
</table>

## 기본 선택자

<table>기본 선택자</table>

|종류|형태|설명|
|---|---|---|
|전체 선택자|*|HTML 페이지 내부의 태그를 모두 선택|
|태그 선택자|태그|HTML 페이지 내부의 특정 태그를 모두 선택|
|아이디 선택자|#아이디|특정 id 속성이 있는 태그 선택, 웹 표준에 id 속성은 웹 페이지 내부에서 중복되면 안 된다는 규정이 있으므로 아이디 선택자는 특정 태그 하나를 선택할 때 사용|
|클래스 선택자|.클래스|특정 클래스가 있는 태그 선택|

### 전체 선택자와 태그 선택자
1. 전체 선택자 적용하기
2. 태그 선택자 적용하기
   - 선택자 여러 개에 속성 적용하기: 쉼표 사용
ex)

```html
<style>
body,p,h1,h2,h3,h4,h5,h6{margin:0;padding:0;}
</style>
```
### 아이디 선택자
### 클래스 선택자
1. 클래스 사용자를 1개 사용하기
2. 클래스 선택자를 여러 개 사용하기

## 속성 선택자
- 속성 선택자
     <table>속성 선택자</table>
|형태|설명|
|---|---|
|선택자[속성]|특정한 속성이 있는 태그 선택|
|선택자[속성=값]|특정한 속성 내부 값이 특정 값과 같은 태그 선택

### 속성 선택자

## 후손 선택자와 자손 선택자
### 후손 선택자
|형태|설명|
|---|---|
|선택자 A 선택자 B|선택자A의 후손인 선택지 B 선택|
- 후손 선택자 여러개를 함께 사용할 경우 주의 사항
- 1) `<header>`태그의 후손인 `<h1>`태그와 일반적인 `<h2>` 태그 선택

```html
<style>
    #header h1,h2{color:red;}
</style>
```
- 2)`<header>`태그의 후손인 `<h1>`태그와 `<header>`태그의 `<h2>` 태그 선택
```html
<style>
    #header h1,#header h2{color:red;}
</style>
```

### 자손 선택자

<table>자손 선택자</table>

|형태|설명|
|---|---|
|선택자A > 선택자 B|선택자 A의 자손인 선택지 B 선택|
- `<table>` 태그 요소 선택할 때 자손 선택자 주의사항
#### 검사를 통한 HTML 페이지의 계층 구조
- 웹 브우저가 `<tbody>` 태그를 자동으로 추가하므로 스타일 속성이 적용되지 않음.
- table 태그에 스타일을 적용할 때에는 자손 선택자를 사용하지 않음

## 반응 ,상태 , 구조 선택자
### 반응 선택자

<table>반응 선택자</table>

|형태|설명|
|---|---|
|:active|사용자가 마우스로 클릭한 태그 선택|
|:hover|사용자가 마우스 커서를 올린 태그 선택| 

### 상태 선택자

<table>상태 선택자</table>

|형태|설명|
|---|---|
|:checked|체크 상태의 input 태그 선택 type 속성이 checkbox 또는 radio인 input 태그가 선택된 상태|
|:focus|포커스를 맞춘 input 태그 선택, 사용자가 바로 입력할 수 있도록 입력 양식에 포커스를 둔 상태, 웹 페이지 하나당 input 태그 하나에만 포커스를 둘 수 있음| 
|:enabled|사용 가능한 태그 선택, input 태그에 값을 입력할 수 있는 상태| 
|:disabled|사용 불가능한 태그 선택,input 태그에 값을 입력할 수 없는 상태| 

### 구조 선택자

<table>구조 선택자</table>

|형태|설명|
|---|---|
|:first-child|형제 관계에서 첫 번째로 등장하는 태그 선택|
|:last-child|형제 관계에서 마지막으로 등장하는 태그 선택| 
|:nth-child(수열)|형제 관계에서 앞에서 수열 번째로 등장하는 태그 선택| 
|:nth-last-child(수열)|형제 관계에서 뒤에서 수열 번째로 등장하는 태그 선택| 

- nth-child와 nth-last-child 선택자
- 2n+1 수열에 0부터 숫자를 넣을 경우 "1,3,5,7,9..."
- 구조 선택자는 수열의  결과 값에 해당하는 위치에 있는 태그에 스타일을 적용
  
- 구조 선택자 사용 시 주의 사항
  - 수열을 지정해주지 않으면 모든 항목이 스타일이 적용됨

## CSS3 단위
### 키워드 단위
 - W3C에서 미리 정의한 단어
 - 키워드를 입력하면 해당하는 스타일이 자동으로 적용
### 크기 단위

<table>크기 단위</table>

|단위|설명|
|---|---|
|%|백분율 단위|
|em|배수 단위|
|px|픽셀 단위|
#### 다양한 크기의 단위 적용
1. HTML 페이지 만들기
2. % 단위 적용하기
 - % 단위는 기본으로 설정된 크기를 기준으로 상대적인 크기를 지정.
 - 초기 설정 크기:100%
3. em 단위 적용하기
   - 1배 = 1em = 100%
   - 1.5배 = 1.5em = 150%
   - 초기 설정 크기: 100%
4. px 단위 적용하기
   - 크기를 절대적으로 지정

### 색상 단위
<table> 색상 단위
    <tr>
        <th rowspan="3">RGB색상</th><td>형태</td><td>rgb(red,green,blue)</td>
        <tr><td>설명</td><td>R(빨간색)과 G(초록색)와 B(파란색)을 조합해 색상을 표현하며, 0부터 255 사이의 숫자를 입력합니다.</td></tr>
        <tr><td>예</td>
        <td>

```html
        <style>
            h1{ background-color:rgb(255,255,255);}
        </style>
```
</td></tr>
<th rowspan="3">RGBA색상</th><td>형태</td><td>rgba(red,green,blue,alpha)</td>
        <tr><td>설명</td><td>RGB 색상 단위에 알파 값을 추가한 형태입니다. 알파 값은 투명도를 나타내며, 0.0부터 1.0사이의 숫자를 입력합니다. 0.0은 완전 투명 상태고, 1.0은 완전 불투명 상태입니다.</td></tr>
        <tr><td>예</td>
        <td>

```html
        <style>
            h1{ background-color:rgbㅁ(255,255,255,0.5);}
        </style>
```
</td></tr>
<th rowspan="3">HEX코드</th><td>형태</td><td>rgb(red,green,blue)</td>
        <tr><td>설명</td><td>RGB 색상 단위를 짧게 입력하는 방법으로 RGB 색상 조합을 #000000같은 16진수로 입력합니다.</td></tr>
        <tr><td>예</td>
        <td>

```html
        <style>
            h1{ background-color:#0094FF;}
        </style>
```
</td></tr>
</tr>
</table>

- 색상 선택 도구
  - 색상 선택 프로그램 예(http://www.colorpicker.com/)

### URL단위
- 이미지나 글꼴 파일을 불러올 때 사용
- url('경로')