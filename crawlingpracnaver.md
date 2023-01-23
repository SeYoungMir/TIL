#### 네이버 메뉴바 및 뉴스 크롤링

- 네이버 메뉴 바 크롤링

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://www.naver.com/"
html=urlopen(url)
soup_n = BeautifulSoup(html,"html.parser")
nav_list=soup_n.select('li.nav_item')

# 메뉴바 리스트 뽑아내기
nav_list

# 메뉴바에서 메뉴와 링크 뽑아내기
for nav in nav_list:
    print(nav.find('a').text,":",nav.find('a')['href'])

#위의 내용을 데이터프레임으로 받아 저장하기
menu=[]
url=[]
for nav in nav_list:
    nav_tag=nav.find('a')
    menu.append(nav_tag.text)
    url.append(nav_tag['href'])
import pandas as pd
df = pd.DataFrame({'메뉴':menu,"URL":url})
df

df.to_csv('c:\\Myexam\\naver_menu.csv',encoding='euc-kr') #cp949, utp-8

```

#### 네이버 뉴스 크롤링
##### 네이버 뉴스는 네이버 정책에 따라 모든 언론사들의 뉴스가 랜덤하게 배치됨
- 단 로그인 후 구독을 추가하면 구독한 언론사들의 뉴스가 나옴
- 헤드라인 뉴스는 표면적으로는 제공되지 않는다.

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://news.naver.com/"
html=urlopen(url)


#html #<http.client.HTTPResponse at 0x1b5fa0cd0d0>
#html_text = html.read() #바이너리 문자열로 반환
# # html_text



#IT 과학 분야 기사 제목 리스트 받아오는 함수
from selenium import webdriver
from selenium.webdriver.common.by import By
article_list = []
def get_article(page):
    driver = webdriver.Chrome()
    driver.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105#&date=%2000:00:00&page=" + str(page))
    articles = driver.find_elements(By.CSS_SELECTOR,'#section_body li')
    for article in articles:
         title = article.find_element(By.CSS_SELECTOR,'dt:not(.photo) > a').text
         article_list.append(title)
    print("end :", page)
    driver.quit()
# 1페이지부터 4페이지까지 크롤링
%%time
for page in range(1, 5):
    get_article(page)

# 출력
 len(article_list), article_list[:30]


#동일한 값을 판다스 데이터프레임으로 받기

import threading
import pandas as pd
df = pd.DataFrame(columns=["title"])
# 함수 선언
def get_article(page):
    driver = webdriver.Chrome()
    driver.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105#&date=%2000:00:00&page=" + str(page))
    articles = driver.find_elements(By.CSS_SELECTOR,'#section_body li')
    for article in articles:
         title = article.find_element(By.CSS_SELECTOR,'dt:not(.photo) > a').text
         df.loc[len(df)]={"title":title,}
    print("end :", page)
    driver.quit()


#페이지 크롤링
%%time
for page in range(1, 5):
    get_article(page)

# 출력
df.tail()
df.head()
```