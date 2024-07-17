# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 3. 텀블러(Tumblr) 대시보드 크롤링하고 검색
### 5. N그램 사용 - 이어서
1. 문장에서 HTML 태그 제거
   - 예제에서는 쉽게 사용할 수 있는 N그램 사용
   - 인덱스 대상 문장이 HTML로 마크업 되어 있는 경우 가정, HTML 태그를 검색할 일은 없을 것이므로 HTML 태그까지 인덱스 생성에 사용하면 검색에 방해가 될 수 잇음. 따라서 HTML 태그는 제거, 문장에서 HTML 태그를 제거하기 위한 목적으로 w3lib라이브러리를 사용
     - w3lib[[URL](https://github.com/scrapy/w3lib)]
   - pip install 명령어로 w3lib 라이브러리 설치
     - ```cmd
       (venv_tumblr_search)$ pip install w3lib
       ```
2. Whoosh의 인덱스 저장 전용 디렉터리 생성
   - 다움 내용을 whoosh_lib.py라는 파일 이름으로 저장.
   - ```python
     import os
     from whoosh import index
     from whoosh.fields import Schema, ID, TEXT, NGRAM

     # 인덱스 데이터를 저장할 디렉터리 지정
     INDEX_DIR = "indexdir"
     # 인덱스 전용 스키마 정의
     schema = Schema(
        # 인덱스 유닛 ID로 글의 URL 사용
        post_url=ID(unique=True, stored=True),
        # 본문을 N그램으로 인덱스화
        body=NGRAM(stored=True),
     )
     def get_or_create_index():
        # 인덱스 전용 디렉터리가 없다면 생성
        if not os.path.exists(INDEX_DIR):
            os.mkdir(INDEX_DIR)
            # 인덱스 전용 파일 생성
            ix = index,.create_in(INDEX_DIR, schema)
            return ix
        # 이미 인덱스 전용 디렉터리가 있다면
        # 기존 인덱스 파일 열어서 사용
        ix = index.open_dir(INDEX_DIR)
        return ix
     ```
   - whoosh_lib.py는 텀블러 API를 기반으로 얻은 글을 인덱스 하는 라이브러리.