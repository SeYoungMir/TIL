## 유튜브 랭크 사이트 크롤링
- 모듈 import 
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
```
- 페이지 URL 생성
```python
url_list=[]
for page in range(1,11):
    url_list.append('https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page='+str(page))
print(url_list)
```
- 빈 객체 생성
```python
url_list=[]
t_list=[]
c_list=[]
s_list=[]
view_list=[]
video_list=[]
rank=0
rank_list=[]
```
- 크롤링
```python
for page in range(1,11):
    url_list.append('https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page='+str(page))
for url in url_list:
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    channel_list = soup.select('form > table > tbody > tr')
    
    for channel in channel_list:
        category = channel.select('p.category')[0].text.strip()
        title = channel.select('h1 > a')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text.replace('만','0000')
        view = channel.select('.view_cnt')[0].text.replace('만','0000').replace('억','')
        video = channel.select('.video_cnt')[0].text.replace('개','').replace(',','')
        rank=rank+1
        rank_list.append(rank)
        t_list.append(title)
        c_list.append(category)
        s_list.append(subscriber)
        view_list.append(view)
        video_list.append(video)
```
- 데이터프레임 생성
```python
df = pd.DataFrame({'rank':rank_list,'title':t_list,"category":c_list,"subscriber":s_list,"view":view_list,"video":video_list})
```
- 데이터 타입 변경
```python
df = df.astype({'subscriber':'float'})
df = df.astype({'view':'float'})
df = df.astype({'video':'float'})
```
- 엑셀로 저장
```python
df.to_excel('c:\\Myexam\\naver_menu.xlsx',encoding='euc-kr',index=False)
```

- 시각화
```python
import matplotlib.font_manager as fm  # 폰트확인 

plt.rcParams['font.family'] = 'Malgun Gothic'

result= df.groupby('category')['subscriber'].sum().reset_index()
result.set_index('category',inplace=True)
result=result.sort_values('subscriber')


pplot=result.plot.pie(y='subscriber',autopct='%.1f%%',figsize=(30,30))
plt.savefig('c:\\Myexam\\test2.png',dpi=600)
plt.show()
```
- 시각화 2
```python
result= df.groupby('category')['view'].sum().reset_index()
result.set_index('category',inplace=True)
result=result.sort_values('view')


pplot=result.plot.pie(y='view',autopct='%.1f%%',figsize=(30,30))
plt.savefig('c:\\Myexam\\test2.png',dpi=600)
plt.show()
```