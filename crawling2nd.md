## HTML5 기본 태그
### 1. 글자 태그
- 페이지에서는 글자 태그가 비중이 큼
#### 제목과 본문 글자 태그
- 제목 글자 태그
  - 문서의 제목을 표현할 때 사용
  - h 는 Heading을 의미
  - h1~h6 제목 글자 생성,크기 조절
- 본문 글자 태그 및 단락 구분
  - p, 본문 문단 생성
  - br 줄바꿈
  - hr 수평 줄 삽입
- 앵커 태그
  - 하이퍼텍스트:사용자의 선택에 따라 특정 정보로 이동하는 조직된 문서
  - a 태그(Anchor):다른 웹 페이지나 웹 페이지 내부의 특정 위치로 이동
  - Href : Hyper Reference를 의미
  - 앵커 태그
  
  |태그|설명|
  |---|---|
  |a|하이퍼링크 생성|
  - ex) `<a href="http://~ ">출력글자</a>`
  - a 태그의 href 속성
    1) 절대 경로
     -  http: // ~ 메인 페이지
     -  /animal.jpg 현재 사이트 최상위 위치의 animal.jpg 파일
    2) 상대 경로
       - animal.jpg 웹페이지가 있는 폴더의 animal.jpg 파일
       - imahe/animal.jpg 웹 페이지가 있는 폴더에 포함된 image 폴더의 animal.jpg 파일
       - ../animal.jpg 웹페이지가 있는 폴더의 상위 폴더에 있는 animal.jpg 파일
    3) 아이디 경로
        - #name - id 속성이 name인 태그의 위치로 이동
    4) 메일 경로
        - mailto: `hanb@hanbit.co.kr`  -해당 주소로 메일 전송
- 글자 모양 태그

|태그|설명|
|---|---|
|b|굵은 글자 <small>bold |
|i|기울어진 글자<small>italic|
|small|작은 글자
|sub|아래 첨자<small>subscript|
|sup|위 첨자<small>superscript|
|ins|밑줄 글자<small>insert|
|del|취소선이 그어진 글자<small>delete|
- 내비게이션 메뉴
  - 웹 사이트의 다른 웹 페이지로 이동할 수 있는 버튼
  - 내비게이션 메뉴를 만들기 위해 주로 사용되는 목록 태그
   - 목록 태그
  
|태그|설명|
|---|---|
|ul|순서가 없는 목록 <small>unordered list</small> 생성|
|ol|순서가 있는 목록 <small>ordered list</small> 생성|
|li|목록 요소<small>list item</small> 생성|

- 테이블 태그
 
|태그|설명|
|---|---|
|table|표 삽입|
|tr|표에 행<small>table row</small> 삽입|
|th|표의 제목 셀<small>table heading</small> 생성|
|td|표의 일반 셀<small>table data</small> 생성|

  - 테이블 태그의 속성

<table>
  <th>태그</th><th>속성</th><th>설명</th>
  <tr><td>table</td><td>border</td><td>표의 테두리 두께 지정</td></tr>
  <tr><td rowspan="2">th,td</td><td>colspan</td><td>셀의 너비 지정</td></tr>
 <tr><td>rowspan</td><td>셀의 높이지정</td></tr>
</table>
- 미디어 태그
  - 이미지, 오디오, 비디오 등 멀티미디어를 넣을 때 사용
- 미디어 태그 구분

|내용물을 가질 수 있는 태그|내용물을 가질 수 없는 태그|
|---|---|
|`<audio></audio>`<br>`<video></video>`|`<img>`|

  - 미디어 태그 속성
    - 이미지, 오디오, 비디오에 필요한 추가 정보는 속성을 사용
  <table>
  <th>태그</th><th>속성</th><th>설명</th>
 <tr> <td rowspan="4">img태그</th><td>src</td><td>이미지의 경로 지정<td></tr>
 <tr><td>alt</td><td>이미지가 없을 때 나오는 글자 지정</td></tr>
  <tr><td>width</td><td>이미지의 너비 지정</td></tr>
   <tr><td>height</td><td>이미지의 높이 지정</td></tr>
   <tr> <td rowspan="5">audio,video태그</th><td>src</td><td>음악, 비디오 파일의 경로 지정<td></tr>
<tr><td>preload</td><td>음악, 비디오를 준비중일 때 데이터를 모두 불러올 지 여부 지정</td></tr>
  <tr><td>autoplay</td><td>음악, 비디오의 자동 재생 여부 지정</td></tr>
  <tr><td>loops</td><td>음악, 비디오의 반복 여부 지정</td></tr>
  <tr><td>controls</td><td>음악, 비디오 재생 도구 출력 여부 지정</td></tr>
  <tr> <td rowspan="2">video태그</th><td>width</td><td> 비디오 의 너비 지정<td></tr>
  <tr><td>height</td><td>비디오의 높이 지정</td></tr>
  </table>

- 멀티미디어 (이미지, 오디오, 비디오) 삽입
  - 1.이미지 삽입하기
    - 이미지 파일 준비: 준비 파일(이미지.jpg)을 HTML 페이지와 같은 폴더에 넣기.
    - 혹은 웹의 이미지 경로 넣기 (src옵션) 
  - 2. 음악 삽입하기
    - 음악 파일 준비: 준비 파일(오디오.mp3)을 HTML 페이지와 같은 폴더에 넣기
  - 3. 웹 브라우저 제약이 없도록 음악 삽입하기.
    - `<source>` 태그
      - 웹 브라우저마다 지원하는 음악 파일 확장자가 다른 문제 해결
      - `<audio>`태그나 `<video>` 태그 내부에 입력
    - ogg 파일 준비:.ogg 확장자 파일을 HTML 페이지와 같은 폴더에 넣기.
  - 4. 동영상 삽입하기
    - 동영상 파일 준비: 준비 파일(동영상.mp4,동영상.webm)을 HTML 페이지와 같은 폴더에 넣기.
  - 5. 동영상을 불러오는 동안 다른 이미지 보여 주기
    - poster 속성
      - `<video>`태그의 속성
      - 동영상을 불러오는 동안 사용자에게 보여 줄 이미지를 지정
      - 이미지 경로 입력
  - (예시)
  ```html
  <body>
    <video controls="controls" poster="http://placehold.it/640x360">
        <source src="Wildlife.mp4" type= "video/mp4">
        <source src="Wildlife.webm" type= "video/webm">
    </video>
  </body>
  ```
## 입력 양식 태그
- 입력 양식
  -  사용자에게 정보를 입력받는 요소
- 입력 양식 개요
  - `<form>` 태그: 영역 생성
```html
<body>
  <form>
    <input type="text" name="search">
    <input type="submit">
  </form>
</body>
```

### 데이터 전달 방식

- `<form>`태그는 method 속성의 방식으로 action 속성 장소에 데이터 전달
```html
<form action="전송 위치" method ="전송 방식">
</form>
```
- 전송 방식
  - GET: 주소에 데이터를 직접 입력해 전달
  - POST:별도의 방법을 사용해 데이터를 해당 주소로 전달 
- 전송 위치
  - 데이터를 전달할 목적지

### 입력 양식 종류
<table>
  <th>태그</th><th>속성</th><th>모양</th><th>설명</th>
  <tr><td>form</td><td>보이지 않음</td><td> </td><td>입력 양식의 시작과 끝 표시</td>
  <tr><td rowspan="10">input</td><td>text</td><td><input type=text name= "text" value="text"></td><td>글자 입력 양식 생성</td></tr>
  <tr><td>button</td><td><input type=button value="button"></td><td>버튼 생성</td></tr>
  <tr><td>checkbox</td><td><input type=checkbox></td><td>체크 박스 생성</td></tr>
  <tr><td>file</td><td><input type=file ></td><td>파일 입력 양식 생성</td></tr>
  <tr><td>hidden</td><td><input type=hidden></td><td>해당 내용 표시 안 함</td></tr>  
  <tr><td>image</td><td><input type=image src="http://placehold.it/100x100"></td><td>이미지 형태 생성</td></tr>
  <tr><td>password</td><td><input type=password name= "password" value= "password"></td><td>비밀번호 입력 양식 생성</td></tr>
  <tr><td>radio</td><td><input type=radio></td><td>라디오 버튼생성</td></tr>
  <tr><td>reset</td><td><input type=reset></td><td>초기화 버튼생성</td></tr>
  <tr><td>submit</td><td><input type=submit></td><td>제출 버튼생성</td></tr>
  <tr><td>textarea</td><td>cols/rows</td><td><textarea rows="2"></textarea> </td><td>여러 행의 글자 입력 양식 생성, cols는 너비를 지정하고 rows는 높이를 지정</td></tr>
  <tr><td>select<br>optgroup<br>option</td><td></td><td><select></select></td><td>선택 양식 생성<br>옵션 그룹화<br>옵션 생성</td></tr>
  <tr><td>fieldset<br>legend</td><td></td><td><fieldset></fieldset></td><td>입력 양식의 그룹 지정<br>입력 양식 그룹의 이름 지정</td></tr>
</table>

### 기본 입력 양식 태그
- `<input>` 태그의 type 속성을 이용해 다양한 기본 입력 양식 생성
### 간단한 입력 양식 생성
- 라디오 버튼의 name 속성을 이용해 여러 대상 중 하나만 선택하는 형태.
```html
<body>
  <form>
    <table>
      <tr>
        <td><label for="username">이름</label></td>
        <td><input id="username" type="text" name="username"></td>
      </tr>
      <tr>
        <td>성별</td>
         <td>
            <input id="man" type="radio" name="gender" value= "m"><label for="man">남자</label>
            <input id="woman" type="radio" name="gender" value= "m"><label for="woman">여자</label>
          </td>
       </tr>
      </table>
    <input type="submit" value="가입">
  </form>
</body>
```
<body>
  <form>
    <table>
      <tr>
        <td><label for="username">이름</label></td>
        <td><input id="username" type="text" name="username"></td>
      </tr>
      <tr>
        <td>성별</td>
         <td>
            <input id="man" type="radio" name="gender" value= "m"><label for="man">남자</label>
            <input id="woman" type="radio" name="gender" value= "m"><label for="woman">여자</label>
          </td>
       </tr>
      </table>
    <input type="submit" value="가입">
  </form>
</body>

### 선택 가능한 입력 양식
  1. 한 항목만 선택하기 : `<select>`태그 이용
    - 목록으로 보여 주는 항목 중 하나 또는 여러 개를 선택할 때 사용
    - 기본적으로 하나만 선택 가능
    - `<optgroup>`,`<option>` 태그를 함께 사용
  <table>form_selectBasic.html</table>

```html
<body>
  <select>
    <option>김밥</option>
    <option>떡볶이</option>
    <option>순대</option>
    <option>어묵</option>
  </select>
</body>
```
<body>
  <select>
    <option>김밥</option>
    <option>떡볶이</option>
    <option>순대</option>
    <option>어묵</option>
  </select>
</body>

  2. 여러 항목 선택하기: `<select>`태그의 multiple 속성 사용
<table>form_selectMulti.html</table>
```html
<body>
  <select multiple="multiple">
    <option>김밥</option>
    <option>떡볶이</option>
    <option>순대</option>
    <option>어묵</option>
  </select>
</body>
```
<body>
  <select multiple="multiple">
    <option>김밥</option>
    <option>떡볶이</option>
    <option>순대</option>
    <option>어묵</option>
  </select>
</body>

  3. 선택 옵션 묶기: `<optgroup>`태그 사용
<table>form_selectGroup.html</table>

```html
<body>
  <select>
    <optgroup label="HTML5">
      <option>Multimedia Tag</option>
      <option>Connectivity</option>
      <option>Device Access</option>
    </optgroup>
    <optgroup label="CSS3">
      <option>Animation</option>
      <option>3D Transform</option>
    </optgroup>
  </select>
</body>
```

<body>
  <select>
    <optgroup label="HTML5">
      <option>Multimedia Tag</option>
      <option>Connectivity</option>
      <option>Device Access</option>
    </optgroup>
    <optgroup label="CSS3">
      <option>Animation</option>
      <option>3D Transform</option>
    </optgroup>
  </select>
</body>

### 연관 있는 입력 양식 그룹으로 묶기
- `<fieldset>`태그, `<legend>`태그
<table>form_group.html</table>

```html
<body>
  <form>
    <fieldset>
      <legend>입력 양식</legend>
      <table>
        <tr>
          <td><label for="name">이름</label></td>
          <td><input id="name" type="text"></td>
        </tr>
        <tr>
          <td><label for="mail">이메일</label></td>
          <td><input id="mail" type="email"></td>
        </tr>
      </table>
      <input type="submit">
    </fieldset>
  </form>
</body>
```

<body>
  <form>
    <fieldset>
      <legend>입력 양식</legend>
      <table>
        <tr>
          <td><label for="name">이름</label></td>
          <td><input id="name" type="text"></td>
        </tr>
        <tr>
          <td><label for="mail">이메일</label></td>
          <td><input id="mail" type="email"></td>
        </tr>
      </table>
      <input type="submit">
    </fieldset>
  </form>
</body>

### 공간 분할 태그
- CSS로 원하는 레이아웃을 구성하기 위해 공간 분할
#### HTML5의 대표적인 공간 분할 태그
- `<div>`태그, `<span>`태그
<table> 기본 공간 분할 태그
  <th>태그</th><th>설명</th>
  <tr><td>div</td><td>블록 형식으로 공간 분할</td></tr>
  <tr><td>span</td><td>인 라인 형식으로 공간 분할</td></tr>
</table>

#### 공간 분할 방법
1. 공간을 블록 형식으로 분할하기
  - div 사용
<table>space_block.html</table>

```html
<body>
  <div>div 태그 -block 형식</div>
  <div>div 태그 -block 형식</div>
  <div>div 태그 -block 형식</div>
  <div>div 태그 -block 형식</div>
  <div>div 태그 -block 형식</div>
</body>
```
1. 공간을 인라인 형식으로 분할하기
  - 자신의 글자 크기만큼 영역 차지
  - 왼쪽에서 오른쪽으로 쌓임
<table>space_inline.html</table>

```html
<body>
  <span>span 태그 - inline 형식</span>
  <span>span 태그 - inline 형식</span>
  <span>span 태그 - inline 형식</span>
  <span>span 태그 - inline 형식</span>
  <span>span 태그 - inline 형식</span>
</body>
```

#### 시맨틱 태그
  - 시맨틱 웹
    - 특정 태그에 의미를 부여한 웹
    - 프로그램이 코드를 읽고 의미를 인식할 수 있는 지능형 웹
  - 시맨틱 태그를 사용한 시맨틱 웹 구현
  
  |태그|설명|
  |---|---|
  |header|머리말(페이지 제목,페이지 소개)|
  |nav|하이퍼링크들을 모아 둔 내비게이션|
  |aside|본문 흐름에 벗어나는 노트나 팁|
  |section|문서의 장이나 절에 해당하는 내용|
  |article|본문과  독립적인 콘텐츠 영역|
  |footer|꼬리말(저자나 저작권 정보)|
 <table>HTML5 시맨틱 태그</table>
  
  - 시맨틱 태그를 이용한 레이아웃 구성
```html
<body>
  <header>
    <h1>HTML5 기본</h1>
  </header>
  <nav>
    <ul>
      <li><a href="#">메뉴 - 1</a></li>
      <li><a href="#">메뉴 - 2</a></li>
      <li><a href="#">메뉴 - 3</a></li>
    </ul>
  </nav>
  <section>
    <article>
      <h1>Lorem ipsum dolor sit amet</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </article>
    <article>
      <h1>Lorem ipsum dolor sit amet</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
    </article>
  </section>
  <footer>
    <address>서울특별시 강서구 내발산동</address>
  </footer>
</body> 
```