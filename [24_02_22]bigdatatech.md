# 4. 스크레이핑 기본
## 4. 데이터를 데이터베이스에 저장, 분석
### 4. 파이썬에서 MySQL에 접속하기
9. 분석한 결과 저장
   - 다음과 같은 처리 추가
   ```python
   import feedparser
   import MySQLdb
   
   #URL 지정, FeedParserDict 객체 생성
   rss= feedparser.parse("<URL 링크>")
   
   # RSS 버전 확인
   print(rss.version)

   # 피드의 제목
   print(rss["feed"]["title"])

   # 반복 적용
   for content in rss["entries"]:
        #데이터 저장
        cursor.execute("INSERT INTO books VALUES(%s,%s)",("책 제목","링크"))
    #이후 커밋과 연결 종료
   ```
10. 셸에서 스크립트 실행
    ```python
    python example.py
    ```
    - 오류없이 정상적으로 실행 완료 시 테이블 내용 확인
# 5. 크롤러 설계/개발(응용)
## 1. 크롤러 발전
### 1. 크롤링 개발에서 직면할 수 있는 문제와 해결 방법
- 크롤러 문제 예시
  - 소요 시간이 긴 경우
  - 버그 등으로 동작 이상 시 알아차릴 수 없음
- 개발 과정에서 비기능적 요구사항(non-functional requirement)이라는 목적 이외의 거을 구현해야 하는 경우 많음
- 대부분의 경우 프로그램 개발은 계속 유지, 과정에서 효율적 동작과 문제 해결을 위한 유지보수와 운용 필요