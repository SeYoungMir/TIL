## 모듈 import
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np
import pymysql
```
## pymysql 연결
```python

db=pymysql.connect(host='localhost',port=3306,user='root',passwd='pswd',charset='utf8')
cursor=db.cursor()

```

## 현재 데이터베이스 확인
```python
sql="show databases"
cursor.execute(sql)
result=cursor.fetchall()
result
```

## 데이터베이스 생성 및 확인
```python
sql = "use db_pri"
cursor.execute(sql)

sql = "select database()"
cursor.execute(sql)
result = cursor.fetchone()
result
```
## table 생성 및 확인
```python
sql = '''
 CREATE TABLE product (
 PRODUCT_CODE int AUTO_INCREMENT NOT NULL,
 TITLE VARCHAR(200) NOT NULL,
 ORI_PRICE VARCHAR(100),
 DISCOUNT_PRICE VARCHAR(100),
 link VARCHAR(200),
 PRIMARY KEY(PRODUCT_CODE)
 );
 '''
cursor.execute(sql)
db.commit()

sql = "show tables"
cursor.execute(sql)
result = cursor.fetchall()
result

sql = 'desc product'
cursor.execute(sql)
result = cursor.fetchall()
result

```
## 크롤링을 위한 url 생성
```python

url_list=[]
for page in range(1,2):
    url_list.append('https://jolse.com/category/toners-mists/1019/?page='+str(page))
print(url_list)
```

## 원하는 내용 긁어오는 코드 작성 및 데이터 넣는 sql문 작성하는 코드 작성
```python
url=url_list[0]
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
beauty_list = soup.select('ul.prdList.grid5 li div.description')

for beauty in beauty_list:
    name=beauty.select('a span')[2].get_text()
    link=beauty.find("strong",{"class":"name"}).find("a")
    sub_link= 'https://jolse.com'+link["href"]
    oprice=beauty.select('ul li')[0].select("span")[1].text
    dprice=beauty.select('ul li')[1].select("span")[1].text
    sql_inner=f'"{name}","{oprice}","{dprice}","{sub_link}"'
    sql= f'"INSERT INTO product (title,ori_price,discount_price,link) values({sql_inner});"'
    print(sql)
    #cursor.execute(sql)
```
- 이 경우 fstring이인식되지 않는 문제 발생. 다른 방법을 찾아보자.