# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 3. 네임스페이스를 사용한 RSS 확장 - 이어서
1. 많이 사용되는 네임 스페이스
   - 공개된 네임 스페이스도 있음. 예를 들어 이미지 주소 등을 다룰 때 사용되는 media가 대표적. 
   - 원래는 야후(Yahoo!)에서 정의했던 네임 스페이스지만, 현재는 다음사이트에서 확인 가능
     - Media RSS Specification version 1.5.1[[URL](http://www.rssboard.org/media-rss)]
   - 또한 파이썬의 대표적인 피드 파서 라이브러리인 feedparser 사이트를 보면 많이 사용되는 네임 스페이스가 공개되어 있음. 참고하면 좋음.
     - feedparser 5.2.0 documentation[[URL](https://pythonhosted.org/feedparser/namespace-handling.html)]
2. 마크업 작성을 포함할 때의 주의사항
   - title과 description 속성의 문자열 값에 HTML 등의 마크업 문서가 포함되어 있으면 탴그 기호가 XML의 태그와 혼동되어 제대로 해석되지 않음. 따라서 문자 참조를 사용하거나 CDATA 섹션을 사용
  - RSS는 XML 형식이므로 이스케이프 방식도 XML의 사양을 따름.
    - HTML의 '숫자 문자 참조'는 XML 세계에서 '문자 참조'라고 부르며, HTML의 '문자 엔티티 참조'는 XML 세계에서'엔티티 참조'라고 부름
    - CDATA 섹션
      - 일반적으로 XML 은 <,> 등의 XML 태그와 혼동될 수 있는 문자를 `&lt;,&gt;` 으로 이스케이프 처리(엔티티 참조) gka.
      - 하지만 관리가 복잡해질 수 있어서 특별하게 `<![CDATA[`와 `]]>`로 감싸서태그와 혼동되지 않게 만들기도 함.
    - ```xml
       // 이스케이프 하지 않은 예
       <description>
            설명 입력 가정
            <a href="http://example.com">이스케이프 처리 확인 전용 링크</a>
       </description>
      ```
    - 문자열 참조 입력 시 다음처럼 입력.
    - ```xml
       <description>
            설명 입력 가정
            &lt;a href="http://example.com&quot;&gt;이스케이프 처리 확인 전용 링크&lt/a&gt;
       </description>
      ```
    - XML에 정의된 엔티티 참조는 &,<,>,",'로 5가지 종류, 각각 `&amp;,&lt;,&gt;,&quot;&apos;` 사용
    - 이 이외의 기호는 문자참조로 작성. 예를 들어 음악 기호 &#x266A; 는 10진수로 지정하면  #9834;, 16진수로 지정 시 `&#x266A;`라고 지정
3. CDATA 섹션 작성.
   - CDATA 섹션을 사용하려면 대상 문서를 `<![CDATA[`와 `]]>`로 감쌈.
   - 위의 예를 CDATA 섹션을 사용해 바꾸면 다음과 같음.
   - ```xml
       <description><![CDATA[
            설명 입력 가정
            <a href="http://example.com">이스케이프 처리 확인 전용 링크</a>
       ]]></description>
      ```