# 6. 스크레이핑 개발(응용)
## 7. 데이터베이스에 저장
### 1. 데이터베이스에 아이템 저장
3. ITEM_PIPELINES 작성
   - my_project/my_project/settings.py의 ITEM_PIPELINES를 다음처럼 작성
   - ```python
     ITEM_PIPELINES={
        'my_project.pipelines.DatabasePipeline':300,
     }
     ```
   - 300은 여러 개의 pipeline을 사용할 때의 우선 순위를 나타냄. 예제에서는 pipeline을 하나만 사용하므로 아무렇게나 지정해도 OK
4. 데이터베이스의 연결 정보 추가 
   - my_project/my_project/settings.py에 데이터베이스 연결 정보를 추가
   - ```python
     DEPTH_LIMIT = 1
     ORATOR_CONFIG = {
        'mysql': {
            'driver':'mysql',
            'host' : 'localhost',
            'database' : 'quotes',
            'user':'root',
            'password':'',
            'prefix':'',
            'log_queries': True,
        }
     }
     ```
5. 데이터베이스의 내용 확인
   - 다음 명령어를 실행, 데이터베이스의 내용 핫인.
   - 데이터베이스의 내용은 실행 시점에 따라 조금씩 다를 수 있음.
   - ```sql
     $ scrapy crwal quotes
     $ mysql -u root quotes

     mysql> select id, author, text from quotes;

     mysql> select id, name from tags;

     mysql> select id, quote_id, tag_id from quotes_tags; 
     ```