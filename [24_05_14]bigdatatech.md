# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 4. 태그 클라우드 생성
#### 1. 텍스트를 기반으로  태그 클라우드 생성
   - 신문의 내용을 스크레이핑, 기반으로 태그 클라우드 생성.
1. KoNLPy 설치
   - 영어 텍스트는 띄어쓰기로 단어를 끊어서 사용, 한국어는 단어 뒤에 조사가 붙기 때문에 띄어쓰기만으로만 구분해서 사용하는 것은 힘듦. 따라서 한국어 형태소 분석 라이브러리인 KoNLPy를 사용.
2. word_cloud,BeautifulSoup,Pilow,requests,lxml설치
   - 태그 클라우드를 만들 때 사용하는 word_cloud 라이브러리를 설치. 스크레이핑을 위한 BeautifulSoup도 설치. 이미지 출력을 위한 Pillow도 설치, HTTP 라이브러리인 requests와 XML(HTML)라이브러리인 lxml 설치
     - word_cloud[[URL](https://github.com/amueller/word_cloud)]
     - BeautifulSoup[[URL](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)]
     - Pillow[[URL](https://github.com/python-pillow/Pillow)]
     - lxml[[URL](http://lxml.de/)]
     - Requests[[URL](http://docs.python-requests.org/en/master/)]
   - requests,beautifulsoup(버전 4),lxml,wordcloud,pillow를 pip install 명령어로 설치
   - ```cmd
     $ pip install requests beautifulsoup4 lxml wordcloud pillow
     ```
3. 주피터(Jupyter) 설치
   - 출력 결과를 보기 쉽게 주피터를 사용, 주피터는 코드를 포함하는 문서를 작성할 수 있게 해주며, 문서 내부에서 실제로 코드를 실행해서 볼 수 있게 해 주는 도구.
     - 주피터(Jupyter)[[URL](https://jupyter.org/)]
   - 주피터를 pip install 명령어로 설치
     - ```cmd
       $ pip install jupyter
       ```
4. 주피터 서버 실행
   - 다음 명령어로 주피터 서버를 실행
   - ```cmd
     $ jupyter notebook
     ```
5. 신규 문서 만들고 실행
   - 브라우저에서 http://localhost:8888/tree 페이지 오픈
   - 페이지 오른쪽 위에 있는 [New]-[Python 3]을 선택해 새로운 문서 생성.
