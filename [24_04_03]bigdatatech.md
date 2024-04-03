# 7. 크롤러로 수집한 데이터 사용
## 1. 피드 생성
### 1. 피드란?
- 블로그에 올린 새로운 포스트(기사)는 RSS등의 피드(발신 전용 데이터)를 발행하는 경우가 많음.
- 이러한 피드를 'Feedly' 등의 피드 리더 등으로 읽어 들이면 다양한 블로그 최신 정보를 확인할 수 있음. 여러 사이트를 정리해주는 서비스도 피드를 활용해 정보를 제공하는 경우 많음
  - Feedly [[URL](https://feedly.com/)]
- 가지고 있는 정보를 RSS로 만들지 않더라도 다른 서비스가 제공하는 RSS를 다룰 때 알아두면 좋은 정보.
- 대표적인 피드 형식으로는 RSS와 Atom.
### 2. RSS 형식
- RSS 사양은 'RSS 2.0 at Harvard Law'에서 확인 가능. 현재 많이 사용되는 최신 버전은 RSS 2.0이며, XML 1.0의 사양을 따름
  - RSS 2.0 at Harvard Law [[URL](https://cyber.harvard.edu/rss/rss.html)]
- 다음 코드의 RSS 데이터 샘플을 살핌. 다음 코드는 'RSS 2.0 at Harvard Law'로 간략하게 생성.
  - ```RSS
    <?xml version="1.0"?>
    <rss version="2.0">
        <channel>
        <title>Liftoff News</title>
        <link>http://liftoff.msfc.nsan.gov/</link>
        <description>Liftoff to Space Exploration.</description>
        <item>
            <title>Star City</title><link>http://liftoff.msfc.nasa.gov/news/2003/news-starcity.asp</link>
            <description>How do Americans get ready to work with Russians aboard the International Space Station...(이하 생략)</description>
            <pubDate>Tue, 03 Jun 2003 09:39:21 GMT</pubDate>
            <guid>http://liftoff.msfc.nasa.gov/2003/06/03.html#item573</guid>
        </item>
        <item>
            <description>(생략)</description>
            <pubdate>(생략)</pubdate>
            <guid>(생략)</guid>
        </item>
    </rss>
    ```
- 위 코드의 첫번째 줄은 <xmp><?xml version="1.0"?></xmp>를 반드시 포하ㅓㅁ해야 함. 이때 앞에 빈 줄이 포함되지 않게 주의, XML 문서를 만들때와 똑같이 하면 됨
- RSS의 최상위 레벨에는 RSS 요소가 있음 문서 요소 전체를 <xmp><rss version="2.0">~ </rss></xmp>로 감싸야 함.
- version 속성은 필수, 기본적으로는 2.0 이외의 버전은 사용하지 않는다고 생각해도 됨. 따라서 고정적인 구문
