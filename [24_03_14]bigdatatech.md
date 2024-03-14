# 6. 스크레이핑 개발(응용)
## 4. CSV로 변환
### 1. CSV 사용하기
- CSV는 스프레드시트 애플리케이션에서도 읽어 들일 수 있으며, 굉장히 많이 사용되는 데이터 형식
- 값을 쉼표로 구분하기만 하면 CSV 파일을 만들 수 있을 것 같지만, 다룰 때 여러 가지 주의 사항을 기억해야 함
- 좋지않은 CSV의 예
```csv
id,title,url,publisher_id,publisher_name,language_id,language_name
71051687,파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발, 1, 위키북스, 1, 한국어
34973284,HTML5 웹 프로그래밍 입문, 2, 한빛미디어,1,한국어
```
- 위 CSV를 프로그램에서 읽어들이면 각 줄을 쉼표로 자르고 요소 추출
- 값 내부에 쉼표가 있다면 요소의 수 자체가 달라짐. 따라서 CSV는 각각의 값을 큰따옴표로 감싸는 것이 일반적, 큰따옴표로 가싸면 값 내부에 쉼표가 포함되어 있어도 구분 가능
- 값 네부에 큰 따옴표가 있다면 큰따옴표를 두번 입력, 이스케이프 처리
- CSV의 기술 사양은 RFC(Request for Comments, 기술 사양의 공개 형식)로 정의,세부적인 사항에 대해서는 CSV를 다루는 프로그램이 임의로 구현할 수 있게 되어 있음.
- 다음과 같은 부분 주의
  - 문자 코드 : EUC-KR인지 UTF-8인지
  - 줄바꿈 문자 :EUC-KR이라면 CRLF, UNIX 형식이라면 LF
  - 구분 기호(Delimiter): 쉼표가 일반적이지만, 세미콜론 또는 하이픈(|)을 사용하는 경우도 있음
  - 이스케이프 : 역슬래시로 이스케이프 처리하는 경우도 있음
1. CSV 모듈 사용
   - 단순한 형식이라고 얕보고 직접 대충 구현 X, XML 또는 JSON처럼 라이브러리를 사용하도록 함. 파이썬은 csv모듈을 표준으로 제공
   ```python
   """DB의 내용을 다양한 형식으로 출력"""
   import csv
   import io
   ### JSON과 동일 부분 생략

    def create_csv():
    """CSV 만들기"""
        output=io.StringIO()
        csv_writer=csv.writer(output,delimiter=','quotechar='"',quoting=csv.QUOTE_ALL)
        header = ["id","title","url","publisher_id","publisher_name","lanuage_id","language_name"]
        cwv_writer.writerow(header)
        publisher=Publisher.all()
        publisher.load('books','books.lanuage') # Eager Loading
        for publisher in publisher:
            for book in publisher.books:
                line=[
                    book.id,
                    book.title,
                    book.publisher.id,
                    book.publisher.name,
                    book.language.id,
                    book.language.name,
                ]
                csv_writer.writerow(line)
            return output.getvalue()
    # main 실행 블록
    if __name__=='__main__':
        csv_str=create_csv()
        print(csv_str)
   ```
   - 출력 학습 내용 기반, XML,CSV,JSON으로 출력하는 기능이 있는 크롤러 프레임워크인 Scrapy 살펴봄.