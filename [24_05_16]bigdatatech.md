# 7. 크롤러로 수집한 데이터 사용
## 3. 장고(Django)로 웹 API 생성.
### 4. 태그 클라우드 생성
#### 1. 텍스트를 기반으로  태그 클라우드 생성
5. 신규 문서 만들고 실행 - 이어서
   - 문서 내부에 다음 코드 입력
   - ```python
     import requests
     from konlpy.tag import Ok
     from bs4 import BeautiifulSoup
     from wordcloud import WordCloud

     # HTML 추출하기 : 운수 좋은 날 텍스트
     url = 'https://raw.githubusercontent.com/rintiantta/raw_files/master/crawl-cloud-sample.txt'
     r = requestss.get(url, timeout= 10)

     # 텍스트 추출
     text= r.text
     
     # 형태소 분석
     okt = Okt()
     words = []
     for line in text.split("\n"):
        words.extend(okt.nouns(line))
    
     # wordcloud 객체 생성
     # 한국어 출력 가능한 폰트 지정
     font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
     wordcloud = WordCloud(background_color="white",font_path=font_path)
     .generate(" ".join(words))

     # 그래프 생성
     import matplotlib.pyplot as plt
     plt.imshow(wordcloud, interpolation= 'bilinear')
     plt.axis("off")
     plt.show()
     ```