# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 4. 태그 클라우드 생성
#### 1. 텍스트를 기반으로  태그 클라우드 생성
5. 신규 문서 만들고 실행 - 이어서
   - url =  부분은 스크레이핑 대상 URL
   - r = 부분은 스크레이핑 대상 URL 에서 HTML 소스를 추출하는 부분
   - text = 부분부터는 KoNLPy의 Okt 형태소 분석기를 사용, 형태소 분석.
   - okt.nouns() 메서드 사용 시 명사만 추출 가능. 이렇게 추출한 명사들은 words 리스트에 넣어줌
   - font_path 부분에서는 .generate 부분에서 사용할 한국어 폰트 경로 지정. 지정하지 않으면 한국어 출력하지 못함. 운영체제에 맞게 알맞은 폰트 경로 입력.
   - .generate 부분에서는 WordCloud 클래스의 객체 생성. 여러 속성을 지정해서 색상과 폰트를 지정. words 리스트를 "".join() 메서드로 하나의 문자열로 합치고, generate() 메서드에 전달.
   - import 부분은 그래프를 그릴 수 있게 해 주는 matplotlib.pyplot 을 plt라는 별칭으로 읽어들임.
   - plt.imshow 메서드로 위에서 만든 wordcloud 객체를 그림. 바이리니어 보완은 이미지를 확대하거나 축소할 때 확대된 이미지를 매끄럽게  만들기 위해서 사용하는 알고리즘 중 하나. 보완 알고리즘은 이미지 처리와 관련된 전문적인 주제.
   - plt.axis 메서드로 그래프 축 출력 지정. off는 축 출력하지 않음.
   - plt.show 메서드로 주피터 노트북 위에 그래프 출력. 그래프 렌더링하는 matplotlib 라이브러리는 많은 기능 존재. 자세한 내용은 공식 문서 참고.
     - pyplot - Matplotlib 2.0.2 documentation[[URL](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.imshow)]
   - 메뉴에서 [Cell] > [Run Cells] 선택, 실행.
   - 이미지 출력. 출현 빈도가 높은 단어가 크게 출력. 태그 클라우드를 만들면 문서의 특징을 시각적으로 확인 가능.