# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 4. feedgen을 사용해서 RSS 생성 - 이어서
5. 피드 생성 프로그램 작성
- 다음은 피드를 생성하는 프로그램 rss_with_feedgen.py 코드
- ```python
  """feedgen 사용해보기"""
  from feedgen.feed import FeedGenerator

  # 이전에 만들었던 feedgen_ext에서 사용자 정의 네임 스페이스 클래스 읽어들이기
  from feedgen_ext import BookEntryExtension, BookFeedExtension
  
  def create_feed():
    """RSS 피드 생성"""
    
    # 피드 데이터 저장 전용 객체
    fg=FeedGenerator()

    # 사용자 정의 네임 스페이스 등록, 이전에 만들었던 클래스 적용
    fg.register_extension(
        'book',
        extenstion_class_feed=BookFeedExtension,
        extenstion_class_entry=BookEntryExtension,
    )
    # <channel><title>요소
    fg.title("도서 목록")
    # <channel><link>요소: <link> 태그의 내용은 href 속성으로 지정
    fg.link(href="http://example.com")
    ## <channel><description>요소
    fg.description(
        "설명 입력했다 가정."
    )

    # <channel><item> 요소
    fe = fg.add_entry()
    # <channel><item><title> 요소
    fe.title("도서 이름")
    # <channel><item><link> 요소
    fe.link(href="http://example.com")
    # <channel><item><description> 요소
    fe.description(
    '<a href="http://example.com">이스케이프 처리 확인 전용 링크</a>'
    )
    # <channel><item><book:writer>요소(사용자 정의 네임스페이스 사용 요소)
    fe.book.publisher({'name':"위키북스",'id':"1"})# 값은 딕셔너리 자료형으로 전달
    # 피드를 RSS 형식으로 변환(pretty=True로 들여쓰기 적용)
    return fg.rss_str(pretty=True)
  if __name__=='__main__':
    rss_str = create_feed()
    print(rss_srt.decode())  
  ``` 
  